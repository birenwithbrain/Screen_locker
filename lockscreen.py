from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QMessageBox,
    QFrame,
)

from PySide6.QtGui import QPixmap
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
        self.password.setFocus()

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

        self.logo = QLabel()
        pixmap = QPixmap("assets/logo.png")

        self.logo.setPixmap(
            pixmap.scaled(
                100,
                100,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )

        self.logo.setAlignment(Qt.AlignCenter)

        self.title = QLabel("📹 Recording Guard")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setObjectName("title")


        self.subtitle = QLabel("Recording in Progress")
        self.subtitle.setAlignment(Qt.AlignCenter)
        self.subtitle.setObjectName("subtitle")

        self.status = QLabel("🟢 Recording Active")
        self.status.setAlignment(Qt.AlignCenter)
        self.status.setObjectName("status")

        self.date_label = QLabel()
        self.date_label.setAlignment(Qt.AlignCenter)
        self.date_label.setObjectName("date")

        self.time_label = QLabel()
        self.time_label.setAlignment(Qt.AlignCenter)
        self.time_label.setObjectName("time")

        self.password = QLineEdit()
        self.password.setPlaceholderText("🔒 Enter your password")
        self.password.setEchoMode(QLineEdit.Password)
        self.password.setAlignment(Qt.AlignCenter)

        self.unlock_button = QPushButton("🔓 Unlock")

        self.card = QFrame()
        self.card.setObjectName("card")

    # ----------------------------
    # Layout
    # ----------------------------

    def create_layout(self):

        # layout = QVBoxLayout()

        # layout.setAlignment(Qt.AlignCenter)
        main_layout = QVBoxLayout()
        main_layout.setAlignment(Qt.AlignCenter)

        card_layout = QVBoxLayout()
        card_layout.setAlignment(Qt.AlignCenter)
        card_layout.setSpacing(15)

        card_layout.addWidget(self.logo)

        card_layout.addWidget(self.title)
        card_layout.addSpacing(10)

        card_layout.addWidget(self.subtitle)
        card_layout.addSpacing(20)

        card_layout.addWidget(self.status)

        card_layout.addWidget(self.date_label)
        card_layout.addWidget(self.time_label)

        card_layout.addSpacing(30)

        card_layout.addWidget(self.password)

        card_layout.addSpacing(20)

        card_layout.addWidget(self.unlock_button)

        card_layout.addSpacing(25)

        footer = QLabel("Unauthorized access prohibited.")
        footer.setAlignment(Qt.AlignCenter)

        card_layout.addWidget(footer)

        # self.setLayout(layout)
        self.card.setLayout(card_layout)

        main_layout.addWidget(self.card)

        self.setLayout(main_layout)

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
            background-image: url("assets/background.jpg");
        }}

        QFrame#card{{
            BACKGROUND:#000000;
            border-radius:20px;
            border:2px solid #333333;
            padding:30px;
            min-width:500px;
            max-width:500px;
        }}

        QLabel {{
            color:white;
            BACKGROUND:#000000;
        }}

        QLabel#title {{
            font-size:34px;
            font-weight:bold;
        }}

        QLabel#subtitle {{
            font-size:18px;
            color:#bbbbbb;
        }}

        QLabel#status{{

            color:#00d26a;

            font-size:16px;

            font-weight:bold;

        }}

        QLabel#date {{
            font-size:16px;
            color:#aaaaaa;
        }}

        QLabel#time {{
            font-size:28px;
            font-weight:bold;
        }}

        QLineEdit{{
            BACKGROUND:#2b2b2b;
            padding:12px;
            border-radius:10px;
            border:2px solid #444444;
            color:white;
            font-size:18px;
        }}

        QLineEdit:focus{{

        border:2px solid #ff3b30;

        }}


        QPushButton{{

            background:#ff3b30;

            padding:12px;

            border-radius:10px;

            font-size:18px;

            font-weight:bold;

            color:white;

        }}

        QPushButton:hover{{

            background:#ff5a52;

        }}

        QPushButton:pressed{{

            BACKGROUND:#d63031;

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