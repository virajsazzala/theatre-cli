import os

MOVIE_EXTENSIONS = {".mp4", ".avi", ".mkv"}

def set_movie_dir():
    home_dir = os.path.expanduser('~')
    dir_name = input("Directory name? ")
    movie_dir = os.path.join(home_dir, "Videos", dir_name)

    if not os.path.exists(movie_dir):
        os.makedirs(movie_dir)
        print(f"Created directory {movie_dir}")
    else:
        print("Directory already exists!")

    print(f"Please move all your movie files to {movie_dir}")
    return movie_dir

def list_movies(movie_dir):
    movie_files = [f for f in os.listdir(movie_dir) if os.path.isfile(os.path.join(movie_dir, f)) and f.lower().endswith(tuple(MOVIE_EXTENSIONS))]
    
    if movie_files:
        print(f"In {movie_dir} directory:")
        for i, movie_file in enumerate(movie_files):
            print(f"{i}: {os.path.splitext(movie_file)[0]}")
    else:
        print("No movies found in the directory.")

def validate_movie_selection(selection, num_movies):
    try:
        selection = int(selection)
        if 0 <= selection < num_movies:
            return True, selection
    except ValueError:
        pass
    return False, None
