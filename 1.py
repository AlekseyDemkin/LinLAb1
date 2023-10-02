from numpy import linalg
import numpy as np
from random import randint


def changestring(st):
    r = ""
    for i in range(0, 3):  # генерируем строку из 3-х случ. символов
        r = r + alf[randint(0, 41)]
    st = r + st[3:]  # заменяем первые три символа на сгенерированную строку
    return st  # возвращаем изменённую строку


def encode(st, Arr, B, t, y):
    for x in range(t, len(st) + 1, t):
        Arr.append(st[x - t:x])  # делим массив из чисел на группы по знач. ранга
    for x in range(0, len(Arr)):
        f = (np.dot(y, Arr[0])) % len(alf)  # кодируем
        Arr.pop(0)
        Arr.append(f)
    Arr = list(np.array(Arr).flatten())
    for x in range(0, len(Arr)):
        B = B + str(alf[Arr[x]])  # преобразовываем числа в символы алфавита
    return B


def transform(st, Y, t):
    massRang = []
    for m in range(0, len(string)):
        massRang.append(int(alf.index(st[m])))
    Arr = []
    for m in range(t, len(massRang) + 1, t):
        Arr.append(massRang[m - t:m])
    B = ""
    for m in range(0, len(Arr)):
        f = (np.dot(Y, Arr[0])) % L
        Arr.pop(0)
        Arr.append(f)
    Arr = list(np.array(Arr).flatten())
    for m in range(0, len(Arr)):
        B = B + str(alf[Arr[m]])
    return B


def MOD(KEY):  # ищем 1/det
    u = round(np.linalg.det(KEY))
    i = 1
    while ((41 * i + 1) / u) % 1 != 0:
        i += 1
    return (int((41 * i + 1) / u)), u


def REVMat(KEY, st, t):
    u, y = MOD(KEY)  # ищем обратную матрицу по модулю
    R = (np.round((np.linalg.inv(KEY) * np.linalg.det(KEY) * u) % 41).astype(int))
    return transform(st, R, t)


alf = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ#!?47905"
L = len(alf)
string = "АПЧИХБАЗАЯЦ7"
stringE = []
P = np.array([[7, 5], [2, 4]])
Q = np.array([[5, 9, 4], [2, 7, 5], [8, 6, 3]])
S = np.array([[15, 2, 3, 4], [5, 4, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]])
for i in range(0, len(string)):  # создаем массив из индексов строки
    stringE.append(int(alf.index(string[i])))
print("Строка:", string)
rP = np.linalg.matrix_rank(P)  # ранг матрицы P
rQ = np.linalg.matrix_rank(Q)  # ранг матрицы Q
rS = np.linalg.matrix_rank(S)  # ранг матрицы S
stringrP, stringrQ, stringrS = [], [], []
stringrPE, stringrQE, stringrSE = "", "", ""
print("Для P ключа")
p = encode(stringE, stringrP, stringrPE, rP, P)
print("Закодированно с помощью ключа P:", p)
p = changestring(p)
print("Закодированно и изменено с помощью ключа P:", p)
print("Декодированно используя ключ P:", REVMat(P, p, rP))
# Для Q ключа
print()
print("Для Q ключа")
q = encode(stringE, stringrQ, stringrQE, rQ, Q)
print("Закодированно с помощью ключа Q:", q)
q = changestring(q)
print("Закодированно и изменено с помощью ключа Q:", q)
print("Декодированно используя ключ Q:", REVMat(Q, q, rQ))
# Для S ключа
print()
print("Для S ключа")
s = encode(stringE, stringrS, stringrSE, rS, S)
print("Закодированно с помощью ключа S:", s)
s = changestring(s)
print("Закодированно и изменено с помощью ключа S:", s)
print("Декодированно используя ключ S:", REVMat(S, s, rS))
