# Задание 1

class Auto:
    def __init__(self, brand, weight, age, color='Black', mark=''):
        self.brand = brand
        self.weight = weight
        self.age = age
        self.color = color
        self.mark = mark

    def move(self):
        print('Move')
    
    def birthday(self):
        self.age+=1
    
    def stop(self):
        print('Stop')

car = Auto('BMW', 1800, 6)
car.move()
car.birthday()
car.stop()
print(car.age)
print(car.color)



# Задание 2
import time

class Truck(Auto):
    def __init__(self, brand, weight, age, max_load, color='Black'):
        self.max_load = max_load
        super().__init__(brand, weight, age, color)

    def move(self):
        print('Attention')
        super().move()
    
    def load(self):
        time.sleep(1)
        print(f'load {self.max_load}')
        time.sleep(1)


class Car(Auto):
    def __init__(self, brand, weight, age, max_speed, color='Black', mark=''):
        self.max_speed = max_speed
        super().__init__(brand, weight, age, color, mark)

    def move(self):
        super().move()
        print(f'Max speed is {self.max_speed}')

t_car = Truck('Volvo', 3000, 2, 15000)
t_car.move()
t_car.load()
print(t_car.color)
print(t_car.brand)
print(t_car.weight)
print(t_car.age)
l_car = Car('Mazda', 1500, 11, 214)
l_car.move()
print(l_car.color)
print(l_car.brand)
print(l_car.weight)
print(l_car.age)



# Задание 3

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def squar(self):
        return 3.14 * self.radius ** 2
    
    def __sub__(self, other):
        new_r = abs(self.radius - other.radius)
        if new_r == 0:
            return Point(0, 0)
        return new_r



class Point:
    def __init__(self, a, b) -> None:
        self.a = a
        self.b = b

    
first_c = Circle(20)
sec_c = Circle(5)
print(first_c - sec_c)