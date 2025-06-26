# import socket
# from command_manager import CommandMessageManager
import sys
from PySide6.QtWidgets import QApplication
from config_manager import Config

import main_window as mw


if __name__ == "__main__":
    Config.load()

    app = QApplication(sys.argv)

    window = mw.MainWindow()
    window.show()

    # test
    # pos = [100.0, -100.0, 100.0, 100.0, 100.0, 100.0]
    # test = CommandMessageManager.build_position_request(pos)
    # test += "(7,0)"
    # s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # s.connect((Config.ip, Config.port))
    # s.sendall("2".encode('utf-8'))
    # s.sendall(test.encode('utf-8'))
    # ans = s.recv(1024).decode('utf-8')
    # print(ans)
    # s.sendall("0".encode('utf-8'))
    # s.close()

    sys.exit(app.exec())