class Bird:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return f"{self.name} bird can walk"
    def fly(self):
        return f"{self.name} bird can fly"
    def __str__(self):
        return f"{self.name} bird can fly"


class FlyingBird(Bird):
    def __init__(self, name, ration="grains"):
        super().__init__(name)
        self.ration = ration

    def eat(self):
        return f"It mostly eats {self.ration}"


class NonFlyingBird(FlyingBird):
    def __init__(self, name, ration="grains"):
        super().__init__(name)
        self.ration = ration
    def fly(self):
        raise AttributeError

    def swim(self):
        return f"{self.name} bird can swim"

class SuperBird(NonFlyingBird):
    def __init__(self, name, ration="grains"):
        super().__init__(name)
        self.ration = ration



tit = Bird("Great Tit")
robin = FlyingBird("Robin")
penguin = NonFlyingBird("Penguin")
cthulhu = SuperBird("Cthulhu")
print(robin.eat())
print(penguin.fly())