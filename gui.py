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

    def init_GUI(self):

        #Cartas reverso:
        carta_reverso = QPixmap('Imgs'+sep+'back.png')
        carta_reverso = carta_reverso.scaled(120,120)
        self.boton = QPushButton(self)
        icon = QIcon(carta_reverso)
        self.boton.setIcon(icon)


        # Grilla con las imagenes
        self.grilla = QGridLayout()
        posiciones = [(i*40, j*40) for i in range(5) for j in range(5)]
        for posicion in posiciones:
            self.grilla.addWidget(self.boton, *posicion)

        # Etiquetas
        self.intentos = QLabel('Intentos: 0', self)
        self.intentos.move(10, 59)
        self.tiempo_restante = QLabel('Tiempo Restante: ', self)

        self.titulo = QLabel(self)
        self.titulo.setText('Prograrice')
        self.titulo.move(400, 15)

        # Boton Ocultar
        self.ocultar = QPushButton(self)
        self.ocultar.setText('Ocultar')
        self.ocultar.move(10, 600)

        # Layouts
        vbox = QVBoxLayout()
        vbox.addStretch(10)
        vbox.addWidget(self.titulo)
        vbox.addWidget(self.tiempo_restante)
        vbox.addWidget(self.intentos)
        self.setLayout(self.grilla)
        vbox.addWidget(self.ocultar)

        vbox.addStretch(1)
        self.setLayout(vbox)

        # Ventana principal:
        self.setWindowTitle('Prograrice')
        self.setGeometry(300, 300, 800, 800)
        self.show()

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
