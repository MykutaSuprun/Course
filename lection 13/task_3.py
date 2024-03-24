class Car:
    def __init__(self, brand, model, year, speed=0):
        self.brand = brand
        self.model = model
        self.year = year
        self.speed = speed

    def accelerate(self):
        self.speed += 5

    def brake(self):
        if self.speed >= 5:
            self.speed -= 5
        else:
            self.speed = 0

    def display_speed(self):
        print(f"The current speed of the {self.brand} {self.model} is {self.speed}.")


car1 = Car("Toyota", "Camry", 2020)
car1.display_speed()  
car1.accelerate()
car1.display_speed()  
car1.brake()
car1.display_speed()  