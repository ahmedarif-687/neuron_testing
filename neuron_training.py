"""
neuron practice
"""
def add_neuron (x):
    '''
function to return odd number in addition
'''
    if x % 2 == 0:
        print("The answer from addition neuron is : ",x+1)
    else:
        print("The answer from addition neuron is : ",x+2)

def sub_neuron (x):
    '''
function to return odd number in subtraction
'''
    if x==0:
        print("Input numbers greater than 0")
    elif x % 2 == 0:
        print("The answer from subtraction neuron is : ",x-1)
    else:
        print("The answer from subtraction neuron is : ",x-2)

def mul_neuron (x):
    '''
function to return odd number in multiplication
'''
    if x==0:
        print("Input numbers greater than 0")
    elif x % 2 == 0:
        print("The answer from multiplication neuron is : ",x*2+1)
    else:
        print("The answer from multiplication neuron is : ", x*3)

def div_neuron (x):
    '''
function to return odd number in division
'''
    if x<=2:
        print("Input number must be greater than 2")
    elif x % 2 == 0:
        if int(x/3) % 2==0:
            print("The answer from division neuron is : ",int(x/3)+1)
        else:
            print("The answer from division neuron is : ", int(x/3))
    else:
        print("The answer from division neuron is : ", int(x/2))

while True:
    input_text =int(input("Enter Text: "))
    if input_text == 0 :
        break
    print("The taken number is: ",input_text )
    div_neuron(input_text)
    mul_neuron(input_text)
    sub_neuron(input_text)
    add_neuron(input_text)
