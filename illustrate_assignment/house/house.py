import pygame
from random import randrange, choice

Black = (0, 0, 0)
White = (255, 255, 255)
Red = (150, 0, 0)
Blue = (0, 0, 150)
SkyBlue = (50, 100, 200)
Green = (0, 150, 0)
Yellow = (220, 220, 110)
Brown = (150, 75, 0)


class Picture:
    def __init__(self, width, height):
        self.mWidth = width
        self.mHeight = height

        self.objects = []
        self.createObjects()

        return

    def createObjects(self):
        sky = Sky(SkyBlue, self.mWidth, self.mHeight)
        house = House(150, 200)

        self.objects.append(sky)
        self.objects.append(house)

        return

    def draw(self, surface):
        for object in self.objects:
            object.draw(surface)

        return


class Cloud:
    def __init__(self, color, width, height, x, y):
        self.color = color
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        self.rect = self.width, self.height, self.x, self.y

    def draw(self, surface):
        pygame.draw.ellipse(surface, self.color, self.rect)


class Sky:
    def __init__(self, color, width, height):
        self.scolor = color
        self.wwidth = width
        self.wheight = height
        self.x = 0
        self.y = 0
        self.rect = (self.x, self.y, self.wwidth, self.wheight)

        self.cloudcolors = [(200, 200, 200), (140, 140, 140)]
        self.clouds = []
        self.getClouds()

    def getClouds(self):
        num_of_clouds = randrange(3, 15)
        for num in range(num_of_clouds):
            color = choice(self.cloudcolors)
            x = randrange(10, self.wwidth - 10)
            y = randrange(5, int(self.wheight / 2))
            width = randrange(100, 200)
            height = randrange(60, 100)
            newcloud = Cloud(color, x, y, width, height)
            self.clouds.append(newcloud)

    def draw(self, surface):
        pygame.draw.rect(surface, self.scolor, self.rect)
        for cloud in self.clouds:
            cloud.draw(surface)


class Window:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 60
        self.height = 60
        self.thick = 5
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface):
        pygame.draw.rect(surface, Green, self.rect)
        pygame.draw.rect(surface, Black, self.rect, self.thick)
        pygame.draw.line(surface, Black, (int(self.x + self.width / 2), self.y),
                         (int(self.x + self.width / 2), self.y + self.height), 3)
        pygame.draw.line(surface, Black, (self.x, int(self.y + self.height / 2)),
                         (self.x + self.width, int(self.y + self.height / 2)), 3)


class Door:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 75
        self.height = 150
        self.thick = 7
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, surface):
        pygame.draw.rect(surface, Blue, self.rect)
        pygame.draw.rect(surface, Black, self.rect, self.thick)
        pygame.draw.circle(surface, Black, (self.x + 60, self.y + 60), 8)


class Roof:
    def __init__(self, x, y, house):
        self.x = x
        self.y = y
        self.points = [(self.x, self.y)]
        self.thick = 10
        self.house = house
        self.getPoints()

    def getPoints(self):
        x1 = self.house.x - 100
        y = self.house.y
        x2 = self.house.x + self.house.width + 100
        self.points.insert(0, (x1, y))
        self.points.append((x2, y))

    def draw(self, surface):
        pygame.draw.polygon(surface, Brown, self.points)
        pygame.draw.polygon(surface, Black, self.points, 10)


class House:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 400
        self.height = 400
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.thick = 10

        self.windows = []
        self.getWindows()
        self.door = None
        self.getDoor()
        self.roof = None
        self.getRoof()

    def getWindows(self):
        num_of_windows = randrange(2, 4)
        xs = [225, 425, 225]
        ys = [275, 275, 450]
        for num in range(num_of_windows):
            x = xs[num]
            y = ys[num]
            window = Window(x, y)
            self.windows.append(window)

    def getDoor(self):
        if len(self.windows) == 3:
            x = 400
            y = 450
        else:
            x = 315
            y = 450
        self.door = Door(x, y)

    def getRoof(self):
        self.roof = Roof(350, 75, self)

    def draw(self, surface):
        pygame.draw.rect(surface, Yellow, self.rect)
        pygame.draw.rect(surface, Black, self.rect, self.thick)
        for window in self.windows:
            window.draw(surface)
        self.door.draw(surface)
        self.roof.draw(surface)
