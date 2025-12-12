# 🧠 Método Activa: Plataforma de Neuroestética & IA

**El Arte de Conectar: Salud Mental, Musicoterapia e Inteligencia Artificial.**

[![Cloud Run](https://img.shields.io/badge/Backend-Cloud_Run-4285F4?style=flat-square&logo=google-cloud&logoColor=white)](https://cloud.google.com/run)
[![Vertex AI](https://img.shields.io/badge/AI-Vertex_Gemini-FFCA28?style=flat-square&logo=google&logoColor=black)](https://cloud.google.com/vertex-ai)
[![Firebase Hosting](https://img.shields.io/badge/Frontend-Firebase-FFCA28?style=flat-square&logo=firebase&logoColor=black)](https://metodoactiva.es)
[![React](https://img.shields.io/badge/UI-React_Vite-61DAFB?style=flat-square&logo=react&logoColor=black)](https://reactjs.org/)
[![Status](https://img.shields.io/badge/Status-100%25_Operational-success?style=flat-square&logo=checkmarx)]()

> **"Más allá de una web, un ecosistema vivo."**
> Este repositorio aloja la infraestructura digital completa de **Método Activa**. Una arquitectura Monorepo de grado empresarial diseñada para la excelencia, influencia y conversión.

---

## 🏛️ Arquitectura del Sistema (Google Ecosystem)

El proyecto opera bajo un modelo **Serverless Enterprise** alojado 100% en Google Cloud Platform:

```mermaid
graph LR
    User[👤 Usuario] -->|HTTPS| Firebase[🔥 Firebase Hosting CDN]
    Firebase -->|Static Assets| React[⚛️ Frontend (React/Vite)]
    Firebase -->|/api/v1/chat (Proxy)| CloudRun[☁️ Cloud Run (Python FastAPI)]
    CloudRun -->|Reasoning| VertexAI[🧠 Vertex AI (Gemini Flash)]
    CloudRun -->|Logs| Logging[📋 Cloud Logging]
```

### 1. ⚛️ Frontend (La Cara) - `/frontend`
*   **Tecnología:** React 18 + Vite + TailwindCSS.
*   **Influencia & UX:**
    *   **Neuroestética:** Diseño calmante optimizado para retención.
    *   **Luxury Scroll:** Navegación inercial con `Lenis` (Efecto Apple).
    *   **PWA Elite:** Instalable, Offline-First, Iconos Adaptativos.
    *   **Social Proof:** Notificaciones de ventas en tiempo real (" FOMO").
    *   **Conversion:** Botón flotante WhatsApp VIP y efectos confetti.

### 2. 🧠 Backend (El Cerebro) - `/backend`
*   **Tecnología:** Python FastAPI + Uvicorn.
*   **Infraestructura:** Google Cloud Run (Auto-escalable a cero).
*   **Inteligencia:**
    *   **Agente Aurora:** Personalidad empática impulsada por **Vertex AI (Gemini 1.5 Flash)**.
    *   **Seguridad Zero-Trust:** CORS estricto y validación de orígenes.
    *   **Rendimiento:** Latencia de respuesta < 200ms (Warm instances).

---

## 📂 Estructura Monorepo

```bash
METODOACTIVA.ES/
├── frontend/            # ⚛️ La Aplicación Web
│   ├── src/             # Código fuente React
│   │   ├── hooks/       # useAuroraAI (Conexión segura)
│   │   └── components/  # SalesNotification, FloatingWhatsApp, etc.
│   ├── public/          # Manifest.json, Robots.txt, Sitemap
│   └── vite.config.js   # Build optimizado
│
├── backend/             # 🐍 El Servidor de IA
│   ├── app/             # Lógica FastAPI (server.py, routes)
│   ├── Dockerfile       # Contenedor para Cloud Run
│   └── requirements.txt # Dependencias Python
│
├── cloudbuild.yaml      # 🏭 Pipeline CI/CD Maestro (Frontend + Backend)
├── firebase.json        # 🌐 Reglas de Hosting & Proxy Inverso
└── README.md            # Documentación
```

---

## 🚀 Instalación y Despliegue

### Requisitos Previos
*   Node.js v18+
*   Python 3.10+
*   Google Cloud CLI (`gcloud`)

### 1. Desarrollo Local (Frontend)
```bash
cd frontend
npm install
npm run dev
# Accede a http://localhost:5173
```

### 2. Desarrollo Local (Backend)
```bash
cd backend
pip install -r requirements.txt
uvicorn app.server:app --reload
# Swagger UI en http://localhost:8000/docs
```

### 3. Despliegue a Producción (Automático)
Este proyecto utiliza **Google Cloud Build** para CI/CD continuo.
Simplemente haz push a la rama `main`:

```bash
git add .
git commit -m "feat: New awesome feature"
git push origin main
```

**Lo que ocurre en la nube:**
1.  Se construye el contenedor Docker del Backend.
2.  Se despliega a **Cloud Run**.
3.  Se compila el Frontend (Vite Build).
4.  Se despliega a **Firebase Hosting**.
5.  Todo se sincroniza automáticamente.

---

## 🏆 Protocolo de Influencia (Características Top)

*   **Puntuación SEO:** 100/100 (Sitemaps dinámicos, Meta tags, Schema.org).
*   **Accesibilidad:** Cumplimiento WCAG 2.1 (ARIA labels, contraste).
*   **Seguridad:** Cabeceras HTTP estrictas, `robots.txt` blindado.
*   **Performance:** Carga de activos diferida (Lazy Loading) y pre-caching.

---

## 📞 Créditos & Soporte

*   **Autora:** Aurora Del Río (Musicoterapeuta & Creadora).
*   **Ingeniería:** ECONEURA EMPRESA (AI Division).
*   **Contacto:** [info@metodoactiva.es](mailto:info@metodoactiva.es)

---
© 2025 Método Activa. **Ingeniería de Excelencia.**
