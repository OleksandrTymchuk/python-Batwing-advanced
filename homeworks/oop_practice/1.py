import random
from abc import ABC, abstractmethod


class Person(ABC):
    def __init__(self, name, age, money, home):
        self.name = name
        self.age = age
        self.money = money
        self.home = home

    @abstractmethod
    def info(self):
        pass

    @abstractmethod
    def make_money(self):
        pass

    @abstractmethod
    def buy_house(self, house):
        pass


class Human(Person, ABC):
    def __init__(self, name, age, money, home):
        super().__init__(name, age, money, home)

    def info(self):
        print(f'Hello, my name is {self.name}, im {self.age} years old')

    def make_money(self):
        self.money = self.money + 10000
        print(f'Hooray, I got paid, so now my wealth = {self.money} ')

    def buy_house(self, house):
        if self.money >= house.cost:
            print('You can buy this house')
        else:

            print("Go to work, you don't have enough money")


class House:
    def __init__(self, area, cost):
        self.area = area
        self.cost = cost

    def house_info(self):
        print(f'House characteristics: area = {self.area}, cost = {self.cost}$ ')


class SmallHouse(House):
    def __init__(self, area, cost):
        super().__init__(area, cost)
        if self.area >= 40:
            self.__class__ = House
        else:
            pass


class Realtor:
    def __init__(self, name, houses, discount):
        self.name = name
        self.houses = houses
        self.discount = discount

    def provide_info(self):
        for i in self.houses:
            i.house_info()

    def steal_money(self, human):
        if random.randint(1, 10) == 10:
            human.money = 0
            print(f'Ups, realtor {self.name} stole my money')
        else:
            print('I am so lucky today!')

    def realtor_discount(self):
        print(f'Hello, my name is {self.name}, I am your realtor and'
              f' I wanna give you a {realtor.discount} purchase discount')


human = Human('Alex', 21, 100, False)
human.info()
human.make_money()
house1 = House(41, 15000)
house2 = House(30, 11000)
house3 = House(15, 5000)
human.buy_house(house1)
human.buy_house(house2)
human.buy_house(house3)
realtor = Realtor('Alice', [house1, house2, house3], '15%')
realtor.provide_info()
realtor.realtor_discount()
realtor.steal_money(human)

