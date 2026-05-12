import sys # sys stands for 'system'
            # It is a built-in Python module that gives your program access to:

            # the Python interpreter itself
            # command-line arguments
            # program exit behavior
            # standard input/output
            # recursion limits
            # Python paths

            # Think of it like:
            # os talks to the operating system
            # sys talks to the Python runtime itself
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 250, 500, 500)
        self.setWindowIcon(QIcon("/home/esis/Python_Learning/pyqt5/my_picture.jpg"))

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()