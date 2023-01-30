a= int(input("Введите возраст: "))
if a>=18:
    print ("Хорошо ваш возраст нам подходит")
    c= str(input("ВВедите Имя: "))
    resul = str(input("Хочешь ли ты сыграть в игру ? Yes/ No: "))
    if resul == "yes" or resul=="Yes" or resul=="YES" or resul =="Да" or resul== "да" or resul== "ДА":
        print("Добро пожаловать в игру")
        print("Первый вопрос ", end="\n")
        qvest1= int(input("2+2 = ? ответ запишите в цифрах: "))
        if qvest1==4:
            print("ВЕРНО!!!")
            print("слудующий вопрос")
            qvest2 = str(input("Стольца России = ? Напишите на русском языке ответ : "))
            if qvest2 =="Москва" or qvest2== "москва" or qvest2=="moscow" or qvest2=="Moscow":
                print("ВЕРНО!!!")
                qvest3= input("Как зовут создателя данной игры?  ")
                if qvest3=="Женя" or qvest3=="женя" or qvest3=="Евгений" or qvest3=="евгений":
                    print("ВЕРНО!!!")
                else:
                    print("Фу как не красиво ! Не приходи больше!")
            else:
                print("Вы ошиблись, КОНЕЦ игры")                 
        else:    
            print("Вы ошиблись, КОНЕЦ ИГРЫ")
    else:
        print("Ну что ж ", c, "Если передумаете приходите вновь , Ваш возраст ", a, "нам подходит! Пока ! ", )             
else:
    print("Ты слишком юн/а, приходи как подростеш")

