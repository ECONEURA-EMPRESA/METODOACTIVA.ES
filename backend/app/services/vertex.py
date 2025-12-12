import vertexai
from vertexai.generative_models import GenerativeModel
from google.cloud import discoveryengine_v1beta as discoveryengine
from app.core.config import settings

# 🧠 CEREBRO RAG DE EXCELENCIA
# Combina Vertex AI Search (Datos) + Gemini Pro (Razonamiento).

class VertexService:
    def __init__(self):
        # Inicializar clientes de Google Cloud una sola vez (Singleton Pattern)
        self.project_id = settings.PROJECT_ID
        self.location = settings.LOCATION
        self.search_client = discoveryengine.SearchServiceClient()
        
        # Configurar Gemini (Vertex AI SDK)
        vertexai.init(project=self.project_id, location=settings.VERTEX_REGION)
        self.model = GenerativeModel("gemini-1.5-pro")

    async def search_book(self, query: str) -> str:
        """
        🔍 Busca en el PDF del libro "Método Activa" usando Vector Search.
        Retorna los fragmentos más relevantes.
        """
        # ID del Data Store creado en Agent Builder (Lo definiremos al desplegar infra)
        serving_config = f"projects/{self.project_id}/locations/global/collections/default_collection/dataStores/metodo-activa-book/servingConfigs/default_search"
        
        request = discoveryengine.SearchRequest(
            serving_config=serving_config,
            query=query,
            page_size=3, # Top 3 fragmentos
            content_search_spec={"snippet_spec": {"return_snippet": True}}
        )
        
        response = self.search_client.search(request)
        
        context = ""
        for result in response.results:
            data = result.document.derived_struct_data
            context += f"\n[Fragmento]: {data.get('snippets', [{}])[0].get('snippet', '')}"
            
        return context

    async def generate_response(self, user_message: str, user_context: str) -> str:
        """
        🗣️ Genera la respuesta empática basada en el libro.
        """
        # 1. Recuperar conocimiento real del libro (RAG)
        book_knowledge = await self.search_book(user_message)
        
        # 2. Prompt de Ingeniería (Chain of Thought)
        system_prompt = f"""
        Eres Aurora, experta en el Método Activa.
        Usa EXCLUSIVAMENTE la siguiente información del libro para responder:
        {book_knowledge}
        
        Contexto del usuario: {user_context}
        
        Instrucciones:
        1. Responde con empatía.
        2. Cita el pilar (Cuerpo/Mente/Corazón) si aparece en el texto.
        3. Si la respuesta no está en el libro, di que no estás segura pero ofrece ayuda general.
        """
        
        response = self.model.generate_content([system_prompt, user_message])
        return response.text

# Instancia global
vertex_service = VertexService()
