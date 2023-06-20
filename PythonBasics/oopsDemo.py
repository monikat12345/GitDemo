class Calculator:
    num = 100 #class variables
    def __init__(self,a,b): ##parameterized constructor, constructor name should be init
        self.first_number = a #instance variable
        self.second_number = b
        print("I am a constructor and called automatically when object is created")

    def getData(self):
        print("first method in class")

    def addition(self):
        return self.first_number+self.second_number+Calculator.num

obj = Calculator(2,3) ##creating object
obj.getData()
print(obj.addition())

obj1 = Calculator(6,7)
obj1.getData()
print(obj1.addition())

print(obj.num)
