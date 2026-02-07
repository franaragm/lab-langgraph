import streamlit as st


# ======================================================
# Configuración de la página
# ======================================================

st.set_page_config(
    page_title="Page Title",
    page_icon="🚀",
    layout="wide"
)

# ======================================================
# Inicialización del estado de sesión
# ======================================================
    
if "example_data" not in st.session_state:
    st.session_state.example_data = {}


# ======================================================
# Aplicación principal
# ======================================================

def main():
    """UI principal del sistema Helpdesk."""

    st.title("titulo")
    st.markdown("*Subtítulo o descripción breve del sistema*")

    

    # ==================================================
    # Sidebar
    # ==================================================
    with st.sidebar:
        st.header("📊 Panel de Control")
        st.metric("Tickets Activos", 8)

        # Estado del sistema RAG
        st.subheader("🔍 Estado RAG")
        

        st.subheader("🔄 Flujo del Sistema")
        st.text(
            """
            1. 📝 Usuario envía consulta
            2. 🤖 Clasificación automática
            3. 🔍 Búsqueda vectorial RAG
            4. 📊 Evaluación de confianza
            5. 👨‍💼 Escalado si es necesario
            6. ✅ Respuesta final
            """
        )

        st.subheader("⚙️ Configuración")
        if st.button("🗑️ Limpiar Tickets"):
            st.session_state.example_data = {}
            st.rerun()

    if not st.session_state.example_data:
        st.warning(
            "⚠️ no hay data "
        )
        return

    # ==================================================
    # Área principal
    # ==================================================
    col1, col2 = st.columns([1, 1])

    # ==================================================
    # col 1
    # ==================================================
    with col1:
        st.subheader("Col1")

        
                    
    # ==================================================
    # col 2
    # ==================================================
    with col2:
        st.subheader("Col2")

        

    # ==================================================
    # Footer
    # ==================================================
    st.markdown("---")

    st.markdown(
        """
        <div style='text-align: center'>
            <small>
                🚀 Powered by LangGraph · 🔍 ChromaDB · 🔄 Streaming · 💾 Checkpointing · 👨‍💼 Human-in-the-Loop
            </small>
        </div>
        """,
        unsafe_allow_html=True
    )
