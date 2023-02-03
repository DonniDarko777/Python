contry= {'G':3 } # певое значение это ключ , второе значение 
print(contry['G'])

bobo= {(5, 6):6} #внутри словоря можно создавать картежи
print(bobo[5,6])

mimi= {'code:' : 'RU', 'name': 'russia', 'popul': 144} # словарь это  ключ:значение, ключ:значение....
print(mimi['name'])

hoho= dict(code='RU', name='russia', popul='144') # тоже самое тока пишется по другому с значением dict
print(hoho['name'])


liz= {'code:' : 'RU', 'name': 'russia', 'popul': 144} 
for go in liz:
    print(go) # так будут выаодится тока кючи 


dodo= {'code' : 'RU', 'name': 'russia', 'popul': 144} 
#for job, key in dodo.items():
print (dodo.items()) # выведет все значение 

fifi = {'code:' : 'RU', 'name': 'russia', 'popul': 144} 
for key, valu in fifi.items():
    print(key , "-", valu) # так будут выаодится ключи и значения 

aiai= {'code' : 'RU', 'name': 'Russia', 'popul': 144} 
#print(aiai.get('name')) #нихера не понятно что за метод get
#aiai.pop('name') # удаляет укзанный значение по ключю 
#aiai.popitem() # удаляет последнее зачение 
#print (aiai.keys()) # выведит тупо ключи 
#print(aiai.values()) # выаодит не ключи а значения ключей 
aiai['code']= 'US' # можно присвоить значения 
print(aiai.items())


