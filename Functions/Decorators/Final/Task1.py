def split(data: str, sep=None, maxsplit=-1):
    if sep is None:
        sep = " "
    
    result = []
    start = 0
    count = 0
    if bool(data) == False:
        return []
    stripped_data = data.strip()
    while maxsplit != count:
        index = stripped_data.find(sep, start)
        if index == -1:
            break
        
        result.append(stripped_data[start:index])
        start = index + len(sep)
        count += 1

    result.append(stripped_data[start:])
    return result
    

print(split("I am a motherfucker")) #expect
print(split("adf<>5","<>", maxsplit=0)) # ['adf<>5']'
print(split('adf 5')) # ['adf', '5']
print(split(' asdf 5 7', maxsplit=0)) 
print(split(' asdf 5 7', maxsplit=1))
print(split(",123,",","))
print(split("")) # expect []
print(split('', '')) # expect []
print(split(' ',","))
print(split('')) # expect []
print(split("adf 5 7", maxsplit=1)) #check
print(split('adf<>5asdf<>aasdf',"<>", maxsplit=1)) # expect 
print(split("adf 5  7",maxsplit=1)) #check
print(split("la-la-la-la","-",maxsplit=1))
print(bool(""))