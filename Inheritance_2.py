'''
Опишите классы графического объекта, прямоугольника и объекта, который может обрабатывать нажатия мыши. Опишите класс
кнопки. Создайте объект кнопки и обычного прямоугольника. Вызовите метод нажатия на кнопку.
'''


class Graphical:
    def click(self):
        print('That', self.__class__.__name__, 'is not clickable')


class Rectangle(Graphical):

    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def draw(self):
        for a in range(self.side_a):
            print('*' * self.side_b)


class Clickable:

    def click(self):
        print(self.__class__.__name__, 'was clicked')


class Button(Clickable, Rectangle):
    pass

