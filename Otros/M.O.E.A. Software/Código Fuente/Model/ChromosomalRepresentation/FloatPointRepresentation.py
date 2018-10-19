#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


import random as aleatorio


"""
   | Este script contiene todas las funcionalidades requeridas para que se pueda hacer uso de una
    codificación de tipo Float Point **(ó Punto Flotante)**; ésto significa que los alelos que
    conforman al cromosoma serán números de punto flotante. 
   | Un número de punto flotante es aquél que tiene una parte entera y una decimal; cabe mencionar que 
    si el número en cuestión no tiene expansión decimal, se le considera un número entero.
"""


def calculate_length_subchromosomes(vector_variables,number_of_decimals,representation_parameters):
    """
       | Realiza el cálculo de subcromosomas de acuerdo a la representación Float Point **(ó Punto Flotante)**.
       | Esta función es de aquéllas que se tienen que implementar obligatoriamente.
    """
   
    #Dado que es una representación de Punto Flotante, la longitud de cada subcromosoma es 1,
    #entonces si hay k variables de decisión; dicho de otra forma, si hay k variables de decisión
    #la longitud total del súper cromosoma es k porque sólo se ocupa un número por alelo.
    #En el código se agrega [1] para que pueda hacerse la asignación de espacio sin problemas.
    #El "1" que se encuentra dentro es inofensivo y se cambia en posteriores métodos.
    return [1]*len(vector_variables)


def create_chromosome(length_subchromosomes,vector_variables,number_of_decimals,representation_parameters):
    """ 
       | Crea un cromosoma con contenido de punto flotante.
       | Esta función es de aquéllas que se tienen que implementar obligatoriamente.
    """

    #La cadena de precisión sirve para acotar el número de decimales exactamente a los que pida el usuario.
    precision_string = "{0:." + str(number_of_decimals) + "f}"

    #Se crea el cromosoma vacío.
    chromosome = []

    #Por cada variable de decisión de hace lo siguiente:
    for single_variable in vector_variables:     
        #Se toma el nombre de la variable y sus límites.
        variable_range = single_variable[1]
        lower_limit = variable_range[0]
        upper_limit = variable_range[1]

        #Ahora se crea un número aleatorio que ronde entre el límite inferior y límite superior, ambos
        #límites a intervalo cerrado, después simplemente se agrega el resultado en el cromosoma
        #verificando con la cadena de precisión que el número de decimales es el indicado.
        number = aleatorio.uniform(lower_limit,upper_limit)
        chromosome.append(float(precision_string.format(number)))

    #Se regresa el súper cromosoma.
    return chromosome


def evaluate_subchromosomes(complete_chromosome,length_subchromosomes,vector_variables,number_of_decimals,representation_parameters): 
    """
       Toma cada porción de cromosoma y la evalúa para luego ser asignada
       a la variable de decisión correspondiente. Este método es de los que se
       debe de implementar obligatoriamente.
    """

    #Se inicializan algunas variables para poder hacer la evaluación.
    value = 0
    variable_name = ""
    single_variable = ""
    variable_name = ""
    decision_variables = {}

    #Por cada porción del súper cromosoma se hace lo siguiente:
    for i in range(len(complete_chromosome)):
        #Se sabe que, dado que se trata de un cromosoma de punto flotante,
        #cada sección la ocupa un sólo número, entonces se toma ese número
        #y se asigna a la variable de decisión correspondiente.

        #Se toma el subcromsoma (que es un sólo valor).
        value = complete_chromosome[i]

        #Se toma la variable de decisión.
        single_variable = vector_variables[i]
        variable_name = single_variable[0]

        #Se hace la asignación de la variable de decisión y su valor otorgado.
        decision_variables[variable_name] = value

    #Se regresa el diccionario con las variables de decisión y sus valores.
    return decision_variables
