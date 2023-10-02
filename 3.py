import numpy as np
from numpy import linalg


def slice(mess_array, array, t):
    for x in range(t, len(array) + 1, t):
        mess_array.append(array[x - t:x])
    return mess_array


def decode(array, message):
    for i in range(len(message)):
        array.append(message[i][:4])
    return array


def find_error(message_hem_error):
    H = [[1, 1, 0], [1, 0, 1], [0, 1, 1], [1, 1, 1], [1, 0, 0], [0, 1, 0], [0, 0, 1]]
    for i in range(len(message_hem_error)):
        tr = list(np.dot(message_hem_error[i], H) % 2)
        if tr != [0, 0, 0]:
            ind = H.index(tr)
            message_hem_error[i][ind] = (message_hem_error[i][ind] + 1) % 2
    return message_hem_error


alf = ["а", "б", "в", "г", "д", "е", "ж", "з", "и", "й", "к", "л", "м", "н", "о", "п", "р", "с", "т", "у", "ф", "х",
       "ц", "ч", "ш", "щ", "ъ", "ы", "ь", "э", "ю", "я"]
message = "кита"
string_array = []
message_array_st = []
for i in range(len(message)):  # преобразуем строку в двоичную систему
    string = ""
    len_letter = len(bin(alf.index(message[i]))[2:])
    if len_letter <= 5:
        string = "0" * (5 - len_letter) + bin(alf.index(message[i]))[2:]
    string_array = string_array + list(map(int, string))
message_array_st = slice(message_array_st, string_array, 4)
G = [[1, 0, 0, 0, 1, 1, 0],
     [0, 1, 0, 0, 1, 0, 1],
     [0, 0, 1, 0, 0, 1, 1],
     [0, 0, 0, 1, 1, 1, 1]]
message_hem = (np.dot(message_array_st, G) % 2)
message_hem = [[0, 1, 0, 1, 0, 1, 0], [0, 0, 1, 0, 0, 1, 1], [0, 0, 1, 0, 0, 1, 1], [0, 1, 0, 0, 1, 0, 1],
               [0, 0, 0, 0, 0, 0, 0]]
message_hem_error = [[0, 1, 0, 0, 0, 1, 0], [0, 0, 1, 0, 0, 0, 1], [0, 0, 1, 0, 0, 1, 1], [0, 1, 0, 0, 1, 0, 1],
                     [0, 0, 0, 0, 0, 0, 0]]
change_message = find_error(message_hem_error)
purp = []
fin = decode(purp, change_message)
t = []
for i in fin:
    t.extend(i)
orqw = []
orqw = slice(orqw, t, 5)
stringfin = []
for i in range(len(orqw)):
    v = ""
    for j in range(len(orqw) + 1):
        v = v + str(orqw[i][j])
    v = int(v, 2)
    stringfin.append(v)
v = ""
for i in range(len(stringfin)):
    v = v + alf[stringfin[i]]
print(v)
