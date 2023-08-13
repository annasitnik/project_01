# Задача 3.1.
# Создайте класс матрицы (или таблицы).
# Требования к классу:
#   - каждая колонка является числом от 1 до n (n любое число, которые вы поставите!)
#   - в каждой ячейке содержится либо число, либо None
#   - доступы следующие методы матрицы:
#       * принимать новые значения,
#       * заменять существующие значения,
#       * выводить число строк и колонок.

# Пример матрицы 10 на 10 из единиц:
# [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
#  [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]

# Примечание!
#   - новый класс не запрещено строить на базе существующих типов данных: списков, словарей и тд.
#   - отображать в таблице/матрице название колонки не обязательно!
#   - использовать готовые классы numpy.array() и pandas.DataFrame() запрещено!
#   - проявите фантазию :)

class Matrix:
# stroks - количество строк, stolbs - количество столбцов
    def __init__(self, stroks, stolbs, value):  
      self.field = [[value for _ in range(stolbs)] for _ in range(stroks)]
      self.stroks = stroks
      self.stolbs = stolbs
      self.value = value

#  принимаем новые значения:
    def get_val(self, strok, stolb):
      return self.field[strok][stolb]

#  заменяем существующие значения:
    def set_val(self, strok, stolb, value):
      self.field[strok][stolb] = value

#  возвращаем количество строк:
    def quantity_stroks(self):
      return self.stroks

#  возвращаем количество столбцов:
    def quantity_stolbs(self):
      return self.stolbs


matr = Matrix(5, 5, 0)
matr.set_val(3, 1, 1) 
for r in range(matr.quantity_stroks()):
    for c in range(matr.quantity_stolbs()):
        print(matr.get_val(r, c), end=' ')
    print()
print(f'Количество строк: {matr.quantity_stroks()}\nКоличество столбцов: {matr.quantity_stolbs()}')