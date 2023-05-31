# # Define ANSI escape sequences for text colors
# RED = '\033[91m'
# GREEN = '\033[92m'
# YELLOW = '\033[93m'
# BLUE = '\033[94m'
# MAGENTA = '\033[95m'
# CYAN = '\033[96m'
# RESET = '\033[0m'  # Reset to default color

# # Print colored text
# print(RED + 'This is red text' + RESET)
# print(GREEN + 'This is green text' + RESET)
# print(YELLOW + 'This is yellow text' + RESET)
# print(BLUE + 'This is blue text' + RESET)
# print(MAGENTA + 'This is magenta text' + RESET)
# print(CYAN + 'This is cyan text' + RESET)



# import tkinter as tk

# def button_click():
#     label.config(text="Button clicked!")

# # Create the main window
# window = tk.Tk()

# # Create a label widget
# label = tk.Label(window, text="Hello GUI!")

# # Create a button widget
# button = tk.Button(window, text="Click me!", command=button_click)

# # Pack the label and button into the window
# label.pack()
# button.pack()

# # Start the GUI event loop
# window.mainloop()




import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("GUI Application")

        # Create a label widget
        self.label = QLabel("Hello PyQt!", self)
        self.label.setGeometry(50, 50, 200, 30)

        # Create a button widget
        self.button = QPushButton("Click me!", self)
        self.button.setGeometry(50, 100, 100, 30)
        self.button.clicked.connect(self.button_click)

    def button_click(self):
        self.label.setText("Button clicked!")


# Create the application instance
app = QApplication(sys.argv)

# Create the main window
window = MainWindow()
window.show()

# Start the application event loop
sys.exit(app.exec())
