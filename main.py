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
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 250, 500, 500)
        
        label = QLabel("Hello", self)
        label.setFont(QFont("Arial", 40))
        label.setGeometry(0, 0, 500, 100)
        label.setStyleSheet("color: #292929;"
                            "background-color: #6fdcf7"
                            "font-weight: bold;"
                            "font-style: italic;"
                            "text-decoration: underline;")
        
        # label.setAlignment(Qt.AlignTop) # VERTICALLY TOP
        # label.setAlignment(Qt.AlignBottom) # VERTICALLY BOTTOM
        # label.setAlignment(Qt.AlignVCenter) # VERTICALLY CENTER
        # label.setAlignment(Qt.AlignRight) # HORIZONTALLY RIGHT
        # label.setAlignment(Qt.AlignHCenter) # HORIZONTALLY CENTER
        # label.setAlignment(Qt.AlignLeft) # HORIZONTALLY LEFT
        
        # Combination of positions using '|'
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignTop) # CENTER & TOP
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignBottom) # CENTER & BOTTOM
        # label.setAlignment(Qt.AlignHCenter | Qt.AlignVCenter) # CENTER & CENTER
        label.setAlignment(Qt.AlignCenter) # CENTER & CENTER

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()