class Dish:
    def __init__(self, name):
        self.name = name


class DishRecord:
    def __init__(self):
        self.dishList = []

    def add(self, dish):
        if dish not in self.dishList:
            self.dishList.append(dish)
        else:
            print("dish already exist")

    def delete(self, dish):
        if dish in self.dishList:
            self.dishList.remove(dish)
        else:
            print("No dish found")

    def showAll(self):
        for dish in self.dishList:
            print(dish.name)
