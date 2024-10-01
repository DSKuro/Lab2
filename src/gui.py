from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import (QApplication, QMainWindow, QDialog, QPushButton, QLabel,
                             QLineEdit, QComboBox, QVBoxLayout, QWidget, QHBoxLayout, QDialogButtonBox)
from classes.wallpaper import Wallpaper
from classes.laminate import Laminate
from classes.bar import Bar

class AlertBox(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Ошибка!")

        q_btn = QDialogButtonBox.StandardButton.Ok
        self.button_box = QDialogButtonBox(q_btn)
        self.button_box.accepted.connect(self.accept)

        layout = QVBoxLayout()
        message = QLabel("Введено не число!")
        layout.addWidget(message)
        layout.addWidget(self.button_box)
        self.setLayout(layout)

class MainWindow(QMainWindow):
    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.result_label = None
        self.square_textbox = None
        self.cost_textbox = None
        self.height_textbox = None
        self.width_textbox = None
        self.combobox = None
        self.setWindowTitle("MyApp")
        self.setFixedSize(QSize(800, 400))
        layout = self.initialize_out_layout()
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

    def initialize_out_layout(self) -> QVBoxLayout:
        layout = QVBoxLayout()
        layout2 = QVBoxLayout()
        horizontal_layout = QHBoxLayout()
        horizontal_layout2 = QHBoxLayout()
        layout.setSpacing(30)
        layout2.setSpacing(30)

        label = QLabel("Количество и стоимость материалов")
        font = label.font()
        font.setPointSize(20)
        label.setFont(font)
        # label.setStyleSheet("""padding-bottom: 10px;""")
        layout.addWidget(label, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.combobox = QComboBox()
        self.combobox.setFixedSize(500, 50)
        self.combobox.addItems(["Обои", "Ламинат", "Плитка"])
        self.combobox.setCurrentIndex(0)
        layout.addWidget(self.combobox, alignment=Qt.AlignmentFlag.AlignHCenter)

        self.initialize_in_layout(horizontal_layout, horizontal_layout2, layout2)

        layout.addLayout(layout2)

        self.result_label = QLabel()
        self.result_label.setFixedSize(800, 40)
        font = self.result_label.font()
        font.setPointSize(15)
        self.result_label.setFont(font)
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        layout.addWidget(self.result_label, alignment=Qt.AlignmentFlag.AlignHCenter)

        button = QPushButton("Запуск")
        button.setFixedSize(100, 40)
        button.clicked.connect(self.button_click)
        layout.addWidget(button, alignment=Qt.AlignmentFlag.AlignHCenter)
        layout.addStretch(1)

        return layout


    def initialize_in_layout(self, horizontal_layout : QHBoxLayout, horizontal_layout2 : QHBoxLayout,
                             layout2 : QVBoxLayout) -> None:
        self.initialize_horizontal_layout(horizontal_layout)

        layout2.addLayout(horizontal_layout)

        self.initialize_horizontal_layout2(horizontal_layout2)

        layout2.addLayout(horizontal_layout2)

    def initialize_horizontal_layout(self, horizontal_layout : QHBoxLayout) -> None:
        self.width_textbox = QLineEdit()
        self.width_textbox.setFixedSize(375, 40)
        self.width_textbox.setPlaceholderText("Введите ширину материала")
        horizontal_layout.addWidget(self.width_textbox)

        self.height_textbox = QLineEdit()
        self.height_textbox.setFixedSize(375, 40)
        self.height_textbox.setPlaceholderText("Введите длину материала")
        horizontal_layout.addWidget(self.height_textbox)

    def initialize_horizontal_layout2(self, horizontal_layout2 : QHBoxLayout) -> None:
        self.cost_textbox = QLineEdit()
        self.cost_textbox.setFixedSize(375, 40)
        self.cost_textbox.setPlaceholderText("Введите цену за 1 единицу материала")
        horizontal_layout2.addWidget(self.cost_textbox)

        self.square_textbox = QLineEdit()
        self.square_textbox.setFixedSize(375, 40)
        self.square_textbox.setPlaceholderText("Введите площадь поверхности")
        horizontal_layout2.addWidget(self.square_textbox)

    def button_click(self) -> None:
        try:
           width = float(self.width_textbox.text())
           height = float(self.height_textbox.text())
           cost_per_unit = float(self.cost_textbox.text())
           square = float(self.square_textbox.text())
        except ValueError:
            dlg = AlertBox()
            dlg.exec()
            return

        index = self.combobox.currentText()
        obj = None
        match index:
            case "Обои":
                obj = Wallpaper(width, height, cost_per_unit, (255, 0, 255))
            case "Ламинат":
                obj = Laminate(width, height, cost_per_unit)
            case "Плитка":
                obj = Bar(width, height, cost_per_unit)
        obj.calculate_cost(square)
        self.result_label.setText(str(obj))


app = QApplication([])

window = MainWindow()
window.show()

app.exec()