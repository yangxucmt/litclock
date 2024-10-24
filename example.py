import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QLabel, QFrame, QSizePolicy

class clockWidget(QLabel):
    def __init__(self, fixedTime=''):
        super(clockWidget, self).__init__()
        self.setText(f"Clock: {fixedTime}")

class Form(QWidget):
    """ Creates the main GUI form """
    def __init__(self, parent=None, fixedTime=''):
        super(Form, self).__init__(parent)
        self.showFullScreen()
        self.setObjectName("MainWindow")
        self.resize(800, 480)
        self.setMaximumSize(800, 480)
        
        myStyleSheet = "QWidget { background-color: white; }"  # Example style
        self.setStyleSheet(myStyleSheet)

        # Main layout
        self.main_layout = QVBoxLayout()

        # Top container with fixed size
        self.top_container = QFrame()
        self.top_container.setFixedSize(800, 400)  # Set fixed size for the top container
        self.top_layout = QVBoxLayout(self.top_container)

        # Clock widget
        self.clock = clockWidget(fixedTime=fixedTime)
        self.top_layout.addWidget(self.clock)

        # Quit button
        self.quitButton = QPushButton("Quit")
        self.quitButton.setFixedSize(20, 20)
        self.quitButton.clicked.connect(self.close)  # Close the application
        self.top_layout.addWidget(self.quitButton)

        # Add the top container to the main layout
        self.main_layout.addWidget(self.top_container)

        # Bottom fixed row with specific height
        self.bottom_row = QLabel('Fixed Bottom Row')
        self.bottom_row.setFixedSize(800, 80)  # Set fixed size for the bottom row
        self.bottom_row.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)  # Ensure it doesn't resize
        self.main_layout.addWidget(self.bottom_row)

        # Set the main layout to the widget
        self.setLayout(self.main_layout)

# Run the application
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Form(fixedTime="12:00 PM")  # Example fixed time
    window.show()
    sys.exit(app.exec_())
