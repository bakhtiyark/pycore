"""Functions. Decorators. Decorators. Final Task 1.
Implement a function that works the same as the str.split method (without using str.split itself, of course).

Example:

   
        
"""
def split(data: str, sep=None, maxsplit=-1):
    part = ""
    result = []
    for i in data:
        if i != sep:
            part += i
        elif part != "":
            result.append(part)
        
    return(result)
    

print(split("I am a motherfucker"," "))
print(split(",123,",","))
print(split(""))