"""
Módulo de estilos compartidos para el sitio de Orion's Eye.
Centraliza la paleta de marca, tipografía y CSS reutilizable
para que las 4 páginas del sitio luzcan consistentes.
"""

import base64
from pathlib import Path

import streamlit as st

ASSETS = Path(__file__).parent / "assets"

# ---- Paleta oficial de marca (Identidad_Orion's Eye) ----
NAVY = "#10122d"       # fondo principal
PURPLE = "#4e4177"     # acento secundario
BLUE = "#3a609f"       # acento primario
LIGHT_BLUE = "#88a5df" # acento claro
PALE_BLUE = "#c8dcf5"  # texto / detalles claros
WHITE = "#f4f6fc"

FONT_HEADING = "'Sora', 'Poppins', sans-serif"   # alternativa web a Codec Pro
FONT_BODY = "'Poppins', sans-serif"


def _b64(path: Path) -> str:
    return base64.b64encode(path.read_bytes()).decode()


def load_base_style():
    """Inyecta fuentes, colores y componentes CSS reutilizables."""
    hero_bg_b64 = _b64(ASSETS / "hero_bg.jpg")

    st.markdown(
        f"""
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700;800&family=Poppins:wght@300;400;500;600;700&display=swap" rel="stylesheet">

        <style>
        html, body, [class*="css"]  {{
            font-family: {FONT_BODY};
        }}
        h1, h2, h3, h4 {{
            font-family: {FONT_HEADING} !important;
            letter-spacing: 0.3px;
        }}

        /* Fondo general con textura de estrellas sutil */
        [data-testid="stAppViewContainer"] {{
            background:
                linear-gradient(180deg, rgba(16,18,45,0.94) 0%, rgba(16,18,45,0.985) 55%, {NAVY} 100%),
                url("data:image/jpg;base64,{hero_bg_b64}");
            background-size: cover;
            background-attachment: fixed;
            background-position: center;
        }}

        [data-testid="stSidebar"] {{
            background: linear-gradient(180deg, {NAVY} 0%, {PURPLE} 220%);
            border-right: 1px solid rgba(136,165,223,0.15);
        }}

        [data-testid="stHeader"] {{
            background: rgba(16,18,45,0.0);
        }}

        /* Tarjetas genéricas */
        .oe-card {{
            background: linear-gradient(160deg, rgba(78,65,119,0.35), rgba(16,18,45,0.55));
            border: 1px solid rgba(136,165,223,0.25);
            border-radius: 18px;
            padding: 1.6rem 1.8rem;
            height: 100%;
            box-shadow: 0 4px 24px rgba(0,0,0,0.25);
        }}

        .oe-pill {{
            display: inline-block;
            padding: 0.25rem 0.9rem;
            border-radius: 999px;
            background: rgba(136,165,223,0.18);
            border: 1px solid rgba(136,165,223,0.45);
            color: {PALE_BLUE};
            font-size: 0.78rem;
            font-weight: 600;
            letter-spacing: 0.6px;
            text-transform: uppercase;
            margin-bottom: 0.6rem;
        }}

        .oe-hero-title {{
            font-family: {FONT_HEADING};
            font-weight: 800;
            font-size: 3.1rem;
            line-height: 1.05;
            background: linear-gradient(90deg, {WHITE} 10%, {LIGHT_BLUE} 60%, {BLUE} 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 0.2rem;
        }}

        .oe-subtitle {{
            color: {PALE_BLUE};
            font-size: 1.15rem;
            font-weight: 300;
            max-width: 720px;
        }}

        .oe-divider {{
            height: 1px;
            border: none;
            background: linear-gradient(90deg, transparent, {LIGHT_BLUE}, transparent);
            margin: 2.2rem 0;
            opacity: 0.5;
        }}

        .oe-team-name {{
            font-family: {FONT_HEADING};
            font-weight: 700;
            font-size: 1.15rem;
            color: {WHITE};
            margin: 0.7rem 0 0.15rem 0;
        }}
        .oe-team-role {{
            color: {LIGHT_BLUE};
            font-weight: 600;
            font-size: 0.92rem;
            margin-bottom: 0.3rem;
        }}
        .oe-team-meta {{
            color: {PALE_BLUE};
            font-size: 0.85rem;
            opacity: 0.85;
            line-height: 1.5;
        }}

        .oe-news-date {{
            color: {LIGHT_BLUE};
            font-size: 0.82rem;
            font-weight: 600;
            letter-spacing: 0.4px;
            text-transform: uppercase;
        }}

        img {{
            border-radius: 14px;
        }}

        [data-testid="stImage"] img {{
            border-radius: 14px;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


def render_logo_header(subtitle: str | None = None):
    """Encabezado con el logo de Orion's Eye, consistente en todas las páginas."""
    logo_b64 = _b64(ASSETS / "logo_white.png")
    st.markdown(
        f"""
        <div style="display:flex; align-items:center; gap:0.9rem; margin-bottom:0.3rem;">
            <img src="data:image/png;base64,{logo_b64}" style="height:52px; border-radius:0;">
        </div>
        {f'<p class="oe-subtitle">{subtitle}</p>' if subtitle else ''}
        """,
        unsafe_allow_html=True,
    )


def render_footer():
    st.markdown('<hr class="oe-divider">', unsafe_allow_html=True)
    st.markdown(
        f"""
        <div style="text-align:center; color:{PALE_BLUE}; opacity:0.65; font-size:0.85rem; padding-bottom:1.5rem;">
            Orion's Eye · Proyecto con el apoyo de JAGUAR SPACE · Guatemala · Costa Rica · Nicaragua · El Salvador
        </div>
        """,
        unsafe_allow_html=True,
    )
