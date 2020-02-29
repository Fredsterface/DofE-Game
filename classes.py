import time
import random

directions = {
'N' : 'North',
'S' : 'South',
'W': 'West',
'E': 'East',
'NE': 'North-East',
'NW': 'North-West',
'SE': 'South-East',
'SW': 'South-West',
}

opposite_directions = {
'N' : 'S',
'S' : 'N',
'W': 'E',
'E': 'W',
'NE': 'SW',
'NW': 'SE',
'SE': 'NW',
'SW': 'NE',
}

class Item:
    def __init__(self, item, names=[]):
        self.item = item
        self.names = names
        self.names.append(self.item.lower())
    def __repr__(self):
        return self.item
    def addName(self,name):
        self.names.append(name)
    def takeFunction(self, person):
        return
    def dropFunction(self, person):
        return
        
class Person:
    def __init__(self):
        self.items = []
        self.maxItems = 2
        self.room = None
    @property
    def maxItems(self):
        return self._maxItems
    @maxItems.setter
    def maxItems(self, value):
        self._maxItems = value
    @property
    def canAddItem(self):
        if len(self.items) < self.maxItems:
            return True
        else:
            return False
    def addItem(self, item):
        assert(isinstance(item, Item))
        if self.canAddItem == True:
            self.items.append(item)
            item.takeFunction(self)
            return True
        else:
            return False
    def hasItem(self, item):
        if item in self.items:
            return True
        else:
            return False
    def removeItem(self, item):
        assert(item in self.items)
        self.items.remove(item)
        item.dropFunction(self)
    def __repr__(self):
        if len(self.items) == 0:
            s = "Person with no items"
        else:
           s = "Person with items\n"
           s += "\n".join("\t%s" % I.__repr__() for I in self.items)
        return s
    
class Room:
    def __init__(self):
        self.items = []        
        self._description = ""
        self._exits = {}
    @property
    def description(self):
        return self._description
    @description.setter
    def description(self, value):
        self._description = value
    @property
    def shortDescription(self):
        if hasattr(self, '_shortDescription'):
            return self._shortDescription
        else:
            return ''
    @shortDescription.setter
    def shortDescription(self, value):
        self._shortDescription = value
    @property
    def exits(self):
        return self._exits
    def addExit(self, key, value, addOpposite=True):
        assert(key in directions.keys())
        assert(isinstance(value, Room))
        self._exits[key] = value
        if addOpposite == True:
            value.addExit(opposite_directions[key], self, addOpposite=False)
    def addItem(self, item):
        self.items.append(item)
    def removeItem(self, item):
        assert(item in self.items)
        self.items.remove(item)
    def enterFunction(self, game):
        #Return true if we are allowed to enter this room
        return True
    def exitFunction(self, game):
        #Return true if we are allowed to exit this room
        return True
    def __repr__(self):
        ret = self.description
        if len(self.items) > 0:
            ret += "\nYou can see:\n"
            for item in self.items:
                ret += "\t%s\n" % item
        if len(self.exits) > 0:
            ret += "\nExits are:\n"
            for e in self.exits.keys():
                ret += "\t" + directions[e] + "\t" + self.exits[e].shortDescription + "\n"
        return ret        

class GameState:
    def __init__(self, person, room):
        self.person = person
        self.room = room
        self.person.room = room
    def updateRoom(self, room):
        #Check if we can exit the room we are currently in
        if self.room.exitFunction(self) == False:
            print("Unable to exit %s\n" % self.room.shortDescription)
            return
        if room.enterFunction(self) == False:
            print("Unable to enter %s\n" % room.shortDescription)
            return        
        self.room = room
        self.person.room = room
    def go(self, d):
        try:
            self.updateRoom(self.room.exits[d])
        except:
            print("You cannot exit in that direction\n")
    def takeItem(self, item):
        if item not in self.room.items:
            print("%s Not in the room." % item)
            return
        flag = self.person.addItem(item)
        if flag == True:
            self.room.removeItem(item)
        else:
            print('You are carrying too much.')
    def dropItem(self, item):
        if item not in self.person.items:
            print("%s Not on person" % item)
        self.room.addItem(item)
        self.person.removeItem(item)
    def __repr__(self):
        ret = "You are in\n\t%s\n" % self.room
        if len(self.person.items) > 0:
            ret += "You are carrying:"
            for i in self.person.items:
                ret += "\t%s\n" % i
        
        return ret
        
if __name__ == "__main__":
    I = Item("Item")
    E = Item("Money")
    A = Item("Sword")
    P = Person()
    P.addItem(A)
    P.addItem(I)
    print(P)
    P.removeItem(A)
    print(P)
    R = Room()
    R0 = Room()
    R.description = "A room with stuff in it."
    R.addItem(Item("Fish"))
    R.addExit('N', R0)
    print(R)
