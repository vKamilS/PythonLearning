inputVarieble = input('podaj parametr funkcji: ')
def printAnimal(animal) :
    #strAnimal = str(animal)
    if animal == 'cat':
        print('Cat drawing')
    elif animal == 'bear':
        print('Bear drawing')
    elif animal == 'bat':
        print('Bat drawing')
    else:
        print("Cannot print %s. Correct values for the parameter are: cat, bear or bat." % animal)

    return
printAnimal(inputVarieble)