'''
Задание
Создайте класс, описывающий автомобиль. Создайте класс автосалона, содержащий в себе список автомобилей,
доступных для продажи, и функцию продажи заданного автомобиля.
'''


class Car:
    wheel_count = 4

    def __init__(self, model, color, weight, price):
        self.model = model
        self.color = color
        self.weight = weight
        self.price = price


class ShowRoom:
    def __init__(self):
        self.cars = []
        self.cash_amount = 0

    def sell_car(self, model):

        for number in range(len(self.cars)):
            if self.cars[number].model == model:
                self.cash_amount += self.cars[number].price
                print("%s sold for %d. Now showroom has %d dollars." % (model,
                                                                        self.cars[number].price,
                                                                        self.cash_amount
                                                                        )
                      )
                self.cars.pop(number)
                return

        print("There is no %s in our showroom!" % model)

    def get_car(self, car):
        self.cars.append(car)
        print("%s added to the showroom" % car.model)
