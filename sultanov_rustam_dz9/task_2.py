

class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def calc_weight(self):
        print(f'{int((self._lenght * self._width * 25 * 5) / 1000)} т')


rd = Road(lenght=5000, width=20)
rd.calc_weight()