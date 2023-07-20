class Sun:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(Sun, cls).__new__(cls)
        return cls._instance

    @classmethod
    def inst(cls):
        return cls()

p = Sun.inst()
f = Sun.inst()
print(p is f)