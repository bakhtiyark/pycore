"""
Develop a class Field with "full encapsulation" whose attributes are accessed, 
and data changes are implemented through method calls.
In OOP, it is generally accepted to start the names of the methods for extracting data
with the word "get" and the names of the methods in which fields are equated to a certain value - "set".
In this task, you must implement get_value and set_value methods for the Field class (__value property)."""

class Field:
    __value = None
    def __init__(self):
        self.__value = None

    def get_value(self):
        return self.__value
    
    def set_value(self, value):
        self.__value = value


kk = Field()

print(kk.get_value())
kk.set_value("kkk")
print(kk.get_value())