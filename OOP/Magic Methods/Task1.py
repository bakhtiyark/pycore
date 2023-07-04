from typing import List


class Counter:
    def __init__(self, values: List[int]):
        self.values = values
    def __add__(self, addition):
        result = []
        for i in self.values:
            result.append(str(i) +" " + addition)
        return result

objet = Counter([1,2,3]) + "Real mofo"
print(objet)
kk = Counter([1,2])
print(Counter)
print(kk)