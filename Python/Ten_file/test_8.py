def read(file_name):
    try:
        with open(file_name) as file_object:
            print(file_object)
    except FileNotFoundError:
        print('The file ' + file_name + ' is not found!')


file_names = ['cat.txt', 'dog.txt', 'mouse.txt']
for file_name in file_names:
    read(file_name)