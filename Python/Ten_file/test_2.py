'''
使用方法replace将Python替换为c
'''
with open('learning_python.txt') as file_name:
    contents=file_name.read()
    new_contents=contents.replace('Python','C')
    print(new_contents)