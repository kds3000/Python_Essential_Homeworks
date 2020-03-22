"""
Напишите итератор, который возвращает элементы заданного списка в обратном порядке (аналог reversed).
"""


class ReversedList:
    def __init__(self, a_list):
        self.a_list = a_list

    def __getitem__(self, index):
        if index < len(self.a_list):
            return self.a_list[len(self.a_list) - 1 - index]
        else:
            raise IndexError('Index out of range')

