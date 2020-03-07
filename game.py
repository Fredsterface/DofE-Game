from classes import Room, Person, Item, GameState
from map import startRoom
P = Person()
G = GameState(P, startRoom)

def parseUserInput(G, userInput):
    if userInput[0] == 'quit':
        quit()
    if userInput[0] == 'go':
        if userInput[1] == 'north' or userInput[1] == 'n':
            G.go('N')
        elif userInput[1] == 'south' or userInput[1] == 's':
            G.go('S')
        elif userInput[1] == 'east' or userInput[1] == 'e':
            G.go('E')
        elif userInput[1] == 'west' or userInput[1] == 'w':
            G.go('W')
        elif userInput[1] == 'northeast' or userInput[1] == 'ne':
            G.go('NE')
        elif userInput[1] == 'northwest' or userInput[1] == 'nw':
            G.go('NW')
        elif userInput[1] == 'southeast' or userInput[1] == 'se':
            G.go('SE')
        elif userInput[1] == 'southwest' or userInput[1] == 'sw':
            G.go('SW')
        else:
            print('Unknown direction')
    elif userInput[0] == 'drop':
        c = 1
        while userInput[c] in {'the', 'a', 'an'}:
            c+=1
        flag = False
        for item in G.person.items:
            if userInput[c] in item.names:
                G.dropItem(item)
                flag = True
        if flag == False:
            print("You can't drop %s" % userInput[c])
    elif userInput[0] == 'take':
        c = 1
        while userInput[c] in {'the', 'a', 'an'}:
            c+=1
        flag = False
        for item in G.room.items:
            if userInput[c] in item.names:
                G.takeItem(item)
                flag = True
        if flag == False:
            print("You can't take %s" % userInput[c])
    elif userInput[0] in {'use', 'give'}:
        c = 1
        while userInput[c] in {'the', 'a', 'an'}:
            c+=1
        flag = False
        item = None
        for _item in G.person.items:
            print(userInput[c], _item.names)
            if userInput[c] in _item.names:
                item = _item
                flag = True
        if flag == False:
            print("You can't use %s" % userInput[c])
            return
        c += 1
        while userInput[c] in {'on', 'to'}:
            c+=1
        flag = False
        enemy = None
        for _enemy in G.room.enemies:
            if userInput[c] in _enemy.names:
                enemy = _enemy
                flag = True
        if flag == False:
            print("No enemy %s" % userInput[c])
            return
        print('Using %s on %s' % (item, enemy))
    else:
        print('You cant do that!')


    
if __name__ == "__main__":        
    while True:
        print(G)
        userInput = input("Enter something ").lower().split()
        parseUserInput(G, userInput)
