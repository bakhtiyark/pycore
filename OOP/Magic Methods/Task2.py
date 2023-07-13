class Bird:
    def __init__(self, name):
        self.name = name

    def walk(self):
        return f"{self.name} bird can walk"

    def __str__(self):
        return f"{self.name} bird can walk"


class FlyingBird(Bird):
    def __init__(self, name, ration="grains"):
        super().__init__(name)
        self.ration = ration
    
    def fly(self):
        return f"{self.name} bird can fly"

    def eat(self):
        return f"It eats mostly {self.ration}"

    def __str__(self):
        return f"{self.name} bird can walk and fly"


class NonFlyingBird(Bird):
    def __init__(self, name, ration="grains"):
        super().__init__(name)
        self.ration = ration

    def swim(self):
        return f"{self.name} bird can swim"

    def eat(self):
        return f"It eats mostly {self.ration}"

    def __str__(self):
        return f"{self.name} bird can walk and swim"


class SuperBird(NonFlyingBird, FlyingBird):
    def __init__(self, name, ration="fish"):
        super().__init__(name)
        self.ration = ration

    def swim(self):
        return f"{self.name} bird can swim"

    def __str__(self):
        return f"{self.name} bird can walk, swim and fly"

tit = Bird("Great Tit")
robin = FlyingBird("Robin")
penguin = NonFlyingBird("Penguin")
cthulhu = SuperBird("Cthulhu")