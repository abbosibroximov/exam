class calculator():
    def __init__(self,  num1, num2):
        self.num1=num1
        self.num2=num2

    def add(self, num1, num2):
        return num1+num2
    def sub(self,  num1, num2):
        return  num1-num2
    def mult(self,  num1, num2):
        return num1*num2
    def div(self,  num1, num2):
        return num1/num2
my_result=calculator(100, 50)
print(my_result.add(100,50))
print(my_result.sub(100,50))
print(my_result.mult(100,50))
print(my_result.div(100,50))
