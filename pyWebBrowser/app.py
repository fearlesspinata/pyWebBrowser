from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QAction, QLineEdit, QVBoxLayout, QWidget, QToolBar
from PyQt5.QtCore import QSize, Qt, QUrl 
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys # needed for command line arguments
from playsound import playsound

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyWebBrowser")
        self.browser= QWebEngineView()
        self.setCentralWidget(self.browser)
        self.input = QLineEdit()
        self.tool_bar = QToolBar()
                
        # Tool Bar Actions
        forward_btn = QAction("►", self)
        back_btn = QAction("◀", self)
        reload_btn = QAction("↻", self)

        # Navigation Tool Bar Signals
        reload_btn.triggered.connect(self.browser.reload)
        forward_btn.triggered.connect(self.browser.forward)
        back_btn.triggered.connect(self.browser.back)
        self.input.returnPressed.connect(self.navigate_to_url)

        # Tool Bar configuration
        self.tool_bar.addAction(back_btn)
        self.tool_bar.addAction(forward_btn)
        self.tool_bar.addAction(reload_btn)
        self.tool_bar.addWidget(self.input)
        
        # Set default URL
        self.browser.setUrl(QUrl("http://www.google.com"))

        # Main Window Layout 
        layout = QVBoxLayout()
        layout.addWidget(self.tool_bar)
        layout.addWidget(self.browser)
        container = QWidget()
        container.setLayout(layout)

        # Set the central widget of the window
        self.setCentralWidget(container)
        self.setMinimumSize(QSize(800, 600))
        self.setMaximumSize(QSize(2560, 1440))

    def navigate_to_url(self):
        url = self.input.text()
        if "https://www." not in url:
            url = "https://wwww." + url
        self.browser.setUrl(QUrl(url))

app = QApplication([]) # instantiating our application

window = MainWindow()# A QWidget object represents our window
window.show() # windows are hidden by defaulkt

app.exec()
