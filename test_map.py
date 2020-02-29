from classes import Room, Person, Item, GameState

rooms = [Room() for i in range(5)]

rooms[0].description = "The centre of the maze"
rooms[0].addExit('NW', rooms[1])
rooms[0].addExit('NE', rooms[2])
rooms[0].addExit('SW', rooms[3])
rooms[0].addExit('SE', rooms[4])
rooms[0].addItem(Item("Chekhov's Gun",['gun']))

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
