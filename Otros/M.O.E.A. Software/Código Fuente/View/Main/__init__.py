#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


import Home
import DecisionVariable
import ObjectiveFunction
import Population
import GeneticOperator
import MOEA


#Este archivo es creado para desde el exterior se pueda hacer uso de todos los
#elementos contenidos en este directorio, lo cuales se ocupan para conformar
#la Ventana Principal (véase View/MainWindow.py).
#Las categorías existentes son:
#Home (u Hogar).
#Decision Variable (ó Variable de Decisión).
#Objective Function (ó Función Objetivo).
#Population (ó Población).
#Genetic Operator (u Operador Genético).
#M.O.E.A. (Multi Objective Evolutionary Algorithm ó Algoritmo Genético Multi Objetivo).
