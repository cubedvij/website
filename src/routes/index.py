import asyncio

import flet as ft


class MainPage(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__(route="/")
        self.page = page
        self.controls = []
        self._image_blur = 2
        self.build_ui()

    def build_ui(self):
        self._logo = ft.Image(
            src="logo.png",
            fit=ft.ImageFit.COVER,
        )
        self._appbar = ft.Row(
            controls=[
                ft.IconButton(
                    content=ft.Icon(
                        ft.Icons.DISCORD,
                        size=24,
                        color=ft.Colors.WHITE,
                        shadows=ft.BoxShadow(
                            color=ft.Colors.BLACK,
                            offset=ft.Offset(1, 1),
                            blur_radius=1,
                        ),
                    ),
                    tooltip="Discord",
                    icon_color=ft.Colors.WHITE,
                    on_click=lambda _: self.page.launch_url(
                        "https://cubedvij.pp.ua/discord"
                    ),
                ),
                ft.IconButton(
                    content=ft.Icon(
                        ft.Icons.TELEGRAM,
                        size=24,
                        color=ft.Colors.WHITE,
                        shadows=ft.BoxShadow(
                            color=ft.Colors.BLACK,
                            offset=ft.Offset(1, 1),
                            blur_radius=1,
                        ),
                    ),
                    tooltip="Telegram",
                    icon_color=ft.Colors.WHITE,
                    on_click=lambda _: self.page.launch_url(
                        "https://cubedvij.pp.ua/telegram"
                    ),
                ),
                ft.IconButton(
                    content=ft.Icon(
                        ft.Icons.CODE,
                        size=24,
                        color=ft.Colors.WHITE,
                        shadows=ft.BoxShadow(
                            color=ft.Colors.BLACK,
                            offset=ft.Offset(1, 1),
                            blur_radius=1,
                        ),
                    ),
                    tooltip="GitHub",
                    icon_color=ft.Colors.WHITE,
                    on_click=lambda _: self.page.launch_url(
                        "https://github.com/cubedvij/launcher"
                    ),
                ),
            ],
            alignment=ft.MainAxisAlignment.END,
            spacing=16,
        )

        self._description = ft.Text(
            "Механіка. Логіка. Твій світ.",
            size=32,
            text_align=ft.TextAlign.CENTER,
            weight=ft.FontWeight.BOLD,
            font_family="Roboto Slab",
            style=ft.TextStyle(
                shadow=ft.BoxShadow(
                    color=ft.Colors.BLACK,
                    offset=ft.Offset(2, 2),
                    blur_radius=0.5,
                ),
                letter_spacing=8,
            ),
        )
        self._small_description = ft.Text(
            "Minecraft сервер в основі якого є мод Create.\n"
            "Створюй заводи, повітряні кораблі, автоматичні ферми й цілі міста — усе це без магії, лише інженерія, логіка й фантазія.",
            size=18,
            text_align=ft.TextAlign.CENTER,
            style=ft.TextStyle(
                shadow=ft.BoxShadow(
                    color=ft.Colors.BLACK,
                    offset=ft.Offset(2, 2),
                    blur_radius=1,
                ),
            ),
        )
        self._footer = ft.Text(
            "© 2025 Кубічний Двіж. Всі права захищені. "
            "Minecraft is a trademark of Mojang AB. © 2009-2025 Mojang AB. All rights reserved.",
            size=12,
            text_align=ft.TextAlign.CENTER,
            color=ft.Colors.ON_SURFACE_VARIANT,
        )
        self._download_button_windows = ft.Button(
            content=ft.Row(
                [
                    ft.Image(
                        src="windows.svg",
                        width=24,
                        height=24,
                        filter_quality=ft.FilterQuality.HIGH,
                        anti_alias=True,
                    ),
                    ft.Text(
                        "Завантажити",
                        size=14,
                        style=ft.TextStyle(
                            shadow=ft.BoxShadow(
                                color=ft.Colors.BLACK,
                                offset=ft.Offset(1, 1),
                                blur_radius=1,
                            ),
                        ),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            height=50,
            expand=True,
            bgcolor=ft.Colors.GREEN_900,
            # foreground_color=ft.Colors.WHITE,
            style=ft.ButtonStyle(
                color=ft.Colors.WHITE,
                shape={
                    ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=8),
                    ft.ControlState.HOVERED: ft.RoundedRectangleBorder(radius=0),
                },
                side={
                    ft.ControlState.HOVERED: ft.BorderSide(
                        2, ft.Colors.WHITE, ft.BorderSideStrokeAlign.INSIDE
                    ),
                    ft.ControlState.DEFAULT: ft.BorderSide(
                        2, ft.Colors.TRANSPARENT, ft.BorderSideStrokeAlign.INSIDE
                    ),
                },
            ),
            on_click=lambda _: self.page.launch_url(
                "https://github.com/cubedvij/launcher/releases/latest/download/cube-launcher.exe"
            ),
        )
        self._download_button_linux = ft.Button(
            content=ft.Row(
                [
                    ft.Image(
                        src="linux.svg",
                        width=24,
                        height=24,
                        filter_quality=ft.FilterQuality.HIGH,
                        anti_alias=True,
                    ),
                    ft.Text(
                        "Завантажити",
                        size=14,
                        style=ft.TextStyle(
                            shadow=ft.BoxShadow(
                                color=ft.Colors.BLACK,
                                offset=ft.Offset(1, 1),
                                blur_radius=1,
                            ),
                        ),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            height=50,
            expand=True,
            bgcolor=ft.Colors.GREEN_900,
            # foreground_color=ft.Colors.WHITE,
            style=ft.ButtonStyle(
                color=ft.Colors.WHITE,
                shape={
                    ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=8),
                    ft.ControlState.HOVERED: ft.RoundedRectangleBorder(radius=0),
                },
                side={
                    ft.ControlState.HOVERED: ft.BorderSide(
                        2, ft.Colors.WHITE, ft.BorderSideStrokeAlign.INSIDE
                    ),
                    ft.ControlState.DEFAULT: ft.BorderSide(
                        2, ft.Colors.TRANSPARENT, ft.BorderSideStrokeAlign.INSIDE
                    ),
                },
            ),
            on_click=lambda _: self.page.launch_url(
                "https://github.com/cubedvij/launcher/releases/latest/download/cube-launcher"
            ),
        )
        self._rules_button = ft.Button(
            content=ft.Row(
                [
                    ft.Icon(
                        ft.Icons.BOOK,
                        size=24,
                        color=ft.Colors.WHITE,
                        shadows=ft.BoxShadow(
                            color=ft.Colors.BLACK,
                            offset=ft.Offset(1, 1),
                            blur_radius=1,
                        ),
                    ),
                    ft.Text(
                        "Правила",
                        size=14,
                        style=ft.TextStyle(
                            shadow=ft.BoxShadow(
                                color=ft.Colors.BLACK,
                                offset=ft.Offset(1, 1),
                                blur_radius=1,
                            ),
                        ),
                    ),
                ],
                alignment=ft.MainAxisAlignment.CENTER,
            ),
            height=50,
            bgcolor=ft.Colors.LIGHT_GREEN_800,
            # foreground_color=ft.Colors.WHITE,
            style=ft.ButtonStyle(
                color=ft.Colors.WHITE,
                shape={
                    ft.ControlState.DEFAULT: ft.RoundedRectangleBorder(radius=8),
                    ft.ControlState.HOVERED: ft.RoundedRectangleBorder(radius=0),
                },
                side={
                    ft.ControlState.HOVERED: ft.BorderSide(
                        2, ft.Colors.WHITE, ft.BorderSideStrokeAlign.INSIDE
                    ),
                    ft.ControlState.DEFAULT: ft.BorderSide(
                        2, ft.Colors.TRANSPARENT, ft.BorderSideStrokeAlign.INSIDE
                    ),
                },
            ),
            on_click=lambda _: self.page.launch_url("https://cubedvij.pp.ua/rules"),
        )
        # Responsive download button column
        is_mobile = self.page.width is not None and self.page.width < 500
        download_button_column = ft.Column(
            controls=[
                ft.Row(
                    controls=[
                        self._download_button_windows,
                        self._download_button_linux,
                    ],
                    alignment=ft.MainAxisAlignment.CENTER,
                    spacing=16,
                    expand=2,
                ),
                self._rules_button,
            ],
            width=None if is_mobile else 400,
        )
        self._main_content_inner = ft.Container(
            ft.Column(
                alignment=ft.MainAxisAlignment.START,
                controls=[
                    self._appbar,
                    ft.Container(
                        content=ft.Column(
                            controls=[
                                ft.Container(
                                    content=self._logo,
                                    alignment=ft.alignment.center,
                                ),
                                ft.Container(
                                    content=ft.Column(
                                        controls=[
                                            self._description,
                                            self._small_description,
                                        ],
                                        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                                        spacing=8,
                                    ),
                                    alignment=ft.alignment.center,
                                ),
                                download_button_column,
                            ],
                            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                            alignment=ft.MainAxisAlignment.START
                            if is_mobile
                            else ft.MainAxisAlignment.CENTER,
                        ),
                        alignment=ft.alignment.center,
                        expand=True,
                        padding=ft.Padding(
                            0, 64 if is_mobile else 0, 0, 0
                        ),  # Add top padding on mobile
                    ),
                ],
            ),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_center,
                end=ft.alignment.bottom_center,
                stops=[0, 1],
                colors=[ft.Colors.BLACK12, ft.Colors.BLACK87],
            ),
            blend_mode=ft.BlendMode.MULTIPLY,
            alignment=ft.alignment.center,
            blur=self._image_blur,
            padding=ft.padding.all(24),
        )
        self._main_content = ft.Container(
            content=self._main_content_inner,
            image=ft.DecorationImage(
                src="cubedvij.webp",
                fit=ft.ImageFit.COVER,
            ),
            height=self.page.height,
            width=self.page.width,
            expand=True,
        )
        self._footer_container = ft.Container(
            content=self._footer,
            alignment=ft.alignment.bottom_center,
            padding=ft.Padding(0, 0, 0, 16),
        )
        self.page.scroll = ft.ScrollMode.AUTO
        self.page.on_resized = self.on_resized
        # self.page.on_view_pop = self.on_view_pop
        self.page.add(self._main_content)
        self.page.add(self._footer_container)

    def on_resized(self, event):
        self._main_content.height = self.page.height
        self._main_content.width = self.page.width
        self._main_content.update()

    async def on_view_pop(self, event):
        steps = self._image_blur + 1
        for t in range(steps):
            # Ease-out cubic: y = 1 - (1 - t/steps)^3
            progress = t / (steps - 1) if steps > 1 else 1
            eased = 1 - pow(1 - progress, 3)
            blur_value = int(self._image_blur * (1 - eased))
            self._main_content_inner.blur = blur_value
            self._main_content_inner.update()
            await asyncio.sleep(0.06)
        self._image_blur = 0
