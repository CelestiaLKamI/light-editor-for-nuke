import nuke
from PySide2.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QHeaderView, QPushButton, QDoubleSpinBox, QSlider, QLabel, QLineEdit, QComboBox, QFrame, QHBoxLayout, QVBoxLayout, QGridLayout, QSizePolicy
from PySide2.QtCore import Qt

class MainWindow(QWidget):
    """
    Main window class for the Light Editor Tool.
    This class creates the UI and handles interactions with Nuke light nodes.
    """
    def __init__(self):
        """
        Initializes the main window and sets up the UI components.
        """
        super().__init__()

        # Create layout containers
        gbox0 = QGridLayout()
        hbox2 = QHBoxLayout()
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        gbox1 = QGridLayout()
        gbox2 = QGridLayout()

        # Create a horizontal separator
        horizontal_separator = QFrame()
        horizontal_separator.setFrameShape(QFrame.HLine)
        horizontal_separator.setFrameShadow(QFrame.Sunken)

        # Create the lights list table
        self.lights_list_table = QTableWidget()
        self.lights_list_table.setColumnCount(4)
        self.lights_list_table.setHorizontalHeaderLabels(["Name", "Light Type", "Color", "Intensity"])
        self.lights_list_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.lights_list_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.lights_list_table.selectionModel().selectionChanged.connect(self.update_selected_rows)
        
        # Create light control buttons
        self.enable_light_button = QPushButton("Disable")
        self.enable_light_button.clicked.connect(self.enable_disable)
        self.reset_button = QPushButton("Reset")
        self.reset_button.clicked.connect(self.reset_to_default)

        gbox0.setColumnStretch(0, 2)
        gbox0.addWidget(self.enable_light_button, 0, 4)
        gbox0.addWidget(self.reset_button, 0, 5)

        # Create labels for light properties
        light_name_label = QLabel("Light Name")
        light_name_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        light_type_label = QLabel("Light Type")
        light_type_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        color_label = QLabel("Color")
        color_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        r_label = QLabel("R")
        r_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        g_label = QLabel("G")
        g_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        b_label = QLabel("B")
        b_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        intensity_label = QLabel("Intensity")
        intensity_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        cone_angle_label = QLabel("Cone Angle")
        cone_angle_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        cone_penumbra_angle_label = QLabel("Cone Penumbra Angle")
        cone_penumbra_angle_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        cone_falloff_label = QLabel("Cone Falloff")
        cone_falloff_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        falloff_type_label = QLabel("Falloff Type")
        falloff_type_label.setAlignment(Qt.AlignRight | Qt.AlignVCenter)

        # Add labels to the grid layout
        gbox1.addWidget(light_name_label, 0, 0)
        gbox1.addWidget(light_type_label, 1, 0)
        gbox1.addWidget(color_label, 2, 0)
        gbox1.addWidget(r_label, 3, 0)
        gbox1.addWidget(g_label, 4, 0)
        gbox1.addWidget(b_label, 5, 0)
        gbox1.addWidget(intensity_label, 6, 0)
        gbox1.addWidget(cone_angle_label, 7, 0)
        gbox1.addWidget(cone_penumbra_angle_label, 8, 0)
        gbox1.addWidget(cone_falloff_label, 9, 0)
        gbox1.addWidget(falloff_type_label, 10, 0)

        # Create labels for transformation properties
        translate_label = QLabel("Translate")
        rotate_label = QLabel("Rotate")
        scale_label = QLabel("Scale")
        x_translate_label = QLabel("X")
        y_translate_label = QLabel("Y")
        z_translate_label = QLabel("Z")
        x_rotate_label = QLabel("X")
        y_rotate_label = QLabel("Y")
        z_rotate_label = QLabel("Z")
        x_scale_label = QLabel("X")
        y_scale_label = QLabel("Y")
        z_scale_label = QLabel("Z")
        uniform_scale_label = QLabel("Uniform Scale")
        
        # Add transformation labels to the grid layout
        gbox2.addWidget(translate_label, 0, 0)
        gbox2.addWidget(rotate_label, 1, 0)
        gbox2.addWidget(scale_label, 2, 0)
        gbox2.addWidget(x_translate_label, 0, 1)
        gbox2.addWidget(y_translate_label, 0, 3)
        gbox2.addWidget(z_translate_label, 0, 5)
        gbox2.addWidget(x_rotate_label, 1, 1)
        gbox2.addWidget(y_rotate_label, 1, 3)
        gbox2.addWidget(z_rotate_label, 1, 5)
        gbox2.addWidget(x_scale_label, 2, 1)
        gbox2.addWidget(y_scale_label, 2, 3)
        gbox2.addWidget(z_scale_label, 2, 5)
        gbox2.addWidget(uniform_scale_label, 3, 0)

        # Create input fields for light properties
        self.light_name_input = QLineEdit()
        self.light_name_input.setPlaceholderText("Enter Light Name")
        self.light_name_input.textChanged.connect(self.edit_name)
        self.light_type_input = QComboBox()
        self.light_type_input.addItems(["point", "directional", "spot"])
        self.light_type_input.currentIndexChanged.connect(self.edit_properties_from_spinbox)
        self.color_input = QPushButton("Color")
        self.color_input.setMaximumWidth(50)
        self.color_input.clicked.connect(self.color_pick)
        self.r_input = QDoubleSpinBox()
        self.r_input.setMaximumWidth(50)
        self.r_input.setRange(0, 1)
        self.r_input.valueChanged.connect(self.edit_properties_from_spinbox)
        self.r_slider_input = QSlider(Qt.Horizontal)
        self.r_slider_input.setRange(1, 100)
        self.r_slider_input.valueChanged.connect(self.edit_properties_from_sliders)
        self.g_input = QDoubleSpinBox()
        self.g_input.setMaximumWidth(50)
        self.g_input.setRange(0, 1)
        self.g_input.valueChanged.connect(self.edit_properties_from_spinbox)
        self.g_slider_input = QSlider(Qt.Horizontal)
        self.g_slider_input.setRange(1, 100)
        self.g_slider_input.valueChanged.connect(self.edit_properties_from_sliders)
        self.b_input = QDoubleSpinBox()
        self.b_input.setMaximumWidth(50)
        self.b_input.setRange(0, 1)
        self.b_input.valueChanged.connect(self.edit_properties_from_spinbox)
        self.b_slider_input = QSlider(Qt.Horizontal)
        self.b_slider_input.setRange(1, 100)
        self.b_slider_input.valueChanged.connect(self.edit_properties_from_sliders)
        self.intensity_input = QDoubleSpinBox()
        self.intensity_input.setMaximumWidth(50)
        self.intensity_input.setRange(0, 50)
        self.intensity_input.valueChanged.connect(self.edit_properties_from_spinbox)
        self.intensity_slider_input = QSlider(Qt.Horizontal)
        self.intensity_slider_input.setRange(0, 50) #(0, 50)
        self.intensity_slider_input.valueChanged.connect(self.edit_properties_from_sliders)
        self.cone_angle_input = QDoubleSpinBox()
        self.cone_angle_input.setMaximumWidth(50)
        self.cone_angle_input.setRange(0, 180)
        self.cone_angle_input.valueChanged.connect(self.edit_properties_from_spinbox)
        self.cone_angle_slider_input = QSlider(Qt.Horizontal)
        self.cone_angle_slider_input.setRange(0, 180)
        self.cone_angle_slider_input.valueChanged.connect(self.edit_properties_from_sliders)
        self.cone_penumbra_angle_input = QDoubleSpinBox()
        self.cone_penumbra_angle_input.setMaximumWidth(50)
        self.cone_penumbra_angle_input.setRange(-60, 60)
        self.cone_penumbra_angle_input.valueChanged.connect(self.edit_properties_from_spinbox)
        self.cone_penumbra_angle_slider_input = QSlider(Qt.Horizontal)
        self.cone_penumbra_angle_slider_input.setRange(-60, 60)
        self.cone_penumbra_angle_slider_input.valueChanged.connect(self.edit_properties_from_sliders)
        self.cone_falloff_input = QDoubleSpinBox()
        self.cone_falloff_input.setMaximumWidth(50)
        self.cone_falloff_input.setRange(0, 1000)
        self.cone_falloff_input.valueChanged.connect(self.edit_properties_from_spinbox)
        self.cone_falloff_slider_input = QSlider(Qt.Horizontal)
        self.cone_falloff_slider_input.setRange(0, 1000)
        self.cone_falloff_slider_input.valueChanged.connect(self.edit_properties_from_sliders)
        self.falloff_type_input = QComboBox()
        self.falloff_type_input.addItems(["None", "Linear", "Quadratic", "Cubic"])
        self.falloff_type_input.currentIndexChanged.connect(self.edit_properties_from_spinbox)

        # Add input fields to the grid layout
        gbox1.addWidget(self.light_name_input, 0, 1, 1, 4)
        gbox1.addWidget(self.light_type_input, 1, 1, 1, 4)
        gbox1.addWidget(self.color_input, 2, 1)
        gbox1.addWidget(self.r_input, 3, 1)
        gbox1.addWidget(self.r_slider_input, 3, 2, 1, 3)
        gbox1.addWidget(self.g_input, 4, 1)
        gbox1.addWidget(self.g_slider_input, 4, 2, 1, 3)
        gbox1.addWidget(self.b_input, 5, 1)
        gbox1.addWidget(self.b_slider_input, 5, 2, 1, 3)
        gbox1.addWidget(self.intensity_input, 6, 1)
        gbox1.addWidget(self.intensity_slider_input, 6, 2, 1, 3)
        gbox1.addWidget(self.cone_angle_input, 7, 1)
        gbox1.addWidget(self.cone_angle_slider_input, 7, 2, 1, 3)
        gbox1.addWidget(self.cone_penumbra_angle_input, 8, 1)
        gbox1.addWidget(self.cone_penumbra_angle_slider_input, 8, 2, 1, 3)
        gbox1.addWidget(self.cone_falloff_input, 9, 1)
        gbox1.addWidget(self.cone_falloff_slider_input, 9, 2, 1, 3)
        gbox1.addWidget(self.falloff_type_input, 10, 1, 1, 4)

        # Create input fields for transformation properties
        self.x_translate_input = QDoubleSpinBox()
        self.x_translate_input.valueChanged.connect(self.edit_translations)
        self.y_translate_input = QDoubleSpinBox()
        self.y_translate_input.valueChanged.connect(self.edit_translations)
        self.z_translate_input = QDoubleSpinBox()
        self.z_translate_input.valueChanged.connect(self.edit_translations)
        self.x_rotate_input = QDoubleSpinBox()
        self.x_rotate_input.valueChanged.connect(self.edit_translations)
        self.y_rotate_input = QDoubleSpinBox()
        self.y_rotate_input.valueChanged.connect(self.edit_translations)
        self.z_rotate_input = QDoubleSpinBox()
        self.z_rotate_input.valueChanged.connect(self.edit_translations)
        self.x_scale_input = QDoubleSpinBox()
        self.x_scale_input.valueChanged.connect(self.edit_translations)
        self.y_scale_input = QDoubleSpinBox()
        self.y_scale_input.valueChanged.connect(self.edit_translations)
        self.z_scale_input = QDoubleSpinBox()
        self.z_scale_input.valueChanged.connect(self.edit_translations)
        self.uniform_scale_input = QDoubleSpinBox()
        self.uniform_scale_input.setRange(0.01, 10)
        self.uniform_scale_input.valueChanged.connect(self.edit_translations)
        self.uniform_scale_slider_input = QSlider(Qt.Horizontal)
        self.uniform_scale_slider_input.setRange(0.01, 10)
        self.uniform_scale_slider_input.valueChanged.connect(self.edit_properties_from_sliders)

        # Add transformation input fields to the grid layout
        gbox2.addWidget(self.x_translate_input, 0, 2)
        gbox2.addWidget(self.y_translate_input, 0, 4)
        gbox2.addWidget(self.z_translate_input, 0, 6)
        gbox2.addWidget(self.x_rotate_input, 1, 2)
        gbox2.addWidget(self.y_rotate_input, 1, 4)
        gbox2.addWidget(self.z_rotate_input, 1, 6)
        gbox2.addWidget(self.x_scale_input, 2, 2)
        gbox2.addWidget(self.y_scale_input, 2, 4)
        gbox2.addWidget(self.z_scale_input, 2, 6)
        gbox2.addWidget(self.uniform_scale_input, 3, 2)
        gbox2.addWidget(self.uniform_scale_slider_input, 3, 3, 1, 4)

        # Add layouts to the vertical layout
        vbox1.addLayout(gbox0)
        vbox1.addWidget(self.lights_list_table)
        vbox2.addLayout(gbox1)
        vbox2.addWidget(horizontal_separator)
        vbox2.addLayout(gbox2)

        # Add vertical layouts to the horizontal layout
        hbox2.addLayout(vbox1)
        hbox2.addLayout(vbox2)

        # Set the main layout
        self.setLayout(hbox2)
        
        # Populate the table with light nodes
        self.populate_table()

    def populate_table(self):
        """
        Populates the lights list table with light nodes from the Nuke script.
        """
        all_nodes = nuke.allNodes()
        target_classes = ["Light", "Light2", "Light3", "Light4"]
        light_nodes = [node for node in all_nodes if node.Class() in target_classes]
        self.lights_list_table.setRowCount(len(light_nodes))
        
        for i, each_light in enumerate(light_nodes):
            if each_light["name"]:
                name_item = QTableWidgetItem(each_light["name"].getValue())
                name_item.setFlags(name_item.flags() & ~Qt.ItemIsEditable)
                self.lights_list_table.setItem(i, 0, name_item)
            
            if "light_type" in each_light.knobs():
                if each_light["light_type"]:   
                    light_type_item = QTableWidgetItem(each_light["light_type"].value())
                    light_type_item.setFlags(light_type_item.flags() & ~Qt.ItemIsEditable)
                    self.lights_list_table.setItem(i, 1, light_type_item)
            else:
                light_type_item = QTableWidgetItem(each_light.Class())
                light_type_item.setFlags(light_type_item.flags() & ~Qt.ItemIsEditable)
                self.lights_list_table.setItem(i, 1, light_type_item)                
               
            if each_light["color"]:
                color_item = QTableWidgetItem(str(each_light["color"].getValue()))
                color_item.setFlags(color_item.flags() & ~Qt.ItemIsEditable)
                self.lights_list_table.setItem(i, 2, color_item)
            
            if each_light["intensity"]: 
                intensity_item = QTableWidgetItem(str(each_light["intensity"].getValue()))                
                intensity_item.setFlags(intensity_item.flags() & ~Qt.ItemIsEditable)
                self.lights_list_table.setItem(i, 3, intensity_item)

    def update_selected_rows(self):
        self.selected_rows = self.lights_list_table.selectionModel().selectedRows()

        if not self.selected_rows:
            return  

        if len(self.selected_rows) > 1:
            self.light_name_input.setDisabled(True)
        else:
            self.light_name_input.setDisabled(False)

            light_name = self.lights_list_table.item(self.selected_rows[0].row(), 0).text()
            light_node = nuke.toNode(light_name)

            if light_node:
                self.light_name_input.setText(light_name)
                self.previous_name = light_name  # Store the current name before renaming
                self.light_type_input.setEnabled("light_type" in light_node.knobs())
            else:
                self.light_name_input.clear()
                self.light_type_input.setDisabled(True)

            self.enable_inputs()

        self.update_spinbox_values()
        self.update_slider_values()
        self.update_enable_button()


    def update_enable_button(self):
        """
        Updates the enable/disable button text based on the selected light nodes.
        """
        if not self.selected_rows:
            self.enable_light_button.setText("Disable")  # Default text
            self.enable_light_button.setDisabled(True)
            return

        # Enable button since at least one row is selected
        self.enable_light_button.setDisabled(False)

        if len(self.selected_rows) > 1:
            self.enable_light_button.setText("Disable")  # Multiple selection case
            return

        # Single selection case: Update based on disable state
        light_name = self.lights_list_table.item(self.selected_rows[0].row(), 0).text()
        light_node = nuke.toNode(light_name)

        if not light_node:
            self.enable_light_button.setText("Disable")
            return

        self.enable_light_button.setText("Enable" if light_node["disable"].value() else "Disable")
        
    def enable_disable(self):
        """
        Toggles the enable/disable state of the selected light nodes.
        """
        if not self.selected_rows:
            nuke.message("Please select at least one light to toggle enable/disable")
            return

        for each_row in self.selected_rows:
            light_name = self.lights_list_table.item(each_row.row(), 0).text()
            light_node = nuke.toNode(light_name)

            if not light_node:
                nuke.message(f"Light node '{light_name}' not found.")
                return

            # Toggle disable state
            current_state = light_node["disable"].value()
            light_node["disable"].setValue(not current_state)

        # Update button text after toggling
        self.update_enable_button()

    def update_spinbox_values(self):
        """
        Updates the light properties input fields with the values from the selected light node.
        """
        if not self.selected_rows:
            return

        light_name = self.lights_list_table.item(self.selected_rows[0].row(), 0).text()
        light_node = nuke.toNode(light_name)

        if not light_node:
            nuke.message("Light node not found")
            return

        if "light_type" in light_node.knobs():
            self.light_type_input.setCurrentText(light_node["light_type"].value())
        
        # Update the color input fields if the knob exists
        if "color" in light_node.knobs():
            color = light_node["color"].value()
            if type(color) == list:
                self.r_input.setValue(color[0])
                self.g_input.setValue(color[1])
                self.b_input.setValue(color[2])
            else:
                self.r_input.setValue(1)
                self.g_input.setValue(1)
                self.b_input.setValue(1)

        if "intensity" in light_node.knobs():
            self.intensity_input.setValue(light_node["intensity"].value())

        if "cone_angle" in light_node.knobs():
            self.cone_angle_input.setValue(light_node["cone_angle"].value())

        if "cone_penumbra_angle" in light_node.knobs():
            self.cone_penumbra_angle_input.setValue(light_node["cone_penumbra_angle"].value())
        
        if "cone_falloff" in light_node.knobs():
            self.cone_falloff_input.setValue(light_node["cone_falloff"].value())

        if "falloff_type" in light_node.knobs():
            self.falloff_type_input.setCurrentText(light_node["falloff_type"].value())

        if "translate" in light_node.knobs():
            translate = light_node["translate"].value()
            self.x_translate_input.setValue(translate[0])
            self.y_translate_input.setValue(translate[1])
            self.z_translate_input.setValue(translate[2])
        
        if "rotate" in light_node.knobs():
            rotate = light_node["rotate"].value()
            self.x_rotate_input.setValue(rotate[0])
            self.y_rotate_input.setValue(rotate[1])
            self.z_rotate_input.setValue(rotate[2])

        if "scale" in light_node.knobs():
            scale = light_node["scale"].value()
            self.x_scale_input.setValue(scale[0])
            self.y_scale_input.setValue(scale[1])
            self.z_scale_input.setValue(scale[2])

        if "uniform_scale" in light_node.knobs():
            self.uniform_scale_input.setValue(light_node["uniform_scale"].value())

    def update_slider_values(self):
        # Update the color slider values
        self.r_slider_input.setValue(self.r_input.value() * 100)
        self.g_slider_input.setValue(self.g_input.value() * 100)
        self.b_slider_input.setValue(self.b_input.value() * 100)

        self.intensity_slider_input.setValue(self.intensity_input.value())
        self.cone_angle_slider_input.setValue(self.cone_angle_input.value())
        self.cone_penumbra_angle_slider_input.setValue(self.cone_penumbra_angle_input.value())
        self.cone_falloff_slider_input.setValue(self.cone_falloff_input.value() )
        self.uniform_scale_slider_input.setValue(self.uniform_scale_input.value())

    def edit_name(self):
        """
        Edits the name of the selected light node.
        """
        if len(self.selected_rows) != 1:
            nuke.message("Please select exactly one light to rename.")
            return

        row = self.selected_rows[0].row()
        old_name = self.lights_list_table.item(row, 0).text()
        light_node = nuke.toNode(old_name)

        if not light_node:
            nuke.message("Selected light node not found in Nuke.")
            return

        # Get the new name from the input field
        new_name = self.light_name_input.text().strip()

        # Prevent renaming if the name has not changed
        if new_name == old_name:
            return  # No need to rename

        # Validate the new name
        if not new_name:
            nuke.message("Please enter a valid light name.")
            return

        if new_name[0].isdigit():
            nuke.message("Light name cannot start with a number.")
            return

        # Check if the new name already exists in Nuke
        if nuke.toNode(new_name):
            nuke.message("A node with this name already exists. Choose a different name.")
            return

        # Apply the new name to the light node
        light_node["name"].setValue(new_name)

        # Update the name in the table
        self.lights_list_table.item(row, 0).setText(new_name)

        # Store the new name as the previous name
        self.previous_name = new_name

    def color_pick(self):
        """
        Opens the color picker dialog to select a color for the light node.
        """
        if not self.selected_rows:
            nuke.message("Please select at least one light to pick a color")
            return

        color = nuke.getColor()

        for each_row in self.selected_rows:
            light_name = self.lights_list_table.item(each_row.row(), 0).text()
            light_node = nuke.toNode(light_name)

            if not light_node:
                nuke.message("Light node not found")
                return

            if color:
                print(f"Raw color value: {color}")  # Debugging raw color value
                
                # Extract RGBA components using correct bitwise operations
                r = (color >> 24) & 255 # Alpha
                g = (color >> 16) & 255 # Red
                b = (color >> 8) & 255 # Green
                a = (color >> 0) & 255 # Blue
                color_normalized = [r, g, b, a]
                # Update GUI input fields with selected color
                self.r_input.setValue(r)
                self.g_input.setValue(g)
                self.b_input.setValue(b)

        # Update the color display with the last selected color
        if color:
            self.color_input.setStyleSheet(f"background-color: rgb({r}, {g}, {b});")

    def edit_properties_from_spinbox(self):
        """
        Edits the properties of the selected light nodes.
        """
        if not self.selected_rows:
            nuke.message("Please select at least one light to edit properties")
            return
        
        for each_row in self.selected_rows:
            light_name = self.lights_list_table.item(each_row.row(), 0).text()
            light_node = nuke.toNode(light_name)

            if not light_node:
                nuke.message("Light node not found")
                return

            if "light_type" in light_node.knobs():
                light_node["light_type"].setValue(self.light_type_input.currentText())
                self.enable_inputs()

            if "intensity" in light_node.knobs():
                light_node["intensity"].setValue(self.intensity_input.value())
                self.lights_list_table.item(each_row.row(), 3).setText(str(self.intensity_input.value()))
            
            if "cone_angle" in light_node.knobs():
                light_node["cone_angle"].setValue(self.cone_angle_input.value())

            if "cone_penumbra_angle" in light_node.knobs():
                light_node["cone_penumbra_angle"].setValue(self.cone_penumbra_angle_input.value())
            
            if "cone_falloff" in light_node.knobs():
                light_node["cone_falloff"].setValue(self.cone_falloff_input.value())

            if "falloff_type" in light_node.knobs():
                light_node["falloff_type"].setValue(self.falloff_type_input.currentText())
            
            if "color" in light_node.knobs():
                light_node["color"].setValue([self.r_input.value(), self.g_input.value(), self.b_input.value()])
                self.lights_list_table.item(each_row.row(), 2).setText(str([self.r_input.value(), self.g_input.value(), self.b_input.value()]))

        self.update_slider_values()

    def edit_properties_from_sliders(self):
        """Edits the properties of the selected light nodes using the sliders."""
        if not self.selected_rows:
            nuke.message("Please select at least one light to edit properties")
            return

        for each_row in self.selected_rows:
            light_name = self.lights_list_table.item(each_row.row(), 0).text()
            light_node = nuke.toNode(light_name)

            if not light_node:
                nuke.message("Light node not found")
                return

            if "color" in light_node.knobs():
                light_node["color"].setValue([self.r_slider_input.value() / 100, self.g_slider_input.value() / 100, self.b_slider_input.value() / 100])

            if "intensity" in light_node.knobs():
                light_node["intensity"].setValue(self.intensity_slider_input.value())

            if "cone_angle" in light_node.knobs():
                light_node["cone_angle"].setValue(self.cone_angle_slider_input.value())

            if "cone_penumbra_angle" in light_node.knobs():
                light_node["cone_penumbra_angle"].setValue(self.cone_penumbra_angle_slider_input.value())

            if "cone_falloff" in light_node.knobs():
                light_node["cone_falloff"].setValue(self.cone_falloff_slider_input.value())

            if "uniform_scale" in light_node.knobs():
                light_node["uniform_scale"].setValue(self.uniform_scale_slider_input.value())
        
        self.update_spinbox_values()

    def edit_translations(self):
        """
        Edits the translation, rotation, and scale properties of the selected light nodes.
        """
        if not self.selected_rows:
            nuke.message("Please select at least one light to edit properties")
            return
        
        # Iterate over each selected row
        for each_row in self.selected_rows:
            light_name = self.lights_list_table.item(each_row.row(), 0).text()
            light_node = nuke.toNode(light_name)

            if not light_node:
                nuke.message("Light node not found")
                return

            # Update the translation, rotation, and scale properties
            light_node["translate"].setValue([self.x_translate_input.value(), self.y_translate_input.value(), self.z_translate_input.value()])
            light_node["rotate"].setValue([self.x_rotate_input.value(), self.y_rotate_input.value(), self.z_rotate_input.value()])
            light_node["scaling"].setValue([self.x_scale_input.value(), self.y_scale_input.value(), self.z_scale_input.value()])
            light_node["uniform_scale"].setValue(self.uniform_scale_input.value())

    def enable_inputs(self): 
        """
        Enables and disables input fields based on the selected light node and its type.
        """
        if not self.selected_rows:
            nuke.message("Please select at least one light to edit properties")
            return
        
        # Get the first selected light node (since this only applies to single selection)
        light_name = self.lights_list_table.item(self.selected_rows[0].row(), 0).text()
        light_node = nuke.toNode(light_name)

        if not light_node:
            nuke.message("Light node not found")
            return

        # Enable all controls initially
        self.cone_angle_input.setEnabled(True)
        self.cone_angle_slider_input.setEnabled(True)
        self.cone_penumbra_angle_input.setEnabled(True)
        self.cone_penumbra_angle_slider_input.setEnabled(True)
        self.cone_falloff_input.setEnabled(True)
        self.cone_falloff_slider_input.setEnabled(True)
        self.falloff_type_input.setEnabled(True)

        # Disable controls based on light type
        if "light_type" in light_node.knobs():
            light_type = light_node["light_type"].value()
            # If the light type is "point", disable few controls
            if light_type == "point":
                self.cone_angle_input.setDisabled(True)
                self.cone_angle_slider_input.setDisabled(True)
                self.cone_penumbra_angle_input.setDisabled(True)
                self.cone_penumbra_angle_slider_input.setDisabled(True)
                self.cone_falloff_input.setDisabled(True)
                self.cone_falloff_slider_input.setDisabled(True)
            # If the light type is "directional", disable few controls
            elif light_type == "directional":
                self.cone_angle_input.setDisabled(True)
                self.cone_angle_slider_input.setDisabled(True)
                self.cone_penumbra_angle_input.setDisabled(True)
                self.cone_penumbra_angle_slider_input.setDisabled(True)
                self.cone_falloff_input.setDisabled(True)
                self.cone_falloff_slider_input.setDisabled(True)
                self.falloff_type_input.setDisabled(True)
        else:
            # If "light_type" doesn't exist, disable these controls
            self.cone_angle_input.setDisabled(True)
            self.cone_angle_slider_input.setDisabled(True)
            self.cone_penumbra_angle_input.setDisabled(True)
            self.cone_penumbra_angle_slider_input.setDisabled(True)
            self.cone_falloff_input.setDisabled(True)
            self.cone_falloff_slider_input.setDisabled(True)
            self.falloff_type_input.setDisabled(False)

    def reset_to_default(self):
        """
        Resets the selected light nodes to their default properties.
        """
        if not self.selected_rows:
            nuke.message("Please select at least one light to reset.")
            return

        for each_row in self.selected_rows:
            light_name = self.lights_list_table.item(each_row.row(), 0).text()
            light_node = nuke.toNode(light_name)

            if not light_node:
                nuke.message(f"Light node '{light_name}' not found.")
                return
            # Resetting Knobs to default values
            light_node.resetKnobsToDefault()

        if self.selected_rows:
            # Clearing the stylesheet from previous selection
            self.color_input.setStyleSheet("")
            
        self.populate_table()
        self.update_selected_rows()

def light_editor():
    """
    Initializes and shows the Light Editor Tool.
    """
    global window
    window = MainWindow()
    window.setMinimumSize(900, 450)
    window.show()