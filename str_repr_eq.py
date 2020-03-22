'''
Создайте класс, описывающий книгу. Он должен содержать информацию об авторе, названии, годе издания и жанре.
Создайте несколько разных книг. Определите для него операции проверки на равенство и неравенство,
методы __repr__ и __str__.
'''


class Book:

    def __init__(self, author, name, year, genre):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre

    def __str__(self):
        return 'That`s a book "{}" in {} genre written by {} in {}'.format(self.name,
                                                                           self.genre,
                                                                           self.author,
                                                                           self.year
                                                                           )

    def __repr__(self):
        return 'Book("{}", "{}", {}, "{}")'.format(self.author,
                                                   self.name,
                                                   self.year,
                                                   self.genre
                                                   )

    def __eq__(self, other):
        return (self.author == other.author and
                self.name == other.name and
                self.year == other.year and
                self.genre == other.genre
                )
