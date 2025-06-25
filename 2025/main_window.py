from PySide6.QtWidgets import QMainWindow
from robot_gui import Ui_MainWindow  # Импорт сгенерированного класса

import robot_axis as ra
from backend_controller import BackendController


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.backend = BackendController()

        self.axis_button_map = {
            'btn_Xp': ("cartesian", ra.CartesianAxis.X, '+'),
            'btn_Xm': ("cartesian", ra.CartesianAxis.X, '-'),
            'btn_Yp': ("cartesian", ra.CartesianAxis.Y, '+'),
            'btn_Ym': ("cartesian", ra.CartesianAxis.Y, '-'),
            'btn_Zp': ("cartesian", ra.CartesianAxis.Z, '+'),
            'btn_Zm': ("cartesian", ra.CartesianAxis.Z, '-'),
            'btn_RXp': ("cartesian", ra.CartesianAxis.A, '+'),
            'btn_RXm': ("cartesian", ra.CartesianAxis.A, '-'),
            'btn_RYp': ("cartesian", ra.CartesianAxis.B, '+'),
            'btn_RYm': ("cartesian", ra.CartesianAxis.B, '-'),
            'btn_RZp': ("cartesian", ra.CartesianAxis.C, '+'),
            'btn_RZm': ("cartesian", ra.CartesianAxis.C, '-'),
            'btn_J1p': ("joint", ra.JointAxis.J1, '+'),
            'btn_J1m': ("joint", ra.JointAxis.J1, '-'),
            'btn_J2p': ("joint", ra.JointAxis.J2, '+'),
            'btn_J2m': ("joint", ra.JointAxis.J2, '-'),
            'btn_J3p': ("joint", ra.JointAxis.J3, '+'),
            'btn_J3m': ("joint", ra.JointAxis.J3, '-'),
            'btn_J4p': ("joint", ra.JointAxis.J4, '+'),
            'btn_J4m': ("joint", ra.JointAxis.J4, '-'),
            'btn_J5p': ("joint", ra.JointAxis.J5, '+'),
            'btn_J5m': ("joint", ra.JointAxis.J5, '-'),
            'btn_J6p': ("joint", ra.JointAxis.J6, '+'),
            'btn_J6m': ("joint", ra.JointAxis.J6, '-'),
        }

        self.linear_step_val = 0.1
        self.degree_1_step_val = 0.1
        self.degree_2_step_val = 0.1
        
        # Инициализация интерфейса
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        # Привязка функций к кнопкам
        # Кнопки главного окна (centralwidget)
        self.ui.btn_connect.clicked.connect(self.button_clicked)
        self.ui.btn_connect.clicked.connect(self.set_connection)
        
        # Кнопки блока Socket Configuration (frame_socket_configuration)
        self.ui.btn_set_socket.clicked.connect(self.button_clicked)
        self.ui.btn_reset_socket.clicked.connect(self.button_clicked)
        
        # Кнопки блока TCP Position (frame_tcp_position)
        self.ui.btn_Xm.clicked.connect(self.button_clicked)
        self.ui.btn_Xp.clicked.connect(self.button_clicked)
        self.ui.btn_Ym.clicked.connect(self.button_clicked)
        self.ui.btn_Yp.clicked.connect(self.button_clicked)
        self.ui.btn_Zm.clicked.connect(self.button_clicked)
        self.ui.btn_Zp.clicked.connect(self.button_clicked)
        
        # Кнопки блока TCP Orientation (frame_tcp_orientation)
        self.ui.btn_RXm.clicked.connect(self.button_clicked)
        self.ui.btn_RXp.clicked.connect(self.button_clicked)
        self.ui.btn_RYm.clicked.connect(self.button_clicked)
        self.ui.btn_RYp.clicked.connect(self.button_clicked)
        self.ui.btn_RZm.clicked.connect(self.button_clicked)
        self.ui.btn_RZp.clicked.connect(self.button_clicked)
        
        # Кнопки блока Joints Orientation (frame_joints_orientation)
        self.ui.btn_J1m.clicked.connect(self.button_clicked)
        self.ui.btn_J1p.clicked.connect(self.button_clicked)
        self.ui.btn_J2m.clicked.connect(self.button_clicked)
        self.ui.btn_J2p.clicked.connect(self.button_clicked)
        self.ui.btn_J3m.clicked.connect(self.button_clicked)
        self.ui.btn_J3p.clicked.connect(self.button_clicked)
        self.ui.btn_J4m.clicked.connect(self.button_clicked)
        self.ui.btn_J4p.clicked.connect(self.button_clicked)
        self.ui.btn_J5m.clicked.connect(self.button_clicked)
        self.ui.btn_J5p.clicked.connect(self.button_clicked)
        self.ui.btn_J6m.clicked.connect(self.button_clicked)
        self.ui.btn_J6p.clicked.connect(self.button_clicked)
        
        
        # Слайдеры
        self.ui.slider_step_mm.valueChanged.connect(self.update_step_value)
        self.ui.slider_step_degrees_1.valueChanged.connect(self.update_step_value)
        self.ui.slider_step_degrees_2.valueChanged.connect(self.update_step_value)
        
        # Начальная синхронизация слайдеров
        self.update_step_value(self.ui.slider_step_mm.value())
        self.update_step_value(self.ui.slider_step_degrees_1.value())
        self.update_step_value(self.ui.slider_step_degrees_2.value())
        
        # Disable при запуске виджета tabWidget с кнопками и т.д.
        self.ui.tabWidget.setEnabled(False)


    def set_connection(self):
        if self.ui.tabWidget.isEnabled():
            self.ui.tabWidget.setEnabled(False)
            self.ui.btn_connect.setText('CONNECT')
        else:
            self.ui.tabWidget.setEnabled(True)
            self.ui.btn_connect.setText('DISCONNECT')
            
                      
    def button_clicked(self):
        btn = self.sender()  # Получаем кнопку, которая отправила сигнал
        if btn is not None:  # Всегда проверяем, что sender существует
            print(f"Нажата кнопка: {btn.text()}, {btn.objectName()}")  # Выводим имя и текст кнопки из Qt Designer
            
    
    def update_step_value(self, slider_value):
        # Получаем слайдер, который вызвал сигнал
        sender_slider = self.sender()
        
        # Конвертируем значение (1-100 -> 0.1-10)
        lineedit_value = slider_value / 10.0
        
        # Определяем, какой lineEdit нужно обновить
        if sender_slider == self.ui.slider_step_mm:
            self.linear_step_val = lineedit_value
            self.ui.lineEdit_step_mm.setText(f"{lineedit_value:.1f}")
        elif sender_slider == self.ui.slider_step_degrees_1:
            self.degree_1_step_val = lineedit_value
            self.ui.lineEdit_step_degrees_1.setText(f"{lineedit_value:.1f}")
        elif sender_slider == self.ui.slider_step_degrees_2:
            self.degree_2_step_val = lineedit_value
            self.ui.lineEdit_step_degrees_2.setText(f"{lineedit_value:.1f}")
