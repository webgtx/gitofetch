import flet as ft
from icecream import ic
from views.fetch import Gitofetch

class Settings:
    def __init__(self, page: ft.Page):
        self.page = page
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.account_username_input = ft.TextField(label="Github Username")

        self.page.add(
            ft.Row([
                ft.Container(
                    content=ft.Column([
                        ft.Text("Welcome to Gitofetch", size=30, weight=ft.FontWeight.BOLD),
                        ft.Text(
                            "".join((
                                "Rather than showcasing neofetch running on arch linux, ",
                                "try to highlight your real development accomplishments"
                            )),
                            size=15
                        ),
                        ft.Row([
                            self.account_username_input,
                            ft.IconButton(
                                icon=ft.icons.DIRECTIONS_SUBWAY_FILLED_OUTLINED,
                                tooltip="Fetch Github Stats", on_click=self._save_n_proceed
                            ),
                        ]),
                    ]),
                    bgcolor="#161616",
                    padding=15,
                    border_radius=13,
                    width=400
                ),
            ], alignment=ft.MainAxisAlignment.CENTER),
        )

    def _save_n_proceed(self, _):
        self.page.client_storage.set(key="ghusername", value=self.account_username_input.value)
        self.page.remove(*self.page.controls)
        Gitofetch(self.page, self.page.client_storage.get("ghusername"))


