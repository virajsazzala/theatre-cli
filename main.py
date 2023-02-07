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
        with open('config.json', 'w') as f:
            config_data = []
            config_data.append({
                "first_time": "false",
                "username": t.user_name,
                "home_dir": t.home_dir,
                "movie_dir": dir_path
            })
            json.dump(config_data, f, indent=2)
    elif req_dir == 0:
        pass
    else:
        print("Enter a valid choice!")
elif first_time == "false".lower():
    pass
else:
    print('Please verify that "first_time" is set to either "true" or "false" in config.json!')

# required variables
movie_dir = config_data[0]['movie_dir']
username = config_data[0]['username']
home_dir =  config_data[0]['home_dir']

print(f"Hey {username}, Welcome to Theatre-CLI!\nHope you are having a good day, even if you arent, it'll get better dw <3")
t.play_movie(movie_dir)
f.close()
