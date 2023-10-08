import json
import os
# Using default .config directory for storing configuration file
CONFIG_DIR = os.path.expanduser("~/.config/theatre-cli")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.json")

def load_config():
    try:
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_config(config_data):
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(config_data, f, indent=2)
