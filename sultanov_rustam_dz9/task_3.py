

class Worker:
    def __init__(self, name, surname, position, incom = {}):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = incom

class Position(Worker):
    def get_total_income(self):
        print(self._income['wage'] + self._income['bonus'])

    def get_full_name(self):
        # self.full_name = self.name + self.surname
        print(f'{self.name} {self.surname}')

wk_ps = Position(name='Артур', surname='Пирожков', position='Мягкий коврик', incom = {'wage': 5000, 'bonus': 3000})
print(wk_ps.position)
wk_ps.get_full_name()
wk_ps.get_total_income()