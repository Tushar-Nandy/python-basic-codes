from art import logo
print(logo)
should_continue=True
def add(a,b):
    """Add two numbers and returns the output"""
    return a+b
def subtract(a,b):
    """Subtracts two number and returns the output"""
    return a-b
def multiply(a,b):
    """Multiplies two number and returns the output
    Example:
    a=5, b=6
    returns a*b     5*6=30
    So, it returns 30 as the output"""
    return a*b
def divide(a,b):
    """Returns a floating point value"""
    return a/b
def power(a,b):
    """Returns exponent or power of a number
    First enter the base and then the exponent.
    Example:
    power(2,3) would return 2^3= 2*2*2=8"""
    return a**b

operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide,
    "^":power
}

num1=float(input("Enter a number: "))
for symbol in operations:
    print(symbol)
operation_symbol=input("Select the operation from above: ")
num2=float(input("Enter a number: "))
calc_func=operations[operation_symbol]
result=calc_func(num1,num2)
while should_continue:    
    print(result)
    ans=input("Enter 'y' to continue or 'n' to exit ")
    if ans=='n':
        break
    operation_symbol=input("Enter the symbol: ")
    num3=float(input("Enter another number: "))
    calc_func=operations[operation_symbol]
    print(calc_func)
    result=calc_func(result,num3)
print(f"The answer is {result}")
    