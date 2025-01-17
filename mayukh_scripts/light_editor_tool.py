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
        self.lights_list_table.setHorizontalHeaderLabels(["Light Type", "Name", "Color", "Intensity"])
        self.lights_list_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        
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

        light_name_input = QLineEdit()
        light_type_input = QComboBox()
        color_input = QPushButton("Color")
        r_input = QDoubleSpinBox()
        r_slider_input = QSlider(Qt.Horizontal)
        g_input = QDoubleSpinBox()
        g_slider_input = QSlider(Qt.Horizontal)
        b_input = QDoubleSpinBox()
        b_slider_input = QSlider(Qt.Horizontal)
        intensity_input = QDoubleSpinBox()
        intensity_slider_input = QSlider(Qt.Horizontal)
        cone_angle_input = QDoubleSpinBox()
        cone_angle_slider_input = QSlider(Qt.Horizontal)
        cone_penumbra_angle_input = QDoubleSpinBox()
        cone_penumbra_angle_slider_input = QSlider(Qt.Horizontal)
        cone_falloff_input = QDoubleSpinBox()
        cone_falloff_slider_input = QSlider(Qt.Horizontal)
        falloff_type_input = QComboBox()

        gbox1.addWidget(light_name_input, 0, 1, 1, 4)
        gbox1.addWidget(light_type_input, 1, 1)
        gbox1.addWidget(color_input, 2, 1)
        gbox1.addWidget(r_input, 3, 1)
        gbox1.addWidget(r_slider_input, 3, 2, 1, 3)
        gbox1.addWidget(g_input, 4, 1)
        gbox1.addWidget(g_slider_input, 4, 2, 1, 3)
        gbox1.addWidget(b_input, 5, 1)
        gbox1.addWidget(b_slider_input, 5, 2, 1, 3)
        gbox1.addWidget(intensity_input, 6, 1)
        gbox1.addWidget(intensity_slider_input, 6, 2, 1, 3)
        gbox1.addWidget(cone_angle_input, 7, 1)
        gbox1.addWidget(cone_angle_slider_input, 7, 2, 1, 3)
        gbox1.addWidget(cone_penumbra_angle_input, 8, 1)
        gbox1.addWidget(cone_penumbra_angle_slider_input, 8, 2, 1, 3)
        gbox1.addWidget(cone_falloff_input, 9, 1)
        gbox1.addWidget(cone_falloff_slider_input, 9, 2, 1, 3)
        gbox1.addWidget(falloff_type_input, 10, 1)

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
                    self.lights_list_table.setItem(i, 0, QTableWidgetItem(each_light["light_type"].value()))
            else:
                self.lights_list_table.setItem(i, 0, QTableWidgetItem(each_light.Class()))
            if each_light["name"]:
                self.lights_list_table.setItem(i, 1, QTableWidgetItem(each_light["name"].getValue()))
            if each_light["color"]: 
                self.lights_list_table.setItem(i, 2, QTableWidgetItem(str(each_light["color"].getValue())))
            if each_light["intensity"]: 
                self.lights_list_table.setItem(i, 3, QTableWidgetItem(str(each_light["intensity"].getValue())))

def light_editor():
    global window
    window = MainWindow()
    window.show()

light_editor()