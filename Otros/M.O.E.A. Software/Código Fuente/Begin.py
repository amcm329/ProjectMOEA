#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "acuarium_329@hotmail.com"
__status__ = "Production"


from View.MainWindow import MainWindow


"""
   Este archivo funge como un launcher (disparador)
   el cual simplemente crea y ejecuta la ventana principal.
"""


#Se crea una instancia de la ventana principal
main_window = MainWindow()

#Se ejecuta el método run
main_window.run()
