class Vector(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def add(self, b):
        addVectorx = (self.x + b.x)
        addVectory = (self.y + b.y)
        return Vector(addVectorx, addVectory)
