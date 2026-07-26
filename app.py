import streamlit as st

from style import (
    load_base_style,
    render_logo_header,
    render_footer,
    LIGHT_BLUE,
    PALE_BLUE,
)

st.set_page_config(
    page_title="Orion's Eye",
    page_icon="assets/logo_dark.png",
    layout="wide",
    initial_sidebar_state="expanded",
)

load_base_style()
render_logo_header()

# ---------------- HERO ----------------
col1, col2 = st.columns([1.3, 1])
with col1:
    st.markdown('<span class="oe-pill">Jaguar Space · Call for Proposals</span>', unsafe_allow_html=True)
    st.markdown(
        '<div class="oe-hero-title">Democratizando la<br>ciencia espacial en<br>Centroamérica</div>',
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <p class="oe-subtitle">
        Orion's Eye es un sistema de seguimiento de estrellas de bajo costo,
        basado en espectrometría, que integra herramientas ópticas,
        electrónicas y digitales en una plataforma accesible para la
        observación y el análisis espectral en tiempo real.
        </p>
        """,
        unsafe_allow_html=True,
    )
    st.write("")
    st.page_link("pages/1_Sobre_el_Proyecto.py", label="🔭  Conocer el proyecto")

with col2:
    st.image("assets/hero_bg.jpg", width='stretch')

st.markdown('<hr class="oe-divider">', unsafe_allow_html=True)

# ---------------- ¿QUÉ ES ORION'S EYE? ----------------
st.markdown("### ¿De qué trata el proyecto?")
c1, c2, c3 = st.columns(3)
cards = [
    ("🔬", "Espectrometría accesible",
     "La luz es el mensajero del cosmos: estudiamos cómo interactúa con la "
     "materia para conocer composición, temperatura y movimiento de objetos celestes."),
    ("🛰️", "Fines educativos y de divulgación",
     "Una plataforma pensada para estudiantes, educadores y astrónomos "
     "aficionados que quieren explorar el universo con herramientas propias."),
    ("🌎", "Con el respaldo de Jaguar Space",
     "Buscamos facilitar el acceso a herramientas astronómicas y promover el "
     "aprendizaje práctico en STEM en la región."),
]
for col, (icon, title, text) in zip([c1, c2, c3], cards):
    with col:
        st.markdown(
            f"""
            <div class="oe-card">
                <div style="font-size:1.8rem;">{icon}</div>
                <div style="font-family:'Sora',sans-serif; font-weight:700; font-size:1.05rem; margin:0.5rem 0 0.4rem 0; color:{LIGHT_BLUE};">{title}</div>
                <div class="oe-team-meta">{text}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown('<hr class="oe-divider">', unsafe_allow_html=True)

# ---------------- REPRESENTANDO MÚLTIPLES NACIONES ----------------
st.markdown("### Un equipo multidisciplinario y multinacional")
st.markdown(
    """
    <p class="oe-team-meta" style="font-size:1rem;">
    Orion's Eye es un proyecto impulsado por un equipo de jóvenes de
    Guatemala, Costa Rica, Nicaragua y El Salvador, con trayectorias en
    ingeniería, tecnología, comunicación y ciencia — unidos para hacer la
    astronomía más accesible en Centroamérica.
    </p>
    """,
    unsafe_allow_html=True,
)

paises = ["Guatemala", "Costa Rica", "Nicaragua", "El Salvador"]
pcols = st.columns(4)
for col, pais in zip(pcols, paises):
    with col:
        st.markdown(
            f"""
            <div class="oe-card" style="text-align:center;">
                <div style="font-size:1.6rem;">🌐</div>
                <div class="oe-team-name" style="text-align:center;">{pais}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.write("")
nav1, nav2 = st.columns(2)
with nav1:
    st.page_link("pages/2_Conoce_al_Equipo.py", label="👥  Conoce al equipo completo")
with nav2:
    st.page_link("pages/3_Noticias.py", label="📰  Ver noticias y avances")

render_footer()
