# Sitio web de Orion's Eye (Streamlit)

## Cómo correrlo

```bash
pip install -r requirements.txt
streamlit run app.py
```

Se abrirá en `http://localhost:8501`.

## Estructura

```
orion_app/
├── app.py                          # Página de inicio (Home)
├── pages/
│   ├── 1_Sobre_el_Proyecto.py      # Misión, visión, objetivos, overview
│   ├── 2_Conoce_al_Equipo.py       # Tarjetas del equipo (8 integrantes)
│   └── 3_Noticias.py               # Noticias/avances con filtro por categoría
├── data/
│   ├── equipo.py                   # 👉 Edita aquí los datos del equipo
│   └── noticias.py                 # 👉 Edita aquí para agregar noticias nuevas
├── assets/                         # Logos, fondo y fotos
├── style.py                        # Paleta de marca, tipografía y CSS compartido
└── requirements.txt
```

## Para editar contenido (sin tocar el código de las páginas)

- **Agregar/editar integrantes del equipo:** abre `data/equipo.py`, edita los
  campos o agrega un nuevo diccionario a la lista `EQUIPO`. Guarda la foto en
  `assets/team/` y apunta el campo `"foto"` a esa ruta.
- **Agregar una noticia:** abre `data/noticias.py` y copia/pega un bloque
  dentro de la lista `NOTICIAS` (instrucciones dentro del archivo).

## Nota sobre el equipo

En el material que compartiste solo venían las fotos y datos de 7 de los 8
integrantes (falta uno). Se dejó un 8vo espacio ("Por asignar") con un avatar
genérico en `data/equipo.py` — solo reemplaza ese bloque cuando tengas los
datos reales.

## Nota sobre tipografía

La identidad de marca usa la fuente **Codec Pro**, que es una fuente de pago
y no está disponible para web vía Google Fonts. Se usó **Sora** (encabezados)
y **Poppins** (texto) como alternativas gratuitas con una geometría/redondez
similar. Si tienes una licencia web de Codec Pro, puedes reemplazar la
importación de Google Fonts en `style.py` por tu propio `@font-face`.
