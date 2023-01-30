#nna= "GHello world"
#for i in range(0, 5): ## выводми количстсво конкреинок количество раз range
   # print(nna)
#t= int(input("введи число : "))
#while t<=5:
#    if t!=3:
#        print(t, end='') # выведет все в отдну строку end=''
#    t=t+1
#    continue # пересккивает

#for j in "hello word":
#    if j=="h":
#        break
#else:
#    print('нет такой буквы')    

#for i in range(1, 6):
 #   print("приве", i) 
 #print(list(range(10, 19)))

#sp1 = [1,2,3,4,5,6,7,8,9,10]
#sp2= ["привет", "пока", "че", "как", "подеба"]
#for i in range(1, 6):
##    for j in range(1, 6):
 #       print(j, i)

found_coins= 20
mag = 10
vor = 2
coins = found_coins
print( found_coins + 365*(mag-vor))


for i  in range(0,365):
    coins=coins+mag -vor
    print("Ден, %s стало монет %s" % (i, coins))