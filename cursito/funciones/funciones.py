
def Function(num1, num2):
    print(f'el resultado de la suma: {num1} + {num2} es  {num1+ num2}')
    return num1 + num2


result = 2
for i in range(5):
    result = Function(result,2)

