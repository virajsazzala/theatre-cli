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

_________________________________________________________________________________________________________________________________________________________________________________________

# Movies File

# Overview

Movie program provides a set of functions to manage movie files, including setting the movie directory, listing movies, validating user selections, and handling movie file extensions.

## Functions

set_movie_dir() -> str

- Creates a new movie directory or retrieves an existing one from the user. This function prompts the user to input a directory name and creates the directory inside the "Videos" folder in the user's home directory.

## Parameters

| Parameters | Type | Description |
| --- | --- | --- |
| set_movie_dir() -> str | str | The absolute path to the created or existing movie directory. |
|  |  |  |

## Code Sample

```python
movie_directory = set_movie_dir()
```

## Functions

list_movies(movie_dir: str) -> List[Movie]

- Lists all the movie files in the specified directory with supported movie file extensions (".mp4", ".avi", ".mkv"). It creates a list of **`Movie`** objects representing the movie files found.

## Parameters

| Parameters | Returns | Description |
| --- | --- | --- |
| movie_dir (str) | List[Movie] | A list of Movie objects representing the movie files found in the directory. |

## Code Sample

```python
movie_files = list_movies("/path/to/movies/directory")
```

## Function

****`validate_movie_selection(selection: str, num_movies: int) -> Tuple[bool, Optional[int]]`****

- Validates the user's movie selection input. It checks if the input is a valid integer within the range of available movies.

## Parameter

- **`selection`** (str): The user's input for movie selection.
- **`num_movies`** (int): The total number of available movies
- 

Returns

- **`Tuple[bool, Optional[int]]`**: A tuple where the first element is a boolean indicating whether the selection is valid, and the second element is the validated selection index (or **`None`** if the input is invalid).

## Code Sample

```python
valid_selection, index = validate_movie_selection("2", num_movies)
```

## Example Usage

```python
from movie_player_utils import set_movie_dir, list_movies, validate_movie_selection

# Set movie directory
movie_directory = set_movie_dir()

# List movies in the specified directory
movie_files = list_movies(movie_directory)

# Validate user's movie selection
selection = input("Enter your choice: ")
valid_selection, index = validate_movie_selection(selection, len(movie_files))
if valid_selection:
    selected_movie = movie_files[index]
    print(f"Selected movie: {selected_movie.file}")
else:
    print("Invalid selection. Please choose a valid movie.")
```
_________________________________________________________________________________________________________________________________________________________________________________________

# Players File

# Overview

The [players.py](http://players.py/) program provides an easy way to play movies from
given directory. It allows a user to select a movie from the list
of available movies in the directory and select a play mode
that is MPV or VLC to play the chosen movie.

### Functions

`play_movie(movie_file, player)`

- - Plays selected movie using the specified player

## Code Sample

```python
play_movie("/path/to/selected_movie.mp4", 0)
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| movie_file(str) | string | This is a path to the selected movie file |
| player(int) | int | It is an integer representing the choice of the
player.
0  -->  MPV
1  -->  VLC |

`choose_player_and_play(movie_dir)`

Displays a list of movies in the specified directory, it allows the user to select a movie and prompts the user to select a player to play the selected movie.

```python
 choose_player_and_play("/path/to/movies/directory")
```

## Parameters

| Parameter | Type | Description |
| --- | --- | --- |
| movie_dir(str) | str | The path to the directory containing movie files. |

## How to use

- Import the necessary functions from the module:

```python
from movie_player_cli import choose_player_and_play
```

- Call the **`choose_player_and_play(movie_dir)`** function, passing the path to the directory containing your movie files as an argument:

```python
choose_player_and_play("/path/to/movies/directory")
```

- The CLI will display a list of movies in the specified directory. Enter the index of the movie you want to play (from 0 to N-1, where N is the number of movies).
- Choose a player by entering the corresponding number (0 for MPV, 1 for VLC).
- The selected movie will start playing in the chosen player.
- To quit the program, enter 'q' when prompted for movie selection.

```python
from movie_player_cli import choose_player_and_play

# Specify the directory containing movie files
movie_directory = "/path/to/movies/directory"

# Start the CLI movie player
choose_player_and_play(movie_directory)
```
