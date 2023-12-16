import importlib
import subprocess
import flet as ft

def main(page: ft.page):
    page.title = "ART-GEN V3.0 Gui based UNGA BUNGA fire 🔥shit "
    page.scroll = "adaptive"
    page.padding = 20    

    page.fonts = {
        "cascadia": r"Flet\ART_GEN_GUI_V3.0\assets\fonts\CascadiaMono-instance.ttf"
    }
    page.appbar = ft.AppBar(
        
    )

    
    # import pyfiglet 
    # import sys 
    # import time
    

    # Changelog
    changelog = {
        "v1.0": "Supports veiwing fonts, creting fonts, Basic error handeling",
        "v2.0": "Added new features - Advanced error handling, menu navigation, enhanced font selection.",
        "v2.1": "Added new features - save and load artwork, customization options.",
        "v2.2": "Added new features - ASCII art gallery, user preferences.",
        "v2.3": "Bug fixes and improvements.",
        "v3.0": "Added Gui support using flet, dynamic launch support added ",
    }

    def print_changelog():
        # Print the changelog
        print("Changelog:")
        for version, changes in changelog.items():
            print(f"Version {version}: {changes}")

    def module_compatibilty_installer():  
        print("---INTIALISATION---")
        modules_required = ["pyfiglet", "subprocess", "time", "sys", "PyQt5","flet"]
        imported_modules = []
        for module_name in modules_required:
                try:        #This part imports the module
                    module = importlib.import_module(module_name)
                    imported_modules.append(module)
                    print(f"successfully imported {module_name}")
                    globals()[module_name] = module
                except:
                    print(f"failed to import {module_name}. INSTALLING......")
                    subprocess.check_call(["pip","install", module_name]) 
                    #parsing error can occur in subprocess.check_call() if the arguments are not passed a single list
                    try:
                        globals()[module_name] = importlib.import_module(module_name)
                    except ImportError:
                        print(f"Failed to import module even after installing.....Fatal error")

    module_compatibilty_installer()

    font_list = pyfiglet.Figlet().getFonts()
    def show_fonts():

        for f in font_list:
            print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-\n","Font Name: ",f)
            pyfiglet.print_figlet(f,f)
        return font_list


    def create_art():
        text_var = user_text.value
        font_var = user_font.value

        # while Font == "":
        #     Font = input("""
        # ──────────────────────────────────────────────────────────────
        #   if you want to see the available fonts type 'show fonts'
        # ──────────────────────────────────────────────────────────────
        #  please enter the font name:""")
        #     # FONT VALIDITY CHECK HERE
        #     if Font.upper() == "SHOW FONTS":
        #         show_fonts()
        #         Font = ""
        #         continue
        #     elif Font not in font_list:
        #         print("     invalid font !!! try again ")
        #         Font = ""
        #         continue

        #     while True:
        #         try:
        #             width = int(input("     Please enter your font width size:"))
        #             if width < 10:
        #                 print("     >>>Please a bigger value than this<<<")
        #                 continue
        #             break
        #         except  ValueError:
        #             print("     Please enter a valid integer!!")



        Thy_Art = pyfiglet.figlet_format(text_var,font_var)
        print(Thy_Art)

        return Thy_Art



    def exit_programm():
        pyfiglet.print_figlet("sayonara", font="speed")
        time.sleep(2)
        sys.exit()

    # def presets():

    def ArtGen():
        menu = """
    ┌──────────────────────────────────────────────────────────────┐
    │                          ARTGEN MENU       *underdevelopement│
    ├──────────────────────────────────────────────────────────────┤
    │                                                              │
    │  1.SHOW FONTS                                                │
    │  2.CREATE ART                                                │
    │  3.MENU                                                      │
    │  4.PRESETS                                                   │
    │  5.EXIT                                                      │
    │                                                              │
    └──────────────────────────────────────────────────────────────┘
    """
        print(menu)
        while True:
            user_input = input("Enter a command (show fonts, create art) or type 'exit' to quit the program: ")
            if user_input.upper() == "SHOW FONTS":
                show_fonts()
            elif user_input.upper() == "CREATE ART":
                print(create_art())
            elif user_input.upper() == "MENU":
                print(menu)
            elif user_input.upper() == "EXIT":
                exit_programm()
            else:
                print('invalid input!!!')



    
    def click(e):
        # retuned_value = f'''{create_art()}'''
        val = create_art()
        greeting.controls.append(ft.Text( value=val,selectable=True, font_family="cascadia" ))
        
        user_text.value= ""
        user_font.value= ""
        page.update()
        user_text.focus()
        user_font.focus()

    def clear(e):
        user_text.value= ""
        user_font.value= ""
        page.update()
        user_text.focus
        user_font.focus
    
    def clear_all(e):
        greeting.controls.clear()
        page.update()
        


    user_text = ft.TextField(width=900, 
                              height=100,
                              label="Text",
                              hint_text="Please enter your text here ")
    
    user_font = ft.TextField(width=900,
                             height=100,
                             label="Font Name",
                             hint_text="Please enter the name of your font here")
    
    submit_button = ft.ElevatedButton(text="submit", on_click=click)
    
    clear_all = ft.ElevatedButton(text="clear", on_click= clear, on_long_press=clear_all)





    control_row = ft.Row(controls=[submit_button,clear_all], alignment=ft.MainAxisAlignment.SPACE_EVENLY)
    Data_fields = ft.Column(controls=[user_text,user_font], alignment=ft.MainAxisAlignment.SPACE_AROUND)
    greeting = ft.Column(controls=[],alignment=ft.MainAxisAlignment.SPACE_AROUND)

    page.add(Data_fields,control_row,greeting)

ft.app(target=main, assets_dir="assets")












# _____________ _______ ___ 
#   __  ___/  __ `/_  __ `__ \
#   _(__  )/ /_/ /_  / / / / /
#   /____/ \__,_/ /_/ /_/ /_/ 
                          
#        _____________ _______ ___ 
# __  ___/  __ `/_  __ `__ \
# _(__  )/ /_/ /_  / / / / /
# /____/ \__,_/ /_/ /_/ /_/ 

# _____________ _______ ___ 
# __  ___/  __ `/_  __ `__ \
# _(__  )/ /_/ /_  / / / / /
# /____/ \__,_/ /_/ /_/ /_/ 

                                                             
# _____________ _______ ___ 
# __  ___/  __ `/_  __ `__ \
# _(__  )/ /_/ /_  / / / / /
# /____/ \__,_/ /_/ /_/ /_/ 
                    

#      _______.     ___      .___  ___.  _______  _______ .______      
#     /       |    /   \     |   \/   | |   ____||   ____||   _  \     
#    |   (----`   /  ^  \    |  \  /  | |  |__   |  |__   |  |_)  |    
#     \   \      /  /_\  \   |  |\/|  | |   __|  |   __|  |      /     
# .----)   |    /  _____  \  |  |  |  | |  |____ |  |____ |  |\  \----.
# |_______/    /__/     \__\ |__|  |__| |_______||_______|| _| `._____|
                                                                     
# ______________                             
# __  ___/__    |______ _____________________
# _____ \__  /| |_  __ `__ \  _ \  _ \_  ___/
# ____/ /_  ___ |  / / / / /  __/  __/  /    
# /____/ /_/  |_/_/ /_/ /_/\___/\___//_/     
                                           
