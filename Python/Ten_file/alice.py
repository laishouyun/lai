def count_words(filename):
    # 计算一个文件大致包含多少个单词
    try:
        with open(file_name) as file_object:
            contents = file_object.read()
    except FileNotFoundError:
        msg = 'Sorry,the file ' + file_name + ' does not exist!'
        print(msg)
    else:
        # 计算文件大致包含多少个单词
        words = contents.split()
        num_words = len(words)
        print('The file ' + file_name + ' has about ' + str(num_words) + ' words!')


file_names = ['alice.txt', 'siddhartha.txt', 'mody_dick.txt','little_women.txt']
for file_name in file_names:
    count_words(file_name)
