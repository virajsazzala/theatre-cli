# Config File

# Overview

The Configuration Management Utilities provide functions to load and save configuration data in JSON format. These functions handle the creation of the configuration directory and file, as well as reading and writing configuration data.

## Functions

****`load_config() -> dict`****

- Loads configuration data from the specified JSON configuration file.

Returns

- **`dict`**: A dictionary containing the loaded configuration data.

## Code Sample

```python
config_data = load_config()
```

## Functions

****`save_config(config_data: dict)`****

- Saves the provided configuration data to the JSON configuration file. If the configuration directory or file does not exist, it creates them.

## Parameters

- **`config_data`** (dict): The configuration data to be saved.

## Code Sample

```python
config_data = {
    "key": "value",
    "another_key": "another_value"
}
save_config(config_data)
```

## Example Usage

```python
from config_utils import load_config, save_config

# Load existing configuration data
config_data = load_config()
print("Loaded Configuration Data:", config_data)

# Modify configuration data
config_data["key"] = "new_value"
config_data["new_key"] = "new_item"

# Save the modified configuration data
save_config(config_data)
print("Configuration Data Saved.")
```
