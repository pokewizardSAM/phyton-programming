import flet as ft
import random


def change_pos(e):
    no_btn.top = random.randint(0,500)
    no_btn.left = random.randint(0,500)
    no_btn.update
    


def main(page: ft.Page):
    page.title = "- - - - You GAY if you Quit !! - - - -"
    global yess_btn, no_btn, text
    text = ft.Text(value="Are you GAY ???", text_align="center")
    yess_btn = ft.OutlinedButton(text="Yes")
    no_btn = ft.OutlinedButton(text="No",on_click=change_pos)

    page.add(text,yess_btn, no_btn)
    page.update


ft.app(target=main)