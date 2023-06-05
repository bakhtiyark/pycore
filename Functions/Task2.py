def union(*args) -> set:
    result = set()
    for i in range(len(args)):
        for k in args[i]:
            result.add(k)
    return result
            
print(union(('S', 'A', 'M'), ['S', 'P', 'A', 'C']))

def intersect(*args) -> set:
    result = set()
    if len(args) == 1:
        return set(args)
    else:
        for i in range(len(args)):
            for k in range(1, len(args)):
                result = set(args[i]).intersection(set(args[k]))
            return result

print(intersect(('S', 'A', 'C'), ('P', 'C', 'S'), ('G', 'H', 'S', 'C')))
print(intersect(('S', 'A'), ('P', 'C'), ('G', 'H')))
print(intersect(['S', 'A', 'M'], ['S', 'P', 'A', 'M', 'C']))