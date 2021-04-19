

class Stationary:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки")

class Pen(Stationary):
    def draw(self):
        print("Запуск отрисовки Ручка")

class Pencil(Stationary):
    def draw(self):
        print("Запуск отрисовки Карандаш")

class Handle(Stationary):
    def draw(self):
        print("Запуск отрисовки Маркер")


stat = Pen(title="BIC")
stat.draw()