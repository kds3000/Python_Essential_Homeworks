'''
Используя ссылки в конце данного урока, ознакомьтесь с таким средством инкапсуляции как свойства.
Ознакомьтесь с декоратором property в Python.
Создайте класс, описывающий температуру и позволяющий задавать и получать температуру по шкале Цельсия и Фаренгейта,
причём данные могут быть заданы в одной шкале, а получены в другой.
'''


class Temperature:
    def __init__(self):
        self.celsius = 0

    @property
    def fahrenheit(self):
        return self.celsius * 1.8 + 32

    @fahrenheit.setter
    def fahrenheit(self, value):
        self.celsius = (value - 32) / 1.8

