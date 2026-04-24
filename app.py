class Car:
    def __init__(self, model):
        self.model = model

    def __str__(self):
        return self.model


class Garage:
    def __init__(self):
        self.cars = []

    def add_car(self, car):
        self.cars.append(car)

    def show_cars(self):
        for car in self.cars:
            print(car)


# Test
g = Garage()
g.add_car(Car("BMW"))
g.add_car(Car("Tesla"))

g.show_cars()
