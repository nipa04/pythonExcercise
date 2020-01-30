class Dish:
    def __init__(self, name, description):
        self.name = name
        self.description = description


class DishRecord:
    def __init__(self):
        self.dishMap = {}

    def add(self, key, value):
        if key not in self.dishMap:
            self.dishMap[key] = value
        else:
            print("Dish is already exist")

    def delete(self, key):
        if key in self.dishMap:
            del self.dishMap[key]
        else:
            print("Dish doesn't exist")

    def showALL(self):
        for k, dish in self.dishMap.items():
            print(dish.name)

    def totalDish(self):
        return (len(self.dishMap))

    def sortDish(self):
        # sorted_x = sorted(x.items(), key=lambda kv: kv[1])
        s = sorted(self.dishMap.items(), key=lambda dish: dish[1].name)
        return s

    def checkDish(self, key):
        if key in self.dishMap:
            return True
        else:
            return False

    def checkDishByName(self, key):
        if key in self.dishMap:
            return self.dishMap[key].description


d1 = Dish("pasta", "pasta is good")
d2 = Dish("pizza", "pizza is yummy")
d3 = Dish("soup", "soup is healthy")
d4 = Dish("fried rice", "popular dish")

dr = DishRecord()
dr.add(d1.name, d1)
dr.add(d2.name, d2)
dr.add(d3.name, d3)
dr.add(d4.name, d4)

dr.showALL()

print()

sortData = dr.sortDish()
for item in sortData:
    print(item)

# print(dr.checkDish(d))

print(dr.checkDishByName("soup"))
