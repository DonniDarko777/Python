import time
time.sleep(1) #заморжено время на 3 секунды 
print('Hello')

import datetime as date
print(date.datetime.now().time()) #date , time 

import sys, os , platform
print(platform.system())


from math import sqrt as s , ceil # и модуля взять конкретную ФУНКЦИЮ тут это sqrt из math
print(ceil(s(100)))
