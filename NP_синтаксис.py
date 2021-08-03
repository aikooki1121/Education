import numpy as np


x = np.zeros(10, dtype=int)
x = np.ones((3, 5), dtype=float)
x = np.full((2, 3), 2)  #
x = np.arange(2, 20, 2)  # Одномерный массив с шагом 2
x = np.linspace(0, 1, 5)  # Массив из 5 значений равнорасположенных между 0 и 1
x = np.random.random((2, 2))
x = np.random.randint(0, 10, (3, 3))  # В идапазон [0:10) рандомные значения
# x = np.eye(3)

print(x)

#  todo ------------------------------------- Атрибуты массивов NumPy ------------------------------------
x1 = np.random.randint(10, size=6)
x2 = np.random.randint(10, size=(2, 4))
x3 = np.random.randint(10, size=(3, 4, 5))  # трехмерный массив

print("\n", 'One dimension matrix:', '\n', x1, "\n", 'x1.dtype: ', x1.dtype, "\n", '\n',
      'Two dimension matrix:', '\n', x2, '\n', 'x2.dtype: ', x2.dtype, '\n', '\n',
      'Three dimension matrix:', '\n', x3, '\n', 'x3.dtype: ', x3.dtype, '\n')

print('x3.shape: ', x3.shape)
print('x3.ndim: ', x3.ndim)
print('x3.size: ', x3.size)
print('x3.itemsize: ', x3.itemsize, 'bytes')
print('x3.nbytes: ', x3.nbytes, 'bytes')


#  todo -------------------------------------------- Индексация массива ----------------------------------
x1 = np.array([5, 0, 3, 3, 7, 9])
print('\nx1:', x1)
print('x1[0]:', x1[0])
print('C конца массива - x1[-1]:', x1[-1], '\n')

x2 = np.array([[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12]])
print('x2:\n', x2)
print('x2[2, 1]:', x2[2, 1])
print('Можно заменить тем же способом: x2[2, 1] = 0')
x2[2, 1] = 0
print('x2:\n', x2)
print('x2[2, 1]:', x2[2, 1], '- PERFECT ! ! !\n')


#  todo ----------------------------------------- Срезы массивов -------------------------------------
#  todo Одномерные массивы
x = np.arange(10)
print('x =', x)
print('Первые пять элементов - x[:5]:', x[:5])
print('Элементы после индекса 5 - x[5:]:', x[5:])
print('Подмассив из середины - x[4:7]:', x[4:7])
print('Каждый второй элемент - x[::2]:', x[::2])
print('Каждый второй элемент начиная с 1 - x[1::2]:', x[1::2])
print('Все элементы с конца с шагом 1(один из способов зареверсить массив) - x[::-1]:', x[::-1], '\n')

# todo Многомерные массивы
x2 = np.array([[1, 2, 3, 4],
               [5, 6, 7, 8],
               [9, 10, 11, 12]])
print('x2:', '\n', x2)
print('Двен строки два столбца x2[:2, :3]:', '\n', x2[:2, :3])
print('Также массив можно переворачивать x2[::-1, ::-1]:\n', x2[::-1, ::-1])

# todo Доступ к строкам и столбцам массива
print('Первый столбец массива - x2[:, 0]:\n', x2[:, 0])
print('Первая строка массива - x2[0, :]:\n', x2[0, :])

# todo Подмассивы как предназначенные только для чтения представления
x2_sub = x2[:2, :2]
print('\nИзвлечем двумерный массив 2х2 - x2_sub = x2[:2, :2] :\n', x2_sub)
print('При изменении выделенного подмассива изменится и сам основной массив x2_sub[0, 0] = 100:')
x2_sub[0, 0] = 100
print(x2_sub)
print('x2:', x2)

# todo Создание копий массивов
x2_sub_copy = x2[:2, :2].copy()
print('\n', x2_sub_copy)
x2_sub_copy[0, 0] = 111
print(x2_sub_copy)
print('\nПри изменении подмассива копии основной массив не меняктся')
print(x2)

# todo Изменение формы массивов (ИМЕЮТСЯ ВОПРОСЫ) ????
grid = np.arange(1, 10)
print('\nПервичный массив', grid)
grid = np.arange(1, 10).reshape((3, 3))
print('После .reshape((3, 3)):\n', grid)

x = np.array([1, 2, 3])
x = x[np.newaxis, :]
print('Преобразорвание массива [1, 2, 3] в вектор строку путём x[np.newaxis, :] \n', x)
x = np.array([1, 2, 3])
x = x[:, np.newaxis]
print('Преобразорвание массива [1, 2, 3] в вектор столбец путём x[:, np.newaxis] \n', x, '\n')


# todo ---------------------------------- Слияние и разбиение массивов -------------------------------------
# todo Слияние массивов

x = np.array([1, 2, 3])
y = np.array([3, 2, 1])
xy = np.concatenate([x, y])
print('Массив х:', x)
print('Массив y:', y)
print('Объединение массивов xy = np.concatenate([x, y]):', xy)
z = np.array([12, 12, 12])
xyz = np.concatenate([x, y, z])
print('Массив z:', z)
print('Объединение массивов xyz = np.concatenate([x, y, z]):', xyz)

grid = np.array([[1, 2, 3],
                [4, 5, 6]])

print('Слияние по первой оси координат', np.concatenate([grid, grid]))
print('Слияние по второй оси координат', np.concatenate([grid, grid], axis=1))


x = np.array([1, 2, 3])
grid = np.array([[1, 2, 3],
                 [9, 8, 7],
                 [6, 5, 4]])
print('x = np.array([1, 2, 3]):', x)
print('grid = np.array([[1, 2, 3], [9, 8, 7],[6, 5, 4]])', grid)
print('', np.vstack([x, grid]))

for i in range(0, 10):
    print(i)
