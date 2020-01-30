class Dish:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class DishRecord:
    def __init__(self):
        self.dishList = []

    def add(self, dish):
        self.dishList.append(dish)

    def showAll(self):
        for dish in self.dishList:
            print(dish.name)

    def uniqueDish(self):
        u = set(self.dishList)
        for item in u:
            print(item.name)

        # uniqueDish = []
        # for dish in self.dishList:
        #     if dish not in uniqueDish:
        #         uniqueDish.append(dish)
        # for dish in uniqueDish:
        #     print(dish.name)


d1 = Dish("pizza", "Yummy pizza")
d2 = Dish("soup", "soup is healthy")
dr = DishRecord()
dr.add(d1)
dr.add(d1)
dr.add(d1)
dr.add(d1)
dr.add(d1)
dr.add(d2)

# dr.showAll()

dr.uniqueDish()

s1 = set([1, 2, 3, 4])
s2 = set([2, 3, 6, 7])
sU = s1.union(s2)
sI = s1.intersection(s2)
print(sU)
print(sI)
