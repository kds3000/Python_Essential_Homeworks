"""
Создайте программу, которая эмулирует работу сервиса по сокращению ссылок. Должна быть реализована возможность ввода
изначальной ссылки и короткого названия и получения изначальной ссылки по её названию.
"""
import string
import random

DOMAIN_NAME = 'http://www.linkshorter.com/'


class FullAndShortLinks:
    def __init__(self, links={},chars_count=6):
        # stores full and short links
        self._links = links
        # number of chars in short link
        self._chars_count = chars_count
        # possible chars
        self._chars = string.ascii_letters + string.digits

    def generate_short_link(self):
        short_link = None
        while short_link is None:
            short_link = ''.join(random.choice(self._chars) for _ in range(self._chars_count))
            if short_link in self._links:
                short_link = None
        return short_link

    def add_links(self):
        full_link = input('Enter a link you need to shorten: \n')
        manual_input = None
        while manual_input is None:
            manual_input = input('Do you want to enter short link name manually? Type Y or N: \n')

            if manual_input in 'yY':
                short_link = input('Enter short name for your link ({} ASCII letters or '
                                   'digits): \n'.format(self._chars_count))
                if short_link in self._links:
                    manual_input = None
                    print('Entered link name is already reserved\n')
                for char in short_link:
                    if char not in self._chars:
                        print('Incorrect input\n')
                        manual_input = None

            elif manual_input in 'nN':
                short_link = self.generate_short_link()
            else:
                print('Incorrect input\n')
                manual_input = None
        self._links[short_link] = full_link
        return short_link + '\n'

    def get_full_link(self):
        short_link = input('Enter short name\n')
        try:
            return self._links[short_link]
        except KeyError:
            print('There is no link bounded to that short name\n')


def main():
    links = FullAndShortLinks()
    input_ = None
    while input_ != 'exit':
        input_ = input('Welcome to the Link Shorter!\n'
                       'If you want to shorten a link, type "shorten".\n'
                       'If you want to get full link, using your short link, type "get".\n'
                       'If you want to quit, type "exit"\n')
        if input_ == 'shorten':
            print(links.add_links())
        elif input_ == 'get':
            print(links.get_full_link())


if __name__ == '__main__':
    main()


