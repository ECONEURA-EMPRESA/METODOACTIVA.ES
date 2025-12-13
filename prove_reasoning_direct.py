import requests
import json
import time

API_KEY = "AIzaSyD6781MucdFE3yH3wdpjVW23YfCjH2ZCuQ"
URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent?key={API_KEY}"

print("🧠 CONECTANDO DIRECTAMENTE CON GEMINI 1.5 FLASH...")
print("==================================================")

def ask_gemini(scenario, prompt):
    print(f"\n🧪 ESCENARIO: {scenario}")
    print(f"   📤 Prompt: {prompt[:100]}...")
    
    payload = {
        "contents": [{
            "parts": [{"text": prompt}]
        }]
    }
    
    start = time.time()
    try:
        response = requests.post(URL, json=payload, timeout=30)
        elapsed = round(time.time() - start, 2)
        
        if response.status_code == 200:
            data = response.json()
            try:
                text = data['candidates'][0]['content']['parts'][0]['text']
                print(f"   🤖 RAZONAMIENTO ({elapsed}s):")
                print(f"   --------------------------------------------------")
                print(f"   {text[:500]}...") 
                print(f"   [...continúa...]")
                print(f"   --------------------------------------------------")
                return True
            except:
                print(f"   ⚠️ Respuesta inesperada: {data}")
        else:
            print(f"   ❌ ERROR {response.status_code}: {response.text}")
            return False
            
    except Exception as e:
        print(f"   ❌ EXCEPTION: {e}")
        return False

# 1. EMPATÍA (Alzheimer)
p1 = """
Actúa como Aurora, experta en musicoterapia y neurociencia.
Usuario: "Hoy mi madre me ha mirado y me ha llamado 'Señora'. Me he ido al baño a llorar. Siento que la he perdido para siempre."
Respuesta (Máximo 3 frases, Empática, Científica):
"""
ask_gemini("EMPATIA PROFUNDA", p1)

# 2. LOGICA (TDAH)
p2 = """
Actúa como Aurora.
Usuario: "¿Cómo ayuda el ritmo a un niño con TDAH? Dame el mecanismo biológico."
Respuesta (Técnica, Precisa, sin magia):
"""
ask_gemini("RAZONAMIENTO TÉCNICO", p2)

# 3. NEGOCIACIÓN (Venta)
p3 = """
Actúa como Aurora.
Usuario: "¿Por qué comprar el libro si está Spotify gratis?"
Respuesta (Persuasiva, Valor Diferencial):
"""
ask_gemini("ARGUMENTACIÓN COMERCIAL", p3)
