# 🚢 METODO ACTIVA - UNIVERSAL DEPLOYMENT SCRIPT
# Orchestrates build and deploy for the Monorepo

$ErrorActionPreference = "Stop"

function Print-Header {
    param($Title)
    Write-Host "`n========================================================" -ForegroundColor Cyan
    Write-Host " $Title" -ForegroundColor White
    Write-Host "========================================================`n" -ForegroundColor Cyan
}

Print-Header "🚀 INICIANDO DESPLIEGUE (MONOREPO PRIME)"

# ---------------------------------------------------------------------------
# 1. FRONTEND BUILD (Apps/Web)
# ---------------------------------------------------------------------------
Print-Header "⚛️  BUILDING FRONTEND (apps/web)"
Set-Location "$PSScriptRoot\..\..\apps\web"

try {
    Write-Host "?? Installing dependencies..." -ForegroundColor Gray
    npm install --silent
    
    Write-Host "?? Compiling..." -ForegroundColor Gray
    npm run build
    
    if ($LASTEXITCODE -ne 0) { throw "Frontend Build Failed" }
    Write-Host "? Frontend Build Success!" -ForegroundColor Green
}
catch {
    Write-Host "? ERROR: $_" -ForegroundColor Red
    exit 1
}

# ---------------------------------------------------------------------------
# 2. FIREBASE DEPLOY
# ---------------------------------------------------------------------------
Print-Header "🔥 DEPLOYING TO FIREBASE HOSTING"
Set-Location "$PSScriptRoot\..\.." # Back to Root

try {
    # Check if firebase is installed
    if (!(Get-Command firebase -ErrorAction SilentlyContinue)) {
        throw "Firebase CLI not found. Please run 'npm install -g firebase-tools'"
    }

    firebase deploy --only hosting
    if ($LASTEXITCODE -ne 0) { throw "Firebase Deploy Failed" }
}
catch {
    Write-Host "? ERROR: $_" -ForegroundColor Red
    exit 1
}

Print-Header "🎉 DESPLIEGUE COMPLETADO"
Write-Host "?? URL: https://metodoactiva.es" -ForegroundColor Cyan
Write-Host "?? Console: https://console.firebase.google.com/project/metodo-activa/overview" -ForegroundColor Gray
