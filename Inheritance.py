'''
Создайте иерархию классов транспортных средств. В общем классе опишите общие для всех транспортных средств поля,
в наследниках – специфичные для них. Создайте несколько экземпляров.
Выведите информацию о каждом транспортном средстве.
'''


class Transport:
    material = 'metal'
    number_of_features = 0
    feature_type = 'nothing'
    engine_type = 'no'
    movement_type = 'Not defined'

    def __str__(self):
        return 'It`s a {} made of {}, with {} {} and {} engine. And it is {}!'.format(
                                                                                    self.__class__.__name__,
                                                                                    self.material,
                                                                                    self.number_of_features,
                                                                                    self.feature_type,
                                                                                    self.engine_type,
                                                                                    self.movement_type
                                                                                    )


class Car(Transport):
    movement_type = 'riding'
    engine_type = 'combustion'
    number_of_features = 4
    feature_type = 'wheels'


class Plane(Transport):
    movement_type = 'flying'
    number_of_features = 2
    engine_type = 'jet'
    feature_type = 'wings'


class ToyCar(Car):
    material = 'plastic'
    engine_type = 'fake'


if __name__ == "__main__":

    car, plane, toycar = Car(), Plane(), ToyCar()
    print(car, plane, toycar, sep='\n')
