from typing import Any


class Human:
    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print(f"hello my name is {self.name}")


class Player(Human):
    def __init__(self, name, xp):
        super().__init__(name)
        self.xp = xp


class Fan(Human):
    def __init__(self, name, fav_team):
        super().__init__(name)
        self.fav_team = fav_team


shinbi = Player("shinbi", 100)
shinbi_fan = Fan("shinbi_fan", "goodteam")
shinbi.say_hello()
shinbi_fan.say_hello()
print(shinbi.name, shinbi.xp)
print(shinbi_fan.name, shinbi_fan.fav_team)


class Dog:
    def __init__(self, name):
        self.name = name

    def woof(self):
        print("woof woof")


class Jindo(Dog):
    def wal(self):
        super().woof()
        print("wal wal")

    def __str__(self):
        print(super().__str__())
        return f"Dog : {self.name}"


class Beagle(Dog):
    def jump(self):
        print("super woof")

    def woof(self):
        print("hahahaha")


dog = Beagle("Beagle")
dog.jump()
dog.woof()
dog = Jindo("Jindo")
dog.wal()
dog.woof()
print(dog)
