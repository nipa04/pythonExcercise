class Meal:
    def __init__(self, name):
        self.name = name


m1 = Meal("Fried rice")
m2 = Meal("Calamari")


class MealRecord:
    def __init__(self):
        self.mealList = []

    def add(self, meal):
        self.mealList.append(meal)

    def showAll(self):
        for item in self.mealList:
            print(item.name)

    def delete(self, meal):
        try:
            self.mealList.remove(meal)
        except:
            print("Meal not found")


m1Re = MealRecord()
m1Re.add(m1)
m1Re.add(m2)
m1Re.showAll()
m1Re.delete(m1)
m1Re.delete(m1)
m1Re.showAll()
