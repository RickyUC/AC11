from random import shuffle
import gui

app = QApplication([])
window = Prograrice()
window.show()
sys.exit(app.exec_())


class Memorize:

    def __init__(self):
        self.cards = [[i, False] for i in range(1, 13)]
        for i in range(1, 13):
            self.cards.append(i)
        self.cards.append("b")
        shuffle(self.cards)
        self.tries = 0

    def draw_cards(self, i, j):
        self.cards_[i][1] = True
        if self.cards[i][0] == "b":
            self.tries += 10
            window.actualizar_intentos(self.tries)
            return window.agregar_func_ocultar(self.ocultar(i))
        self.cards[j][1] = True
        if self.cards[j][0] == "b":
            self.tries += 10
            window.actualizar_intentos(self.tries)
            return window.agregar_func_ocultar(self.ocultar(i, j))
        self.tries += 1
        window.actualizar_intentos(self.tries)
        if self.cards[i][0] == self.cards[j][0]:
            return True
        else:
            return window.agregar_func_ocultar(self.ocultar(i, j))

        def ocultar(self, i, j=None):
            j = j if j else None
            self.cards[i][1] = False
            if j:
                self.cards[j][1] = False
