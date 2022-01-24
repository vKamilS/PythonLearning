import math

def giveGeomSeqElement(a1=2, factor=2, index=2):
    #Funkcja wylicza wartość ciągu geometrycznego
    for i in range(1,index):
        a1=a1*factor
    return a1

#print(giveGeomSeqElement(2,4,3))

def geomElements(a1=3, factor=2, index=10):
    elementList = []
    for i in range (0, index):
        elementList.append(a1)
        a1=a1*factor
    return elementList

#print(geomElements())

def giveFactorForGeomSeq(term, nextterm):
    if type(term) == int and type(nextterm) == int:
        factor = nextterm/term
        return factor
    else:
        functionError = 'Provided argument are not integer types.'
        return functionError
#print(giveFactorForGeomSeq(32, 46))

def giveSumOfElementsGeomSeq (a1=2, factor=2, index=2):
    if factor == 1:
        funcSum=a1*index
        return funcSum
    elif type(a1) != int or type(factor) != int or type(index) != int:
        funcError = 'Provided wrong arguments.'
        return funcError
    else:
        funcSum = a1*(1-factor**index)/(1-factor)
        return funcSum

#print(giveSumOfElementsGeomSeq(1,3,'a'))