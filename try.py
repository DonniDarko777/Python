# try:
#     x= int(input('введите число: '))
#     x+=5
#     print(x)
# except ValueError:
#     print("введите лучше число")

           



x= 0
while x==0 :
    try:
        x= int(input('Сколько вам лет ? : '))
        if x>=18:
            print('заходи дорогой ;-)')
            # name = str(input("введите ваше имя "))
            # lastname = str(input("введите вашу Фамилию "))
            yes = str(input("Хотите сыграть в игру?"))
            if yes=='Yes' or yes=='yes':
                print('Очень хорошо , тогда начнем')
                qvest = int('Первый ворос сколько будет 2+2= ? : 1 вариант =4 , 2-ой вариант = 5, Укажите вариант ответи 1 или 2')
                if qvest==1:
                    print('Вы верно ответили')
                else:
                    print('Вы ответили не верно ! ')    
            else:
                print('Очень жаль , всего хорошего ')    
        else:
            print('Вы слишком малы для данной программы ')        
    except ValueError:
        print("введите лучше число")  

