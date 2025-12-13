import { initializeApp } from 'firebase/app';
import { getFirestore } from 'firebase/firestore';
import { getFunctions } from 'firebase/functions';

// Firebase configuration (Hardcoded for Guaranteed Connectivity v5.0)
const firebaseConfig = {
    apiKey: "AIzaSyD6781MucdFE3yH3wdpjVW23YfCjH2ZCuQ",
    authDomain: "project-c465bc45-299b-470d-8b6.firebaseapp.com",
    projectId: "project-c465bc45-299b-470d-8b6",
    storageBucket: "project-c465bc45-299b-470d-8b6.appspot.com",
    messagingSenderId: "476151355322",
    appId: "1:476151355322:web:641875880086"
};

import { getAuth } from 'firebase/auth';

const app = initializeApp(firebaseConfig);
export const db = getFirestore(app);
export const functions = getFunctions(app);
export const auth = getAuth(app);

// Export Gemini API Key for use in chat component
export const GEMINI_API_KEY = import.meta.env.VITE_GEMINI_API_KEY;
