import importlib
import subprocess
import time
import sys
import os



# Global variables
font_list = []
user_preferences = {
    "default_font": "standard",
    "default_font_size": 80,
    "default_width": 80,
}

def load_user_preferences():
    # Load user preferences from a file or database
    # Set the values in the user_preferences dictionary

def save_user_preferences():
    # Save user preferences to a file or database
    # Use the values from the user_preferences dictionary

def update_changelog(version, changes):
    # Update the changelog dictionary with a new version and its changes
    changelog[version] = changes

def print_changelog():
    # Print the changelog
    print("Changelog:")
    for version, changes in changelog.items():
        print(f"Version {version}: {changes}")

def import_module(module_name):
    try:
        module = importlib.import_module(module_name)
        globals()[module_name] = module
        print(f"Successfully imported {module_name}")
        return module
    except Exception as e:
        print(f"Failed to import {module_name}: {e}")
        return None

def install_module(module_name):
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", module_name])
        return True
    except Exception as e:
        print(f"Failed to install {module_name}: {e}")
        return False

def import_required_modules(modules_required):
    for module_name in modules_required:
        if import_module(module_name) is None:
            print(f"Installing {module_name}...")
            if install_module(module_name):
                import_module(module_name)

def show_fonts():
    for f in font_list:
        print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-==-=-\n", "Font Name: ", f)
        pyfiglet.print_figlet(f, f)
    return font_list

def create_art():
    user_text = input("Please enter the text you want to work with: ")
    Font = ""
    
    while Font == "":
        Font = input("""
    ──────────────────────────────────────────────────────────────
      If you want to see the available fonts, type 'show fonts'
    ──────────────────────────────────────────────────────────────
     Please enter the font name: """)
        
        if Font.upper() == "SHOW FONTS":
            show_fonts()
            Font = ""
            continue
        elif Font not in font_list:
            print("Invalid font! Please try again.")
            Font = ""
            continue

        while True:
            try:
                width = int(input("Please enter your font width size: "))
                if width < 10:
                    print("Please enter a value greater than or equal to 10.")
                    continue
                break
            except ValueError:
                print("Please enter a valid integer!")
                
    Thy_Art = pyfiglet.figlet_format(user_text, Font, justify="centre", width=width)
    
    return Thy_Art

def save_artwork(artwork):
    filename = input("Enter the filename to save the artwork: ")
    with open(filename, "w") as file:
        file.write(artwork)
    print(f"Artwork saved successfully as {filename}!")

def load_artwork():
    filename = input("Enter the filename to load artwork from: ")
    try:
        with open(filename, "r") as file:
            artwork = file.read()
        print("Loaded artwork:")
        print(artwork)
    except FileNotFoundError:
        print("File not found. Please enter a valid filename.")

def exit_program():
    print("Goodbye!")
    save_user_preferences()
    sys.exit()

def ArtGen():
    print_changelog()
    import_required_modules(["pyfiglet", "subprocess", "time", "sys"])

    while True:
        print("""
┌──────────────────────────────────────────────────────────────┐
│                          ARTGEN MENU                         │
├──────────────────────────────────────────────────────────────┤
│                                                              │
│  1. SHOW FONTS                                               │
│  2. CREATE ART                                               │
│  3. SAVE ARTWORK                                             │
│  4. LOAD ARTWORK                                             │
│  5. MENU                                                     │
│  6. EXIT                                                     │
│                                                              │
└──────────────────────────────────────────────────────────────┘
""")
        user_input = input("Enter a command (show fonts, create art, save artwork, load artwork) "
                           "or type 'exit' to quit the program: ")
        
        if user_input.upper() == "SHOW FONTS":
            show_fonts()
            
        elif user_input.upper() == "CREATE ART":
            print(create_art())
            
        elif user_input.upper() == "SAVE ARTWORK":
            artwork = create_art()
            save_artwork(artwork)
            
        elif user_input.upper() == "LOAD ARTWORK":
            load_artwork()
            
        elif user_input.upper() == "MENU":
            continue
            
        elif user_input.upper() == "EXIT":
            exit_program()
            
        else:
            print("Invalid input!")

ArtGen()
