import theatre as t
import json

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
        dir_path = t.set_movie_dir()
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
            "username": t.user_name,
            "home_dir": t.home_dir,
            "movie_dir": dir_path
        })
        json.dump(config_data, f, indent=2)
elif first_time == "false".lower():
    # required variables
    movie_dir = config_data[0]['movie_dir']
    username = config_data[0]['username']
    home_dir =  config_data[0]['home_dir']

    # choose and play movie
    print(f"Hey {username}, Welcome to Theatre-CLI!\nHope you are having a good day, even if you arent, it'll get better dw <3")
    t.play_movie(movie_dir)
else:
    print('Please verify that "first_time" is set to either "true" or "false" in config.json!')
    exit(0)
