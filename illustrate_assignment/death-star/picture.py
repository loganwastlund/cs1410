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


class Picture:

    def __init__( self, width, height ):
        self.mWidth = width
        self.mHeight = height

        return

    # methods for user interface

    # draws the current state of the system
    def draw( self, surface ):
        
        # rectangle to fill the background
        rect = pygame.Rect( int ( 0 ), int ( 0 ), int ( self.mWidth ), int ( self.mHeight ) )
        pygame.draw.rect( surface, BLACK, rect, 0 )
        one = Star(WHITE, 300, 300, 10)
        one.drawLuminosity(surface)
        one.draw(surface)

        return


class Circle:
    def __init__(self, color, x, y, radius, width=0):
        pos = x, y
        self.color = color
        self.pos = pos
        self.r = radius
        self.width = width

    def draw(self, surface):
        pygame.draw.circle(surface, self.color, self.pos, self.r, self.width)


class Star(Circle):
    def __init__(self, color, x, y, radius, width=0):
        Circle.__init__(self, color, x, y, radius, width)

    def drawLuminosity(self, surface):
        radius = self.r * 1.5
        dif = 40
        color = (self.color[0] - dif, self.color[1] - dif, self.color[2] - dif)

        pygame.draw.circle(surface, color, self.pos, int(radius), self.width)
