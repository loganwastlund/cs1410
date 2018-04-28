
class Ball:
    def __init__(self, size, min_x, max_x, min_y, max_y, left_paddle_x, right_paddle_x):
        self.mX = min_x
        self.mY = min_y
        self.mSize = size
        self.mDX = 0
        self.mDY = 0
        self.mMinX = min_x
        self.mMaxX = max_x
        self.mMinY = min_y
        self.mMaxY = max_y
        self.LeftPaddleX = left_paddle_x
        self.LeftPaddleMinY = min_y
        self.LeftPaddleMaxY = max_y
        self.RightPaddleX = right_paddle_x
        self.RightPaddleMinY = min_y
        self.RightPaddleMaxY = max_y

    def getX(self):
        return self.mX
    def getY(self):
        return self.mY
    def getSize(self):
        return self.mSize
    def getDX(self):
        return self.mDX
    def getDY(self):
        return self.mDY
    def getMinX(self):
        return self.mMinX
    def getMaxX(self):
        return self.mMaxX
    def getMinY(self):
        return self.mMinY
    def getMaxY(self):
        return self.mMaxY
    def getLeftPaddleX(self):
        return self.LeftPaddleX
    def getLeftPaddleMinY(self):
        return self.LeftPaddleMinY
    def getLeftPaddleMaxY(self):
        return self.LeftPaddleMaxY
    def getRightPaddleX(self):
        return self.RightPaddleX
    def getRightPaddleMinY(self):
        return self.RightPaddleMinY
    def getRightPaddleMaxY(self):
        return self.RightPaddleMaxY

    def setPosition(self, x, y):
        if self.mMinX < x and x + self.mSize < self.mMaxX:
            if self.mMinY < y and y + self.mSize < self.mMaxY:
                self.mX = x
                self.mY = y

    def setSpeed(self, dx, dy):
        self.mDX = dx
        self.mDY = dy

    def setLeftPaddleY(self, paddle_min_y, paddle_max_y):
        if paddle_max_y > paddle_min_y >= self.mMinY:
            if paddle_max_y <= self.mMaxY:
                self.LeftPaddleMinY = paddle_min_y
                self.LeftPaddleMaxY = paddle_max_y

    def setRightPaddleY(self, paddle_min_y, paddle_max_y):
        if paddle_max_y > paddle_min_y >= self.mMinY:
            if paddle_max_y <= self.mMaxY:
                self.RightPaddleMinY = paddle_min_y
                self.RightPaddleMaxY = paddle_max_y

    def checkTop(self, new_y):
        if new_y >= self.mMinY:
            return new_y
        else:
            self.mDY *= -1
            diff = self.mMinY - new_y
            act_y = self.mMinY + diff
            return act_y

    def checkBottom(self, new_y):
        # print(new_y)
        # print(self.mSize)
        # print(self.mMaxY)
        # print(self.mDY)
        if new_y + self.mSize <= self.mMaxY:
            return new_y
        else:
            self.mDY *= -1
            # print(self.mDY)
            diff = new_y - self.mMaxY
            # print(diff)
            act_y = self.mMaxY - diff
            # print(act_y)
            # print(self.mDX)
            return act_y

    def checkLeft(self, new_x):
        if new_x >= self.mMinX:
            return new_x
        else:
            self.setSpeed(0, 0)
            diff = self.mMinX - new_x
            act_x = self.mMinX + diff
            return act_x

    def checkRight(self, new_x):
        if new_x <= self.mMaxX:
            return new_x
        else:
            self.setSpeed(0, 0)
            diff = new_x - self.mMaxX
            act_x = self.mMaxX - diff
            return act_x
