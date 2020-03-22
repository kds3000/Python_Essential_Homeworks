'''
Создайте класс, описывающий отзыв к книге. Добавьте в класс книги поле – список отзывов.
Сделайте так, что при выводе книги на экран при помощи функции print также будут выводиться отзывы к ней.
'''


class Book:

    def __init__(self, author, name, year, genre):
        self.author = author
        self.name = name
        self.year = year
        self.genre = genre
        self.reviews_list = []

    def __str__(self):

        reviews_as_string = ''
        for i in self.reviews_list:
            reviews_as_string += str(i) + '; \n'

        return 'That`s a book "{}" in {} genre written by {} in {}. ' \
               '\nBook has reviews:\n{}'.format(self.name,
                                                self.genre,
                                                self.author,
                                                self.year,
                                                reviews_as_string
                                                )

    def add_review(self, review):
        self.reviews_list.append(review)


class BookReview:
    def __init__(self, author, text):
        self.author = author
        self.text = text

    def __str__(self):
        return '{}. That review has written by {}'.format(self.text,
                                                          self.author
                                                          )


