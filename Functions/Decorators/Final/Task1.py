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

print(split(' adf 5 7'))
print(split(' adf 5 7',maxsplit=1))