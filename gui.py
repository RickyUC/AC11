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

        # Grilla con las imagenes
        self.grilla = QGridLayout()

        # Etiquetas
        self.intentos = QLabel('Intentos: 0', self)
        self.tiempo_restante = QLabel('Tiempo Restante: ', self)

        self.titulo = QLabel(self, 'Prograrice')

        # Boton Ocultar
        self.ocultar = QPushButton(self)
        self.ocultar.setText('Ocultar')
        self.ocultar.clicked.connect() # falta: funcion

        # Layouts


        # Ventana principal:
        self.setWindowTitle('Prograrice')
        self.setGeometry(100, 100, 200, 300)
        self.show()

    def actualizar_intentos(self, numero):
        self.intentos.setText('Intentos: {}'.format(numero))

if __name__ == '__main___':
    app = QApplication([])
    window = Prograrice()
    window.show()
    sys.exit(app.exec_())


'''
icon = QtGuii.QPixmap()
button = QtGui.QPushBoton(self)
buton.setIcon(icon)
'''