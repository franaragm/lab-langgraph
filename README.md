# LangGraph Lab


## 🐍 Requisitos de Python

* Python 3.13.2 (recomendado, probado en macOS Apple Silicon y Windows)
* Python 3.11 (ideal para Mac Intel)

⚠️ No usar Python 3.14+, ya que rompe compatibilidad con:

* Pydantic
* ChromaDB
* LangChain Core

---

## 🚀 Instalación y uso

### 🔧 1) Crear entorno virtual

python -m venv .venv
source .venv/bin/activate      # macOS / Linux
.venv\Scripts\activate         # Windows

---

### 📦 2) Instalar dependencias

pip install -r requirements.txt
pip install -r requirements.lock

Para fijar nuevas dependencias:

pip freeze > requirements.lock

---

### 🔐 3) Configurar variables de entorno

cp .env.example .env

Editar `.env` con tus claves:

OPENAI_API_KEY=API_KEY_HERE
GOOGLEAI_API_KEY=API_KEY_HERE
OPENROUTER_API_KEY=API_KEY_HERE
OPENROUTER_BASE_URL=https://openrouter.ai/api/v1
GROQ_API_KEY=API_KEY_HERE
GROQ_BASE_URL=https://api.groq.com/openai/v1
ENV=dev

> Solo se usan las APIs que tengas configuradas; OpenAI y OpenRouter son opcionales según tu flujo.

---

### ▶️ 4) Ejecutar la aplicación

streamlit run run_app.py

Disponible en: [http://localhost:8501](http://localhost:8501)

---


## 📚 Recursos

* LangChain → [https://www.langchain.com/](https://www.langchain.com/)
* Streamlit → [https://streamlit.io/](https://streamlit.io/)
* ChromaDB → [https://www.trychroma.com/](https://www.trychroma.com/)
* Pydantic → [https://docs.pydantic.dev/](https://docs.pydantic.dev/)

---