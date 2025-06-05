import flet as ft


def setup_theme_settings(
    page: ft.Page,radius: int, shape_type: str = None
):
    """
    Setup the theme settings for the Flet page.
    Args:
        page (ft.Page): The Flet page to apply the theme settings to.
        radius (int): The border radius for the controls.
        shape_type (str): The shape type for the controls. Default is "roundedRectangle".
    """
    if shape_type == "roundedRectangle":
        shape = ft.RoundedRectangleBorder(radius)
    elif shape_type == "beveledRectangle":
        shape = ft.BeveledRectangleBorder(radius)
    elif shape_type == "continuousRectangle":
        shape = ft.ContinuousRectangleBorder(radius)
    page.theme = ft.Theme(
        page_transitions=ft.PageTransitionsTheme(
            linux=ft.PageTransitionTheme.FADE_FORWARDS,
            windows=ft.PageTransitionTheme.FADE_FORWARDS,
        ),
        card_theme=ft.CardTheme(
            shape=shape,
            margin=ft.Margin(0, 4, 0, 0),
        ),
        text_button_theme=ft.TextButtonTheme(
            shape=shape,
        ),
        elevated_button_theme=ft.ElevatedButtonTheme(
            shape=shape,
        ),
        button_theme=ft.ButtonTheme(
            shape=shape,
        ),
        outlined_button_theme=ft.OutlinedButtonTheme(
            shape=shape,
            bgcolor=ft.Colors.SECONDARY_CONTAINER,
            foreground_color=ft.Colors.ON_SECONDARY_CONTAINER,
            border_side=ft.BorderSide(
                color=ft.Colors.TRANSPARENT,
                width=0,
            ),
        ),
        icon_button_theme=ft.IconButtonTheme(
            shape=shape,
        ),
        floating_action_button_theme=ft.FloatingActionButtonTheme(
            shape=shape,
        ),
        appbar_theme=ft.AppBarTheme(
            shape=shape,
        ),
        list_tile_theme=ft.ListTileTheme(
            shape=shape,
        ),
        dialog_theme=ft.DialogTheme(
            shape=shape,
        ),
    )
