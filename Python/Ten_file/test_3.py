file_name = 'guest.txt'
with open(file_name, 'a') as file_object:
    for i in range(2):
        name = input('\nEnter your name:')
        a = 'hello '+name+'\n'
        print(a)
        file_object.write(a)

print(file_object)