inputVarieble = input('podaj parametr funkcji: ')
def printAnimal(*animal) :
    print(animal[0].split())
    for listAnimal in animal[0].split():

        if listAnimal == 'cat':
            print('Cat drawing')
        elif listAnimal == 'bear':
            print('Bear drawing')
        elif listAnimal == 'bat':
            print('Bat drawing')
        else:
            print("Cannot print %s. Correct values for the parameter are: cat, bear or bat." % listAnimal)

    return
printAnimal(inputVarieble)