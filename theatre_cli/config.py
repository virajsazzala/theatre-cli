import yaml

CONFIG_FILE = "config.json"

def load_config():
    try:
        with open(CONFIG_FILE, "r") as yf:
            # fullLoader converts yaml to py dict
            return yaml.load(yf,Loader=yaml.FullLoader)
    except FileNotFoundError:
        return []

def save_config(config_data):
    with open(CONFIG_FILE, "w") as yf:
        yaml.dump(config_data, yf, indent=2)
        print("Write successful")