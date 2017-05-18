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

    def draw_first(self, i):
        self.cards_[i][1] = True
        if self.cards[i][0] == "b":
            self.tries += 10
            window.actualizar_intentos(self.tries)
            return window.agregar_func_ocultar(self.ocultar(i))
        return self.draw_second(i, j)

    def draw_second(self, i, j):
        self.cards[j][1] = True
        if self.cards[j][0] == "b":
            self.tries += 10
            window.actualizar_intentos(self.tries)
            return window.agregar_func_ocultar(self.ocultar(i, j))
        self.tries += 1
        window.actualizar_intentos(self.tries)
        if self.cards[i][0] == self.cards[j][0]:
            return self.win()
        else:
            return window.agregar_func_ocultar(self.ocultar(i, j))

        def ocultar(self, i, j=None):
            j = j if j else None
            self.cards[i][1] = False
            if j:
                self.cards[j][1] = False
            return self.draw_first(i)

        def win(self):
            for i in self.cards:
                if i[1] == "b":
                    continue
                if not i[1]:
                    return self.draw_cards()
            return True  # boton de ganar
