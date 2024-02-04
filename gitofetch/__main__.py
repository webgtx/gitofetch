import flet as ft
from views.settings import Settings

def main(page: ft.Page):
    page.title = "Gitofetch"
    page.window_title_bar_hidden = True
    page.theme_mode = "dark"
    Settings(page)

ft.app(target=main)
