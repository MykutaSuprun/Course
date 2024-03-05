def apply_operation(operation, operand1, operand2):
    return operation(operand1, operand2)

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

operand=0
a=input('Choose mathematical operation with two operand (add, subtract, multiply, divide) ')
x=int(input('Write x '))
y=int(input('Write y '))
if a == 'add':
    operand=add
elif a =='subtract':
    operand=subtract
elif a == 'multiply':
    operand= multiply
elif a == 'divide':
    operand= divide
    
result=apply_operation(operand,x,y)
print(result)

#я зробив універсальну функцію але якщо треба саме тести то наприклад 
#print(apply_operation(add,1,2))
#print(apply_operation(divide,1,2))