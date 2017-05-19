__author__ = 'Ricardo Del Río', 'Tomás Verdugo'

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtTest import QTest

from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize

from os import sep


import sys


class Prograrice(QWidget):
    def __init__(self):
        super().__init__()
        self.init_GUI()

        self.c_intentos = 0

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

        # Layouts
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

    def clock_sobre_imagen(self):
        self.c_intentos += 1

    def actualizar_intentos(self, numero):
        self.intentos.setText('Intentos: {}'.format(numero))

    def agregar_func_ocultar(self,funcion):
        self.ocultar.clicked.connect(funcion)

    def imagenes_a_mostrar(self,lista):
        for nombre_imagen in lista:
            pass


if __name__ == '__main__':
    app = QApplication([])
    window = Prograrice()
    window.show()
    sys.exit(app.exec_())
