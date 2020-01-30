

from datetime import datetime


class Dish:
    def __init__(self, name, category, description, datetime):
        self.name = name
        self.category = category
        self.description = description
        self.datetime = datetime


class DishRecord:
    def __init__(self):
        self.dishlist = []

    def add(self, dish):

        if dish not in self.dishlist:
            return self.dishlist.append(dish)
        else:
            print("{} already exist".format(dish.name))

    def delete(self):
        try:
            self.dishlist.pop()
        except:
            print("dish not in list")

    def showAll(self):
        for item in self.dishlist:
            print(item.name)

    def description(self, name):
        for dish in self.dishlist:
            if dish.name == name:
                return dish.description
        return "Dish not found"

    def totalDish(self):
        print(len(self.dishlist))

    def sortDish(self):
        # sorted(student_objects, key=lambda student: student.age)
        # s = sorted(self.dishlist, key=lambda dish: dish.name)
        # return s
        #  dates.sort(key = lambda date: datetime.strptime(date, '%d %b %Y'))
        # s = self.dishlist.sort(
        #     key=lambda datetime: datetime.strptime(datetime, '%d %b %y'))
        # return s
        s = sorted(self.dishlist, key=lambada dish: datetime.strptime(dish.datetime, "%d %b %y"))
        return (s)


d1 = Dish("Pasta", "Italian", "pasta is good", "1-jan-2019")
d2 = Dish("Soup", "Thai", "soup is healthy", "3-Jan-2019")
d3 = Dish("Pizza", "Italian", "Pizza is yummy", "4-jan-2019")
d4 = Dish("Fried rice", "Indian", "popular dish", "5-jan-2019")

dr = DishRecord()
dr.add(d1)
dr.add(d2)
dr.add(d3)
dr.add(d4)
# dr.add(d4)
dr.showAll()
# dr.delete(d4)
print(dr.description("egg"))

dr.totalDish()
dr.sortDish()
for item in dr.sortDish():
    print(item.datetime)
