# https://www.codewars.com/kata/5235c913397cbf2508000048

class Calculator(object):
    def evaluate(self, string):
        def resolve(array):
            operators_1 = ['/', '*']
            operators_2 = ['+', '-']
            while '/' in array or '*' in array:
                for char in array:
                    if char in operators_1:
                        pos = array.index(char)
                        a, b = array[pos - 1], array[pos + 1]
                        if char == '/':
                            array[pos - 1:pos + 2] = [float(a) / float(b)]
                            break
                        elif char == '*':
                            array[pos - 1:pos + 2] = [float(a) * float(b)]
                            break
            while '+' in array or '-' in array:
                for char in array:
                    if char in operators_2:
                        pos = array.index(char)
                        a, b = array[pos - 1], array[pos + 1]
                        if char == '-':
                            array[pos - 1:pos + 2] = [float(a) - float(b)]
                            break
                        elif char == '+':
                            array[pos - 1:pos + 2] = [float(a) + float(b)]
                            break
            return str(array[0])

        def get_bracket(array):
            start_pos = 0
            start = end = None
            for id, char in enumerate(array):
                if char == '(':
                    start_pos = id
                if char == ')':
                    start = start_pos
                    end = id
                    break
            rez = resolve(array[start + 1:end])
            array[start:end + 1] = [rez]
            return array

        string = string.split(' ')
        while '(' in string:
            string = get_bracket(string)
        string = resolve(string)
        return float(string)
