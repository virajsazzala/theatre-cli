# `theatre_cli/player.py``
This module, `player.py`, handles the selection of a media player and playing a chosen movie. It provides functions for playing movies with popular media players.

## Functions:
1. `play_movie(movie_file, player)`
    * **Description:** This function plays a selected movie file using a specified media player (MPV or VLC). It uses the system's command line to execute the chosen player.
    * **Usage:**

        ```python
        play_movie(movie_file, player)
        ```

    * **Input:**
        * `movie_file`: The path to the movie file to be played.
        * `player`: An integer representing the selected media player (0 for MPV, 1 for VLC).
    * **Output:** None

2. `choose_player_and_play(movie_dir)`
    * **Description:** Lists available movies in the specified directory, asks the user to choose a movie to play, and prompts the user to select a media player. It then plays the chosen movie.
    * **Usage:**

        ```python
        choose_player_and_play(movie_dir)
        ```

    * **Input:**
        * `movie_dir`: A string representing the path to the movie directory.
    * **Output:** None