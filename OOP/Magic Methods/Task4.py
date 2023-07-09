"""
You must implement the class Book with the attributes price, author, and name.

The author and name fields have to be immutable;
The price field may have changes but has to be in the 0 <= price <= 100 range.
If a user tries to change the author or name fields after an initialization or set price is out of range, the ValueError should be raised.

Implement descriptors PriceControl and NameControl to validate parameters.

Example
>>> b = Book("William Faulkner", "The Sound and the Fury", 12)
>>> print(f"Author='{b.author}', Name='{b.name}', Price='{b.price}'")
Author='William Faulkner', Name='The Sound and the Fury', Price='12'

>>> b.price = 55
>>> b.price
55
>>> b.price = -12  # => ValueError: Price must be between 0 and 100.
>>> b.price = 101  # => ValueError: Price must be between 0 and 100.

>>> b.author = "new author"  # => ValueError: Author can not be changed.
>>> b.name = "new name"      # => ValueError: Name can not be changed.
"""
