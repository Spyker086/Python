
class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Поехали')

    def stop(self):
        print('Остановились')

    def turn(self, direction=0):
        if direction == 0:
            print('Прямо')
        elif direction == 1:
            print('Влево')
        elif direction == 2:
            print('Вправо')
        else:
            print('Разворот')

    def show_speed(self):
        print(self.speed)

class TownCar(Car):
    def show_speed(self):
        if self.speed > 60:
            print("Превышение скорости")

class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            print("Превышение скорости")


car = Car(speed=70, color='черная', name='Ford_1', is_police=True)
car.go()
car.show_speed()
car.turn(direction=3)
print(car.is_police)