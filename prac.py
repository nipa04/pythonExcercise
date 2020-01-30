class Dish:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class DishRecord:
    def __init__(self):
        self.dishMap = {}

    def add(self, key, dish):

        self.dishMap[key] = dish

    def delete(self, key):
        if key in self.dishMap:
            del self.dishMap[key]

        else:
            print("Dish not found")

    def showAll(self):
        for k, v in self.dishMap.items():
            print(v.name)

    def sortDish(self):
        s = sorted(self.dishMap.items(), key=lambda dish: dish[1].name)
        return s
        #  s = sorted(self.dishMap.items(), key=lambda dish: dish[1].name)

    def checkDish(self, key):
        if key in self.dishMap:
            return self.dishMap[key].description
        return ("dish not found")
        # for k, v in self.dishMap.items():
        #     if v.name == name:
        #         return v.description
        # return ("dish not found")


d1 = Dish("pasta", "heloo")
d2 = Dish("calamary", "belllo")

dr = DishRecord()
dr.add(d1.name, d1)
dr.add(d2.name, d2)
dr.showAll()


sortData = dr.sortDish()
for item in sortData:
    print(item[1].name)

print(dr.checkDish("calamary"))
