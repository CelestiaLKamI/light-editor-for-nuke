import nuke
from production_path import set_prod_path
from shot_builder import shot_builder

print("Loading menu.py...")

menu = nuke.menu("Nuke")
my_scripts = menu.addMenu("Mayukh Scripts Test")

shot_builder_tool = my_scripts.addMenu("Shot Builder Tools")
shot_builder_tool.addCommand("Set Production Path", set_prod_path)
shot_builder_tool.addCommand("Shot Builder", shot_builder)