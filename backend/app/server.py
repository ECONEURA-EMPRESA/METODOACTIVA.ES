from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import settings

# 🏗️ FASTAPI FACTORY
# El corazón del servidor Serverless.

app = FastAPI(
    title="Método Activa Brain",
    description="API Enterprise-Grade para Metodo Activa (Cloud Run + Vertex AI)",
    version="2.0.0",
    docs_url="/docs", # Swagger UI
    redoc_url="/redoc"
)

# 🚦 CORS Policy (Seguridad Militar)
# Solo permitimos peticiones desde nuestra Web Oficial (Firebase).
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.ALLOWED_ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)

# 🔗 Conectar Rutas
from app.api import chat
app.include_router(chat.router, prefix="/api/v1")

@app.get("/")

def health_check():
    """
    💓 Latido del sistema.
    Cloud Run usa esto para saber que estamos vivos.
    """
    return {"status": "online", "system": "Método Activa Brain V2", "env": "Cloud Run"}

@app.get("/warmup")
def warmup():
    """
    🔥 Calentamiento de neuronas.
    Llamado por Cloud Scheduler para evitar 'Cold Starts'.
    """
    return {"status": "ready"}
