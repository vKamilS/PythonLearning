colors = ['Hearts', 'Diamonds', 'Clubs', 'Pikes']
figures = ['Ace', 'King', 'Queen', 'Jack', '10', '9']

allCards = []

for color in colors:
    for figure in figures:
        allCards.append(color+' '+figure)
#print(allCards)

import random
random.shuffle(allCards)
print(allCards)

player1 = []
player2 = []
max = len(allCards)

for i in range(max-1):
    if (i%2)==0:
        player1.append(allCards.pop(0))
    else:
        player2.append(allCards.pop(0))

print(' ')
print(player1)
print(' ')
print(player2)

