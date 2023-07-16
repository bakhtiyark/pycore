class PriceControl:
    """
    Descriptor which don't allow to set price
    less than 0 and more than 100 included.
    """
    pass


class NameControl:
    """
    Descriptor which don't allow to change field value after initialization.
    """
    pass


class Book:
    author = NameControl()
    name = NameControl()
    price = PriceControl()
