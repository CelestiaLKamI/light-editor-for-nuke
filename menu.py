import nuke
from light_editor_tool import light_editor

print("Loading menu.py...")

menu = nuke.menu("Nuke")
my_scripts = menu.addMenu("Mayukh Scripts")

light_editor_tool = my_scripts.addMenu("Light Editor")
light_editor_tool.addCommand("Light Editor", light_editor)