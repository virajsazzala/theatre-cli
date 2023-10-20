import yaml
import os
# Using default .config directory for storing configuration file
CONFIG_DIR = os.path.expanduser("~/.config/theatre-cli")
CONFIG_FILE = os.path.join(CONFIG_DIR, "config.yaml")

def load_config():
    try:
        with open(CONFIG_FILE, "r") as yf:
            return (yaml.safe_load(yf))
    except FileNotFoundError:
        return []
    
print(CONFIG_FILE)   

def save_config(config_data):
    os.makedirs(CONFIG_DIR, exist_ok=True)
    with open(CONFIG_FILE, "w") as yf:
        yaml.dump(config_data, yf, indent=2)

