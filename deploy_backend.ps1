# 🚀 DEPLOY BACKEND TO CLOUD RUN
# Automates Container Build and Serverless Deployment.

$PROJECT_ID = "project-c465bc45-299b-470d-8b6"
$SERVICE_NAME = "metodo-activa-brain"
$REGION = "us-central1"

Write-Host "🚢 INICIANDO DESPLIEGUE DE BACKEND (CLOUD RUN)..." -ForegroundColor Cyan
Write-Host "📌 Project: $PROJECT_ID | Service: $SERVICE_NAME" -ForegroundColor Gray

# 1. Configurar Proyecto
gcloud config set project $PROJECT_ID

# 2. Ejecutar Pipeline de Continuous Deployment (Cloud Build)
Write-Host "🏭 Ejecutando Pipeline Enterprise (cloudbuild.yaml)..." -ForegroundColor Yellow
gcloud builds submit --config cloudbuild.yaml .

if ($LASTEXITCODE -ne 0) { throw "❌ Error en Pipeline." }

Write-Host "✅ ¡BACKEND DESPLEGADO CON ÉXITO!" -ForegroundColor Green
Write-Host "El Cerebro de Método Activa está vivo en la nube." -ForegroundColor White
