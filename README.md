# 🎵 Método Activa | Monorepo Prime

**Activa tu Cuerpo, Mente y Corazón con arte.**

[![Status](https://img.shields.io/badge/Status-Production-success?style=flat-square)]()
[![Frontend](https://img.shields.io/badge/App-React_19-61DAFB?style=flat-square&logo=react)](apps/web)
[![Backend](https://img.shields.io/badge/API-FastAPI-009688?style=flat-square&logo=fastapi)](apps/api)
[![Infrastructure](https://img.shields.io/badge/Infra-Docker_Compose-2496ED?style=flat-square&logo=docker)](docker-compose.yml)

El proyecto ha sido restructurado como un **Monorepo** moderno para garantizar escalabilidad, aislamiento y una experiencia de desarrollo superior.

---

## 🏗️ Arquitectura del Monorepo

```bash
METODO-ACTIVA/
├── apps/
│   ├── web/             # Frontend (React 19 + Vite + Tailwind)
│   └── api/             # Backend (Python FastAPI + Gemini AI)
├── tools/
│   ├── scripts/         # Herramientas de despliegue y mantenimiento
│   └── devtools/        # Configuraciones compartidas
├── packages/            # Librerías compartidas (Futuro)
├── docker-compose.yml   # Orquestación local completa
└── cloudbuild.yaml      # Pipeline de CI/CD (Google Cloud)
```

---

## 🚀 Inicio Rápido (Local Development)

### Opción A: Docker (Recomendado)
Levanta todo el stack (Frontend + Backend) con un solo comando.

```bash
docker-compose up --build
```
- **Frontend:** http://localhost:5173
- **Backend:** http://localhost:8080/docs

### Opción B: Manual
Si prefieres correr cada servicio por separado:

**1. Frontend:**
```bash
cd apps/web
npm install
npm run dev
```

**2. Backend:**
```bash
cd apps/api
# (Activa tu venv)
pip install -r requirements.txt
python debug_run.py
```

---

## 🚢 Despliegue en Producción

El proyecto utiliza un script universal de despliegue ubicado en `tools/scripts`.

```powershell
# Desde la raíz del proyecto:
./tools/scripts/deploy.ps1
```

Este script se encarga de:
1. Construir el Frontend optimizado (`apps/web`).
2. Desplegar los assets a Firebase Hosting.
3. Verificar la integridad del build.

---

## 🛠️ Tecnologías

### Frontend (`apps/web`)
*   **Core:** React 19, Vite.
*   **Estilos:** Tailwind CSS 4, Framer Motion.
*   **IA:** Google Vertex AI SDK (Client-side optimized).

### Backend (`apps/api`)
*   **Core:** Python 3.11, FastAPI.
*   **AI:** Google Gemini Pro Integration.
*   **Hosting:** Google Cloud Run (Dockerized).

---

## 📞 Soporte
*   **Web Oficial:** [www.metodoactiva.es](https://metodoactiva.es)
*   **Email:** info@metodoactiva.es
*   **Autor:** Aurora Del Río

---
© 2025 Método Activa. Engineered for Excellence.
