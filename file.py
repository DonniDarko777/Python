# date= input('введите текст')
# file = open('data/text.txt', 'a') # метод записи 'w' будет посмтоянно меняться в зависимости что мы написали  а если 'a', по к ранее созданому добавиться текст,  
# # file.write('Hello')
# # file.write('!!!' '\n') # перевод на новую строку
# # file.write('Perevod \n')  
# # file.write('sisi \n')  
# file.write (date + "\n")
# file.close()

file= open('data/text.txt', 'r') # r чтение 
#print(file.read()) # можно вывести определенное количество символов указав параметр в примере 4 
for line in file: #можно через file.read  а можно через цикл for
    print(line, end='')
file.close