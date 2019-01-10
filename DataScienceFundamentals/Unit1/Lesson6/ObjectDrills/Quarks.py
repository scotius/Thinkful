class Quark(object):
    def __init__(self, color, flavor):
        self.color = color
        self.flavor = flavor
    baryon_number = 1 / 3

    def interact(self, inputQuark):
         tempColor1 = self.color
         tempColor2 = inputQuark.color
         self.color = tempColor2
         inputQuark.color = tempColor1
