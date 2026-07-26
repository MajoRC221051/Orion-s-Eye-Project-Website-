"""
NOTICIAS / ACTUALIZACIONES DEL PROYECTO
=========================================
Para agregar una noticia nueva, copia uno de los bloques de abajo,
pégalo al INICIO de la lista NOTICIAS (para que salga primero, ya que
la página las muestra en el orden en que aparecen aquí) y edita los
campos. No necesitas tocar ningún otro archivo del proyecto.

Campos:
- fecha:      texto libre, ej. "Julio 2026"
- titulo:     título de la noticia
- categoria:  "Hardware" | "Software" | "Equipo" | "General"
              (se usa para los filtros de la página de Noticias)
- resumen:    1-3 líneas de texto
- imagen:     ruta a una imagen dentro de la carpeta assets/news/
              (usa None si no tienes imagen todavía)
"""

NOTICIAS = [
    {
        "fecha": "Julio 2026",
        "titulo": "Primera etapa del proyecto completada",
        "categoria": "General",
        "resumen": (
            "Los equipos de Hardware y Software cerraron la primera etapa de "
            "Orion's Eye: parámetros de componentes definidos, diseño CAD, base "
            "del espectrómetro y primer prototipo armado, junto con la "
            "arquitectura de software y las pantallas principales de la app."
        ),
        "imagen": "assets/news/hardware_prototipo.jpg",
    },
    {
        "fecha": "Julio 2026",
        "titulo": "Diseño CAD y base del espectrómetro",
        "categoria": "Hardware",
        "resumen": (
            "Se definieron los parámetros de los componentes ópticos y se "
            "modeló en CAD la base del espectrómetro, sentando las bases para "
            "el armado del prototipo físico."
        ),
        "imagen": "assets/news/hardware_cad.jpg",
    },
    {
        "fecha": "Julio 2026",
        "titulo": "Arquitectura de software y flujo de datos",
        "categoria": "Software",
        "resumen": (
            "Quedó definida la arquitectura del sistema: la app se comunica vía "
            "API Gateway y Lambda con un ESP32 a través de IoT Core, "
            "almacenando observaciones en DynamoDB y S3."
        ),
        "imagen": "assets/news/software_arquitectura.jpg",
    },
    {
        "fecha": "Julio 2026",
        "titulo": "Primer prototipo de hardware armado",
        "categoria": "Hardware",
        "resumen": (
            "Tras validar el diseño base, el equipo terminó el armado del "
            "primer prototipo físico del sistema de seguimiento."
        ),
        "imagen": "assets/news/hardware_diseno.jpg",
    },
    {
        "fecha": "Julio 2026",
        "titulo": "Retos identificados para la siguiente etapa",
        "categoria": "General",
        "resumen": (
            "Se identificaron puntos a resolver antes de las pruebas de campo: "
            "calentamiento de componentes, precisión de seguimiento, "
            "comportamiento de motores y algunos bugs de software."
        ),
        "imagen": None,
    },
    {
        "fecha": "Próximamente",
        "titulo": "Próxima etapa: pruebas de prototipo y de la aplicación",
        "categoria": "General",
        "resumen": (
            "El plan para la siguiente etapa incluye pruebas del prototipo "
            "físico, pruebas de la aplicación móvil y el refinamiento general "
            "del sistema."
        ),
        "imagen": None,
    },
]
