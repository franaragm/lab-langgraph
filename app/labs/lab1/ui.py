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
    """UI principal de la aplicación"""

    st.title("titulo App")
    st.markdown("*Subtítulo o descripción breve del sistema*")
    
    st.text_input("Input de ejemplo", key="example_input")
    if st.button("Guardar dato en sesión"):
        st.session_state.example_data["input"] = st.session_state.example_input
        st.success("Dato guardado en sesión")
        
    if st.session_state.example_data.get("input"):
        st.info(f"Dato en sesión: {st.session_state.example_data['input']}")
    else:
        st.warning("⚠️ No hay datos en sesión")

    # ==================================================
    # Sidebar
    # ==================================================
    with st.sidebar:
        st.header("Sidebar Title")
        st.metric("Cantidad de caracteres", len(st.session_state.example_data.get("input", "")))

        # Estado del sistema RAG
        st.subheader("Subtítulo del sistema")
        

        st.subheader("Sumario del proceso ejemplo RAG")
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
        if st.button("🗑️ Limpiar Data"):
            st.session_state.example_data = {}
            st.rerun()

    

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
