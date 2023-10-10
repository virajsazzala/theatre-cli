# `theatre_cli/movie.py`
This module, `movie.py`, is responsible for managing movie-related operations in your Theater CLI application. It contains functions for setting the movie directory, listing available movies, and validating movie selections.

## Functions:
1. `set_movie_dir()`
    * Description: This function allows users to set the movie directory. It prompts the user for a directory name and creates the directory if it doesn't already exist in the user's home directory.
    * Usage:
        ```python
        movie_dir = set_movie_dir()
        ```
    * Input: None
    * Output: A string representing the path to the chosen movie directory.

2. `list_movies(movie_dir)`
    * Description: Lists all movie files in the specified directory, filtering files with extensions such as .mp4, .avi, and .mkv.
    * Usage:
        ```python
        list_movies(movie_dir)
        ```
    * Input:
        * `movie_dir`: A string representing the path to the movie directory.
    * Output: None (prints a list of available movies to the console).

3. `validate_movie_selection(selection, num_movies)`
    * Description: Validates the user's movie selection, ensuring that the input is a valid index within the range of available movies.
    * Usage:
        ```python
        valid_selection, index = validate_movie_selection(selection, num_movies)
        ```
    * Input:
        * `selection`: User input for the movie selection.
        * `num_movies`: The number of available movies.
    * Output:
        * `valid_selection`: A boolean indicating if the selection is valid.
        * `index`: The validated index of the selected movie.