# условный опреатор 
jo = int(input("Введите свой возвраст: "))
hap = False
name = str(input("Введи имя :"))
lastname =str(input("Введи фамилию :"))
if jo >=18 and jo <=30 :
    print(name, lastname, "Доброе пожаловать в Клуб" ,"тебе :", jo) 
elif jo >= 31 and jo <= 60 :
    print(name, lastname,"Старпер","тебе :", jo) 
elif jo >= 61 and jo <=100:
    print(name, lastname,"дорога на кладбище ","тебе :", jo)         
else: 
    print(name, lastname,"Вали отсюда ","тебе :", jo)


