"""Перепишите решение первого задания с помощью генератора. """


def reversed_list_generator(a_list):
    for i in range(len(a_list)):
        yield a_list[len(a_list) - i - 1]


class ReversedList:
    def __init__(self, a_list):
        self.a_list = a_list

    def __getitem__(self, index):
        if index < len(self.a_list):
            return self.a_list[len(self.a_list) - 1 - index]
        else:
            raise IndexError('Index out of range')
