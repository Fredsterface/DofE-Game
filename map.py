from classes import Room, Person, Item, GameState, Enemy
from types import MethodType

#Define some items
potatoes = Item('Bag of potatoes',['potatoes', 'taters', 'potats', 'spuds'])

backpack = Item('Backpack',['bag', 'backpack', 'rucksack'])
def updateMaxItems(self, person):
    person.maxItems = 5
backpack.takeFunction = MethodType(updateMaxItems, backpack)
def dropEverything(self, person):
    for item in person.items:
        person.removeItem(item)
        person.room.addItem(item)
backpack.dropFunction = MethodType(dropEverything, backpack)

food = Item('Some food',['food', 'foods'])

water = Item('A bottle of water',['water', 'bottle', 'waters'])

boots = Item('Walking boots',['boots', 'walking boots', 'shoes'])

stick = Item('Stick',['stick', 'twig', 'branch'])

#Define some enemies

cow = Enemy('Cow')


#Construct some rooms
startRoom = Room()
startRoom.description = "DofE storage warehouse, everything you need is layed out in front of you"
startRoom.shortDescription = "DofE warehouse"
startRoom.addItem(potatoes)
startRoom.addItem(backpack)
startRoom.addItem(food)
startRoom.addItem(water)
startRoom.addItem(boots)

Footpath1 = Room()
Footpath1.description = 'A footpath'
Footpath1.addItem(stick)
Footpath1.shortDescription = "Footpath with trees"

Road1 = Room()
Road1.description = 'A road'
Road1.shortDescription = "Road"
#Car as obsticle. Be careful to cross road.

Field1 = Room()
Field1.description = 'A field with cow'
Field1.shortDescription = 'Cow field'
Field1.addEnemy(cow)
#Cow as obsticle. Blocking exit
#Use food to lure cow away from exit to proceed

Footpath2 = Room()
Footpath2.description = 'Another footpath'
Footpath2.shortDescription = "A footpath"

Field2 = Room()
Field2.description = 'A field that is very muddy'
Field2.shortDescription = "Muddy field"
def haveBoots(self, game):
    person = game.person
    if person.hasItem(boots):
        return True
    else:
        return False
Field2.enterFunction = MethodType(haveBoots, Field2)
#Walking boots to cross muddy field

#Link rooms together
startRoom.addExit('N', Field1)
startRoom.addExit('S', Road1)
Field1.addExit('W', Footpath1)
Field1.addExit('SW', Footpath2)
Footpath1.addExit('NE', Field2)
Footpath1.addExit('W', Footpath2)






"""
#Add items to the rooms

startRoom.addItem(Item("Chekhov's Gun",['gun']))
rooms.append(startRoom)

rooms[1].description = "The first room"
rooms[1].addExit('E', rooms[2])
rooms[1].addExit('S', rooms[3])
rooms[1].addItem(Item("Yakimov's Knife",['knife']))

rooms[1].addExit('SE', rooms[0])

rooms[2].description = "The second room"

rooms[2].addExit('W', rooms[1])
rooms[2].addExit('S', rooms[4])
rooms[2].addExit('SW', rooms[0])

rooms[3].description = "The third room"
rooms[3].addExit('N', rooms[1])
rooms[3].addExit('E', rooms[4])
rooms[3].addExit('NE', rooms[0])
rooms[3].addItem(Item("Rudnikov's Spatula",['spatula']))

rooms[4].description = "The fourth room"
rooms[4].addExit('N', rooms[2])
rooms[4].addExit('W', rooms[3])
rooms[4].addExit('NW', rooms[0])
rooms[4].addItem(Item("Shvedov's Rope",['rope']))
rooms[4].addItem(Item("Shvedov's Axe",['axe']))

if __name__ == '__main__':
    P = Person()
    G = GameState(P, rooms[1])
"""
