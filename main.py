import sys
from PySide6.QtWidgets import QApplication, QTextEdit
from PySide6.QtCore import Qt
from gui import App

if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = App()
    for widget in app.allWidgets():
        if isinstance(widget, QTextEdit):
            widget.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            widget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
            widget.setReadOnly(True)
    
    janela.show()
    app.exec()
