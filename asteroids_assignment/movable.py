class Movable:
    def __init__(self, x, y, dx, dy, world_width, world_height):
        self.mX = x
        self.mY= y
        self.mDX = dx
        self.mDY = dy
        self.mWorldWidth = world_width
        self.mWorldHeight = world_height

    def getX(self):
        return self.mX

    def getY(self):
        return self.mY

    def getDX(self):
        return self.mDX

    def getDY(self):
        return self.mDY

    def getWorldWidth(self):
        return self.mWorldWidth

    def getWorldHeight(self):
        return self.mWorldHeight

    def move(self, dt):
        return

    def accelerate(self):
        return

    def evolve(self):
        return

    def draw(self):
        return
