import nuke
from light_editor_tool import light_editor

print("Loading menu.py...")

menu = nuke.menu("Nuke")
my_scripts = menu.addMenu("Mayukh Scripts Test")

shot_builder_tool = my_scripts.addMenu("Light Editor")
shot_builder_tool.addCommand("Light Editor", light_editor)