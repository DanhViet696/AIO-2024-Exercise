import math
def is_number(x):
    try:
        float(x)
        return True
    except ValueError:
        print('x must be a number')
        return False
def sigmoid(x):
    return 1/(1+math.exp(-x))
def relu(x):
    return max(0,x)

def elu(x):
    alpha=0.01
    return x if x>0 else alpha*(math.exp(-x)-1)
#So sánh item name
def apply_activation_function(x, activation_function):
    if activation_function == 'sigmoid':
        return sigmoid(x)
    elif activation_function == 'relu':
        return relu(x)
    elif activation_function == 'elu':
        return elu(x)
    else:
        print(f"{activation_function} is not supported")
        return None

x_input = input("Nhập giá trị x: ")
activation_function = input("Nhập tên activation function (sigmoid, relu, elu): ")

if not is_number(x_input):
    print("x must be a number")
else:
    x = float(x_input)
    if activation_function not in ['sigmoid', 'relu', 'elu']:
        print(f"{activation_function} is not supported")
    else:
        result = apply_activation_function(x, activation_function)
        if result is not None:
            print(f"{activation_function}: f({x}) = {result}")