import nuke
from light_editor_tool import light_editor

print("Loading menu.py...")

menu = nuke.menu("Nuke")
my_scripts = menu.addMenu("Mayukh Scripts")

my_scripts.addCommand("Light Editor", light_editor)