# -*- coding: utf-8 -*-
"""
Ejemplo Oficial de Integración con MEION-SDK
Guarda y busca recuerdos semánticamente en meionia.com en 5 líneas de código.
"""
import os
import time
from meion_client import MeionClient

# Helper para cargar archivo .env manualmente sin dependencias requeridas
def load_env_file():
    if os.path.exists(".env"):
        with open(".env", "r", encoding="utf-8") as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith("#") and "=" in line:
                    key, val = line.split("=", 1)
                    os.environ[key.strip()] = val.strip()

# Cargar configuración local de .env
load_env_file()

def test_meion():
    print("🧠 --- INICIANDO PRUEBA DE CONEXIÓN CON MEIONIA.COM --- 🧠\n")
    
    try:
        # Inicializar el cliente (leerá automáticamente MEION_API_KEY del entorno)
        client = MeionClient()
    except Exception as e:
        print(f"❌ Error de Inicialización: {e}")
        print("💡 Recuerda ejecutar 'python install.py' primero para registrar tu clave API.")
        return

    # 1. Guardar un nuevo recuerdo en el cerebro molecular
    print("📥 1. Guardando un nuevo recuerdo en el cerebro molecular...")
    nuevo_recuerdo = (
        "El cumpleaños de mi hija Sofia es el 14 de Noviembre. "
        "Le encantan las películas de ciencia ficción y los videojuegos retro."
    )
    
    save_result = client.memorize(nuevo_recuerdo)
    print(f"👉 Respuesta del Servidor: {save_result}")
    
    if save_result.get("status") == "success":
        print(f"✅ ¡Recuerdo guardado con éxito!")
        print(f"⚖️ Peso Original: {save_result.get('original_weight')} bytes")
        print(f"⚛️ Peso Molecular (Comprimido): {save_result.get('molecular_weight')} bytes")
        print(f"📈 Ahorro de espacio logrado: {save_result.get('savings')}%")
    else:
        print(f"⚠️ Nota de conexión: {save_result.get('message')}")
        
    print("\n" + "-"*60 + "\n")
    time.sleep(1)

    # 2. Buscar recuerdos semánticamente
    print("🔍 2. Realizando búsqueda semántica de recuerdos relevantes...")
    criterio_busqueda = "¿Cuándo es el cumpleaños de Sofia y qué regalos le gustan?"
    
    search_result = client.search(criterio_busqueda)
    print(f"👉 Resultados encontrados para: '{criterio_busqueda}'\n")
    
    if isinstance(search_result, list):
        if not search_result:
            print("📭 No se encontraron recuerdos sobre ese tema en tu cerebro digital.")
        for idx, item in enumerate(search_result):
            print(f"  Recuerdo #{idx + 1} (Guardado: {item.get('timestamp')})")
            print(f"  📄 Contenido: \"{item.get('texto')}\"")
            print(f"  ⚡ Relevancia Semántica: {item.get('score', 'N/A')}\n")
    else:
        print(f"⚠️ Nota de búsqueda: {search_result.get('message')}")

    print("\n" + "-"*60 + "\n")
    time.sleep(1)

    # 3. Obtener contexto optimizado para inyectar a tu Inteligencia Artificial (LLM)
    print("🤖 3. Recuperando el bloque de contexto optimizado para tu Agente de IA...")
    ai_context = client.search(criterio_busqueda, format_ai=True)
    
    if "context" in ai_context:
        print(f"👇 Envía este bloque exacto en el prompt de tu IA para darle memoria a largo plazo:")
        print("="*60)
        print(ai_context.get("context"))
        print("="*60)
    else:
        print(f"⚠️ Error al recuperar contexto para IA: {ai_context}")

if __name__ == "__main__":
    test_meion()
