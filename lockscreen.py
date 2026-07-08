from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton,
    QLineEdit,
    QVBoxLayout,
    QHBoxLayout,
    QMessageBox,
    QFrame,
)

import random
from PySide6.QtGui import QPainter, QPixmap, QColor

from PySide6.QtCore import Qt, QTimer
from datetime import datetime

from config import *
from auth import verify_password
from PySide6.QtWidgets import QGraphicsDropShadowEffect


class LockScreen(QWidget):

    def paintEvent(self, event):
        painter = QPainter(self)

        pixmap = QPixmap("assets\\background.jpg")

        painter.drawPixmap(self.rect(), pixmap)

    def __init__(self):
        super().__init__()

        self.setup_window()
        self.create_widgets()
        self.create_layout()
        self.connect_signals()
        self.apply_styles()
        self.start_clock()

        self.setFocusPolicy(Qt.StrongFocus)
        self.setFocus()

        self.logo_timer = QTimer(self)
        self.logo_timer.timeout.connect(self.change_logo)
        self.logo_timer.start(10000)   # 60 seconds
        

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
    # Swap Logo
    # ----------------------------

    def change_logo(self):

        num = random.randint(1, 8)

        filename = f"assets/logo{num}.png"

        pixmap = QPixmap(filename)

        self.left_logo.setPixmap(
            pixmap.scaled(
                250,
                250,
                Qt.KeepAspectRatio,
                Qt.SmoothTransformation
            )
        )

    # ----------------------------
    # Create Widgets
    # ----------------------------

    def create_widgets(self):

        self.left_logo = QLabel()
        # from PySide6.QtGui import QPixmap
        # num = random.randint(1, 5)  # Random number between 1 and 5

        # filename = f"assets/logo{num}.png"

        # pixmap = QPixmap(filename)

        # self.left_logo.setStyleSheet("background: transparent;")
        # self.left_logo.setPixmap(
        #     pixmap.scaled(
        #         250,
        #         250,
        #         Qt.KeepAspectRatio,
        #         Qt.SmoothTransformation
        #     )
        # )

        self.change_logo()

        self.left_logo.setAlignment(Qt.AlignCenter)


        self.title = QLabel("📹 Recording Guard")
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setObjectName("title")


        # self.subtitle = QLabel("Recording in Progress")
        self.subtitle = QLabel(RECORDING_MESSAGE)
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

        # ---------- Card Container ----------

        self.card_container = QFrame()
        self.card_container.setObjectName("cardContainer")

        # ---------- Card ----------

        self.card = QFrame()
        self.card.setObjectName("card")

        # ---------- Shadow ----------

        shadow = QGraphicsDropShadowEffect(self)

        shadow.setBlurRadius(200)

        shadow.setOffset(0, 0)

        # shadow.setColor(Qt.white)
        shadow.setColor(
            QColor(247,180,22,120)
        )

        self.card_container.setGraphicsEffect(shadow)

    # ----------------------------
    # Layout
    # ----------------------------

    def create_layout(self):



        # =========== left layout ===========

        left_layout = QVBoxLayout()

        left_layout.addSpacing(200)

        left_layout.addWidget(self.left_logo)

        left_layout.addStretch()


        # =========== right layout ===========


        right_layout = QVBoxLayout()
        right_layout.setAlignment(Qt.AlignCenter)
        right_layout.setSpacing(15)

        right_layout.addWidget(self.title)

        right_layout.addSpacing(10)

        right_layout.addWidget(self.subtitle)
        right_layout.addSpacing(20)

        right_layout.addWidget(self.status)

        right_layout.addWidget(self.date_label)
        right_layout.addWidget(self.time_label)

        right_layout.addSpacing(30)

        right_layout.addWidget(self.password)

        right_layout.addSpacing(20)

        right_layout.addWidget(self.unlock_button)

        right_layout.addSpacing(25)

        # footer = QLabel("Unauthorized access prohibited.")
        footer = QLabel(FOOTER)
        footer.setAlignment(Qt.AlignCenter)

        right_layout.addWidget(footer)

        # self.setLayout(layout)
        self.card.setLayout(right_layout)

        # =========== main layout ===========

        main_layout = QHBoxLayout()

        main_layout.addSpacing(300)

        main_layout.addLayout(left_layout)

        main_layout.addStretch()

        # main_layout.addWidget(self.card)
        container_layout = QVBoxLayout()

        container_layout.setContentsMargins(25,25,25,25)

        container_layout.addWidget(self.card)

        self.card_container.setLayout(container_layout)

        main_layout.addWidget(self.card_container)

        main_layout.addSpacing(90)

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
        }}

        QFrame#cardContainer{{
            background:transparent;
            border-radius:30px;
            margin:0px;
            padding:0px;
            
            
        }}

        QFrame#card{{
            background:rgba(0,0,0,250);
            border-radius:30px;
            border:2px solid #f7b416;
            padding:30px;
            min-width:500px;
            max-width:500px;
            max-height:600px;
            
        }}

        QLabel {{
            color:white;
            background-color: transparent;
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
            background:#2b2b2b;
            padding:12px;
            border-radius:20px;
            border:2px solid #444444;
            color:white;
            font-size:18px;
        }}

        QLineEdit:focus{{

        border:2px solid #ff3b30;

        }}


        QPushButton{{

            background:#FF7D0B;

            padding:12px;

            border-radius:20px;

            font-size:18px;

            font-weight:bold;

            color:white;

        }}

        QPushButton:hover{{

            background:#f7b416;

        }}

        QPushButton:pressed{{

            background:#d63031;

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

    