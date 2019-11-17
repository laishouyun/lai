#加法运算
while True:
    try:
        first_number = input('Enter number, Carefull it is number ,not content:')
        number1 = int(first_number)
        second_number = input('Enter number,Carefull it is number ,not content:')
        number2 = int(second_number)
    except ValueError:
        print('You input is not number!')
    else:
        number3=number1+number2
        print(number3)


