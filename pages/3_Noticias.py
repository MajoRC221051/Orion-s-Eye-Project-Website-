import streamlit as st

from style import load_base_style, render_logo_header, render_footer, LIGHT_BLUE
from data.noticias import NOTICIAS

st.set_page_config(page_title="Noticias · Orion's Eye", page_icon="assets/logo_dark.png", layout="wide")

load_base_style()
render_logo_header("Noticias y avances del proyecto")

st.markdown('<div class="oe-hero-title" style="font-size:2.3rem;">Noticias</div>', unsafe_allow_html=True)
st.markdown(
    '<p class="oe-subtitle">Avances realizados por los equipos de Hardware y '
    'Software durante la primera etapa del proyecto, y lo que viene después.</p>',
    unsafe_allow_html=True,
)

# ---------------- FILTROS ----------------
categorias = ["Todas"] + sorted({n["categoria"] for n in NOTICIAS})
filtro = st.radio("Filtrar por categoría", categorias, horizontal=True, label_visibility="collapsed")

noticias_mostrar = NOTICIAS if filtro == "Todas" else [n for n in NOTICIAS if n["categoria"] == filtro]

st.markdown('<hr class="oe-divider">', unsafe_allow_html=True)

if not noticias_mostrar:
    st.info("Todavía no hay noticias en esta categoría.")

for n in noticias_mostrar:
    img_col, text_col = st.columns([1, 2]) if n["imagen"] else (None, st.columns([1])[0])

    with st.container():
        st.markdown('<div class="oe-card" style="margin-bottom:1.2rem;">', unsafe_allow_html=True)
        c1, c2 = st.columns([1, 2]) if n["imagen"] else (None, None)
        if n["imagen"]:
            with c1:
                st.image(n["imagen"], width='stretch')
            with c2:
                st.markdown(f'<span class="oe-news-date">{n["fecha"]} · {n["categoria"]}</span>', unsafe_allow_html=True)
                st.markdown(f'<div class="oe-team-name" style="font-size:1.3rem;">{n["titulo"]}</div>', unsafe_allow_html=True)
                st.markdown(f'<div class="oe-team-meta" style="font-size:0.95rem;">{n["resumen"]}</div>', unsafe_allow_html=True)
        else:
            st.markdown(f'<span class="oe-news-date">{n["fecha"]} · {n["categoria"]}</span>', unsafe_allow_html=True)
            st.markdown(f'<div class="oe-team-name" style="font-size:1.3rem;">{n["titulo"]}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="oe-team-meta" style="font-size:0.95rem;">{n["resumen"]}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

st.info(
    "💡 ¿Quieres agregar una noticia nueva? Edita el archivo "
    "`data/noticias.py` — no necesitas tocar el resto del código.",
    icon="📝",
)

render_footer()
