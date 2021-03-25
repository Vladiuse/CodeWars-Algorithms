# https://www.codewars.com/kata/52bb6539a4cf1b12d90005b7

battleField = [[1, 0, 0, 0, 0, 1, 1, 0, 0, 0],
               [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
               [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
               [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
               [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def validate_battlefield(battlefield):
    def shell(array):
        for id, line in enumerate(array):
            array[id].insert(0, 0)
            array[id].append(0)
        array.insert(0, [0] * 12)
        array.append([0] * 12)
        return array

    def get_ships(array):

        battleField = array
        dic = {
            1: [],
            2: [],
            3: [],
            4: [],
        }
        for x in range(1, 11):
            for y in range(1, 11):
                dir_x = 1
                dir_y = 1
                point = battleField[x][y]
                if point == 1:
                    ship = [[x, y]]
                    battleField[x][y] = 'O'
                    if battleField[x][y + dir_y] == 1:
                        point = battleField[x][y + dir_y]
                        while point:
                            ship.append([x, y + dir_y])
                            battleField[x][y + dir_y] = 'O'
                            dir_y += 1
                            point = battleField[x][y + dir_y]
                    else:
                        point = battleField[x + dir_x][y]
                        while point:
                            ship.append([x + dir_x, y])
                            battleField[x + dir_x][y] = 'O'
                            dir_x += 1
                            point = battleField[x + dir_x][y]
                    try:
                        dic[len(ship)].append(ship)
                    except KeyError:
                        return False
        for k, v in dic.items():
            if 5 - len(v) == k:
                pass
            else:
                return False
        return dic

    def check_ship(ship):
        shots = [[1, 0], [-1, 0], [0, 1], [0, -1], [1, 1], [-1, 1], [1, -1], [-1, -1]]
        for xx, yy in ship:
            for shot_x, shot_y in shots:
                x = xx
                y = yy
                x += shot_x
                y += shot_y
                shot = battleField[x][y]
                if shot != 0:
                    if [x, y] not in ship:
                        return False
        return True

    battleField = shell(battlefield)
    ships_cors = get_ships(battleField)
    li = []
    if ships_cors:
        for k, ships in ships_cors.items():
            for ship in ships:
                rez = check_ship(ship)
                li.append(rez)
    else:
        return False
    return all(li)


print(validate_battlefield(battleField))
