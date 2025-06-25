import sys
from PySide6.QtWidgets import QApplication
from config_manager import Config

import main_window as mw


if __name__ == "__main__":
    Config.load()

    app = QApplication(sys.argv)

    window = mw.MainWindow()
    window.show()

    sys.exit(app.exec())