# Lesson below is:
# Menus and submenus
from Tkinter import *
import os
from tkFileDialog import *

os.system('cls')

# Define new classes

# Define new functions
def doNothing():
	print "OK ok I wont..."

# Define the root window
root = Tk()

# Define/Create it
base_menu = Menu(root)
fileMenu = Menu(base_menu)	#Used for "File" Commands
editMenu = Menu(base_menu)	#Used for "Edit" Commands
helpMenu = Menu(base_menu)	#Used for "Help" information window

# Configure
root.config(menu=base_menu)

base_menu.add_cascade(label = "file", menu = fileMenu)
fileMenu.add_command(label = "Load stage file...", command=doNothing)
fileMenu.add_separator()
fileMenu.add_command(label = "Exit", command=exit)

base_menu.add_cascade(label="Parameters", menu = editMenu)
editMenu.add_command(label="Select Parameters", command=doNothing)

base_menu.add_cascade(label="Help", menu = helpMenu)
helpMenu.add_command(label="About", command=doNothing)

# Bind function

# Place it

# Run the mainloop
root.mainloop()