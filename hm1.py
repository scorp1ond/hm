class Animal:
    def __init__(self, name, species, legs):
        self.name = name
        self.species = species
        self.legs = legs

    def voice(self):
        return "The {} {} makes a sound.".format(self.species, self.name)

    def move(self):
        return "The {} {} moves.".format(self.species, self.name)


class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name, "dog", 4)
        self.breed = breed

    def bark(self):
        return "The {} {} barks.".format(self.species, self.name)

    def fly(self):
        return "The {} {} cannot fly.".format(self.species, self.name)


class Bird(Animal):
    def __init__(self, name, wingspan):
        super().__init__(name, "bird", 2)  # Птах завжди має 2 ноги
        self.wingspan = wingspan

    def fly(self):
        return "The {} {} flies with a wingspan of {} meters.".format(self.species, self.name, self.wingspan)

    def bark(self):
        return "The {} {} cannot bark.".format(self.species, self.name)



my_dog = Dog("Buddy", "Golden Retriever")
my_bird = Bird("Robin", 0.3)


print(my_dog.voice())
print(my_dog.move())
print(my_dog.bark())
print(my_dog.fly())

print(my_bird.voice())
print(my_bird.move())
print(my_bird.fly())
print(my_bird.bark())