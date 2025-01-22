import nuke
from PySide2.QtWidgets import QWidget, QTableWidget, QTableWidgetItem, QHeaderView, QPushButton, QDoubleSpinBox, QSlider, QLabel, QLineEdit, QComboBox, QFrame, QHBoxLayout, QVBoxLayout, QGridLayout
from PySide2.QtCore import Qt

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        hbox1 = QHBoxLayout()
        hbox2 = QHBoxLayout()
        vbox1 = QVBoxLayout()
        vbox2 = QVBoxLayout()
        gbox1 = QGridLayout()
        gbox2 = QGridLayout()

        horizontal_separator = QFrame()
        horizontal_separator.setFrameShape(QFrame.HLine)
        horizontal_separator.setFrameShadow(QFrame.Sunken)

        self.lights_list_table = QTableWidget()
        self.lights_list_table.setColumnCount(4)
        self.lights_list_table.setHorizontalHeaderLabels(["Light Type/Class", "Name", "Color", "Intensity"])
        self.lights_list_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.lights_list_table.setSelectionBehavior(QTableWidget.SelectRows)
        self.lights_list_table.selectionModel().selectionChanged.connect(self.update_selected_rows)
        
        point_light_button = QPushButton("Point")
        spot_light_button = QPushButton("Spot")
        directional_light_button = QPushButton("Directional")
        enable_light_button = QPushButton("Enable")
        disable_light_button = QPushButton("Disable")

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

        self.light_name_input = QLineEdit()
        self.light_name_input.setPlaceholderText("Enter Light Name")
        self.light_name_input.textChanged.connect(self.edit_name)
        self.light_type_input = QComboBox()
        self.light_type_input.addItems(["Point", "Spot", "Directional"])
        self.light_type_input.currentIndexChanged.connect(self.edit_properties)
        color_input = QPushButton("Color")
        self.r_input = QDoubleSpinBox()
        self.r_input.setRange(0, 1)
        self.r_input.valueChanged.connect(self.edit_properties)
        self.r_slider_input = QSlider(Qt.Horizontal)
        self.r_slider_input.setRange(0, 1)
        self.g_input = QDoubleSpinBox()
        self.g_input.setRange(0, 1)
        self.g_input.valueChanged.connect(self.edit_properties)
        self.g_slider_input = QSlider(Qt.Horizontal)
        self.g_slider_input.setRange(0, 1)
        self.b_input = QDoubleSpinBox()
        self.b_input.setRange(0, 1)
        self.b_input.valueChanged.connect(self.edit_properties)
        self.b_slider_input = QSlider(Qt.Horizontal)
        self.b_slider_input.setRange(0, 1)
        self.intensity_input = QDoubleSpinBox()
        self.intensity_input.setRange(0, 50)
        self.intensity_input.valueChanged.connect(self.edit_properties)
        self.intensity_slider_input = QSlider(Qt.Horizontal)
        self.intensity_slider_input.setRange(0, 50)
        self.cone_angle_input = QDoubleSpinBox()
        self.cone_angle_input.setRange(0, 180)
        self.cone_angle_input.valueChanged.connect(self.edit_properties)
        self.cone_angle_slider_input = QSlider(Qt.Horizontal)
        self.cone_angle_slider_input.setRange(0, 180)
        self.cone_penumbra_angle_input = QDoubleSpinBox()
        self.cone_penumbra_angle_input.setRange(-60, 60)
        self.cone_penumbra_angle_input.valueChanged.connect(self.edit_properties)
        self.cone_penumbra_angle_slider_input = QSlider(Qt.Horizontal)
        self.cone_penumbra_angle_slider_input.setRange(-60, 60)
        self.cone_falloff_input = QDoubleSpinBox()
        self.cone_falloff_input.setRange(0, 1000)
        self.cone_falloff_input.valueChanged.connect(self.edit_properties)
        self.cone_falloff_slider_input = QSlider(Qt.Horizontal)
        self.cone_falloff_slider_input.setRange(0, 1000)
        self.falloff_type_input = QComboBox()
        self.falloff_type_input.addItems(["None", "Linear", "Quadratic", "Cubic"])
        self.falloff_type_input.currentIndexChanged.connect(self.edit_properties)

        gbox1.addWidget(self.light_name_input, 0, 1, 1, 4)
        gbox1.addWidget(self.light_type_input, 1, 1)
        gbox1.addWidget(color_input, 2, 1)
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
        gbox1.addWidget(self.falloff_type_input, 10, 1)

        x_translate_input = QDoubleSpinBox()
        y_translate_input = QDoubleSpinBox()
        z_translate_input = QDoubleSpinBox()
        x_rotate_input = QDoubleSpinBox()
        y_rotate_input = QDoubleSpinBox()
        z_rotate_input = QDoubleSpinBox()
        x_scale_input = QDoubleSpinBox()
        y_scale_input = QDoubleSpinBox()
        z_scale_input = QDoubleSpinBox()
        uniform_scale_input = QDoubleSpinBox()
        uniform_scale_slider_input = QSlider(Qt.Horizontal)

        gbox2.addWidget(x_translate_input, 0, 2)
        gbox2.addWidget(y_translate_input, 0, 4)
        gbox2.addWidget(z_translate_input, 0, 6)
        gbox2.addWidget(x_rotate_input, 1, 2)
        gbox2.addWidget(y_rotate_input, 1, 4)
        gbox2.addWidget(z_rotate_input, 1, 6)
        gbox2.addWidget(x_scale_input, 2, 2)
        gbox2.addWidget(y_scale_input, 2, 4)
        gbox2.addWidget(z_scale_input, 2, 6)
        gbox2.addWidget(uniform_scale_input, 3, 2)
        gbox2.addWidget(uniform_scale_slider_input, 3, 3, 1, 4)

        hbox1.addWidget(point_light_button)
        hbox1.addWidget(spot_light_button)
        hbox1.addWidget(directional_light_button)
        hbox1.addWidget(enable_light_button)
        hbox1.addWidget(disable_light_button)

        vbox1.addLayout(hbox1)
        vbox1.addWidget(self.lights_list_table)
        vbox2.addLayout(gbox1)
        vbox2.addWidget(horizontal_separator)
        vbox2.addLayout(gbox2)

        hbox2.addLayout(vbox1)
        hbox2.addLayout(vbox2)

        self.setLayout(hbox2)

        self.populate_table()

    def populate_table(self):
        all_nodes = nuke.allNodes()
        target_classes = ["Light", "Light2", "Light3", "Light4"]
        light_nodes = []
        for node in all_nodes:
            if node.Class() in target_classes:
                light_nodes.append(node)

        self.lights_list_table.setRowCount(len(light_nodes))
        
        for i, each_light in enumerate(light_nodes):
            if "light_type" in each_light.knobs():
                if each_light["light_type"]:   
                    light_type_item = QTableWidgetItem(each_light["light_type"].value())
                    light_type_item.setFlags(light_type_item.flags() & ~Qt.ItemIsEditable)
                    self.lights_list_table.setItem(i, 0, light_type_item)
            else:
                light_type_item = QTableWidgetItem(each_light.Class())
                light_type_item.setFlags(light_type_item.flags() & ~Qt.ItemIsEditable)
                self.lights_list_table.setItem(i, 0, light_type_item)                
            if each_light["name"]:
                name_item = QTableWidgetItem(each_light["name"].getValue())
                name_item.setFlags(name_item.flags() & ~Qt.ItemIsEditable)
                self.lights_list_table.setItem(i, 1, name_item)
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
        if len(self.selected_rows) > 1:
            self.light_name_input.setDisabled(True)
        else:
            self.light_name_input.setEnabled(True)
            self.update_light_properties_values()

    def update_light_properties_values(self):
        if not self.selected_rows:
            return

        light_name = self.lights_list_table.item(self.selected_rows[0].row(), 1).text()
        light_node = nuke.toNode(light_name)

        if not light_node:
            nuke.message("Light node not found")
            return

        if "light_type" in light_node.knobs():
            self.light_type_input.setCurrentText(light_node["light_type"].value())
        
        if "color" in light_node.knobs():
            color = light_node["color"].value()
            self.r_input.setValue(color[0])
            self.g_input.setValue(color[1])
            self.b_input.setValue(color[2])

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

    def edit_name(self):
        light_name = self.lights_list_table.item(self.selected_rows[0].row(), 1).text()
        light_node = nuke.toNode(light_name)

        if not light_node:
                nuke.message("Light node not found")
                return

        if not self.light_name_input.text():
            nuke.message("Please enter a name for the light")
            self.light_name_input.clear()
            return

        if self.light_name_input.text()[0].isdigit():
            nuke.message("Light name cannot start with a number")
            self.light_name_input.clear()
            return

        light_node["name"].setValue(self.light_name_input.text())
        self.lights_list_table.item(self.selected_rows[0].row(), 1).setText(self.light_name_input.text())
     
    def edit_properties(self):
        if not self.selected_rows:
            nuke.message("Please select atleast a light to edit properties")
            return
        
        for each_row in self.selected_rows:
            light_name = self.lights_list_table.item(each_row.row(), 1).text()
            light_node = nuke.toNode(light_name)

            if not light_node:
                nuke.message("Light node not found")
                return
            
            if "light_type" in light_node.knobs():
                light_node["light_type"].setValue(self.light_type_input.currentText())
                self.lights_list_table.item(each_row.row(), 0).setText(self.light_type_input.currentText())
                            
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


def light_editor():
    global window
    window = MainWindow()
    window.show()

light_editor()