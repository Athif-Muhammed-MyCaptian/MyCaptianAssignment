#construction of a calculator
a, b = map(int, input("Enter two values\n").split(', '));
def calculator(a1,b1):
    print('calculator\n1.Additon\n2.Subtraction\n3.Division\n4.Multiplication')
    c1=int(input('enter your choice:'));
    if c1==1:
        print(a+b);
    elif c1==2:
        print(a-b);
    elif c1==3:
        print(a/b);
    elif c1==4:
        print(a*b);

calculator(a,b)
