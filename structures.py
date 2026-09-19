"""Módulos reutilizables para la construcción del portafolio en Flet."""

from __future__ import annotations

import asyncio
from dataclasses import dataclass
from typing import Callable

import flet as ft


@dataclass(frozen=True)
class SkillCardData:
    title: str
    icon: str
    description: str


@dataclass(frozen=True)
class ProjectCardData:
    title: str
    images: tuple[str, ...]
    description: str
    tags: tuple[str, ...]
    repo_url: str | None = None
    demo_url: str | None = None


@dataclass(frozen=True)
class SocialLinkData:
    label: str
    url: str
    icon: str | ft.IconData


def create_social_button(data: SocialLinkData, on_click: Callable[[ft.ControlEvent], None] | None = None) -> ft.IconButton:
    """Crea un botón de enlace con estilo visual consistente."""
    icon = (
        ft.Image(src=data.icon, width=22, height=22, fit=ft.BoxFit.CONTAIN)
        if isinstance(data.icon, str)
        else data.icon
    )
    return ft.IconButton(
        icon=icon,
        tooltip=data.label,
        url=data.url,
        on_click=on_click,
        icon_color=ft.Colors.WHITE,
        bgcolor=ft.Colors.with_opacity(0.12, ft.Colors.WHITE),
        style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12)),
        width=42,
        height=42,
    )


def wrap_in_container(content: ft.Control, *, width: float | None = None, padding: int = 18) -> ft.Container:
    """Envoltorio común para tarjetas con fondo uniforme."""
    return ft.Container(
        content=content,
        width=width,
        padding=padding,
        border_radius=18,
        bgcolor="#1F103A",
        border=ft.Border.all(1, "#351A5E"),
        shadow=ft.BoxShadow(
            color="#00000044",
            blur_radius=18,
            spread_radius=1,
            offset=ft.Offset(0, 12),
        ),
    )


def skill_card(data: SkillCardData) -> ft.Container:
    """Genera una tarjeta representativa para una habilidad técnica."""
    icon = ft.Image(src=data.icon, width=31, height=31, fit=ft.BoxFit.CONTAIN)
    return wrap_in_container(
        ft.Column(
            controls=[
                ft.Row(
                    controls=[icon, ft.Text(data.title, size=15, weight=ft.FontWeight.BOLD)],
                    spacing=8,
                    vertical_alignment=ft.CrossAxisAlignment.CENTER,
                ),
                ft.Text(
                    data.description,
                    size=12,
                    color="#C4B5FD",
                    max_lines=5,
                    overflow=ft.TextOverflow.ELLIPSIS,
                ),
            ],
            spacing=8,
            tight=True,
        ),
        width=None,
        padding=13,
    )


async def rotate_carousel(carousel: ft.PageView, image_count: int) -> None:
    """Avanza el carrusel automáticamente cada 3,5 segundos."""
    current_index = 0
    while True:
        await asyncio.sleep(3.5)
        current_index = (current_index + 1) % image_count
        await carousel.go_to_page(current_index, animation_duration=700)


def project_card(data: ProjectCardData, page: ft.Page) -> ft.Container:
    """Genera la tarjeta de proyecto con vista previa, etiquetas y acciones."""
    tags_row = ft.Row(
        controls=[
            ft.Chip(
                label=tag,
                bgcolor="#3B1F68",
                label_text_style=ft.TextStyle(
                    color="#F5F3FF",
                    size=13,
                    weight=ft.FontWeight.W_600,
                ),
                show_checkmark=False,
                shape=ft.RoundedRectangleBorder(radius=10),
                padding=ft.Padding.symmetric(horizontal=10, vertical=6),
            )
            for tag in data.tags
        ],
        wrap=True,
        spacing=8,
        run_spacing=8,
    )

    actions = []
    if data.repo_url:
        actions.append(
            ft.Button(
                "Código en GitHub",
                url=data.repo_url,
                bgcolor="#8B5CF6",
                color="#F5F3FF",
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12)),
                icon=ft.Icons.CODE,
            )
        )
    if data.demo_url:
        actions.append(
            ft.OutlinedButton(
                "Ver proyecto",
                url=data.demo_url,
                icon=ft.Icons.OPEN_IN_NEW,
                style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=12)),
            )
        )

    carousel = ft.PageView(
        controls=[
            ft.Image(
                src=image,
                fit=ft.BoxFit.COVER,
                width=500,
                height=260,
                border_radius=12,
            )
            for image in data.images
        ],
        width=500,
        height=260,
        selected_index=0,
        viewport_fraction=1,
        clip_behavior=ft.ClipBehavior.HARD_EDGE,
    )
    if len(data.images) > 1:
        page.run_task(rotate_carousel, carousel, len(data.images))

    return wrap_in_container(
        ft.Column(
            controls=[
                carousel,
                ft.Text(data.title, size=24, weight=ft.FontWeight.BOLD),
                ft.Text(data.description, size=15, color="#D8B4FE"),
                tags_row,
                ft.Row(controls=actions, wrap=True, spacing=10),
            ],
            spacing=16,
            tight=True,
        ),
        width=520,
    )
