import json


def get_stored_username():
    filename = 'username.json'
    try:
        with open(filename) as j_obj:
            username = json.load(j_obj)
    except FileNotFoundError:

        return none
    else:
        return username


def get_new_username():
    username = input('What is your name?')
    filename = 'username.json'
    with open(filename, "w") as j_obj:
        json.dump(username, j_obj)
def greet_user():
    username = get_stored_username()
    if username:
        print('Welcome back ' + username + '!')
    else:
        print('We will remember you when you come back, ' + username + '!')


greet_user()
