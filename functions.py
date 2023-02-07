import os

home_dir = os.path.expanduser('~')
user_name = os.environ.get('USERNAME')

def set_movie_dir():
    dir_name = input("Directory name? ")
    print(f"Creating directory /{dir_name} at {home_dir}/Videos")
    try:
        os.mkdir(f'{home_dir}/Videos/{dir_name}')
    except(FileExistsError):
        print("Directory already exists!")
    print(f"Please move all your movie files to {home_dir}/Videos/{dir_name}")
    return f'{home_dir}/Videos/{dir_name}'


def play_movie(movie_dir):
    filesincwd = os.listdir(movie_dir)
    if len(filesincwd) > 0:
        print(f"Hey {user_name}, Welcome to Theatre-CLI!\nHope you are having a good day, even if you arent, it'll get better dw <3")
        print(f"In {movie_dir} directory:")
        for i in range(len(filesincwd)):
            print(f"{i}: {(filesincwd[i])[:-4]}")

        selection = input(f"Enter your choice ({0} to {len(filesincwd)-1}) or (q to quit): ")
        if selection == 'q':
            print("Bye bye! see you later <3")
            return 0
        else:
            try:
                selection = int(selection)
            except (ValueError):
                print("please enter a valid option!")
                return 0

        if selection > len(filesincwd) or selection < 0:
            print("Choose a valid index")
            return 0
        else:
            player = int(input("Player:\n0: Mpv\n1: Vlc\nChoose: "))
            if player == 0:
                os.system(f"mpv {movie_dir}/{filesincwd[selection]}")
            elif player == 1:
                os.system(f"vlc {movie_dir}/{filesincwd[selection]}")
            else:
                print("Choose a valid index!")
                return 0
    else:
        print("Please add some movies to the specified movies dir!")