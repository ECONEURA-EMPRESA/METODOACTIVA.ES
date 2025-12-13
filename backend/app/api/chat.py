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
    💬 Endpoint Híbrido:
    - Intenta validar Token (Seguridad).
    - Si falla o no hay token, PERMITE el paso (Modo Fallback para garantizar servicio).
    """
    user_id = "anonymous_fallback"
    
    # 🔐 Intento de Validación (Soft-Auth)
    if authorization:
        try:
            user_payload = verify_firebase_token(authorization)
            user_id = user_payload.get('uid', 'verified_user')
            print(f"✅ User Authenticated: {user_id}")
        except Exception as e:
            print(f"⚠️ Auth Token Invalid, proceeding as Anonymous: {e}")
    else:
        print("⚠️ No Token provided, proceeding as Anonymous")
        
    try:
        # LLamada al Cerebro (Gemini)
        ai_response = await vertex_service.generate_response(request.message, request.user_context)
        
        return ChatResponse(
            response=ai_response,
            suggested_session="Análisis Completado"
        )
    except Exception as e:
        print(f"❌ Error Critical: {e}")
        raise HTTPException(status_code=500, detail="Neural Network Overload")
