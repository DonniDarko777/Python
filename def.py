# def summa(a, b):
#     return a+b
# res=summa(5,7 )
# print(res)
# print(summa('h', 'i'))


# ########## Выводим минимальное значение 
# nums1 = [1,5,7,-1,0,17,23]
# min= nums1[0]
# for el in nums1:
#     if el<min:
#         min=el
# print(min)

########## уменьшаем код 

def minim(l):
    min_numb=l[0] #мнимальное значение
    for ex in l:
        if ex< min_numb:
            min_numb= ex 
    return min_numb

nums1 = [1,5,7,-1,0,17,23] 
min = minim(nums1)   
nums2 = [1,-75,7,-156,0,1754,423]
min2= minim(nums2)

if min< min2:
    print(min)
else:
    print(min2)
################################### LANBDA

func= lambda x,y,: x*y
#print(func(5,5)) # можно так 
res = (func(5,5)) # а можно поместить в перменную 
print(res)   
################################# тоже самое через функцию но получиться длинее 
def summa(a,b): 
    return a*b
res = summa(2,2)
print(res)    
