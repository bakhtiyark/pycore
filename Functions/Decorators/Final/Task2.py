from typing import List

def split_by_index(s: str, indexes: List[int]) -> List[str]:
    result = []
    start = 0

    for index in indexes:
        if index >= 0 and index < len(s):
            result.append(s[start:index])
            start = index
    result.append(s[start:])

    return result

print(split_by_index("pythoniscool,isn'tit?", [6, 8, 12, 13, 18]))
print(split_by_index("no luck", [42]))