def greet(fx):
    def mfx():
        print("Hello!")
        fx()
        print("Bye")
    return mfx

@greet
def hi():
    print("Hi!")
    
hi()
@greet
def add():
    x = int(input("Enter a num: "))
    y = int(input("Enter a num: "))
    print(x+y)

print(add())
