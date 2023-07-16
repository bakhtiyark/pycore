class Currency:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"{self.value} {self.currency_name()}"

    @classmethod
    def course(cls, to_currency):
        if cls == to_currency:
            return f"1 {cls.currency_name()} for 1 {cls.currency_name()}"
        else:
            return f"{cls.exchange_rate(to_currency)} {to_currency.currency_name()} for 1 {cls.currency_name()}"

    @classmethod
    def exchange_rate(cls, to_currency):
        if cls == to_currency:
            return 1.0
        elif cls == Euro:
            return to_currency.exchange_rate_to_euro()
        elif cls == Dollar:
            return to_currency.exchange_rate_to_dollar()
        elif cls == Pound:
            return to_currency.exchange_rate_to_pound()

    def to_currency(self, to_currency):
        if self.__class__ == to_currency:
            return self
        else:
            converted_value = self.value * self.exchange_rate(to_currency)
            return to_currency(converted_value)

    def __add__(self, other):
        if self.__class__ == other.__class__:
            return self.__class__(self.value + other.value)
        else:
            converted_value = self.value + other.value * self.exchange_rate(other.__class__)
            return self.__class__(converted_value)

    def __sub__(self, other):
        if self.__class__ == other.__class__:
            return self.__class__(self.value - other.value)
        else:
            converted_value = self.value - other.value * self.exchange_rate(other.__class__)
            return self.__class__(converted_value)

    def __lt__(self, other):
        if self.__class__ == other.__class__:
            return self.value < other.value
        else:
            converted_value = other.value * self.exchange_rate(other.__class__)
            return self.value < converted_value

    def __gt__(self, other):
        if self.__class__ == other.__class__:
            return self.value > other.value
        else:
            converted_value = other.value * self.exchange_rate(other.__class__)
            return self.value > converted_value

    def __eq__(self, other):
        if self.__class__ == other.__class__:
            return self.value == other.value
        else:
            converted_value = other.value * self.exchange_rate(other.__class__)
            return self.value == converted_value

    @staticmethod
    def currency_name():
        raise NotImplementedError("currency_name() method must be implemented in the derived class.")


class Euro(Currency):
    @staticmethod
    def exchange_rate_to_dollar():
        return 2.0

    @staticmethod
    def exchange_rate_to_pound():
        return 100.0

    @staticmethod
    def exchange_rate_to_euro():
        return 1.0

    @staticmethod
    def currency_name():
        return "EUR"


class Dollar(Currency):
    @staticmethod
    def exchange_rate_to_euro():
        return 0.5

    @staticmethod
    def exchange_rate_to_pound():
        return 50.0

    @staticmethod
    def exchange_rate_to_dollar():
        return 1.0

    @staticmethod
    def currency_name():
        return "USD"


class Pound(Currency):
    @staticmethod
    def exchange_rate_to_euro():
        return 0.01

    @staticmethod
    def exchange_rate_to_dollar():
        return 0.02

    @staticmethod
    def exchange_rate_to_pound():
        return 1.0

    @staticmethod
    def currency_name():
        return "GBP"


# Example usage
e = Euro(100)
r = Pound(100)
d = Dollar(200)

print(f"Euro.course(Pound)   ==> {Euro.course(Pound)}")
print(f"Dollar.course(Pound) ==> {Dollar.course(Pound)}")
print(f"Pound.course(Euro)   ==> {Pound.course(Euro)}")
print(f"Pound.course(Euro)   ==> {Pound.course(Dollar)}")

print(f"e = {e}")
print(f"e.to_currency(Dollar) = {e.to_currency(Dollar)}")
print(f"e.to_currency(Pound) = {e.to_currency(Pound)}")
print(f"e.to_currency(Euro)   = {e.to_currency(Euro)}")

print(f"r = {r}")
print(f"r.to_currency(Dollar) = {r.to_currency(Dollar)}")
print(f"r.to_currency(Euro)   = {r.to_currency(Euro)}")
print(f"r.to_currency(Pound) = {r.to_currency(Pound)}")

print(f"e + r  =>  {e + r}")
print(f"r + d  =>  {r + d}")
print(f"d + e  =>  {d + e}")
