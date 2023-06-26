"""Functions. Decorators. Decorators. Final Task 1.
Implement a function that works the same as the str.split method (without using str.split itself, of course).

Example:

   
        for char in firstsentence:
    if char == " ":
        words.append(current_word)
        current_word = ""
    else:
        current_word += char
"""
def split(data: str, sep=None, maxsplit=-1):
    part = ""
    result = []
    if(len(data)==0):
        return result
    if(sep == None):
        sep=" "
    for i in data:
        if i == sep:
            result.append(part)
            part = ""
        else:
            part+=i
                
    result.append(part)
    if(maxsplit==-1):
        return(result)
    else:
        return(result[0:maxsplit+1])
    

print(split("I am a motherfucker")) #check
print(split("adf<>5","<>", maxsplit=0))
print(split(",123,",","))
print(split(",123,",","))
print(split(",123,",","))
print(split(""))
print(split(''))
print(split("adf 5 7")) #check
print(split("adf 5  7",maxsplit=1)) #check
print(split("la-la-la-la","-",maxsplit=3))