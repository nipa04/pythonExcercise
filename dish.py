# stack base implementation
# queue base implementation
# dictionary base implementaion
# set base implementation


import datetime
import uuid


class Dish:

    def __init__(self, name, datetime, origin, dishIngredients):
        self.name = name
        self.datetime = datetime
        self.origin = origin
        self.dishIngredients = dishIngredients
        self.id = uuid.uuid4()


class DishIngredients:

    def __init__(self, dishIngredientName, foodValue):
        self.dishIngredientName = dishIngredientName
        self.foodValue = foodValue


class FoodValue:
    def __init__(self, calories, protein, carbohydrates, fat):
        self.calories = calories
        self.protein = protein
        self.carbohydrates = carbohydrates
        self.fat = fat


chili_fv = FoodValue(10, 0, 2, 0)
tomato_fv = FoodValue(10, 5, 6, 0)
egg_fv = FoodValue(60, 25, 10, 15)
rice_fv = FoodValue(60, 1, 35, 0)


chili = DishIngredients("chili", chili_fv)
tomato = DishIngredients("tomato", tomato_fv)
egg = DishIngredients("egg", egg_fv)
rice = DishIngredients("rice", rice_fv)


d1 = Dish("Pasta", "1-Jan-2019", "Italian", [chili, tomato])
d2 = Dish("Soup", "5-Feb-2019", "Thai", [egg, tomato])
d3 = Dish("Pizza", "10-Mar-2019", "Italian", [tomato, chili])
d4 = Dish("Fried rice", "25-Apr-2019", "Indian", [rice, egg])


class DishRecord:
    def __init__(self):
        self.dishlist = []

    def add(self, dish):
        self.dishlist.append(dish)

    def delete(self, dish):
        try:
            self.dishlist.remove(dish)
        except:
            print("dish not in list")

    def showAll(self):
        for item in self.dishlist:
            print(item.name)

    def totalDish(self):
        return (len(self.dishlist))

    def checkDish(self, dish):
        for item in self.dishlist:
            if item.name in dish.name:
                return True
        return False

    def sortList(self):

        s = sorted(self.dishlist, reverse=True,
                   key=lambda dish: dish.datetime)
        return s


dr = DishRecord()

dr.add(d1)
dr.add(d2)
dr.add(d3)
dr.add(d4)

dr.showAll()
print(dr.totalDish())

print(dr.checkDish(d1))

sortData = dr.sortList()
for item in sortData:
    print(item.name, item.datetime)
    # print("The dish name {} was created on {} and the origin is {} and {}".format(
    #     item.name, item.datetime, item.origin, item.id))
    print(f("{item.name}, {item.datetime}, {item.id}"))
