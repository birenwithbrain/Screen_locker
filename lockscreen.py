from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QMessageBox,
)

from PySide6.QtCore import Qt, QTimer
from datetime import datetime

from config import *
from auth import verify_password


class LockScreen(QWidget):

    def __init__(self):
        super().__init__()

        self.setup_window()
        self.create_widgets()
        self.create_layout()
        self.connect_signals()
        self.apply_styles()
        self.start_clock()

    # ----------------------------
    # Window Setup
    # ----------------------------

    def setup_window(self):
        self.setWindowTitle(WINDOW_TITLE)

        self.setWindowFlags(
            Qt.Window |
            Qt.WindowStaysOnTopHint |
            Qt.FramelessWindowHint
        )

        self.showFullScreen()

    # ----------------------------
    # Create Widgets
    # ----------------------------

    def create_widgets(self):

        self.title = QLabel("📹 Recording Guard")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setObjectName("title")

        self.subtitle = QLabel("Recording in Progress")
        self.subtitle.setAlignment(Qt.AlignCenter)
        self.subtitle.setObjectName("subtitle")

        self.date_label = QLabel()
        self.date_label.setAlignment(Qt.AlignCenter)
        self.date_label.setObjectName("date")

        self.time_label = QLabel()
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setObjectName("time")

        self.password = QLineEdit()
        self.password.setPlaceholderText("Enter Password")
        self.password.setEchoMode(QLineEdit.Password)

        self.unlock_button = QPushButton("🔓 Unlock")

    # ----------------------------
    # Layout
    # ----------------------------

    def create_layout(self):

        layout = QVBoxLayout()

        layout.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.title)
        layout.addSpacing(10)

        layout.addWidget(self.subtitle)
        layout.addSpacing(20)

        layout.addWidget(self.date_label)
        layout.addWidget(self.time_label)

        layout.addSpacing(30)

        layout.addWidget(self.password)

        layout.addSpacing(20)

        layout.addWidget(self.unlock_button)

        layout.addSpacing(25)

        footer = QLabel("Unauthorized access prohibited.")
        footer.setAlignment(Qt.AlignCenter)

        layout.addWidget(footer)

        self.setLayout(layout)

    # ----------------------------
    # Signals
    # ----------------------------

    def connect_signals(self):

        self.unlock_button.clicked.connect(self.unlock)

        self.password.returnPressed.connect(self.unlock)

    # ----------------------------
    # Styles
    # ----------------------------

    def apply_styles(self):

        self.setStyleSheet(f"""

        QWidget {{
            background:{BACKGROUND};
            color:{TEXT};
            font-family:Segoe UI;
        }}

        QLabel {{
            color:white;
        }}

        QLabel#title {{
            font-size:34px;
            font-weight:bold;
        }}

        QLabel#subtitle {{
            font-size:18px;
            color:#bbbbbb;
        }}

        QLabel#date {{
            font-size:16px;
            color:#aaaaaa;
        }}

        QLabel#time {{
            font-size:28px;
            font-weight:bold;
        }}

        QLineEdit {{
            padding:12px;
            font-size:18px;
            border-radius:10px;
            border:2px solid #444444;
            background:#222222;
            color:white;
        }}

        QLineEdit:focus {{
            border:2px solid {ACCENT};
        }}

        QPushButton {{
            background:{ACCENT};
            color:white;
            padding:12px;
            border:none;
            border-radius:10px;
            font-size:18px;
        }}

        QPushButton:hover {{
            background:#ff5a52;
        }}

        """)

    # ----------------------------
    # Clock
    # ----------------------------

    def start_clock(self):

        self.timer = QTimer(self)

        self.timer.timeout.connect(self.update_clock)

        self.timer.start(1000)

        self.update_clock()

    def update_clock(self):

        now = datetime.now()

        self.date_label.setText(
            now.strftime("%A\n%d %B %Y")
        )

        self.time_label.setText(
            now.strftime("%I:%M:%S %p")
        )

    # ----------------------------
    # Unlock
    # ----------------------------

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

    # ----------------------------
    # Future Feature
    # ----------------------------

    def center_card(self):
        """
        Placeholder.

        In the next sprint this method will create
        a rounded central panel (card) that contains
        all widgets, instead of placing them directly
        on the window.
        """
        pass