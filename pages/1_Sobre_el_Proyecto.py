import streamlit as st

from style import load_base_style, render_logo_header, render_footer, LIGHT_BLUE

st.set_page_config(page_title="Sobre el Proyecto · Orion's Eye", page_icon="assets/logo_dark.png", layout="wide")

load_base_style()
render_logo_header("Sobre el proyecto")

st.markdown('<div class="oe-hero-title" style="font-size:2.3rem;">Sobre Orion\'s Eye</div>', unsafe_allow_html=True)
st.markdown(
    """
    <p class="oe-subtitle">
    Entendiendo el universo a través de la luz: la espectrometría estudia cómo
    la luz interactúa con la materia. Cada objeto celeste deja un patrón único
    en la luz que emite o refleja — descifrarlo nos permite conocer su
    composición, temperatura y movimiento.
    </p>
    """,
    unsafe_allow_html=True,
)

st.markdown('<hr class="oe-divider">', unsafe_allow_html=True)

# ---------------- MISIÓN / VISIÓN ----------------
m, v = st.columns(2)
with m:
    st.markdown(
        f"""
        <div class="oe-card">
            <span class="oe-pill">Misión</span>
            <p class="oe-team-meta" style="font-size:1rem; color:white; opacity:1;">
            Diseñar y desarrollar un sistema de seguimiento asequible y de
            código abierto basado en espectrometría, que empodere a
            estudiantes, educadores y astrónomos aficionados para explorar y
            comprender el universo mediante la observación en tiempo real y
            el análisis espectral.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with v:
    st.markdown(
        f"""
        <div class="oe-card">
            <span class="oe-pill">Visión</span>
            <p class="oe-team-meta" style="font-size:1rem; color:white; opacity:1;">
            Democratizar el acceso a la ciencia espacial en los países en
            desarrollo de Centroamérica, haciendo que las herramientas
            astronómicas avanzadas sean inclusivas, asequibles e
            inspiradoras.
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<hr class="oe-divider">', unsafe_allow_html=True)

# ---------------- OBJETIVOS ----------------
st.markdown("### Objetivos del proyecto")
o1, o2 = st.columns(2)
with o1:
    st.markdown(
        """
        <div class="oe-card">
        <b>1. Sistema de seguimiento celeste</b>
        <p class="oe-team-meta">
        Crear un sistema práctico y asequible que combine control motorizado,
        sensores, tecnología de espectrometría y una aplicación móvil para
        visualización en tiempo real.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )
with o2:
    st.markdown(
        """
        <div class="oe-card">
        <b>2. Plataforma y educación</b>
        <p class="oe-team-meta">
        Crear una plataforma web colaborativa y producir documentación
        educativa accesible para garantizar usabilidad, participación
        comunitaria y un impacto de largo plazo en la educación astronómica
        en Centroamérica y más allá.
        </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown('<hr class="oe-divider">', unsafe_allow_html=True)

# ---------------- ¿POR QUÉ ES IMPORTANTE? ----------------
st.markdown("### ¿Por qué es importante?")
r1, r2, r3 = st.columns(3)
razones = [
    ("💡", "Accesible y asequible",
     "Hace que la observación espacial y la espectrometría sean accesibles, "
     "especialmente para regiones con menos recursos."),
    ("🧩", "Menos barreras técnicas",
     "Reduce las barreras técnicas para estudiantes, educadores y "
     "astrónomos aficionados."),
    ("🚀", "Educación STEM inclusiva",
     "Promueve una educación STEM inclusiva e inspira a nuevas generaciones "
     "de exploradores del espacio."),
]
for col, (icon, title, text) in zip([r1, r2, r3], razones):
    with col:
        st.markdown(
            f"""
            <div class="oe-card">
                <div style="font-size:1.6rem;">{icon}</div>
                <div style="font-family:'Sora',sans-serif; font-weight:700; margin:0.5rem 0 0.4rem 0; color:{LIGHT_BLUE};">{title}</div>
                <div class="oe-team-meta">{text}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

st.markdown('<hr class="oe-divider">', unsafe_allow_html=True)

# ---------------- APLICACIONES ----------------
st.markdown("### Usos comunes de la espectrometría")
st.markdown(
    """
    <p class="oe-team-meta" style="font-size:1rem;">
    Astronomía · Medicina · Agricultura · Exploración espacial
    </p>
    <p class="oe-team-meta" style="font-style:italic;">
    "Al descifrar la luz, convertimos puntos distantes en historias sobre su
    origen y su naturaleza."
    </p>
    """,
    unsafe_allow_html=True,
)

render_footer()
