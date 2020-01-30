class Dish:
    def __init__(self, name):
        self.name = name


class DishRecord:
    def __init__(self):
        self.dishlist = []

    def add(self, dish):
        self.dishlist.append(dish)

    def delete(self):
        # try:
        #     self.dishlist.remove(dish)
        # except:
        #     print("dish not in list")

        if len(self.dishlist) != 0:
            return self.dishlist.pop(0)
        else:
            print("No dish found")
            return None

    def showAll(self):
        for item in self.dishlist:
            print(item.name)


d1 = Dish("Pasta")
d2 = Dish("Soup")
d3 = Dish("Pizza")
d4 = Dish("Fried rice")
d5 = Dish("chicken curry")

dr = DishRecord()
dr.add(d1)
dr.add(d2)
dr.add(d3)
dr.add(d4)

# dr.showAll()


# dr.showAll()

dr.add(d5)

dr.delete()
dr.delete()
dr.delete()
dr.delete()
dr.showAll()
dr.delete()
dr.delete()
dr.showAll()
 for item in self.dishlist:
            if item.name == name:
                return item.description
        return ("dish name not found")
