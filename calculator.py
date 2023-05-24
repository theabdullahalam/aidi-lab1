class Calculator:

    def add(self, a, b):
        return a + b

    def difference(self, a, b):
        return a - b

    def product(self, a, b):
        return a * b

    def quotient(self, a, b):
        return a/b

    def remainder(self, a, b):
        return a % b

    def power(self, a, b):
        return a ** b

a = float(input("a: "))
b = float(input("b: "))

calculator = Calculator()

print("Sum: ", calculator.add(a,b))
print("Difference: ", calculator.difference(a,b))
print("Product: ", calculator.product(a,b))
print("Quotient: ", calculator.quotient(a,b))
print("Remainder: ", calculator.remainder(a,b))
print("Power: ", calculator.power(a,b))