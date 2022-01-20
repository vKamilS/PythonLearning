colors =  ['Hearts', 'Diamonds', 'Clubs', 'Picks']
figures = [
    {'Figure':'Ace', 'Power':14},
    {'Figure':'King', 'Power':13},
    {'Figure':'Queen', 'Power':12},
    {'Figure':'Jack', 'Power':11},
    {'Figure':'10', 'Power':10},
    {'Figure':'9', 'Power':9}
    ]

allCards = []

for c in colors:
    for f in figures:
        aCard=f.copy()
        aCard['Color'] = c
        allCards.append(aCard)

import random
random.shuffle(allCards)
#print(allCards)


player1 = []
player2 = []

max=len(allCards)

for i in range(max):
    if i%2==0:
        player1.append(allCards.pop(0))
    else:
        player2.append(allCards.pop(0))

print('------CardsInfo------')
print('player 1 has %d Cards' % len(player1))
print('player 2 has %d Cards' % len(player2))

print('-----Player1 cards-----')
print(player1)
print('-----Player2 cards-----')
print(player2)

i = 0
while len(player1)>0 and len(player2)>0:
    i = i+1
    card1 = player1.pop(0)
    card2 = player2.pop(0)
    if card1['Power'] > card2['Power']:
        player1.append(card1)
        player1.append(card2)
        print(i, 'Player1: %d cards      Player2: %d cards' % (len(player1),len(player2)))

    elif card1['Power'] < card2['Power']:
        player2.append(card1)
        player2.append(card2)
        print(i, 'Player1: %d cards      Player2: %d cards' % (len(player1),len(player2)))

    else:
        player1.append(card1)
        player2.append(card2)
        print(i, 'Player1: %d cards      Player2: %d cards' % (len(player1),len(player2)))

if len(player1)!=0:
    print('Player 1 win')
else:
    print('Player 2 win')


