__author__ = 'Ricardo Del Río', 'Tomás Verdugo'

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtTest import QTest

from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize

from os import sep
from sys import exit
from time import sleep


from new_backend import PBackend


class Prograrice(QWidget):
    def __init__(self):
        super().__init__()
        self.init_GUI()
        self.primera_carta = False

    def init_GUI(self):

        #Cartas reverso:
        carta_reverso = QPixmap('Imgs'+sep+'back.png')
        carta_reverso = carta_reverso.scaled(100,100)
        icon = QIcon()
        icon.addPixmap(carta_reverso)

        # Grilla con las imagenes
        self.grilla = QGridLayout()
        posiciones = [(i, j) for i in range(5) for j in range(5)]
        for posicion in posiciones:
            boton = QPushButton(self)
            boton.setIcon(icon)
            size = QSize(90,90)
            boton.setIconSize(size)
            boton.setFixedSize(100,100)
            boton.clicked.connect(self.click_sobre_imagen)
            self.grilla.addWidget(boton, *posicion)

        # Etiquetas
        self.intentos = QLabel('Intentos: 0', self)
        self.tiempo_restante = QLabel('Tiempo Restante: ', self)

        self.titulo = QLabel(self)
        self.titulo.setText('PROGRARICE')

        # Boton Ocultar
        self.ocultar = QPushButton(self)
        self.ocultar.setText('Ocultar')
        self.ocultar.setFixedSize(100,30)

        # Layouts
        hbox1 = QHBoxLayout()
        hbox1.addStretch(1)
        hbox1.addWidget(self.titulo)
        hbox1.addStretch(1)
        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.tiempo_restante)
        hbox2.addStretch(1)
        hbox2.addWidget(self.intentos)
        hbox3 = QHBoxLayout()
        hbox3.addStretch(4)
        hbox3.addWidget(self.ocultar)

        vbox = QVBoxLayout()
        vbox.addStretch(2)
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(self.grilla)
        vbox.addStretch(1)
        vbox.addLayout(hbox3)
        vbox.addStretch(2)
        self.setLayout(vbox)

        # Ventana principal:
        self.setWindowTitle('Prograrice')
        self.setWindowIcon(icon)
        self.setGeometry(100, 100, 500, 600)
        self.show()

    def actualizar_intentos(self):
        self.intentos.setText('Intentos: {}'.format(PBackend.tries))

    def click_sobre_imagen(self):
        print('1')
        apretado = self.sender()
        idx = self.grilla.indexOf(apretado)
        print(idx)
        if PBackend.se_puede_presionar(idx):
            print('2')
            carta_anverso = QPixmap('Imgs{0}{1}.png'.format(sep, PBackend.cards[idx][0]))
            carta_anverso = carta_anverso.scaled(100, 100)
            icon = QIcon()
            icon.addPixmap(carta_anverso)
            apretado.setIcon(icon)
            size = QSize(90, 90)
            apretado.setIconSize(size)
            # PBackend.draw(idx)
            self.actualizar_intentos()

            if self.primera_carta:
                sleep(3)
                # PBackend.ocultar()

                self.primera_carta = False

        else:
            pass

    def agregar_func_ocultar(self,funcion):
        self.ocultar.clicked.connect(funcion)

    '''def ocultar_todo(self):
        posiciones = [(i, j) for i in range(5) for j in range(5)]
        i = 1
        for posicion in posiciones:
            if self

            boton = QPushButton(self)
            boton.setIcon(icon)
            size = QSize(90, 90)
            boton.setIconSize(size)
            boton.setFixedSize(100, 100)
            boton.clicked.connect(self.click_sobre_imagen)
            self.grilla.addWidget(boton, *posicion)

            self.grilla.

            i += 1'''



if __name__ == '__main__':
    app = QApplication([])
    window = Prograrice()
    window.show()
    exit(app.exec_())
