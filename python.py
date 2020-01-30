# dish app
# should add ,delete and showlist
# Meal should have a property date which indicate when that meal created.
# Meal record system should have a system which return total number of
# meal added in the record.
# 26
# Add a functionality in Meal record system which return boolean to check if
# a meal exist in the system or not.


# Add functionality in your Dish record so that it return all dish in sorted way
# based on most
# recent recent date. Consider dish added
# '2020-01-01, 2019-12-09, 2020-01-20 then it should reutrn 2020-01-20, 2020-01-01, 2019-12-09.

# Consider name is a unique key of a dish. How you will change your Dish
# record implementation
# to reflect that change?

from datetime import datetime
import uuid


class Dish:
    Italian, Indian, Chinese, Thai, Greek, Lebanese, Mexican = range(7)

    def __init__(self, name, datetime, origin, dishIngredients):
        self.name = name
        self.datetime = datetime
        self.origin = origin
        self.dishIngredients = dishIngredients
        self.id = uuid.uuid4()

    def description(self):
        return self.name + "," + self.datetime + "," + str(self.origin)


class DishIngredients:

    def __init__(self, ingredientsName, foodValue):
        self.ingredientsName = ingredientsName
        self.foodValue = foodValue


class FoodValue:
    def __init__(self, calories, protein, fat, carbohydrates):
        self.calories = calories
        self.protein = protein
        self.fat = fat
        self.carbohydrates = carbohydrates


chili_fv = FoodValue(10, 0, 0, 4)
egg_fv = FoodValue(40, 15, 6, 3)
rice_fv = FoodValue(20, 0, 0, 35)
beef_fv = FoodValue(100, 50, 30, 5)


chili = DishIngredients("chili", chili_fv)
egg = DishIngredients("egg", egg_fv)
rice = DishIngredients("rice", rice_fv)
beef = DishIngredients("beef", beef_fv)


d1 = Dish("pasta", "5-Mar-18", Dish.Italian, [chili, egg, rice])
d2 = Dish("soup", "7-Mar-18", Dish.Thai, [egg, rice])
d3 = Dish("potol ar dolma", "8-Jan-18", Dish.Indian, [chili, rice])
d4 = Dish("Beef", "7-Mar-18", Dish.Indian, [chili, beef])


# print(d1.datetime)
# print(d2.datetime)
# print(d3.datetime)
# checkout the dish record


class DishRecord():
    def __init__(self):
        self.dishMap = {}
        # self.dishList = []

    def add(self, dish):
        # self.dishList[dish.name] = dish
        if dish.name not in self.dishMap:
            self.dishMap[dish.name] = dish
        else:
            print("dish already exist")

    def showAll(self):
        # for item in self.dishlist:
        #     print(item.name)
        for k, v in self.dishMap.items():
            print(v.description())

    def delete(self, dish):
        try:
            # self.dishList.remove(dish)
            del self.dishMap[dish.name]
        except:
            print("the dish can't found")

    def totalDish(self):
        # return(len(self.dishList))
        return(len(self.dishMap))

    def checkDish(self, dish):

        if dish.name in self.dishMap:
            return True
        else:
            return False
        # # loop through all list of dishes
        # for k, v in self.dishMap.items():
        #     # check each item with the parameter dish
        #     if self.dishMap[dish.name] == dish.name:
        #         # if we find match we return True
        #         return True
        # # or end of loop we return false
        # return False

    def sortDish(self):
        # sort by dish name
        #         # self.dishList.sort(key=lambda dish: dish.name)
        # sort by late datetime of creation
        #         # s = sorted(self.dishList, reverse=True,
        #         #            key=lambda dish: datetime.strptime(dish.datetime, "%d-%b-%y"))
        #         # return (s)
        s = dict(sorted(self.dishMap.items(),
                        key=lambda item: item[1].datetime))
        return s


dR = DishRecord()
dR.add(d1)
dR.add(d1)
dR.add(d2)
dR.add(d3)
dR.add(d4)
dR.showAll()
dR.delete(d1)
dR.delete(d1)
dR.showAll()

print(dR.totalDish())

print(dR.checkDish(d4))

sortedData = dR.sortDish()
for item in sortedData:
    print(item.datetime)
