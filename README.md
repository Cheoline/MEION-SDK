# 🧠 MEION-SDK: Memoria Persistente y Molecular para IAs y Agentes

---

## 🚫 MEION NO ES UN CHATBOT

**MEION es un motor avanzado de memoria persistente molecular y semántica.** 

A diferencia de las bases de datos de vectores tradicionales o las memorias de sesión efímeras, MEION actúa como un **núcleo de almacenamiento de memoria a largo plazo unificado**. Está específicamente diseñado para que **Inteligencias Artificiales, Agentes Autónomos, Chatbots y Asistentes Cognitivos se conecten a él mediante su API.**

Al conectar tus agentes a MEION, les otorgas la habilidad de recordar conversaciones previas, hechos exactos sobre tus preferencias, contexto histórico extendido y datos corporativos confidenciales, **eliminando por completo las alucinaciones de la IA** y garantizando que **nunca olviden nada.**

---

## 🔒 Privacidad Absoluta y Cifrado Molecular

Tus recuerdos y pensamientos están completamente blindados:
- **Aislamiento de Usuario por API Key:** Tu clave API es personal e intransferible. Tus recuerdos están 100% aislados; ningún otro usuario o agente en la red de MEION puede acceder a ellos.
- **Criptografía Molecular (Stoms):** Los recuerdos textuales ingresados se codifican, fragmentan y cifran en micro-coordenadas 3D compactas (*stoms*) a nivel de base de datos. Si el servidor físico fuera inspeccionado, tu información sería completamente ilegible e indescifrable.
- **Tránsito Blindado:** Toda comunicación entre tus agentes inteligentes y los servidores de MEION viaja bajo cifrado HTTPS seguro de extremo a extremo.

---

## 🚀 Instalación Rápida

El repositorio público de MEION-SDK contiene únicamente el conector de cliente y guías de uso. Los algoritmos de compresión molecular (QTOM V5) e ITOM Cromático residen de manera segura en la nube privada de **meionia.com**, garantizando que tu código no pueda ser plagiado ni filtrado.

### 1. Clona este repositorio o descarga los archivos
```bash
git clone https://github.com/Cheoline/MEION-SDK.git
cd MEION-SDK
```

### 2. Ejecuta el instalador interactivo
Este comando iniciará el asistente de terminal interactivo para configurar tu entorno en segundos:
```bash
python install.py
```

> **🔑 ¿Cómo obtengo mi API Key?**
> Tu API Key única se genera **de forma automática al registrarte y crear tu cuenta en [meionia.com](https://meionia.com)**. Solo debes iniciar sesión, ir a tu panel de configuración y copiar tu clave para ingresarla en el instalador.

---

## 💻 Integración Rápida con Python

Integrar la memoria persistente en tu código de IA toma menos de 5 líneas con nuestro cliente oficial:

```python
from meion_client import MeionClient

# 1. Inicializar el cliente (carga automáticamente las llaves de tu archivo .env local)
client = MeionClient()

# 2. Enviar un nuevo pensamiento para que tu IA lo memorice para siempre
client.memorize("El color favorito de mi cliente es el azul cobalto y prefiere reportes mensuales en PDF.")

# 3. Buscar recuerdos semánticamente en el prompt de tu IA
recuerdos = client.search("¿Qué color prefiere mi cliente?")
print(recuerdos)
```

---

## 🤖 Formato Especial para Inteligencias Artificiales (Gemma, GPT, Claude)

Si estás construyendo un chatbot o agente autónomo, necesitas proveerle el historial de recuerdos de forma ordenada y cronológica para evitar alucinaciones. MEION lo hace por ti automáticamente mediante el parámetro `format_ai=True`:

```python
# Realiza la búsqueda semántica y devuelve un bloque de contexto pre-formateado listo para tu LLM
ai_context = client.search("¿Qué le gusta a mi cliente?", format_ai=True)

# El resultado contendrá las instrucciones de prioridad cronológica y las memorias ordenadas
prompt_completo = f"""
Eres un asistente corporativo de alto rendimiento. Utiliza el siguiente bloque de memoria 
como la verdad absoluta para responder la duda del usuario:

{ai_context['context']}

Pregunta del Usuario: ¿Qué le gusta a mi cliente?
Respuesta:
"""
```

---

## 📡 Referencia de la API de meionia.com (Para otros lenguajes)

Si deseas conectar tus aplicaciones en **Node.js, Go, PHP o Rust**, puedes consumir los endpoints REST directamente. Toda petición requiere la cabecera `X-API-Key`.

### 1. Guardar Recuerdos
- **Endpoint:** `POST /api/memorize`
- **Cabeceras:**
  ```http
  X-API-Key: tu_api_key_personal
  Content-Type: application/json
  ```
- **Cuerpo del Mensaje (JSON):**
  ```json
  {
    "texto": "Sofia prefiere reuniones los miércoles por la tarde."
  }
  ```

### 2. Buscar Recuerdos Semánticamente
- **Endpoint:** `GET /api/search`
- **Cabeceras:**
  ```http
  X-API-Key: tu_api_key_personal
  ```
- **Parámetros de Consulta (Query Params):**
  - `q`: Consulta de búsqueda semántica (ej: `¿cuándo prefiere reunirse Sofia?`).
  - `format`: Usa `ai` para recibir el bloque estructurado listo para prompts.
  - `desde`: Filtrar recuerdos desde una fecha específica (`YYYY-MM-DD`).
  - `hasta`: Filtrar recuerdos hasta una fecha específica (`YYYY-MM-DD`).

---

## 🎨 Compresión Cromática ITOM y Grafo Molecular

- **¿Qué es ITOM?:** Una tecnología exclusiva de mapeo cromático molecular que asocia y comprime imágenes ligadas a recuerdos de texto, permitiendo a tus Agentes Inteligentes tener "memoria cromática visual".
- **Visualización en Grafo:** Accede al panel interactivo tridimensional de tu cuenta en [meionia.com](https://meionia.com) para observar las relaciones moleculares compartidas (*stoms*) entre tus ideas y recuerdos en tiempo real.

---

*Desarrollado y optimizado por el equipo de ingeniería de **MEIONia**.*
