from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QMessageBox,
)

from PySide6.QtCore import Qt

from config import *
from auth import verify_password


class LockScreen(QWidget):

    def __init__(self):
        super().__init__()

        self.setup_ui()

    def setup_ui(self):

        self.setWindowTitle(WINDOW_TITLE)

        self.setWindowFlags(
            Qt.Window |
            Qt.WindowStaysOnTopHint |
            Qt.FramelessWindowHint
        )

        self.showFullScreen()

        self.setStyleSheet(f"""
            QWidget {{
                background:{BACKGROUND};
                color:{TEXT};
                font-size:18px;
            }}

            QLabel {{
                font-size:30px;
                font-weight:bold;
            }}

            QLineEdit {{
                padding:10px;
                font-size:18px;
                border-radius:8px;
            }}

            QPushButton {{
                background:{ACCENT};
                color:white;
                padding:10px;
                border:none;
                border-radius:8px;
                font-size:18px;
            }}

            QPushButton:hover {{
                background:#ff5a52;
            }}
        """)

        layout = QVBoxLayout()

        layout.setAlignment(Qt.AlignCenter)

        title = QLabel("📹Recording Guard")
        title.setAlignment(Qt.AlignCenter)

        subtitle = QLabel("Recording in Progress")
        subtitle.setAlignment(Qt.AlignCenter)

        self.password = QLineEdit()
        self.password.setPlaceholderText("Enter Password")
        self.password.setEchoMode(QLineEdit.Password)

        unlock = QPushButton("Unlock")

        unlock.clicked.connect(self.unlock)

        layout.addWidget(title)
        layout.addSpacing(20)
        layout.addWidget(subtitle)
        layout.addSpacing(30)
        layout.addWidget(self.password)
        layout.addSpacing(20)
        layout.addWidget(unlock)

        self.setLayout(layout)

    def unlock(self):

        if verify_password(self.password.text()):
            self.close()

        else:
            QMessageBox.warning(
                self,
                "Wrong Password",
                "Incorrect Password!"
            )
            self.password.clear()

    