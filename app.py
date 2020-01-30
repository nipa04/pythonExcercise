import datetime
from collections import OrderedDict


class Dish:
    def __init__(self, name, datetime, origin, ingredient):
        self.name = name
        self.datetime = datetime
        self.origin = origin
        self.ingredient = ingredient


class Ingredient:
    def __init__(self, ingredientName, foodValue):
        self.ingredientName = ingredientName
        self.foodValue = foodValue


class FoodValue:
    def __init__(self, calories, fat, carb, protein):
        self.calories = calories
        self.fat = fat
        self.carb = carb
        self.protein = protein


chili_fv = FoodValue(10, 0, 2, 0)
tomato_fv = FoodValue(10, 0, 2, 0)
rice_fv = FoodValue(60, 0, 40, 0)
egg_fv = FoodValue(40, 0, 15, 8)


chili = Ingredient("chili", chili_fv)
tomato = Ingredient("tomato", tomato_fv)
rice = Ingredient("rice", rice_fv)
egg = Ingredient("egg", egg_fv)

d1 = Dish("Pasta", "1-Jan-2019", "Italian", [chili, egg])
d2 = Dish("Soup", "4-Feb-2019", "Thai", [egg, tomato])
d3 = Dish("Pizza", "21-Mar-2019", "Italian", [tomato, egg])
d4 = Dish("Fried rice", "14-Apr-2019", "Indian", [rice, egg])


class DishRecord:
    def __init__(self):
        self.dishDict = {}

    def add(self, dish):
        self.dishDict[dish.name] = dish

    def delete(self, dish):
        try:
            del(self.dishDict[dish.name])
        except:
            print("Dish not found!")

    def showAll(self):
        for key, dish in self.dishDict.items():
            print(dish.name)

    def totalDish(self):
        return len(self.dishDict)

    def checkDish(self, dish):
        if dish.name in self.dishDict:
            return True
        else:
            return False

    def sortDish(self):
        # sorted_x = sorted(x.items(), key=lambda kv: kv[1])
        sorted_dishDict = sorted(
            self.dishDict.items(), key=lambda kv: kv[1].name)
        return sorted_dishDict

        # sorted_dishDict = sorted(
        #     self.dishDict.items(), key=lambda kv: datetime.datetime.strptime(kv[1].datetime, "%d-%b-%y"))
        # return sorted_dishDict

        # s = OrderedDict(sorted(self.dishDict.items(),
        #                        key=lambda dish: dish[1].datetime))
        # return s


dr = DishRecord()
dr.add(d1)
dr.add(d2)
dr.add(d3)
dr.add(d4)

# dr.showAll()

dr.showAll()
print(dr.totalDish())
print(dr.checkDish(d4))
sortData = dr.sortDish()
for k, dish in sortData:
    print(dish.datetime)
