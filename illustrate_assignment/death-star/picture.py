from random import randrange, choice
import pygame

# this example game draws 3 concentric circles on top of a single color background
# the circles move down every time frame
# the user can control the circles by:
# - clicking the left mouse button to relocate them
# - holding the UP key to move them up
# - pressing the A key to move them to the left of the window
# - holding the A key to gradually move them to the right
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (100, 0, 0)
BLUE = (0, 0, 100)
GREEN = (0, 100, 0)


class Picture:

    def __init__( self, width, height ):
        self.mWidth = width
        self.mHeight = height
        self.objects = []
        two = Planet(BLUE, 400, 400, 200)
        self.objects.append(two)

        return

    # methods for user interface

    # draws the current state of the system
    def draw( self, surface ):
        
        # rectangle to fill the background
        rect = pygame.Rect( int ( 0 ), int ( 0 ), int ( self.mWidth ), int ( self.mHeight ) )
        pygame.draw.rect( surface, BLACK, rect, 0 )
        for object in self.objects:
            object.draw(surface)
            object.drawBlotches(surface)

        # one = Star(WHITE, 300, 300, 4)
        # one.drawLuminosity(surface)
        # one.draw(surface)

        return


class Circle:
    def __init__(self, color, x, y, radius, width=0):
        pos = x, y
        self.color = color
        self.x = x
        self.y = y
        self.pos = pos
        self.r = radius
        self.width = width

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.r, self.width)


class Star(Circle):  # radius: 2-5 color: WHITE
    def __init__(self, color, x, y, radius, width=0):
        Circle.__init__(self, color, x, y, radius, width)

    def drawLuminosity(self, surface):
        radius = self.r * 1.5
        dif = 40
        color = (self.color[0] - dif, self.color[1] - dif, self.color[2] - dif)

        pygame.draw.circle(surface, color, self.pos, int(radius), self.width)


class Planet(Circle):
    def __init__(self, color, x, y, radius, width=0):
        Circle.__init__(self, color, x, y, radius, width)
        shapes = {"circle1": (self.getRandomColor(), (self.x + int(self.r / 10), self.y + int(self.r / 10)),
                             int(self.r / 5)),
                  "ellipse": (self.getRandomColor(), pygame.Rect(self.x - (self.r + (self.r / 10)),
                                                                 self.y - (self.r + (self.r / 10)),
                                                                 self.r, (self.r / 2))),
                  "circle2": (self.getRandomColor(), (self.x - int(self.r / 2), self.y + (self.r - int(self.r / 2))),
                              int(self.r / 3))}
        self.shapes = shapes

    def drawBlotches(self, surface):
        for shape in self.shapes:
            if "circle" in shape:
                pygame.draw.circle(surface, self.shapes[shape][0], self.shapes[shape][1], self.shapes[shape][2])
            elif shape == "ellipse":
                pygame.draw.ellipse(surface, self.shapes[shape][0], self.shapes[shape][1])
        pygame.draw.circle(surface, BLACK, self.pos, (self.r * 2) - int(self.r / 2), int(self.r / 2) + 5)

    def getRandomColor(self):
        colors = []
        lightercolor = ()
        for i in range(len(self.color)):
            if self.color[i] <= 215:
                lightercolor = lightercolor + (self.color[i] + 40,)
            else:
                lightercolor = lightercolor + (255,)
        colors.append(lightercolor)

        darkercolor = ()
        for i in range(len(self.color)):
            if self.color[i] >= 40:
                darkercolor = darkercolor + (self.color[i] - 40,)
            else:
                darkercolor = darkercolor + (0,)
        colors.append(darkercolor)

        complementarycolor = ()
        for i in range(len(self.color)):
            if self.color[i] >= 127:
                complementarycolor = complementarycolor + (self.color[i] - 100,)
            else:
                complementarycolor = complementarycolor + (self.color[i] + 100,)
        colors.append(complementarycolor)
        color = choice(colors)
        return color


# ACM.CS.DIXIE.EDU
