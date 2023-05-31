import pyfiglet 
import sys 
import time

font_list = pyfiglet.Figlet().getFonts()


def show_fonts():
    
    for f in font_list:
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-\n","Font Name: ",f)
        pyfiglet.print_figlet(f,f)
    return font_list

# def font_validity_check():
    # if in font_list:


def create_art():
    user_text = input("Please enter the text you want to work with:")
    Font= ""
    
    while Font == "":
        Font = input("""
    ──────────────────────────────────────────────────────────────
      if you want to see the available fonts type 'show fonts'
    ──────────────────────────────────────────────────────────────
     please enter the font name:""")
        
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
│  3.EXIT                                                      │
│                                                              │
└──────────────────────────────────────────────────────────────┘
"""
    print(menu)
    while True:
        user_input = input("Enter a command or type 'exit' to quit the program: ")
        if user_input.upper() == "SHOW FONTS":
            show_fonts()
        elif user_input.upper() == "CREATE ART":
            print(create_art())
        elif user_input.upper() == "EXIT":
            exit_programm()
        elif user_input.upper() == "MENU":
            print(menu)
        else:
            print('invalid input!!!')



ArtGen()