file_path='/Users/lai/Desktop/haha.txt'
file_name='pi_digits.txt'
with open(file_name) as file_object:
    lines=file_object.readlines()
    pi_string=''
    for line in lines:
        pi_string += line.strip()
    print(pi_string[:52]+'...')
    print(len(pi_string))
        #print(line.rstrip())
    #contents = file_object.read()
    #print(contents.rstrip())

    birthday=input('Enter your birthday,in the form mmddyy:')
    if birthday in pi_string:
        print('Your birthday appears in the first million digits of pi!')
    else:
        print('Your birthday does not appear in the first million digits of pi!')