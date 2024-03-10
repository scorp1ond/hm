class Animal:
    def __init__(self, species):
        self.species = species

    def make_sound(self):
        pass

    def move(self):
        pass


class Mammal(Animal):
    def __init__(self, species, num_legs):
        super().__init__(species)
        self.num_legs = num_legs

    def give_birth(self):
        pass


class Dog(Mammal):
    def __init__(self, breed, name):
        super().__init__("Canine", 4)
        self.breed = breed
        self.name = name

    def make_sound(self):
        pass