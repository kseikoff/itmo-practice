from PySide6.QtWidgets import QMainWindow

from robot_gui import Ui_MainWindow

import robot_axis as ra
from backend_controller import BackendController
from config_manager import Config
from command_manager import CommandMessageManager


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.backend = BackendController()

        self.axis_button_map = {
            'btn_Xp': ("cartesian_linear", ra.CartesianAxis.X.value, '+'),
            'btn_Xm': ("cartesian_linear", ra.CartesianAxis.X.value, '-'),
            'btn_Yp': ("cartesian_linear", ra.CartesianAxis.Y.value, '+'),
            'btn_Ym': ("cartesian_linear", ra.CartesianAxis.Y.value, '-'),
            'btn_Zp': ("cartesian_linear", ra.CartesianAxis.Z.value, '+'),
            'btn_Zm': ("cartesian_linear", ra.CartesianAxis.Z.value, '-'),
            'btn_RXp': ("cartesian_rotation", ra.CartesianAxis.A.value, '+'),
            'btn_RXm': ("cartesian_rotation", ra.CartesianAxis.A.value, '-'),
            'btn_RYp': ("cartesian_rotation", ra.CartesianAxis.B.value, '+'),
            'btn_RYm': ("cartesian_rotation", ra.CartesianAxis.B.value, '-'),
            'btn_RZp': ("cartesian_rotation", ra.CartesianAxis.C.value, '+'),
            'btn_RZm': ("cartesian_rotation", ra.CartesianAxis.C.value, '-'),
            'btn_J1p': ("joint_rotation", ra.JointAxis.J1.value, '+'),
            'btn_J1m': ("joint_rotation", ra.JointAxis.J1.value, '-'),
            'btn_J2p': ("joint_rotation", ra.JointAxis.J2.value, '+'),
            'btn_J2m': ("joint_rotation", ra.JointAxis.J2.value, '-'),
            'btn_J3p': ("joint_rotation", ra.JointAxis.J3.value, '+'),
            'btn_J3m': ("joint_rotation", ra.JointAxis.J3.value, '-'),
            'btn_J4p': ("joint_rotation", ra.JointAxis.J4.value, '+'),
            'btn_J4m': ("joint_rotation", ra.JointAxis.J4.value, '-'),
            'btn_J5p': ("joint_rotation", ra.JointAxis.J5.value, '+'),
            'btn_J5m': ("joint_rotation", ra.JointAxis.J5.value, '-'),
            'btn_J6p': ("joint_rotation", ra.JointAxis.J6.value, '+'),
            'btn_J6m': ("joint_rotation", ra.JointAxis.J6.value, '-'),
        }

        self.linear_step_val = 0.1 # TODO improve slider
        self.degree_1_step_val = 0.1
        self.degree_2_step_val = 0.1

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_connect.clicked.connect(self.handle_connection)

        # self.ui.btn_set_socket.clicked.connect(self.handle_socket) TODO set/reset ip, port
        # self.ui.btn_reset_socket.clicked.connect(self.handle_socket)

        self.ui.btn_Xm.clicked.connect(self.handle_axis_button)
        self.ui.btn_Xp.clicked.connect(self.handle_axis_button)
        self.ui.btn_Ym.clicked.connect(self.handle_axis_button)
        self.ui.btn_Yp.clicked.connect(self.handle_axis_button)
        self.ui.btn_Zm.clicked.connect(self.handle_axis_button)
        self.ui.btn_Zp.clicked.connect(self.handle_axis_button)

        self.ui.btn_RXm.clicked.connect(self.handle_axis_button)
        self.ui.btn_RXp.clicked.connect(self.handle_axis_button)
        self.ui.btn_RYm.clicked.connect(self.handle_axis_button)
        self.ui.btn_RYp.clicked.connect(self.handle_axis_button)
        self.ui.btn_RZm.clicked.connect(self.handle_axis_button)
        self.ui.btn_RZp.clicked.connect(self.handle_axis_button)

        self.ui.btn_J1m.clicked.connect(self.handle_axis_button)
        self.ui.btn_J1p.clicked.connect(self.handle_axis_button)
        self.ui.btn_J2m.clicked.connect(self.handle_axis_button)
        self.ui.btn_J2p.clicked.connect(self.handle_axis_button)
        self.ui.btn_J3m.clicked.connect(self.handle_axis_button)
        self.ui.btn_J3p.clicked.connect(self.handle_axis_button)
        self.ui.btn_J4m.clicked.connect(self.handle_axis_button)
        self.ui.btn_J4p.clicked.connect(self.handle_axis_button)
        self.ui.btn_J5m.clicked.connect(self.handle_axis_button)
        self.ui.btn_J5p.clicked.connect(self.handle_axis_button)
        self.ui.btn_J6m.clicked.connect(self.handle_axis_button)
        self.ui.btn_J6p.clicked.connect(self.handle_axis_button)


        self.ui.slider_step_mm.valueChanged.connect(self.update_step_value)
        self.ui.slider_step_degrees_1.valueChanged.connect(self.update_step_value)
        self.ui.slider_step_degrees_2.valueChanged.connect(self.update_step_value)

        self.update_step_value(self.ui.slider_step_mm.value()) # TODO improve slider
        self.update_step_value(self.ui.slider_step_degrees_1.value())
        self.update_step_value(self.ui.slider_step_degrees_2.value())

        self.ui.tabWidget.setEnabled(False)

        self.ui.IP_value.setText(Config.ip)
        self.ui.Port_value.setText(str(Config.port))


    def update_ui_axis(self):
        cartesian_axis = self.backend.robot.cartesian
        joint_axis = self.backend.robot.joint

        self.ui.lineEdit_X.setText(f"{cartesian_axis[0]:.1f}")
        self.ui.lineEdit_Y.setText(f"{cartesian_axis[1]:.1f}")
        self.ui.lineEdit_Z.setText(f"{cartesian_axis[2]:.1f}")
        self.ui.lineEdit_RX.setText(f"{cartesian_axis[3]:.1f}")
        self.ui.lineEdit_RY.setText(f"{cartesian_axis[4]:.1f}")
        self.ui.lineEdit_RZ.setText(f"{cartesian_axis[5]:.1f}")

        self.ui.lineEdit_J1.setText(f"{joint_axis[0]:.1f}")
        self.ui.lineEdit_J2.setText(f"{joint_axis[1]:.1f}")
        self.ui.lineEdit_J3.setText(f"{joint_axis[2]:.1f}")
        self.ui.lineEdit_J4.setText(f"{joint_axis[3]:.1f}")
        self.ui.lineEdit_J5.setText(f"{joint_axis[4]:.1f}")
        self.ui.lineEdit_J6.setText(f"{joint_axis[5]:.1f}")


    def update_step_value(self, slider_value):
        sender_slider = self.sender()

        lineedit_value = slider_value / 10.0

        if sender_slider == self.ui.slider_step_mm:
            self.linear_step_val = lineedit_value
            self.ui.lineEdit_step_mm.setText(f"{lineedit_value:.1f}")
        elif sender_slider == self.ui.slider_step_degrees_1:
            self.degree_1_step_val = lineedit_value
            self.ui.lineEdit_step_degrees_1.setText(f"{lineedit_value:.1f}")
        elif sender_slider == self.ui.slider_step_degrees_2:
            self.degree_2_step_val = lineedit_value
            self.ui.lineEdit_step_degrees_2.setText(f"{lineedit_value:.1f}")


    def handle_connection(self):
        if self.backend.is_connected():
            self.backend.disconnect()

            if not self.backend.is_connected():
                self.ui.tabWidget.setEnabled(False)
                self.ui.btn_connect.setText("CONNECT")
        else:
            try:
                ip = Config.ip
                port = Config.port
                self.backend.connect(ip, port)

                if self.backend.is_connected():
                    response = self.backend.get_pos()
                    joints, cartesian, kinematic_sol = CommandMessageManager.parse_position_response(response)

                    self.backend.robot.update_cartesian(cartesian, kinematic_sol)
                    self.backend.robot.update_joint(joints)

                    self.update_ui_axis()

                    self.ui.tabWidget.setEnabled(True)
                    self.ui.btn_connect.setText("DISCONNECT")
            except Exception as e:
                print(f"Caught exception: {e}")


    def handle_axis_button(self):
        btn = self.sender()
        if not btn:
            return

        btn_name = btn.objectName()
        if btn_name not in self.axis_button_map:
            print(f"Unexpected button: {btn_name}")
            return

        move_info = self.axis_button_map[btn_name]
        mode, _, _ = move_info

        if "cartesian" in mode:
            if not "rotation" in mode:
                step = self.linear_step_val
            else:
                step = self.degree_1_step_val
        else:
            step = self.degree_2_step_val

        if not self.backend.is_connected():
            print("Unexpected event: no connection")
            return

        try:
            response = self.backend.move_axis(move_info, step)
            joints, cartesian, kinematic_sol = CommandMessageManager.parse_position_response(response)

            self.backend.robot.update_cartesian(cartesian, kinematic_sol)
            self.backend.robot.update_joint(joints)

            self.update_ui_axis()
        except Exception as e:
            print(f"Caught exception: {e}")
