import flet as ft

def main(page: ft.Page):
    
    
    val = r"""
  _____________ _______ ___ 
  __  ___/  __ `/_  __ `__ \
  _(__  )/ /_/ /_  / / / / /
  /____/ \__,_/ /_/ /_/ /_/ """
    
    greeting = ft.Column(controls=[ft.Text( value=val, selectable=True, font_family="cascadia" )],alignment=ft.MainAxisAlignment.SPACE_AROUND)

    page.add(greeting)

ft.app(target=main)
