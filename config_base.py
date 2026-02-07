from pathlib import Path

# ==========================================================
# Define rutas y parámetros comunes para LLM, RAG y almacenamiento.
# ==========================================================

# === Rutas base ===

# Ruta absoluta a la raíz del repositorio
ROOT_DIR = Path(__file__).resolve().parent

# Carpeta de bases vectoriales persistentes (ChromaDB)
CHROMA_PATH = ROOT_DIR / "chroma_db"

# Carpeta de aplicación
APP_PATH = ROOT_DIR / "app"

# Carpeta de documentos
DOCUMENTS_DIR = ROOT_DIR / "app" / "documents"

# === Configuración técnica ===

# Nombre de la colección de documentos en la base de datos
COLLECTION_NAME = "document_collection"

# Modelos LLMs default 
OPENAI_LLM_MODEL = "gpt-4o-mini"
GOOGLE_LLM_MODEL = "gemini-2.5-flash"
GROQ_LLM_MODEL = "openai/gpt-oss-120b"