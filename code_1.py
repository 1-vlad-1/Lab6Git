def capitalize(String): # функция выводящая слова с большой буквы
    return String.title()
capitalize("ant") # [Ant] master and future
capitalize("python programming") # [Python Programming]
capitalize("how are you!") # [How Are You!]

def merge(dic1,dic2): # функция для слияния словарей
    dic3=dic1.copy()
    dic3.update(dic2)
    return dic3 # возвращаем получившийся словарь
dic1={1:"start", 2:"end"} # master
dic2={3:"Python", 4:"Programming"}
merge(dic1,dic2) # {1: 'start', 2: 'end', 3: 'Python', 4: 'Programming'} master

import time
start_time= time.time()
def fun():
    a=2
    b=3
    c= a ** b # future
end_time= time.time()
fun()
timetaken = end_time - start_time
print("Your program takes: ", timetaken)