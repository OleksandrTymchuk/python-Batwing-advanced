#  1_____________________________________________

class Animal:
    def __init__(self, name, eat, sleep):
        self.name = name
        self.eat = eat
        self.sleep = sleep

    def get_animal_name(self):
        print(f'Animal name is: {self.name}')

    def get_type_of_food(self):
        print(f'Type of food is - {self.eat}')

    def get_time_of_sleep(self):
        print(f'Time of sleeping = {self.sleep}')


class Turtle(Animal):
    def __init__(self, name, eat, sleep):
        super().__init__(name, eat, sleep)

    def voice_command(self):
        print('Im so fast, Im - Flash!')

    def turtle_flif(self):
        print('Are u crazy? I will not do it!')


Michelangelo = Turtle('Michelangelo', 'Pizza', '23')
Michelangelo.get_animal_name()
Michelangelo.get_type_of_food()
Michelangelo.get_time_of_sleep()
Michelangelo.voice_command()
Michelangelo.turtle_flif()
print(issubclass(Turtle, Animal))


class Dog(Animal):
    def __init__(self, name, eat, sleep):
        super().__init__(name, eat, sleep)

    def voice_command(self):
        print('Gav Gav Gav')

    def fake_own_death(self):
        print('No gav')


patron = Dog('Patron', 'Meat', '10')
patron.get_animal_name()
patron.get_type_of_food()
patron.get_time_of_sleep()
patron.voice_command()
patron.fake_own_death()
print(issubclass(Dog, Animal))


class Cat(Animal):
    def __init__(self, name, eat, sleep):
        super().__init__(name, eat, sleep)

    def voice_command(self):
        print('Meow, Meow, Meow')

    def hunt_mice(self):
        print('Are u seriusly? Im domestic cat!')


turbik = Cat('Turbik', 'Whiskas', '15')
turbik.get_animal_name()
turbik.get_type_of_food()
turbik.get_time_of_sleep()
turbik.voice_command()
turbik.hunt_mice()
print(issubclass(Cat, Animal))


class Pig(Animal):
    def __init__(self, name, eat, sleep):
        super().__init__(name, eat, sleep)

    def voice_command(self):
        print('Oink, Oink, Oink')

    def find_swamp(self):
        print('Im going to search a swamp')


pepa = Pig('Pepa', 'Beet', '5')
pepa.get_animal_name()
pepa.get_type_of_food()
pepa.get_time_of_sleep()
pepa.voice_command()
pepa.find_swamp()
print(issubclass(Pig, Animal))


class Parrot(Animal):
    def __init__(self, name, eat, sleep):
        super().__init__(name, eat, sleep)

    def voice_command(self):
        print('Slava Ukraini')


gosha = Parrot('Gosha', 'Apples', '10')
gosha.get_animal_name()
gosha.get_type_of_food()
gosha.get_time_of_sleep()
gosha.voice_command()
print(issubclass(Parrot, Animal))


#  1.a____________________________________________
class Human:
    def __init__(self, eat, sleep, study, work):
        self.eat = eat
        self.sleep = sleep
        self.study = study
        self.work = work

    def print_human_info(self):
        print(f'Im eating {self.eat}, sleeping {self.sleep} hours,'
              f' study at {self.study} and working in the {self.work}')


class Centaur(Animal, Human):
    def __init__(self, name, eat, sleep, study, work, wife_name):
        Animal.__init__(self, name, eat, sleep)
        Human.__init__(self, eat, sleep, study, work)
        self.wife_name = wife_name

    def print_centaur_info(self):
        print(f'My name is: {self.name}, Im eating {self.eat},'
              f' sleeping {self.sleep} hours,'f' study at {self.study}, '
              f'working in the {self.work} and my wife name is {self.wife_name}')


firenze = Centaur('Firenze', 'Mushrooms', '10', 'school', 'forest', 'Elizabeth')
firenze.print_centaur_info()
