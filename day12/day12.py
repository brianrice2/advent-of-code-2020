# Load input data
with open('day12/input.txt', 'r') as file:
    orders = file.read().split('\n')

class Ship():
    facing = 0
    x = 0
    y = 0

    def __abs__(self):
        return abs(self.x) + abs(self.y)

    def get_direction(self):
        if self.facing == 0:
            return 'E'
        elif self.facing == 90:
            return 'N'
        elif self.facing == 180:
            return 'W'
        else:
            return 'S'

    def rotate(self, direction, degrees):
        if direction == 'L':
            self.facing = (self.facing + degrees) % 360
        else:
            self.facing = (self.facing - degrees) % 360

    def move(self, direction, distance):
        if direction == 'F':
            self.move(self.get_direction(), distance)
        elif direction == 'N':
            self.y = self.y + distance
        elif direction == 'S':
            self.y = self.y - distance
        elif direction == 'E':
            self.x = self.x + distance
        elif direction == 'W':
            self.x = self.x - distance


# Part 1
myShip = Ship()
for order in orders:
    action = order[0]
    args = int(order[1:])

    if action in 'LR':
        myShip.rotate(action, args)
    else:
        myShip.move(action, args)

print(abs(myShip))


# Part 2
class ShipWithWaypoint(Ship):
    waypointx = 10
    waypointy = 1

    def rotate(self, direction, degrees):
        for _ in range(degrees // 90):
            if direction == 'L':
                self.waypointx, self.waypointy = -self.waypointy, self.waypointx
            else:
                self.waypointx, self.waypointy = self.waypointy, -self.waypointx

    def move(self, direction, distance):
        if direction == 'F':
            for _ in range(distance):
                # Move to the waypoint
                self.x = self.x + self.waypointx
                self.y = self.y + self.waypointy
        elif direction == 'N':
            self.waypointy = self.waypointy + distance
        elif direction == 'S':
            self.waypointy = self.waypointy - distance
        elif direction == 'E':
            self.waypointx = self.waypointx + distance
        elif direction == 'W':
            self.waypointx = self.waypointx - distance


newShip = ShipWithWaypoint()

for order in orders:
    action = order[0]
    args = int(order[1:])

    if action in 'LR':
        newShip.rotate(action, args)
    else:
        newShip.move(action, args)

print(abs(newShip))
