'''
Создайте иерархию классов с использованием множественного наследования. Выведите на экран порядок разрешения методов
для каждого из классов. Объясните, почему линеаризации данных классов выглядят именно так.
'''


class Human:
    pass


class Grandfather(Human):
    pass


class Grandmother(Human):
    pass


class Father(Grandfather, Grandmother):
    pass


class Mother(Grandfather, Grandmother):
    pass


class Kid(Father, Mother):
    pass


if __name__ == '__main__':
    print(Kid.__mro__)
