# Light Editor for Nuke

## Overview
Light Editor for Nuke is a tool adapted from Autodesk Maya's Light Editor Window. It allows users to manipulate basic attributes of light objects simultaneously. In addition to modifying attributes like intensity and color, this tool enables users to adjust translation, scaling, and rotation of light nodes within Nuke.

## Features
- List all light nodes in the Nuke script.
- Modify light properties such as intensity, color, cone angle, and falloff type.
- Transform light nodes by adjusting translation, rotation, and scale.
- Enable/disable lights quickly.
- Reset selected lights to their default properties.
- Seamless integration with Nuke’s UI.

## Installation
1. Copy the `light_editor_tool.py`, `init.py`, and `menu.py` files to your Nuke scripts directory.
2. Ensure the `mayukh_scripts` folder is properly referenced in `init.py`:
   ```python
   import nuke
   nuke.pluginAddPath(r"mayukh_scripts")
   ```
3. Restart Nuke to load the tool.

## Usage
1. Open Nuke and navigate to **Mayukh Scripts** in the menu bar.
2. Click on **Light Editor** to launch the tool.
3. Select a light from the list and modify its attributes using the UI controls.
4. Use the enable/disable button to toggle lights on/off.
5. Click **Reset** to revert a light’s properties to default.

## Dependencies
- Nuke
- PySide2

## Notes
- The tool automatically detects and lists all light nodes of type `Light`, `Light2`, `Light3`, and `Light4`.
- It includes both numerical inputs and sliders for precise adjustments.
- The UI dynamically updates based on the selected light type.

## License
This tool is free to use and modify. Attribution to the original author is appreciated.

## Author
**Mayukh Mitra**

---
For any issues or feature requests, feel free to open an issue on the Git repository.
