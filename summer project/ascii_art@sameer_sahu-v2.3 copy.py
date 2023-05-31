import importlib
import pyfiglet 
# import sys 
# import time
import subprocess


# Changelog
changelog = {
    "v1.0": "Supports veiwing fonts, creting fonts, Basic error handeling",
    "v2.0": "Added new features - Advanced error handling, menu navigation, enhanced font selection.",
    "v2.1": "Added new features - save and load artwork, customization options.",
    "v2.2": "Added new features - ASCII art gallery, user preferences.",
    "v2.3": "Bug fixes and improvements.",
}

def print_changelog():
    # Print the changelog
    print("Changelog:")
    for version, changes in changelog.items():
        print(f"Version {version}: {changes}")

def module_compatibilty_installer():  
    print("---INTIALISATION---")
    modules_required = ["pyfiglet", "subprocess", "time", "sys"]
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
    user_text = input("Please enter the text you want to work with:")
    Font= ""
    
    while Font == "":
        Font = input("""
    ──────────────────────────────────────────────────────────────
      if you want to see the available fonts type 'show fonts'
    ──────────────────────────────────────────────────────────────
     please enter the font name:""")
        # FONT VALIDITY CHECK HERE
        if Font.upper() == "SHOW FONTS":
            show_fonts()
            Font = ""
            continue
        elif Font not in font_list:
            print("     invalid font !!! try again ")
            Font = ""
            continue

        while True:
            try:
                width = int(input("     Please enter your font width size:"))
                if width < 10:
                    print("     >>>Please a bigger value than this<<<")
                    continue
                break
            except  ValueError:
                print("     Please enter a valid integer!!")
                
         
        
    Thy_Art = pyfiglet.figlet_format(user_text,Font,justify= "centre" ,width=width)
    
    return Thy_Art



def exit_programm():
    pyfiglet.print_figlet("sayonara", font="speed")
    time.sleep(2)
    sys.exit()
         

def ArtGen():
    menu = """
┌──────────────────────────────────────────────────────────────┐
│                          ARTGEN MENU                         │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  1.SHOW FONTS                                                │
│  2.CREATE ART                                                │
│  3.MENU                                                      │
│  4.EXIT                                                      │
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



ArtGen()