# `theatre_cli/config.py`

The `config.py` module is responsible for managing configuration settings for your Theater CLI application. It handles loading and saving user settings, such as the movie directory and first-time setup.

## Functions:
1. `load_config()`
    * Description: Loads the configuration from a file named "config.json." It returns the configuration data as a list of dictionaries.
    * Usage:
        ```python
        config_data = load_config()
        ```
    * Input: None
    * Output: A list containing configuration data (e.g., movie directory and first-time setup status).

2. `save_config(config_data)`

    * Description: Saves the provided configuration data to the "config.json" file.
    * Usage:
        ```python
        save_config(config_data)
        ```
    * Input:
    `config_data`: A list containing configuration data to be saved.
    * Output: None