import flet as ft


def main(page: ft.page):
    page.window_width= 880
    page.window_height= 400
    page.bgcolor = "blue"

    def add_new_niggas(p):
        TaskTextField = ft.TextField(value= TextField.value, width=600, text_size=14 )
        checkbutton = ft.Checkbox(value=False)
        taskrow = ft.Row(controls=  [TaskTextField,checkbutton], alignment=ft.MainAxisAlignment.SPACE_AROUND)
        page.add(taskrow)


    TextField = ft.TextField(width=600, text_align= "center")
    Simbutton = ft.ElevatedButton(text="click me nigga", on_click=add_new_niggas)

    main_row = ft.Row(controls=[TextField,Simbutton], 
                        alignment=ft.MainAxisAlignment.SPACE_AROUND)



    # SimText = ft.Text("MEO MEO",bgcolor="red",color="black", style=ft.TextThemeStyle.HEADLINE_LARGE )
    # simple_filled_BTN = ft.FilledButton(text="hehe nigger, see me!!")
    # simple_column = ft.Column(controls=[SimText,simple_filled_BTN],alignment=ft.MainAxisAlignment.SPACE_BETWEEN)

    page.add(main_row)

ft.app(target=main)