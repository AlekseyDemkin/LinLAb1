from numpy import linalg
import numpy as np


def smashstring(stringA4):
    for i in range(0, len(stringA4)):
        stringE.append(int(alf.index(stringA4[i])))
    return stringE


def encode(stringE, A):
    for i in range(2, len(stringE) + 1, 2):
        A.append(stringE[i - 2:i])
    return A


def transform(st, Y):
    o = []
    for i in range(0, len(stringBR)):
        o.append(int(alf.index(st[i])))
    A = []
    for i in range(2, len(o) + 1, 2):
        A.append(o[i - 2:i])
    B = ""
    for i in range(0, len(A)):
        f = (np.dot(Y, A[0])) % len(alf)
        A.pop(0)
        A.append(f)
    A = list(np.array(A).flatten())
    for i in range(0, len(A)):
        B = B + str(alf[A[i]])
    return B


def MOD(KEY):
    u = round(np.linalg.det(KEY))
    i = 1
    while ((L * i + 1) / u) % 1 != 0:
        i += 1
    return (int((L * i + 1) / u)), u


def REVMat(MASS, p):
    u, y = MOD(MASS)
    R = (np.round((np.linalg.inv(MASS) * np.linalg.det(MASS) * u) % L).astype(int))
    KEY = np.transpose(np.dot(R, code) % L)
    u, y = MOD(KEY)
    R = (np.round((np.linalg.inv(KEY) * np.linalg.det(KEY) * u) % L).astype(int))
    print("Найденный ключ:\n", KEY)
    return transform(p, R)


alf = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ#!?47905"
L = len(alf)
stringА = "АПЧИХБАЗАЯЦ7"
print("Первое сообщение:", stringА)
stringАR = "0ЦЗВ4Ж5Я7ЕСЭ"
print("Зашифрованное первое сообщение:", stringАR)
stringBR = "ЧХХЕГПИЫ4ФЪО"
print("Зашифрованное второе сообщение:", stringBR)
stringA4 = stringА[:4]
stringAR4 = stringАR[:4]
stringE = []
stringeRP = []
stringE = smashstring(stringA4)
uncode = encode(stringE, stringeRP)
stringE = []
stringeRP = []
stringE = smashstring(stringAR4)
code = encode(stringE, stringeRP)
MG = REVMat(uncode, stringBR)
print("Второе сообщение после расшифровки:", MG)
