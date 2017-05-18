__author__ = 'Ricardo Del Río', 'Tomás Verdugo'

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout, QGridLayout
from PyQt5.QtWidgets import QPushButton, QLabel
from PyQt5.QtTest import QTest

from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt, QSize



import sys

class Prograrice(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_GUI()

    def init_GUI(self):

        #Cartas reverso:
        carta_reverso = QPixmap('Imgs'+sep+'back.png')
        carta_reverso = carta_reverso.scaled(120,120)
        self.boton = QPushButton(self)
        self.boton.setIcon(carta_reverso)

        # Grilla con las imagenes
        self.grilla = QGridLayout()
        posiciones = [(i, j) for i in range(5) for j in range(5)]
        for posicion in posiciones:
            self.grilla.addWidget(self.boton, *posicion)

        # Etiquetas
        self.intentos = QLabel('Intentos: 0', self)
        self.tiempo_restante = QLabel('Tiempo Restante: ', self)

        self.titulo = QLabel(self, 'Prograrice')

        # Boton Ocultar
        self.ocultar = QPushButton(self)
        self.ocultar.setText('Ocultar')

        # Layouts
        vbox = QVBoxLayout()
        vbox.addStretch(1)
        vbox.addWidget(self.titulo)
        vbox.addWidget(self.tiempo_restante)
        vbox.addWidget(self.intentos)
        vbox.addLayout(self.grilla)
        vbox.addWidget(self.ocultar)
        vbox.addStretch(1)
        self.setLayout(vbox)

        # Ventana principal:
        self.setWindowTitle('Prograrice')
        self.setGeometry(100, 100, 200, 300)
        self.show()

    def actualizar_intentos(self, numero):
        self.intentos.setText('Intentos: {}'.format(numero))

    def agregar_func_ocultar(self,funcion):
        self.ocultar.clicked.connect(funcion)

    def imagenes_a_mostrar(self,lista):
        for nombre_imagen in lista:
            pass




if __name__ == '__main___':
    app = QApplication([])
    window = Prograrice()
    window.show()
    sys.exit(app.exec_())

