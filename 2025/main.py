import sys
from PySide6.QtWidgets import QApplication

import main_window as mw


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = mw.MainWindow()
    window.show()

    sys.exit(app.exec())