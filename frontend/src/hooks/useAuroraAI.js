import { useState } from 'react';
import { auth } from '../firebase';
import { signInAnonymously } from 'firebase/auth';

/**
 * Hook de Inteligencia Artificial - V3 CLOUD RUN (Enterprise)
 * Conecta al Backend Python en Google Cloud con Seguridad Zero-Trust.
 */
const BACKEND_URL = "https://metodo-activa-brain-476151355322.us-central1.run.app/api/v1/chat";

export const useAuroraAI = () => {
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState(null);

    const sendMessage = async (message, userContext = "general") => {
        setIsLoading(true);
        setError(null);

        try {
            // 1. Autenticación Silenciosa (Zero-Trust)
            // Si el usuario no está logueado, entramos como anónimo.
            let user = auth.currentUser;
            if (!user) {
                const userCredential = await signInAnonymously(auth);
                user = userCredential.user;
            }

            // 2. Obtener Token Seguro (JWT)
            const token = await user.getIdToken();

            // 3. Llamada al Cerebro (Cloud Run)
            const response = await fetch(BACKEND_URL, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify({
                    message: message,
                    user_context: userContext
                })
            });

            if (!response.ok) {
                const errorData = await response.json();
                throw new Error(errorData.detail || "Error connecting to Brain");
            }

            const data = await response.json();

            return {
                response: data.response,
                suggested_session: data.suggested_session
            };

        } catch (err) {
            console.error("Error AI Service:", err);
            setError(err.message);

            return {
                response: "Lo siento, mi conexión con el servidor seguro se ha interrumpido. Por favor intenta de nuevo en un momento.",
                suggested_session: "Error de Conexión"
            };
        } finally {
            setIsLoading(false);
        }
    };

    return {
        sendMessage,
        isLoading,
        error
    };
};
