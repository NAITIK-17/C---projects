#this a basic calculator program
add = lambda x,y: x+y
subtract = lambda x,y: x-y
multiply = lambda x,y: x*y
divide = lambda x,y: x/y if y != 0 else "Cannot divide by zero"

def calculate():
    a = float(input("Enter a number: "))
    while True:
        operations = {
            'add': add,
            'sutract':subtract,
            'multiply': multiply,
            'divide': divide
        }
        print("Available operations: add, subtract, multiply, divide")
        op = input("Enter operator or 'q' to quit: ").lower()
        if op == 'q':
            print("Thanks for using the calculator!")
            break
        if op not in operations:
            print("Invalid operator! Please try again.")
            continue
        b = float(input("Enter another number: "))
        result = operations[op](a,b)
        return result
        a = result

if __name__ == "__main__":
    calculate()
