import math

def multiple_inputs (input_list):
    """
    multiple inputs
    """
    d=0
    for i in input_list:
        d += i**2
    print("Answer for the required input is: ", math.sqrt(d))

while True:
    # input_text1 =int(input("Enter number 1: "))
    # input_text2 =int(input("Enter number 2: "))
    # input_text3 =int(input("Enter number 3: "))
    print("enter your values , after giving a value give space before adding another value")
    inputs = [int(i) for i in input().split()]
    if 0 in inputs:
        print("No input value can be zero")
        break
    print(inputs)
    print("The taken numbers are: ",inputs )
    multiple_inputs(inputs)
