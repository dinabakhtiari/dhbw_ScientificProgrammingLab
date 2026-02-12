class Person:
    def __init__(self, name, age, height):
        self.name = name
        self.age = age
        self.height = height

    def birthday(self):
        self.age += 1
        print("Happy Birthday, Will! You are now " + str(self.age) + " years old.")

will = Person("Will", 19, 189)
will.birthday()

will.birthday()