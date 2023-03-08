class WinDoor:
    def __init__(self, x, y):
        self.square = x * y

class Room:
    def __init__(self, x, y, z):
        self.square = 2 * z * (x + y)
        self.wd = []
    def add_wd(self, w, h):
        self.wd.append(WinDoor(w, h))
    def work_surface(self):
        new_square = self.square
        for i in self.wd:
            new_square -= i.square
        return new_square
#-----------------------------------
r1 = Room(6, 3, 2.7)
print(r1)
print(r1.square) # вывод: 48.6
r1.add_wd(1, 1)
r1.add_wd(1, 1)
r1.add_wd(1, 2)
print(r1.work_surface())