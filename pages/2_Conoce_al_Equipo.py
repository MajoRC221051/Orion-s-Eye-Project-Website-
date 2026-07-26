import streamlit as st

from style import load_base_style, render_logo_header, render_footer
from data.equipo import EQUIPO

st.set_page_config(page_title="Conoce al Equipo · Orion's Eye", page_icon="assets/logo_dark.png", layout="wide")

load_base_style()
render_logo_header("Conoce al equipo")

st.markdown('<div class="oe-hero-title" style="font-size:2.3rem;">El equipo</div>', unsafe_allow_html=True)
st.markdown(
    """
    <p class="oe-subtitle">
    Orion's Eye es un proyecto impulsado por un equipo multidisciplinario de
    jóvenes de Guatemala, Costa Rica, Nicaragua y El Salvador. Con
    trayectorias en ingeniería, tecnología, comunicación y ciencia, unimos
    habilidades técnicas y creativas para hacer la astronomía más accesible
    en Centroamérica, contando siempre con el respaldo de asesoría
    especializada.
    </p>
    """,
    unsafe_allow_html=True,
)

st.markdown('<hr class="oe-divider">', unsafe_allow_html=True)

# Grid de 4 columnas
cols_per_row = 4
rows = [EQUIPO[i:i + cols_per_row] for i in range(0, len(EQUIPO), cols_per_row)]

for row in rows:
    cols = st.columns(cols_per_row)
    for col, persona in zip(cols, row):
        with col:
            st.image(persona["foto"], width='stretch')
            st.markdown(
                f"""
                <div class="oe-team-name">{persona['nombre']}</div>
                <div class="oe-team-role">{persona['rol']}</div>
                <div class="oe-team-meta">
                    🌎 {persona['pais']}<br>
                    🎓 {persona['universidad']}
                </div>
                """,
                unsafe_allow_html=True,
            )
            st.write("")

render_footer()
