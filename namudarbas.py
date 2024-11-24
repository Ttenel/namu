class Car:
    def __init__(self, brand, age, mark, color=None, weight=None):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weight = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1

Car1 = Car(brand="Lexus", age=12, mark="lx 500", color="black", weight=1800)

print(Car1.brand)

Car1.move()

Car1.stop()

Car1.birthday()

Car1.birthday()

print(Car1.age)
