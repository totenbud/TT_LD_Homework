import ldclient
from ldclient.config import Config
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPixmap
import sys

# Initialize ldclient with environment specific SDK key
if __name__ == "__main__":
  ldclient.set_config(Config("sdk-27d47704-226a-4106-bba1-e530a5164def"))

# Set User Information
user = {
  "key": "thiefForDwarves",
  "firstName": "Bill",
  "lastName": "Bobaggins",
  "custom": {
    "groups": "ring_bearers"
  }
}

show_feature = ldclient.get().variation("invisibility", user, False)

# Define the main application window
class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__()
        # win.setGeometry values = (xposition, yposition, width, height)
        self.setGeometry(200, 200, 600, 600)
        self.setWindowTitle('Helix ALM Stuff')
        self.initUI()

    def initUI(self):
        
        self.label = QtWidgets.QLabel(self)
        self.label.setText('Are you invisible?')
        self.label.move(200, 50)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText('Test!')
        self.b1.move(200, 0)
        self.b1.clicked.connect(self.b1Click)
        
        self.imageLabel = QtWidgets.QLabel(self)
        self.pixmap = QPixmap('images/QuestionMark.png')
        self.imageLabel.setPixmap(self.pixmap)
        self.imageLabel.resize(self.pixmap.width(), self.pixmap.height())
        self.imageLabel.move(200, 100)

    # Trigger one feature path when you click the button
    def b1Click(self):
        if show_feature:
            self.label.setText("No hobbits here! You're invisible.")
            self.pixmap = QPixmap('images/invisibleHobbit.png')
            self.imageLabel.setPixmap(self.pixmap)
        else:
            self.label.setText("You're a visible hobbit!")
            self.pixmap = QPixmap('images/visibleHobbit.png')
            self.imageLabel.setPixmap(self.pixmap)
        self.update()

    def update(self):
        self.label.adjustSize()
        self.imageLabel.adjustSize()

def window():
    app = QApplication(sys.argv)
    win = MyWindow()
   
    win.show()
    sys.exit(app.exec_())

window()

ldclient.get().close()