import json


filename = 'like_number.json'
try:
    with open(filename) as k_obj:
        number=json.load(k_obj)
        print('you like the number ' + number + '!')
except FileNotFoundError:
    like_number = input('Enter you like\'s number:')
    with open(filename,'w') as k_obj:
        json.dump(like_number,k_obj)
        print('you like the number '+like_number+'!')





