# config.py

import json


with open("settings.json", "r") as file:
    SETTINGS = json.load(file)


APP_NAME = SETTINGS["app_name"]
WINDOW_TITLE = SETTINGS["window_title"]

PASSWORD = SETTINGS["password"]

BACKGROUND = SETTINGS["background"]
ACCENT = SETTINGS["accent"]
TEXT = SETTINGS["text"]

SHOW_CLOCK = SETTINGS["show_clock"]
SHOW_DATE = SETTINGS["show_date"]

RECORDING_MESSAGE = SETTINGS["recording_message"]

FOOTER = SETTINGS["footer"]




# APP_NAME = "Recording Guard"

# WINDOW_TITLE = "Recording Guard"

# PASSWORD = "12345"  # Temporary
# # We'll replace this with a secure password hash in the next version.

# # BACKGROUND = "#111111"
# BACKGROUND = "#000000"

# # ACCENT = "#ff3b30"
# ACCENT = "#FFA31A"

# TEXT = "#ffffff"

