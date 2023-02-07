#!/usr/bin/python3

import os
import json

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
            player = int(input("Which Player do you prefer?\n0: Mpv\n1: Vlc\nChoose: "))
            if player == 0:
                os.system(f"mpv {movie_dir}/{filesincwd[selection]}")
            elif player == 1:
                os.system(f"vlc {movie_dir}/{filesincwd[selection]}")
            else:
                print("Choose a valid index!")
                return 0
    else:
        print("Please add some movies to the specified movies dir!")

if __name__ == "__main__":
    # loading config.json file
    with open('config.json') as f:
        config_data = json.load(f)

    # Checking for first time setup
    first_time = config_data[0]['first_time']

    # if true - performing first time setup
    if first_time == "true".lower():
        print('Performing first time setup...')
        req_dir = int(input("Do you have a movies dir or would you like to make one?\n0: use an existing one\n1. make a new one\nEnter choice: "))

        if req_dir:
            dir_path = set_movie_dir()
        elif req_dir == 0:
            dir_path = input("Enter the directory path (from home dir): ")
        else:
            print("Enter a valid choice!")
            exit(0)

        # addes the new configuration to config.json 
        with open('config.json', 'w') as f:
            config_data = []
            config_data.append({
                "first_time": "false",
                "username": user_name,
                "home_dir": home_dir,
                "movie_dir": dir_path
            })
            json.dump(config_data, f, indent=2)
    elif first_time == "false".lower():
        pass
    else:
        print('Please verify that "first_time" is set to either "true" or "false" in config.json!')
        exit(0)

    # required variables
    movie_dir = config_data[0]['movie_dir']
    username = config_data[0]['username']
    home_dir =  config_data[0]['home_dir']

    # choose and play movie
    play_movie(movie_dir)