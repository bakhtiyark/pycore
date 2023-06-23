class HistoryDict:
    def __init__(self, dict) -> None:
        self.dict = dict
        self.history = []
    def getDict(self):
        return self.dict
    def set_value(self,key,value):
        self.dict.clear()
        self.dict[key]=value
        if (len(self.history)<5):
            self.history.append(key)
        else:
            self.history.pop(0)
            self.history.append(key)
    def get_history(self):
        return self.history

kkk = HistoryDict({"foo": 42})

print(kkk.getDict())
kkk.set_value("bar",1)
print(kkk.getDict())
kkk.set_value("Donkey",2)
print(kkk.getDict())
kkk.set_value("Kong",3)
print(kkk.getDict())
kkk.set_value("Dr Who",4)
print(kkk.getDict())
kkk.set_value("Saddam",5)
print(kkk.getDict())
kkk.set_value("Hussein",6)

print(kkk.get_history())