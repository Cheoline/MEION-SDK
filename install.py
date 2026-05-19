# -*- coding: utf-8 -*-
import os
import sys
import time
import json

# Soporte para colores ANSI en Windows
if sys.platform == "win32":
    os.system("color")

# Códigos de color ANSI para estética neon cyberpunk
C_CYAN = "\033[96m"
C_PURPLE = "\033[95m"
C_GREEN = "\033[92m"
C_YELLOW = "\033[93m"
C_RED = "\033[91m"
C_RESET = "\033[0m"
C_BOLD = "\033[1m"

def print_slow(text, delay=0.01):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print("")

def main():
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # ASCII Art de MEION
    ascii_art = f"""{C_CYAN}{C_BOLD}
███╗   ███╗███████╗██╗██████╗ ███╗   ██╗    ███████╗██████╗ ██╗  ██╗
████╗ ████║██╔════╝██║██╔═══██╗████╗  ██║    ██╔════╝██╔══██╗██║ ██╔╝
██╔████╔██║█████╗  ██║██║   ██║██╔██╗ ██║    ███████╗██║  ██║█████╔╝ 
██║╚██╔╝██║██╔══╝  ██║██║   ██║██║╚██╗██║    ╚════██║██║  ██║██╔═██╗ 
██║ ╚═╝ ██║███████╗██║╚██████╔╝██║ ╚████║    ███████║██████╔╝██║  ██╗
╚═╝     ╚═╝╚══════╝╚═╝ ╚═════╝ ╚═╝  ╚═══╝    ╚══════╝╚═════╝ ╚═╝  ╚═╝{C_RESET}
    {C_PURPLE}--- CONECTOR OFICIAL DE MEMORIA PERSISTENTE PARA IAS ---{C_RESET}
    """
    print(ascii_art)
    
    print_slow(f"{C_BOLD}{C_CYAN}[i]{C_RESET} Iniciando instalador interactivo de MEION-SDK...")
    time.sleep(0.5)
    
    print("\n" + "="*70)
    print(f"{C_BOLD}{C_GREEN}🔒 ¿Qué es MEION y qué estamos configurando?{C_RESET}")
    print("MEION no es un chatbot. Es un núcleo de almacenamiento de memoria persistente.")
    print("Este instalador configurará tu entorno local para que tus Agentes de IA,")
    print("Chatbots o aplicaciones cognitivas se conecten a la red de meionia.com.")
    print("="*70 + "\n")
    
    # 1. Solicitar clave API
    print(f"{C_BOLD}{C_YELLOW}Paso 1: Autenticación de Usuario{C_RESET}")
    print_slow("Por favor, introduce tu API Key única personal de MEION.")
    print("(Recuerda que tu API Key se crea automáticamente al registrarte y crear tu cuenta en meionia.com)")
    
    api_key = ""
    while not api_key:
        api_key = input(f"{C_BOLD}{C_CYAN}API Key > {C_RESET}").strip()
        if not api_key:
            print(f"{C_RED}❌ La API Key no puede estar vacía.{C_RESET}")
            
    # 2. Definir URL del servidor
    print(f"\n{C_BOLD}{C_YELLOW}Paso 2: Dirección del Servidor de Memoria{C_RESET}")
    print("Por defecto nos conectaremos a la nube oficial: meionia.com")
    print("Presiona Enter para usar el servidor oficial, o introduce una URL personalizada (ej. local).")
    
    custom_url = input(f"{C_BOLD}{C_CYAN}Servidor [https://meionia.com] > {C_RESET}").strip()
    server_url = custom_url if custom_url else "https://meionia.com"
    
    # Sanitizar URL
    if not server_url.startswith("http://") and not server_url.startswith("https://"):
        server_url = "https://" + server_url
    if server_url.endswith("/"):
        server_url = server_url[:-1]
        
    print_slow(f"\n{C_CYAN}[...] Generando archivos de entorno de memoria...{C_RESET}")
    time.sleep(1)
    
    # Crear archivo .env
    env_content = f"""# Configuración de Conexión de Memoria MEION
MEION_API_KEY={api_key}
MEION_SERVER_URL={server_url}
"""
    try:
        with open(".env", "w", encoding="utf-8") as f:
            f.write(env_content)
        print(f"{C_GREEN}✅ Archivo de entorno '.env' creado exitosamente.{C_RESET}")
    except Exception as e:
        print(f"{C_RED}❌ Error al escribir el archivo .env: {e}{C_RESET}")
        return

    # Crear archivo de prueba config.json opcional para otros lenguajes
    config_data = {
        "meion_api_key": api_key,
        "meion_server_url": server_url
    }
    try:
        with open("meion_config.json", "w", encoding="utf-8") as f:
            json.dump(config_data, f, indent=4)
        print(f"{C_GREEN}✅ Archivo de configuración 'meion_config.json' creado exitosamente.{C_RESET}")
    except Exception as e:
        pass

    print("\n" + "="*70)
    print(f"{C_BOLD}{C_GREEN}🎉 ¡INSTALACIÓN COMPLETADA EXITOSAMENTE!{C_RESET}")
    print_slow(f"Tu entorno está listo. Los algoritmos de compresión molecular y")
    print_slow(f"procesamiento cromático (QTOM V5 y ITOM) residen seguros en {server_url}.")
    print_slow(f"Tus datos de conversación ahora viajarán encriptados a tu cerebro privado.")
    print("\n" + "="*70)
    
    print(f"\n{C_BOLD}{C_YELLOW}💡 Próximos pasos recomendados:{C_RESET}")
    print(f"  1. Ejecuta {C_CYAN}python example.py{C_RESET} para guardar y buscar tus primeros pensamientos de prueba.")
    print(f"  2. Lee el {C_CYAN}README.md{C_RESET} para aprender cómo integrar MEION con tu chatbot o agente de IA.")
    print(f"\n{C_PURPLE}¡Gracias por expandir tu cerebro digital con MEION!{C_RESET}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{C_RED}❌ Instalación cancelada por el usuario.{C_RESET}\n")
