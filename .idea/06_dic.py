##################Словари и списковые ключения################
# Задача 5

# Поиск самых высокооплачиваемых работников 

# Нужно найти всех сотрудников
# зарабатывающих по крайней мере 100 000 долларов в год

employees = {'Alice' : 100000,
    'Bob' : 99817,
    'Carol' : 122908,            
    'Frank' : 88123,
    'Eva' : 93121}
# Вариант 1
top_mgrs = []

for name in employees:
    if employees [name] >= 100000:
        top_mgrs.append(name)
print("Список топ-менеджеров", top_mgrs)        

# Вариант 2


 #if salary >= 100000:
   # top_mgr.append()

# for name, salary employees.item():    



# Про словари
#capitals = {'Россия': 'Москва'}   
# Запросить из словаря
#print(capitals['Россия'])
# Добавление в словарь
#capitals['Италия'] = 'Рим'
#capitals['Франция'] = 'Париж'

#print(capitals) # {'Россия': 'Москва', 'Италия': 'Рим', 'Франция': 'Париж'}
# print(capitals['Италия'][::-1])

# методы словарей
#from pprint import pprint
#pprint(dir(capitals))

#print('ключи', capitals.keys())
#print('значения', capitals.values())
#print('пары "ключи-значения"', capitals.items())

# Про списковые включения
# развернутый вариант for

lst = [1, 2, 3, 4, 5]

new_lst = []
for i in lst:
    new_lst.append(i ** 2)

 # однострочник for
oneL = [i ** 2 for i in [1, 2, 3, 4, 5]]  