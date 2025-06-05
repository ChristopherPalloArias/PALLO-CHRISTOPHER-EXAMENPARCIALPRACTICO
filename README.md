# 🧠 Clasificador Inteligente de Mensajes con IA

Este proyecto implementa una solución completa de clasificación automática de mensajes utilizando **Gemini** (Google AI) y una interfaz gráfica en **Streamlit**, expuesta mediante una **API REST con FastAPI**.

---
## 👨‍💻 Autor

**Christopher Pallo -**
SI10 P01 – Sistemas de Información -
Universidad Central del Ecuador

---
## 🎬 Video tutorial
[![Ver en YouTube](https://img.youtube.com/vi/0XkFtcwQtRU/0.jpg)](https://youtu.be/0XkFtcwQtRU)

Haz clic en la imagen o visita el siguiente enlace para ver la presentación completa del proyecto:

🔗 https://youtu.be/0XkFtcwQtRU

---
## 🧩 Tecnologías utilizadas

- 🐍 Python 3.11+
- ⚡ FastAPI
- 🎨 Streamlit
- 🤖 Gemini API
- 📦 Variables de entorno con `.env`
- 🧪 Pruebas tipo Postman con archivo `.http` en IntelliJ
- 🎨 CSS personalizado (`styles.css`)

---

## 📁 Estructura del proyecto

```
FastAPIProject/
├── backend/
│   ├── main.py                 # API REST (FastAPI)
│   └── classifier_service.py   # Lógica de clasificación con Gemini
├── frontend/
│   ├── streamlit_app.py        # Interfaz Streamlit
│   └── styles.css              # Estilos personalizados
├── tests/
│   └── api_test.http           # Pruebas tipo Postman (IntelliJ)
├── .env                        # Clave de API Gemini
└── README.md                   # Documentación del proyecto
├── .gitignore                  # Archivos y carpetas que serán ignorados en el repositorio
├── requirements.txt            # Dependencias necesarias para ejecutar backend y frontend
```

---

## 🚀 Cómo ejecutar el proyecto

### 1. Clona el repositorio

```bash
git clone https://github.com/ChristopherPalloArias/PALLO-CHRISTOPHER-EXAMENPARCIALPRACTICO.git
cd PALLO-CHRISTOPHER-EXAMENPARCIALPRACTICO
```

### 2. Crea y activa un entorno virtual

```bash
python3 -m venv .venv
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows
```

### 3. Instala las dependencias

```bash
pip install -r requirements.txt
```

> Asegúrate de tener un archivo `.env` con el contenido:
> ```
> GEMINI_API_KEY=tu_clave_de_api
> ```

### 4. Ejecuta el backend (FastAPI)

```bash
cd backend
uvicorn main:app --reload
```

Disponible en: [http://localhost:8000](http://localhost:8000)

### 5. Ejecuta el frontend (Streamlit)

> 💡 **Importante:** Si abriste una nueva terminal para el frontend, asegúrate de **activar nuevamente el entorno virtual**, ya que cada terminal tiene su propio contexto.

```bash
# Si estás en una nueva terminal, activa el entorno:
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate         # Windows

# Luego ejecuta el frontend:
cd frontend
streamlit run streamlit_app.py

```

Disponible en: [http://localhost:8501](http://localhost:8501)

---

## 🔎 Pruebas con archivo `.http` en IntelliJ

Abre el archivo `test_main.http` y prueba las siguientes peticiones:

### Verificar API
```http
GET http://localhost:8000/
```

### Clasificar mensaje urgente
```http
POST http://localhost:8000/clasificar
Content-Type: application/json

{
  "texto": "¡Hay un incendio en el laboratorio! Necesitamos ayuda inmediata."
}
```

### Clasificar mensaje moderado
```http
POST http://localhost:8000/clasificar
Content-Type: application/json

{
  "texto": "He notado que algunos correos no llegan a tiempo. Sería bueno revisarlo en los próximos días."
}
```

### Clasificar mensaje normal
```http
POST http://localhost:8000/clasificar
Content-Type: application/json

{
  "texto": "Les recuerdo que la reunión del viernes fue reprogramada para el lunes a las 10am."
}
```

---

## 📘 Documentación  de la API

FastAPI genera automáticamente una interfaz de documentación accesible desde tu navegador.

Una vez que el backend esté ejecutándose, visita:

- [http://localhost:8000/docs](http://localhost:8000/docs) → Documentación Swagger UI  
- [http://localhost:8000/openapi.json](http://localhost:8000/openapi.json) → Esquema OpenAPI en formato JSON

Desde `/docs` puedes:
- Ver los endpoints disponibles (`GET /`, `POST /clasificar`)
- Probar la API directamente desde el navegador
- Ver y validar los esquemas de entrada (`MensajeEntrada`)
---

## ✅ Funcionalidades implementadas

- ✔️ Clasificación automática con IA (Gemini)
- ✔️ API REST con FastAPI
- ✔️ Interfaz visual en Streamlit
- ✔️ Estilo personalizado con CSS e íconos Font Awesome
- ✔️ Botones de ejemplo rápido y limpieza inmediata
- ✔️ Pruebas usando archivo `.http` desde IntelliJ



