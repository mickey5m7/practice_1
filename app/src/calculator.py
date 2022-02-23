class Calculator():
    def add(self, num1,num2):
        return num1 + num2
    def sub(self,num1,num2):
        return num1-num2

if __name__ == "__main__":
    cal=Calculator()
    print(cal.add(1,3))
