from __future__ import annotations

from pathlib import Path

import flet as ft

from config import (
    COLOR_BG_DARK,
    COLOR_BG_GLASS,
    COLOR_BORDER,
    COLOR_PRIMARY,
    COLOR_PRIMARY_LIGHT,
    COLOR_SECONDARY,
    COLOR_TEXT_MUTED,
    COLOR_TEXT_PRIMARY,
    DEV_ALIAS,
    DEV_NAME,
    DEV_SUBTITLE,
    DEV_TITLE,
    EMAIL_CONTACT,
    ICON_FLET,
    ICON_GITHUB,
    ICON_GODOT,
    ICON_ITCHIO,
    ICON_PYTHON,
    ICON_SQL,
    ICON_TKINTER,
    ICON_TWITTER,
    ICON_VSCODE,
    ICON_N8N,
    IMG_PROJECT_GAME_1,
    IMG_PROJECT_GAME_2,
    IMG_PROJECT_TODO,
    PATH_PROFILE_PIC,
    URL_GITHUB,
    URL_ITCHIO,
    URL_PROJECT_GAME,
    URL_PROJECT_TODO,
    URL_TWITTER,
    URL_PROJECT_LIBRARY,
    IMG_PROJECT_LIBRARY_1,
    IMG_PROJECT_LIBRARY_2,
    IMG_PROJECT_LIBRARY_3,
    IMG_PROJECT_LIBRARY_4,
    IMG_PROJECT_CHATBOT_1,
    IMG_PROJECT_CHATBOT_2
)
from structures import ProjectCardData, SkillCardData, SocialLinkData, create_social_button, project_card, skill_card


def build_portfolio(page: ft.Page) -> None:
    page.title = "Blangel | Portafolio"
    page.window_width = 1280
    page.window_height = 900
    page.bgcolor = COLOR_BG_DARK
    page.padding = 0
    page.scroll = ft.ScrollMode.AUTO
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.fonts = {
        "Urbanist": "https://fonts.googleapis.com/css2?family=Urbanist:wght@400;500;600;700;800&display=swap"
    }
    page.theme = ft.Theme(font_family="Urbanist")
    page.theme_mode = ft.ThemeMode.DARK

    def navigate_to(section_key: str):
        async def handler(_: ft.ControlEvent) -> None:
            await page.scroll_to(scroll_key=section_key, duration=350)

        return handler

    profile_image = ft.Image(
        src=PATH_PROFILE_PIC,
        width=56,
        height=56,
        fit=ft.BoxFit.COVER,
        border_radius=18,
    )

    brand_name = ft.Text(DEV_ALIAS, size=30, weight=ft.FontWeight.BOLD, color=COLOR_TEXT_PRIMARY)
    brand = ft.Row(
        controls=[profile_image, brand_name],
        spacing=10,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )
    nav_buttons = [
        ft.TextButton("Sobre mí", on_click=navigate_to("sobre-mi")),
        ft.TextButton("Habilidades", on_click=navigate_to("habilidades")),
        ft.TextButton("Proyectos", on_click=navigate_to("proyectos")),
        ft.TextButton("Contacto", on_click=navigate_to("contacto")),
    ]
    nav_links = ft.Row(
        controls=nav_buttons,
        spacing=10,
    )
    desktop_nav_content = ft.Row(
        controls=[brand, nav_links],
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
    )
    mobile_nav_content = ft.Column(
        controls=[
            brand,
            ft.Row(controls=nav_buttons[:2], spacing=0),
            ft.Row(controls=nav_buttons[2:], spacing=0),
        ],
        spacing=0,
        horizontal_alignment=ft.CrossAxisAlignment.START,
    )
    nav_bar = ft.Container(
        content=desktop_nav_content,
        width=1200,
        padding=12,
        margin=ft.Margin(top=18),
        border_radius=24,
        bgcolor=COLOR_BG_GLASS,
        border=ft.Border.all(1, COLOR_BORDER),
        shadow=ft.BoxShadow(
            color="#00000044",
            blur_radius=20,
            spread_radius=1,
            offset=ft.Offset(0, 8),
        ),
    )

    hero_name = ft.Text(DEV_NAME, size=50, weight=ft.FontWeight.BOLD, color=COLOR_TEXT_PRIMARY)
    hero_title = ft.Text(DEV_TITLE, size=28, weight=ft.FontWeight.W_600, color=COLOR_SECONDARY)
    hero = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Hola, soy ", size=22, color=COLOR_TEXT_MUTED),
                hero_name,
                hero_title,
                ft.Text(DEV_SUBTITLE, size=16, color="#C4B5FD"),
                ft.Row(
                    controls=[
                        ft.Button(
                            "Ver Proyectos",
                            on_click=navigate_to("proyectos"),
                            bgcolor=COLOR_PRIMARY,
                            color=COLOR_TEXT_PRIMARY,
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=14)),
                            icon=ft.Icons.ARROW_FORWARD,
                        ),
                        ft.OutlinedButton(
                            "Descargar CV",
                            url="https://drive.google.com/file/d/1Tm-4IE8M8WO2eed_B1n-uBJ09EbaDazp/view?usp=sharing",
                            icon=ft.Icons.DOWNLOAD,
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=14)),
                        ),
                    ],
                    wrap=True,
                    spacing=18,
                ),
            ],
            spacing=16,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        ),
        padding=30,
    )

    code_preview = ft.Container(
        content=ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        ft.Container(width=12, height=12, border_radius=6, bgcolor="#ff5f57"),
                        ft.Container(width=12, height=12, border_radius=6, bgcolor="#febc2e"),
                        ft.Container(width=12, height=12, border_radius=6, bgcolor="#28c840"),
                    ],
                    spacing=8,
                ),
                ft.Container(
                    content=ft.Column(
                        controls=[
                            ft.Text("import flet as ft", size=18, color="#A78BFA"),
                            ft.Text("def main(page):", size=18, color="#F9A8D4"),
                            ft.Text("    task_list = []", size=18, color="#C4B5FD"),
                            ft.Text("    page.add(ft.Text('Lista de tareas'))", size=18, color="#FDE68A"),
                            ft.Text("    page.update()", size=18, color="#86EFAC"),
                        ],
                        spacing=6,
                    ),
                    padding=20,
                    border_radius=18,
                    bgcolor="#12091F",
                    border=ft.Border.all(1, "#341A52"),
                ),
            ],
            spacing=18,
        ),
        padding=18,
        width=430,
        border_radius=24,
        bgcolor="#1C0F2E",
        border=ft.Border.all(1, COLOR_BORDER),
        shadow=ft.BoxShadow(
            color="#7C3AED55",
            blur_radius=28,
            spread_radius=1,
            offset=ft.Offset(0, 18),
        ),
    )

    hero_section = ft.Row(
        controls=[hero, code_preview],
        wrap=True,
        alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
        vertical_alignment=ft.CrossAxisAlignment.CENTER,
        width=1200,
    )

    about_content = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Sobre mí", size=30, weight=ft.FontWeight.BOLD, color=COLOR_TEXT_PRIMARY),
                ft.Text(
                    "Me apasiona resolver problemas reales con código y transformar ideas en experiencias útiles, claras y visualmente impactantes.",
                    size=17,
                    color="#DDD6FE",
                ),
                ft.Text(
                    "Mi camino en programación me ha llevado a trabajar con Python, SQL, Flet, Tkinter y Godot, enfocado en construir herramientas de gestión, interfaces funcionales y videojuegos con personalidad. Me interesa la lógica, pero también la claridad del producto final y la experiencia del usuario.",
                    size=17,
                    color="#DDD6FE",
                ),
                ft.Text(
                    "Busco seguir creciendo con proyectos prácticos, aprender de cada reto y crear soluciones que ayuden a personas, equipos o negocios a trabajar mejor y ver resultados concretos.",
                    size=17,
                    color="#DDD6FE",
                ),
            ],
            spacing=16,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        ),
        padding=26,
        border_radius=26,
        bgcolor="#160C29",
        border=ft.Border.all(1, COLOR_BORDER),
        key=ft.ScrollKey("sobre-mi"),
    )

    skill_cards = [
        SkillCardData(
            title="Python",
            icon=ICON_PYTHON,
            description="Desarrollo backend, automatización, lógica de negocio y aplicaciones interactivas con enfoque en rendimiento y mantenibilidad.",
        ),
        SkillCardData(
            title="SQL",
            icon=ICON_SQL,
            description="Diseño de esquemas, consultas relacionales, integración de SQLite y arquitectura de datos aplicando buenas prácticas.",
        ),
        SkillCardData(
            title="Flet",
            icon=ICON_FLET,
            description="Creación de interfaces modernas y multiplataforma con Python, enfocadas en usabilidad y experiencia visual limpia.",
        ),
        SkillCardData(
            title="Tkinter",
            icon=ICON_TKINTER,
            description="Desarrollo de aplicaciones de escritorio con interfaces funcionales y rápidas de prototipar para tareas del día a día.",
        ),
        SkillCardData(
            title="Godot",
            icon=ICON_GODOT,
            description="Programación de juegos en GDScript, lógica de gameplay, sistemas de progreso y proyectos pensados para navegador y móvil.",
        ),
        SkillCardData(
            title="Git & GitHub",
            icon=ICON_GITHUB,
            description="Control de versiones, trabajo colaborativo, flujo de ramas y publicación de proyectos con organización profesional.",
        ),      
        SkillCardData(
            title="VS Code",
            icon=ICON_VSCODE,
            description="Entorno de desarrollo práctico y moderno para escribir, depurar y mantener proyectos de software con claridad.",
        ),
        SkillCardData(
            title="N8N",
            icon=ICON_N8N,
            description="Software de automatización de flujos de trabajos repetitivos, chatbots y asistentes virtuales.",
        ),
    ]

    skills_grid = ft.GridView(
        runs_count=3,
        max_extent=240,
        child_aspect_ratio=1.65,
        spacing=14,
        run_spacing=14,
        controls=[skill_card(item) for item in skill_cards],
        height=300,
        key=ft.ScrollKey("habilidades"),
    )

    project_items = [
        ProjectCardData(
            title="Lista de Tareas",
            images=(IMG_PROJECT_TODO,),
            description="Aplicación para organizar tareas diarias con filtros, edición, eliminación, notificaciones nativas en Windows y almacenamiento local con SQLite.",
            tags=("Python", "Flet", "SQLite", "Productividad"),
            repo_url=URL_PROJECT_TODO,
            demo_url=None,
        ),
        ProjectCardData(
            title="The Decimal Dungeon Abyss",
            images=(IMG_PROJECT_GAME_1, IMG_PROJECT_GAME_2),
            description="Juego roguelite pixel-art con mecánicas de progreso, dificultad creciente y experiencia jugable pensada para navegador, Windows y móvil.",
            tags=("Godot", "GDScript", "Pixel Art", "Roguelite"),
            repo_url=None,
            demo_url=URL_PROJECT_GAME,
        ),
        ProjectCardData(
            title="Sistema De Gestión De Biblioteca",
            images=(IMG_PROJECT_LIBRARY_1, IMG_PROJECT_LIBRARY_2, IMG_PROJECT_LIBRARY_3, IMG_PROJECT_LIBRARY_4),
            description="Aplicación para tener un inventario, obetener reportes y realizar prestamos de libros a usuarios, cuenta con avisos de retrasos y usa una base de datos SQLite local.",
            tags=("Python", "Flet", "SQLite", "Finanzas", "Productividad"),
            repo_url=URL_PROJECT_LIBRARY,
            demo_url=None,
        ),
        ProjectCardData(
            title="ChatBot Para WhatsApp",
            images=(IMG_PROJECT_CHATBOT_1, IMG_PROJECT_CHATBOT_2),
            description="Un Bot Funcional Para WhatsApp Capaz de Conectarse A Una Base De Datos Dar Respuestas Con Informaciòn De Allí Y Pudiendo Recordar Conversaciones Anteriores. Creado Con N8N.",
            tags=("N8N", "Automatización", "Bot", "Finanzas", "Productividad", "Clientes"),
            repo_url=None,
            demo_url=None,
        ),
    ]

    project_card_controls = [project_card(item, page) for item in project_items]
    projects_row = ft.Row(
        controls=[card for card, _ in project_card_controls],
        wrap=True,
        spacing=22,
        key=ft.ScrollKey("proyectos"),
        run_spacing=22,
        width=1200,
    )
    projects_content = ft.Column(
        controls=[
            ft.Text("Proyectos", size=30, weight=ft.FontWeight.BOLD, color=COLOR_TEXT_PRIMARY),
            projects_row,
        ],
        spacing=22,
    )

    social_links = [
        SocialLinkData("GitHub", URL_GITHUB, ICON_GITHUB),
        SocialLinkData("Itch.io", URL_ITCHIO, ICON_ITCHIO),
        SocialLinkData("Twitter", URL_TWITTER, ICON_TWITTER),
        SocialLinkData("Correo", f"mailto:{EMAIL_CONTACT}", ft.Icons.EMAIL),
    ]

    contact_card = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Contacto", size=30, weight=ft.FontWeight.BOLD, color=COLOR_TEXT_PRIMARY),  
                ft.Row(
                    controls=[create_social_button(item) for item in social_links],
                    spacing=12,
                ),
            ],
            spacing=18,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        ),
        padding=26,
        border_radius=26,
        bgcolor="#160C29",
        border=ft.Border.all(1, COLOR_BORDER),
        key=ft.ScrollKey("contacto"),
    )

    footer_text = ft.Text(
        "© 2026 Ángel Mendoza. Diseñado y desarrollado en Python.",
        color="#C4B5FD",
        text_align=ft.TextAlign.CENTER,
    )
    footer_row = ft.Row(
        controls=[footer_text],
        alignment=ft.MainAxisAlignment.CENTER,
        wrap=True,
    )
    footer = ft.Container(
        content=footer_row,
        padding=18,
        margin=ft.Margin.only(bottom=25),
    )

    main_stack = ft.Column(
        controls=[
            nav_bar,
            ft.Container(height=30),
            hero_section,
            ft.Container(height=60),
            about_content,
            ft.Container(height=60),
            ft.Text("Habilidades técnicas", size=30, weight=ft.FontWeight.BOLD, color=COLOR_TEXT_PRIMARY),
            skills_grid,
            ft.Container(height=60),
            projects_content,
            ft.Container(height=60),
            contact_card,
            ft.Container(height=25),
            footer,
        ],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=0,
    )

    page.add(main_stack)

    def resize_layout(_: ft.ControlEvent | None = None) -> None:
        viewport_width = page.width or 1280
        content_width = min(max(viewport_width - 32, 0), 1200)
        is_mobile = viewport_width < 700
        is_compact = viewport_width < 1050
        columns = 1 if is_mobile else 2 if viewport_width < 1000 else 3
        skill_cell_width = (content_width - 14 * (columns - 1)) / columns
        skill_cell_width = min(skill_cell_width, skills_grid.max_extent)
        skill_rows = (len(skill_cards) + columns - 1) // columns

        main_stack.width = content_width
        nav_bar.width = content_width
        nav_bar.padding = 8 if is_mobile else 12
        nav_bar.content = mobile_nav_content if is_mobile else desktop_nav_content
        mobile_nav_content.width = max(content_width - 16, 0)
        profile_image.width = 42 if is_mobile else 56
        profile_image.height = 42 if is_mobile else 56
        brand_name.size = 24 if is_mobile else 30
        nav_links.spacing = 10
        hero_section.width = content_width
        hero.width = content_width if is_compact else 560
        hero.padding = 20 if is_mobile else 30
        hero_name.size = 36 if is_mobile else 50
        hero_title.size = 22 if is_mobile else 28
        code_preview.width = content_width if is_compact else 430
        about_content.width = content_width
        skills_grid.width = content_width
        skills_grid.runs_count = columns
        skills_grid.height = skill_rows * (skill_cell_width / skills_grid.child_aspect_ratio) + 14 * (skill_rows - 1)
        projects_row.width = content_width
        project_width = (
            content_width
            if viewport_width < 900
            else min(520, (content_width - projects_row.spacing) / 2)
            if viewport_width < 1200
            else 520
        )
        for card, carousel in project_card_controls:
            card.width = project_width
            carousel.width = max(project_width - 38, 0)
            carousel.height = 190 if is_mobile else 260
            for image in carousel.controls:
                image.width = carousel.width
                image.height = carousel.height
        contact_card.width = content_width
        footer.width = content_width
        footer_text.width = max(content_width - 36, 0)
        footer_row.width = max(content_width - 36, 0)
        page.update()

    page.on_resize = resize_layout
    resize_layout()


if __name__ == "__main__":
    ft.run(
        main=build_portfolio,
        view=ft.AppView.WEB_BROWSER,
        assets_dir=str(Path(__file__).resolve().parent / "assets"),
    )
