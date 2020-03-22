"""
Опишите класс сотрудника, который включает в себя такие поля, как имя, фамилия, отдел и год поступления на работу.
Конструктор должен генерировать исключение, если заданы неправильные данные. Введите список работников с клавиатуры.
Выведите всех сотрудников, которые были приняты после заданного года.
"""
DEPARTMENTS = ['sales', 'development']  # Отделы, существующие в компании
MIN_YEAR = 2003  # Год основания компании ("заданный год")


class Employee:

    def __init__(self, name, surname, department, year_of_employment):
        self.name = name
        self.surname = surname
        self.department = department
        self.year_of_employment = year_of_employment

    def __repr__(self):
        return 'Employee("{0}", "{1}", "{2}", {3})'.format(self.name,
                                                           self.surname,
                                                           self.department,
                                                           self.year_of_employment
                                                           )

    @staticmethod
    def read_employee():
        """Статический метод безопасного считывания ввода с клавиатуры данных сотрудника"""
        name = base_check('Enter name: ', not_empty_check)
        surname = base_check('Enter surname: ', not_empty_check)
        department = base_check('Enter department: ', dept_check)
        year_of_employment = base_check('Enter year of employment: ', year_check)
        return Employee(name, surname, department, year_of_employment)


def base_check(message, condition_func):
    """Функция безопасного чтения данных с клавиатуры
    :param message:        поясняющее сообщение
    :param condition_func: функция проверки корректности введенных данных
    :return:               введённое значение
    """
    while True:
        try:
            entered_data = input(message)
            condition_func(entered_data)
        except ValueError as error:
            print(error)
        else:
            return entered_data


def not_empty_check(data):
    """Функция, вызывающая исключение ValueError, если введено пустое значение"""
    if len(data) == 0:
        raise ValueError('It cannot be empty')


def dept_check(data):
    """Функция проверки отдела, вызывающая исключение ValueError, если введеный отдел не существует в компании"""
    not_empty_check(data)
    if data not in DEPARTMENTS:
        raise ValueError('Department must be one of :{}'.format(DEPARTMENTS))


def year_check(data):
    """
    Функция проверки, вызывающая исключение ValueError, если введенное значение,
    лежит за пределами промежутка времени между годом основания компании и 2019-м годом
    """
    not_empty_check(data)
    if MIN_YEAR > int(data) or int(data) > 2019:
        raise ValueError('Year value must be between {} and 2019'.format(MIN_YEAR))


def main():
    employee_count = int(input('Enter employee count: '))
    employee_list = []
    while employee_count > len(employee_list):
        employee = Employee.read_employee()
        employee_list.append(employee)
    print('Employee list:', employee_list)


if __name__ == '__main__':
    main()
