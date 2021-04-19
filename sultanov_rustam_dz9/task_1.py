from time import sleep
import os


class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']
    def running(self):
        while True:
            print(self.__color[0])
            sleep(7)
            print(self.__color[1])
            sleep(2)
            print(self.__color[2])
            sleep(5)

tl_1 = TrafficLight()

tl_1.running()