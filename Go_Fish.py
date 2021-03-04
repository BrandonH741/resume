from random import choice
from time import sleep
from os import system

def clear():
    system('cls')

def sorting_criteria_numbers(card):
    global numbers
    return numbers.index(card[0])

def sorting_criteria_suits(card):
    global suits
    return suits.index(card[1])

def sort(hand):
    hand.sort(key = sorting_criteria_numbers)
    for x in hand:
        working = [card for card in hand if card[0] == x[0]]
        for y in working:
            hand.remove(y)
        working.sort(key = sorting_criteria_suits)
        hand.extend(working)
        hand.sort(key = sorting_criteria_numbers)

def display():
    display = ''
    for x in range(len(hands[0]) - 1):
        card = hands[0][x]
        display += card + ', '
    display += hands[0][-1]
    print("User's Hand:" , display , '\n')
    sleep(1)

def pairs(hand):
    global hands
    rang = iter(range(len(hand) - 1))
    working = []
    for x in rang:
        if hand[x][0] == hand[x+1][0]:
            if hand == hands[0]:
                print('User made a pair in ' + spelled[numbers.index(hand[x][0])] + '!\n')
                sleep(1)
                #return True
            elif hand == hands[1]:
                print('Computer made a pair in ' + spelled[numbers.index(hand[x][0])] + '!\n')
                sleep(1)
            next(rang, '')
        elif hand[x][0] != hand[x+1][0]:
            working.append(hand[x])
    if hand[-1][0] != hand[-2][0]:
        working.append(hand[-1])
    hands[hands.index(hand)] = working

def user_turn():
    display()
    ask = input('Ask if Computer has a: ')
    print('')
    ask = ask.upper()
    if ask == 'QUIT':
        print('Goodbye')
        return True
    #sleep(1)
    if ask in spelled_a:
        ask = numbers[spelled_a.index(ask)]
    working = []
    for card in hands[1]:
        working.append(card[0])
    if ask not in working:
        print('"Go Fish!"\n')
        hands[0].append(choice(deck))
        deck.remove(hands[0][-1])
        sort(hands[0])
        pairs(hands[0])
        #display()
    elif ask in working:
        for hand in hands:
            for card in hand:
                if card[0] == ask:
                    hand.remove(card)
        print('User made a pair in ' + spelled[numbers.index(ask[0])] + '!\n')
    if hands[0] == [] or hands[1] == []:
        print('User Won!')
        return True
    display()
    return False

def comp_turn():
    ask = choice(hands[1])
    ask = ask[0]
    print('Ask if User has a:', spelled_a[numbers.index(ask)], '\n')
    #input()
    sleep(1)
    working = []
    for card in hands[0]:
        working.append(card[0])
    if ask not in working:
        input('Press "enter" to say "Go Fish!"\n')
        print('"Go Fish!"\n')
        hands[1].append(choice(deck))
        deck.remove(hands[1][-1])
        sort(hands[1])
        pairs(hands[1])
    elif ask in working:
        for hand in hands:
            for card in hand:
                if card[0] == ask:
                    hand.remove(card)
        print('Computer made a pair in ' + spelled[numbers.index(ask[0])] + '!\n')
    if hands[0] == [] or hands[1] == []:
        print('Computer Won!')
        return True
    return False

#

print('\nWelcome to Go Fish!\n')
sleep(1)

diff = input('Difficulty: ')
diff = diff.lower()
print('')

spelled = ('Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes', 'Sevens', 'Eights', 'Nines', 'Tens', 'Jacks', 'Queens', 'Kings')
spelled_a = []
for x in spelled:
    x = x[0:-1].upper()
    spelled_a.append(x)
spelled_a[5] = 'SIX'
numbers = 'A23456789TJQK'
suits = 'SDHC'
deck = []
for number in numbers:
    for suit in suits:
        card = number + suit
        deck.append(card)

hands = [[], []]
for player in hands:
    for card in range(7):
        #card = choice(deck)
        #deck.remove(card)
        #player.append(card)
        player.append(choice(deck))
        deck.remove(player[-1])
    sort(player)
display()

input('Press "enter" to lay down beginning pairs.\n')

for hand in hands:
    pairs(hand)
input('Press enter to continue.\n')

coin = choice(['User', 'Computer'])
print('Coin flip says that' , coin , 'goes first!\n')
sleep(1)

test = False

if coin == 'User':
    test = user_turn()
else:
    display()

while test == False:
    test = comp_turn()
    if test == True:
        break
    test = user_turn()