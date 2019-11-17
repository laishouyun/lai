import json
filename = 'username.json'
with open(filename) as j_obj:
    username=json.load(j_obj)
    print('Wellcome back '+username+'!')