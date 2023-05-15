def capitalize(String):
    return String.title()
capitalize("new year") # [New Year]
capitalize("python programming") # [Python Programming]
capitalize("how are you!") # [How Are You!]

def merge(dic1,dic2):
    dic3=dic1.copy()
    dic3.update(dic2)
    return dic3
dic1={1:"keyboard", 2:"screen"}
dic2={3:"Python", 4:"Programming"}
merge(dic1,dic2) # {1: 'keyboard', 2: 'screen', 3: 'Python', 4: 'Programming'}

import time # импортируем модуль
start_time= time.time()
def fun():
    a=2
    b=3
    c=b * a ** 2 / b 
end_time= time.time()
fun() # вызываем функцию
timetaken = end_time - start_time
print("Your program takes: ", timetaken) #выводим время выполнения функции
