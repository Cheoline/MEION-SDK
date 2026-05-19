# Arquitectura Completa del Sistema MEION 🧠🧬

Este documento presenta una guía visual y técnica detallada sobre cómo opera el ecosistema de **MEION**, desde la ingesta de datos por parte de las Inteligencias Artificiales y los usuarios, hasta el procesamiento molecular topológico (**QTOM V5**), compresión cromática (**ITOM**) y persistencia de memoria a largo plazo.

---

## 🗺️ Diagrama de Flujo y Arquitectura de MEION

El siguiente diagrama de arquitectura en formato **Mermaid** describe paso a paso cómo viaja la información dentro del cerebro digital de MEION.

```mermaid
graph TD
    %% Estilos de Nodos Premium
    classDef client fill:#001E3D,stroke:#00f2ff,stroke-width:2px,color:#fff;
    classDef gateway fill:#1A0033,stroke:#bd93f9,stroke-width:2px,color:#fff;
    classDef engine fill:#1F3C1F,stroke:#50fa7b,stroke-width:2px,color:#fff;
    classDef storage fill:#3A0007,stroke:#ff5555,stroke-width:2px,color:#fff;
    classDef maint fill:#332900,stroke:#f1fa8c,stroke-width:2px,color:#fff;

    %% 1. Capa de Clientes e Ingesta
    subgraph INGESTA ["Capa de Clientes (Ingesta)"]
        A1["💻 Dashboard Web (Usuario)"]:::client
        A2["🤖 Agentes de IA / Bots (MEION-SDK)"]:::client
    end

    %% 2. Pasarela de Enrutamiento y Seguridad
    subgraph ROUTER ["API Gateway (dashboard.py)"]
        B1{"🔑 Validar API Key<br>(Decorator require_api_key)"}:::gateway
        B2["📡 Endpoints RESTful"]:::gateway
        
        B2 -->|/api/memorize| B3["📥 Ingesta de Recuerdos"]:::gateway
        B2 -->|/api/search| B4["🔍 Consulta Semántica"]:::gateway
        B2 -->|/api/itom/compress| B5["📸 Procesamiento Visual"]:::gateway
    end

    %% Enlaces Ingesta -> Router
    A1 & A2 ==>|Peticiones HTTP / JSON / Form-Data| B1
    B1 -->|Acceso Autorizado| B2

    %% 3. Motores de Procesamiento Molecular (Compresión)
    subgraph ENGINES ["Motores de Transmutación Molecular"]
        %% Procesamiento de Texto
        subgraph QTOM ["Topological Memory Engine (QTOM V5)"]
            C1["📝 Entrada de Texto Plano"]:::engine
            C2["📐 Topologización y Mapeo en Rejilla"]:::engine
            C3["🧬 Codificación en Stoms (PUA Symbols)"]:::engine
            C4["📚 Diccionario Compartido (Léxico)"]:::engine

            C1 --> C2 --> C3
            C3 <-->|Consultar/Registrar Palabra| C4
        end

        %% Procesamiento de Imágenes
        subgraph ITOM ["Chromatic Compression Engine (ITOM)"]
            D1["🖼️ Entrada de Imagen (PNG/JPG)"]:::engine
            D2["🎨 Descomposición de Canales Cromáticos"]:::engine
            D3["📦 Compresión Física de Matriz (.itom)"]:::engine

            D1 --> D2 --> D3
        end
    end

    %% Enlaces Router -> Motores
    B3 -->|Guardar Texto| C1
    B5 -->|Subir Imagen| D1

    %% 4. Capa de Persistencia y Base de Datos Atómica
    subgraph STORAGE ["Núcleo de Persistencia (meion_brain.db)"]
        E1[("💾 Tabla: usuarios<br>(Credenciales y API Keys)")]:::storage
        E2[("🧬 Tabla: recuerdos<br>(Texto Molecular Cifrado)")]:::storage
        E3[("⚡ FTS5 Virtual Table<br>(Búsquedas Rápidas Indexadas)")]:::storage
        E4[("📸 Tabla: itom_metadata<br>(Registro de Imágenes)")]:::storage
        E5[("🕸️ Tabla: memory_connections<br>(Enlaces del Grafo Neuronal)")]:::storage

        %% Flujo Interno base de datos
        E2 -->|Triggers automáticos| E3
        E2 <-->|Relaciones moleculares por stoms compartidos| E5
    end

    %% Enlaces Motores -> Persistencia
    C3 -->|Texto Molecular Generado| E2
    D3 -->|Guardar Imagen .itom en Disco VPS| D4["📂 Directorio local: static/uploads/"]:::storage
    D3 -->|Guardar peso y metadata| E4

    %% 5. Búsqueda y Recuperación Semántica Jaccard
    subgraph RETRIEVAL ["Motor de Recuperación Cognitiva"]
        F1["🔎 Búsqueda Semántica Jaccard"]:::engine
        F2["🔄 Coincidencia de Stoms (Query vs Cerebro)"]:::engine
        F3["🤖 Prompt Context Inyection (Format AI)"]:::engine

        B4 --> F1
        F1 <-->|Escaneo y Comparación| E2
        F1 --> F2 --> F3
    end

    %% Retorno de Información
    F3 ==>|Inyectar contexto optimizado en tiempo real| A2
    E3 -->|Resultados rápidos de coincidencia| B4

    %% 6. Ciclo de Mantenimiento y Estabilidad
    subgraph MAINTENANCE ["Ciclo de Consolidación y Mantenimiento"]
        G1["⚙️ Mantenimiento Automático (02:00 AM)"]:::maint
        G2["🧹 Purga de archivos temporales desvinculados"]:::maint
        G3["📊 Reciclaje de stoms no utilizados en Léxico"]:::maint

        G1 --> G2 & G3
        G3 -.->|Actualizar Léxico| C4
    end
```

---

## ⚙️ Explicación Técnica de las Capas

### 1. Capa de Ingesta (Clientes)
Los recuerdos pueden provenir de dos fuentes principales:
* **Dashboard Web:** El usuario interactúa directamente de manera visual en una interfaz futurista (Dark Mode, Glassmorphism, animaciones CSS).
* **Agentes Inteligentes y Bots (MEION-SDK):** Sistemas externos (asistentes GPT, bots de Telegram, aplicaciones de escritorio) envían información a través del conector oficial en Python.

### 2. Capa de Seguridad y Ruteo (API Gateway)
Todo tráfico entrante pasa obligatoriamente por el decorador `@require_api_key` en `dashboard.py`:
* **Aislamiento:** Cada usuario cuenta con un espacio lógico aislado y encriptado. Una API Key comprometida no compromete el cerebro de otros usuarios.
* **Canales Separados:** Las solicitudes se separan en flujos textuales (/api/memorize) y cromáticos visuales (/api/itom/compress).

### 3. Motores de Transmutación Molecular
Es el corazón algorítmico y de compresión matemática de MEION:
* **QTOM V5:** No almacena palabras en texto plano. Analiza las sílabas del texto, las proyecta en una rejilla matemática tridimensional y las mapea en símbolos moleculares especiales (**Stoms**) que pertenecen al rango PUA (*Private Use Area* de Unicode). Esto permite representar ideas muy largas utilizando una fracción mínima de espacio en disco.
* **ITOM:** Descompone las imágenes en matrices de canales cromáticos moleculares y las guarda directamente en archivos ligeros `.itom`, logrando porcentajes de compresión asombrosos (habitualmente superiores al **70% de ahorro**).

### 4. Núcleo de Persistencia (SQLite & Disco)
Toda la información reside en `meion_brain.db`:
* **FTS5:** Permite realizar búsquedas rápidas textuales indexadas de manera extremadamente eficiente.
* **Triggers de SQLite:** Triggers automatizados sincronizan las inserciones, ediciones o eliminaciones de la tabla `recuerdos` con la tabla virtual de búsqueda FTS5 en tiempo real.
* **Grafo de Recuerdos (`memory_connections`):** Conecta dinámicamente recuerdos que comparten stoms (conceptos) similares para construir la red neuronal del usuario.

### 5. Recuperación Semántica Jaccard
Cuando una IA realiza una consulta (ej: *"¿Qué película le gusta a Sofia?"*):
1. MEION **comprime la consulta de la IA** a stoms.
2. Utiliza el **Coeficiente de Similitud Jaccard** para comparar la intersección de stoms de la pregunta con todos los recuerdos guardados del usuario en la base de datos.
3. Ordena los resultados por mayor score semántico y fecha.
4. Genera un bloque de contexto limpio y formateado listo para inyectarse directamente en el prompt del LLM (GPT, Claude, Llama).

---

> [!TIP]
> **Privacidad Absoluta:** Debido a que el texto se guarda en formato molecular (stoms codificados en PUA), si un intruso lograra acceder a la base de datos `meion_brain.db`, solo vería cadenas de símbolos ininteligibles. Solo el usuario autenticado con su API Key correspondiente tiene el poder de restaurar las moléculas a texto legible.
