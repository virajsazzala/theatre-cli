import os
from theatre_cli.movie import list_movies, validate_movie_selection, MOVIE_EXTENSIONS

def play_movie(movie_file, player):
    players = ["mpv", "vlc"]
    
    if 0 <= player < len(players):
        os.system(f"{players[player]} '{movie_file}'")
    else:
        print("Choose a valid player!")

def choose_player_and_play(movie_dir):
    list_movies(movie_dir)
    movie_files = [f for f in os.listdir(movie_dir) if os.path.isfile(os.path.join(movie_dir, f)) and f.lower().endswith(tuple(MOVIE_EXTENSIONS))]

    if not movie_files:
        print("No movies found in the directory.")
        return

    num_movies = len(movie_files)
    
    while True:
        selection = input(f"Enter your choice (0 to {num_movies - 1}) or (q to quit): ")
        if selection == 'q':
            print("Bye bye! See you later <3")
            return
        
        valid_selection, index = validate_movie_selection(selection, num_movies)
        
        if valid_selection:
            break
        else:
            print("Choose a valid index.")

    player = int(input("Which player do you prefer?\n0: MPV\n1: VLC\nChoose: "))
    play_movie(os.path.join(movie_dir, movie_files[index]), player)
