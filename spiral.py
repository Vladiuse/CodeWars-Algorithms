# https://www.codewars.com/kata/534e01fbbb17187c7e0000c6
# make = [[1, 1, 1, 1, 1, 1, 1],
#        [0, 0, 0, 0, 0, 0, 1],
#        [1, 1, 1, 1, 1, 0, 1],
#        [1, 0, 0, 0, 1, 0, 1],
#        [1, 0, 1, 1, 1, 0, 1],
#        [1, 0, 0, 0, 0, 0, 1],
#        [1, 1, 1, 1, 1, 1, 1]]

def round_array(arr, number):
    new = []
    arr = arr.copy()
    length = len(arr)
    plus_li = [number] * (length + 2)
    for i in arr:
        if isinstance(i, int):
            new.append([number, i, number])
            break
        li = i.copy()
        li.insert(0, number)
        li.append(number)
        new.append(li)
    new.append(plus_li)
    new.insert(0, plus_li)
    if number == 0:
        new[1][0] = 1
    else:
        new[1][0] = 0
    return new


def spiralize(size):
    center = size % 4
    dic = {1: {'spiral': [[1]], 'start_number': 0},
           2: {'spiral': [[1, 1], [0, 1]], 'start_number': 0},
           3: {'spiral': [[0]], 'start_number': 1},
           0: {'spiral': [[0, 0], [0, 0]], 'start_number': 1},
           }
    spiral = dic[center]['spiral']
    start_number = dic[center]['start_number']
    while len(spiral) < size:
        spiral = round_array(spiral, start_number)
        if start_number == 0:
            start_number = 1
        else:
            start_number = 0
    return spiral


rez = spiralize(7)
for i in rez:
    print(i)
