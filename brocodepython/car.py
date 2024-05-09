class Car:

    wheels = 4 # class variable

    def __init__(self, make, model, year, color): #constructer
        self.make = make  # instance variable
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")