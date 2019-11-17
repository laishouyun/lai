file_name='learning_python.txt'
with open(file_name) as file_object:

    #the first read style
    #contents=file_object.read()
    #print(contents.rstrip())

    #the secend read style
    #lines = file_object.readlines()
    #for line in lines:
        #print(line.rstrip())

    #the last read style
    txt_string=''
    txt_string = file_object.readlines()
    txt_list=list(txt_string)
print(txt_list)


