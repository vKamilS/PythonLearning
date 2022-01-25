#a1 = input('Type a parameter: ')
#b1 = input('Type b parameter: ')
#c1 = input('Type c parameter: ')

from math import sqrt

def check_int(s):
    s=str(s)
    if s[0] == '-' or s[0] =='+':
        return s[1:].isdigit()
    else:
        return s.isdigit()

def squareFunction(a, b, c):

    parameterList = [a, b, c]

    for parameter in parameterList:
        if check_int(parameter):
            continue
        else:
            return ('Not all provided parameters are integer. Please rum programme one again and the provide correct parameters')

    if a==0:
        return ('This is not square equation.')
    else:
        delta=b**2-(4*a*c)
        if delta<0:
           return ('The equation has no solution.')
        elif delta==0:
            x1=(-b-sqrt(delta))/(2*a)
            return ('The equation has 1 solution =', x1)
        else:
            x1 = (-b-sqrt(delta))/(2*a)
            x2 = (-b+sqrt(delta))/(2*a)
            return ('The equation has 2 solutions =', x1, 'and', x2)


print(squareFunction(3, 4, 1))
print(squareFunction(5, 4, -1))
print(squareFunction(5, 4, 1))
print(squareFunction(2, 0, 0))
print(squareFunction(0, 3, 4))
print(squareFunction('one', 1, 1))