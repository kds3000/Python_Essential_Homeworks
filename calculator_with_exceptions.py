'''
Напишите программу-калькулятор, которая поддерживает следующие операции: сложение, вычитание, умножение, деление и
возведение в степень. Программа должна выдавать сообщения об ошибке и продолжать работу при вводе некорректных данных,
делении на ноль и возведении нуля в отрицательную степень.
'''


def calc():
    correct_operations = ('+', '-', '*', '/', '**')
    while True:
        x = input('It`s a calculator. Press Enter to continue, type "exit" to quit: ')
        if x == 'exit':
            break
        while True:
            try:
                a = int_check('Enter first number: ')
                operation = operation_check(
                                            'Enter an operation {}: '.format(correct_operations),
                                            correct_operations
                                            )
                b = int_check('Enter second number: ')
                calc_and_print_result(operation, a, b)
                break
            except (ZeroDivisionError, ValueError, AssertionError) as error:
                print(error)
                print('Enter values again')
            finally:
                print()


def int_check(message):
    """
    Функция, вызывающая ValueError, если введеное значение не является действительным числом
    :param message:     Сообщение для пользователя
    :return:            Введенное значение
    :raises ValueError: Вызывает ValueError, если введеное значение не является действительным числом
    """
    try:
        value = float(input(message))
        return value
    except ValueError:
        raise ValueError('Entered value isn`t a real number')


def operation_check(message, correct_operations):
    """
    Функция, вызывающая AssertionError, если введеное значение не является корректной математической операцией
    :param message:             Сообщение для пользователя
    :param correct_operations:  Кортеж из допустимых математических операций
    :return:                    Введенное значение
    :raises AssertionError:     Вызывает AssertionError, если введеное операция не в числе допустимых
    """
    operation = input(message)
    assert operation in correct_operations, 'Incorrect operation'
    return operation


def calc_and_print_result(operation, a, b):
    if operation == '+':
        print('The result of adding {} and {} is {}'.format(a, b, a + b))
    elif operation == '-':
        print('Subtraction result of {} and {} is {}'.format(a, b, a - b))
    elif operation == '*':
        print('The result of multiplying {} and {} is {}'.format(a, b, a * b))
    elif operation == '/':
        print('The result of dividing {} by {} is {}'.format(a, b, a / b))
    elif operation == '**':
        print('The result of raising {} to the {} power is {}'.format(a, b, a ** b))


if __name__ == '__main__':
    calc()
