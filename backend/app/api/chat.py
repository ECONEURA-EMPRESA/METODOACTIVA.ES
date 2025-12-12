from fastapi import APIRouter, HTTPException, Header
from pydantic import BaseModel
from app.services.vertex import vertex_service
from app.services.auth import verify_firebase_token

router = APIRouter()

class ChatRequest(BaseModel):
    message: str
    user_context: str = "general"

class ChatResponse(BaseModel):
    response: str
    suggested_session: str

@router.post("/chat", response_model=ChatResponse)
async def chat_endpoint(request: ChatRequest, authorization: str = Header(None)):
    """
    💬 Endpoint Protegido de Chat.
    Requiere Token de Firebase Auth (Validado Criptográficamente).
    """
    # 🔐 Validación Zero-Trust
    if not authorization:
        raise HTTPException(status_code=401, detail="Missing Security Token")
    
    # Verificar firma real (Si falla, lanza 401)
    user_payload = verify_firebase_token(authorization)
    user_id = user_payload.get('uid')
    
    print(f"✅ User Authenticated: {user_id}")
    
    try:
        # LLamada al Cerebro RAG
        ai_response = await vertex_service.generate_response(request.message, request.user_context)
        
        return ChatResponse(
            response=ai_response,
            suggested_session="Análisis Completado"
        )
    except Exception as e:
        print(f"❌ Error Critical: {e}")
        raise HTTPException(status_code=500, detail="Neural Network Overload")
