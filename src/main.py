import os

import flet as ft
from dotenv import load_dotenv

from routes import MainPage
from utils import setup_theme_settings

load_dotenv()

async def main(page: ft.Page):
    page.title = "Кубічний Двіж"
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.padding = ft.Padding(0, 0, 0, 0)

    setup_theme_settings(page, radius=0, shape_type="roundedRectangle")

    views = {
        "/": MainPage(page),
    }

    page.views.append(views["/"])


if __name__ == "__main__":
    ft.app(
        target=main,
        view=ft.WEB_BROWSER,
        host=os.getenv("HOST", "localhost"),
        port=os.getenv("PORT", "8550"),
        assets_dir="./assets",
    )
