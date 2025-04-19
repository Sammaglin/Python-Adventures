num1 = float(input('Enter your number'))
op = input('Enter your operator')
num2 = float(input('Enter your number'))

if op == '+':
    print(num1+num2)
elif op == '-':
    print(num1-num2)
elif op == '*':
    print(num1*num2)
elif op == '/':
    print(num1/num2)
else:
    print('Invalid Protocol')