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


from datetime import datetime


class Dish:
    def __init__(self, name, datetime):
        self.name = name
        self.datetime = datetime


d1 = Dish("pasta", "(2020, 1, 17)")
d2 = Dish("soup", "(2020, 5, 17)")
d3 = Dish("potol ar dolma", "(2020, 1, 14)")
d4 = Dish("Beef", "(2020, 1, 17)")

print(d1.datetime)
print(d2.datetime)
print(d3.datetime)
# checkout the dish record


class DishRecord():
    def __init__(self):
        self.dishList = []

    def add(self, dish):
        self.dishList.append(dish)

    def showAll(self):
        for item in self.dishList:
            print(item.name)

    def delete(self, dish):
        try:
            self.dishList.remove(dish)
        except:
            print("the dish can't found")

    def totalDish(self):
        return(len(self.dishList))

    def checkDish(self, dish):

        # loop through all list of dishes
        for item in self.dishList:
            # check each item with the parameter dish
            if item.name == dish.name:
                # if we find match we return True
                return True
        # or end of loop we return false
        return False

    def sortDish(self):
        self.dishList.sort(
            key=lambda date: datetime.strptime(date, "%y-%b-%d"))
        return (self.dishList)


dR = DishRecord()
dR.add(d1)
dR.add(d2)
dR.add(d3)
dR.add(d4)
dR.showAll()
dR.delete(d1)
dR.delete(d4)
dR.showAll()

print(dR.totalDish())

print(dR.checkDish(d4))
print(dR.sortDish())
