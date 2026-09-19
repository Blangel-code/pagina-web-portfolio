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
    IMG_PROJECT_GAME_1,
    IMG_PROJECT_GAME_2,
    IMG_PROJECT_TODO,
    PATH_PROFILE_PIC,
    URL_GITHUB,
    URL_ITCHIO,
    URL_PROJECT_GAME,
    URL_PROJECT_TODO,
    URL_TWITTER,
)
from structures import ProjectCardData, SkillCardData, SocialLinkData, create_social_button, project_card, skill_card


def build_portfolio(page: ft.Page) -> None:
    page.title = "Blangel | Portafolio"
    page.window_width = 1280
    page.window_height = 900
    page.bgcolor = COLOR_BG_DARK
    page.padding = 0
    page.scroll = ft.ScrollMode.AUTO
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

    nav_bar = ft.Container(
        content=ft.Row(
            controls=[
                ft.Row(
                    controls=[profile_image, ft.Text(DEV_ALIAS, size=30, weight=ft.FontWeight.BOLD, color=COLOR_TEXT_PRIMARY)],
                    spacing=10,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Row(
                    controls=[
                        ft.TextButton(
                            "Sobre mí",
                            on_click=navigate_to("sobre-mi"),
                        ),
                        ft.TextButton(
                            "Habilidades",
                            on_click=navigate_to("habilidades"),
                        ),
                        ft.TextButton(
                            "Proyectos",
                            on_click=navigate_to("proyectos"),
                        ),
                        ft.TextButton(
                            "Contacto",
                            on_click=navigate_to("contacto"),
                        ),
                    ],
                    spacing=10,
                ),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            vertical_alignment=ft.CrossAxisAlignment.CENTER,
        ),
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

    hero = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Hola, soy ", size=22, color=COLOR_TEXT_MUTED),
                ft.Text(DEV_NAME, size=50, weight=ft.FontWeight.BOLD, color=COLOR_TEXT_PRIMARY),
                ft.Text(DEV_TITLE, size=28, weight=ft.FontWeight.W_600, color=COLOR_SECONDARY),
                ft.Text(DEV_SUBTITLE, size=16, color="#C4B5FD", max_lines=4),
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
                            url="https://drive.google.com/",
                            icon=ft.Icons.DOWNLOAD,
                            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=14)),
                        ),
                    ],
                    spacing=18,
                ),
            ],
            spacing=16,
            horizontal_alignment=ft.CrossAxisAlignment.START,
            width=560,
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
        width=1200,
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
    ]

    skills_grid = ft.GridView(
        runs_count=3,
        max_extent=240,
        child_aspect_ratio=1.65,
        spacing=14,
        run_spacing=14,
        controls=[skill_card(item) for item in skill_cards],
        width=1200,
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
    ]

    projects_content = ft.Column(
        controls=[
            ft.Text("Proyectos", size=30, weight=ft.FontWeight.BOLD, color=COLOR_TEXT_PRIMARY),
            ft.Row(
                controls=[project_card(item, page) for item in project_items],
                wrap=True,
                spacing=22,
                key=ft.ScrollKey("proyectos"),
                run_spacing=22,
                width=1200,
            ),
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
                ft.TextField(label="Nombre", width=500, border_color=COLOR_PRIMARY_LIGHT),
                ft.TextField(label="Correo electrónico", width=500, border_color=COLOR_PRIMARY_LIGHT),
                ft.TextField(label="Mensaje", multiline=True, min_lines=5, max_lines=8, width=500, border_color=COLOR_PRIMARY_LIGHT),
                ft.Button(
                    "Enviar mensaje",
                    icon=ft.Icons.SEND,
                    bgcolor=COLOR_PRIMARY,
                    color=COLOR_TEXT_PRIMARY,
                    style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=14)),
                    width=180,
                ),
            ],
            spacing=18,
            horizontal_alignment=ft.CrossAxisAlignment.START,
        ),
        padding=26,
        width=1200,
        border_radius=26,
        bgcolor="#160C29",
        border=ft.Border.all(1, COLOR_BORDER),
        key=ft.ScrollKey("contacto"),
    )

    footer = ft.Container(
        content=ft.Row(
            controls=[
                ft.Text("© 2026 Ángel Mendoza. Diseñado y desarrollado en Python.", color="#C4B5FD"),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
        ),
        width=1200,
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
        width=1280,
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=0,
    )

    page.add(main_stack)


if __name__ == "__main__":
    ft.run(
        main=build_portfolio,
        view=ft.AppView.WEB_BROWSER,
        assets_dir=str(Path(__file__).resolve().parent),
    )
