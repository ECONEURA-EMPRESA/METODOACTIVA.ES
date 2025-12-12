import google.generativeai as genai
from app.core.config import settings

# 🧠 CEREBRO SIMPLE (GEMINI DIRECTO)
# Implementación robusta usando API KEY según petición del usuario.

class VertexService:
    def __init__(self):
        # Configurar con API Key (Resiliente)
        if not settings.GEMINI_API_KEY:
            print("⚠️ WARNING: GEMINI_API_KEY no encontrada. El chat fallará.")
        
        genai.configure(api_key=settings.GEMINI_API_KEY)
        
        # Modelo Gemini Pro optimizado
        self.model = genai.GenerativeModel('gemini-1.5-flash')

    async def generate_response(self, user_message: str, user_context: str) -> str:
        """
        🗣️ Genera la respuesta empática usando Gemini Flash.
        """
        try:
            # Prompt de Identidad (System Prompt)
            identity = """
            Eres Aurora, la asistente virtual del libro 'Método Activa' de Aurora Del Río.
            Tu misión es ayudar a terapeutas, cuidadores de ancianos y padres de niños especiales (TDAH/Autismo).
            
            PRINCIPIOS:
            1. EMPATÍA RADICAL: Hablas con calidez. Entiendes el agotamiento del cuidador.
            2. EXPERTA EN MÚSICA: Sabes que la musicoterapia conecta cerebro y emoción.
            3. VENTA SUAVE: Si preguntan por soluciones profundas, sugiere el libro '21 Sesiones de Musicoterapia'.
            
            ESTILO:
            - Respuestas concisas pero amorosas.
            - Usa emojis suaves (🎵, ✨, 💙).
            - No inventes hechos médicos.
            """
            
            # Generar contenido (Prompt + Mensaje)
            # Nota: Gemini 1.5 Flash soporta system instructions, pero lo simulamos aquí para compatibilidad.
            prompt = f"{identity}\n\nContexto Usuario: {user_context}\nPregunta: {user_message}"
            
            response = self.model.generate_content(prompt)
            return response.text
            
        except Exception as e:
            print(f"❌ Error Gemini API: {e}")
            return "Lo siento, mi conexión musical está interferida. ¿Podrías repetirlo? 🎵"

# Instancia global
vertex_service = VertexService()
