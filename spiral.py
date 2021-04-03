# def spiralize(size):
#     spiral = [[0] * size] * size
#     return spiral
def round_array(arr, number):
    new = []
    arr = arr.copy()
    length = len(arr)
    plus_li = [number] * (length + 2)
    for i in arr:
        if isinstance(i, int):
            new.append([number,i,number])
            break
        li = i.copy()
        li.insert(0,number)
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
    x = size % 4
    if x == 1:
        spiral = [[1]]
        start_number = 0
    if x == 3:
        spiral = [[0]]
        start_number = 1
    if x == 2:
        spiral = [[1,1], [0,1]]
        start_number = 0
    if x == 0:
        spiral = [[0,0], [0,0]]
        start_number = 1
    while len(spiral) < size:
        spiral = round_array(spiral,start_number)
        if start_number == 0:
            start_number = 1
        else:
            start_number = 0
    return spiral
rez = spiralize(5)
for i in rez:
    print(i)

rez = spiralize(6)
for i in rez:
    print(i)


rez = spiralize(7)
for i in rez:
    print(i)

