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
from PyQt5.QtGui import QPixmap

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My cool first GUI")
        self.setGeometry(700, 250, 500, 500)
        
        label = QLabel(self)
        label.setGeometry(0, 0, 250, 250)
        
        pixmap = QPixmap("my_picture.jpg")
        label.setPixmap(pixmap)

        label.setScaledContents(True)
        # BOTTOM RIGHT
        # label.setGeometry(self.width() - label.width(),
        #                   self.height() - label.height(),
        #                   label.width(),
        #                   label.height())
        
        # BOTTOM LEFT
        # label.setGeometry(0,
        #                   self.height() - label.height(),
        #                   label.width(),
        #                   label.height())
        
        # CENTER
        label.setGeometry((self.width() - label.width()) // 2,
                          (self.height() - label.height()) // 2,
                          label.width(),
                          label.height())
        
def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()