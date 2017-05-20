from random import shuffle
from time import sleep

class PBackend:
    def __init__(self):
        self.cards = [[i, False, False] for i in range(1, 13)]
        for i in range(1, 13):
            self.cards.append(i)
        self.cards.append("b")
        shuffle(self.cards)
        self.tries = 0
        self.first = False

    def draw(self, i):
        if not self.first:
            self.cards[i][1] = True
            if self.cards[i][0] == "b":
                self.tries += 10
            else:
                self.first = True
                self.second = False
        elif self.firt:
            self.cards[i][1] = True
            if self.cards[i][0] == "b":
                self.tries += 10
            else:
                self.tries += 1
            self.first = False
            if self.cards[i][0] == self.cards[j][0]:
                self.cards[i][2] = True
                self.cards[i][2] = True

    def se_puede_presionar(self, i):
        print('Si entro a se_puede_presiona()')
        if self.cards[i][1]:
            return False
        return True

    def ocultar(self, i):
        for carta in self.cards:
            if not carta[i][2]:
                carta[i][1] == False



        j = j if j else None
        self.cards[i][1] = False
        if j:
            self.cards[j][1] = False
        return self.draw_first(i)




