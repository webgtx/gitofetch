import flet as ft
from icecream import ic
from github import Github as gh

class Gitofetch:
    def __init__(self, page: ft.Page, github_username: str):
        self.page = page
        self.page.vertical_alignment = ft.MainAxisAlignment.CENTER
        self.github_user = gh().get_user(github_username)
        self.fetchinfo = {
            "Name": self.github_user.name,
            "Bio": self.github_user.bio,
            "Website": self.github_user.blog,
            "Public Repos": self.github_user.public_repos,
            "Public Gists": self.github_user.public_gists
        }
        
        
        self.page.add(
            ft.Row([
                ft.Container(
                    content=ft.Image(src=self.github_user.avatar_url),
                    padding=15,
                    bgcolor="#000000",
                    border_radius=13,
                    height=400,
                    width=400
                ),
                ft.Container(
                    content=ft.Column([ft.Text(f"{k}: {v}") for k,v in self.fetchinfo.items()]),
                    padding=15,
                    bgcolor="#161616",
                    border_radius=13,
                    height=400,
                    width=500
                ),
            ], alignment=ft.MainAxisAlignment.CENTER)
        )
        ic([ft.Text(f"{k}: {v}") for k,v in self.fetchinfo.items()])

