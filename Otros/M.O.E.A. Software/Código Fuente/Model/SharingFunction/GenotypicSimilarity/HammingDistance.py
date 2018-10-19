#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


"""
   | La Distancia de Hamming **(ó Hamming Distance)** es una implementación
    perteneciente a la subcategoría Genotypic Similarity **(ó Similaridad Genotípica)**.
   | Esta consiste en comparar los alelos entre los cromosomas de los Individuos y devolver un valor numérico
    que indica en cuántos alelos los cromosomas de los Individuos resultaron tener valores diferentes.
   | Como consecuencia lógica, la magnitud de la Distancia de Hamming es inversamente proporcional a la calidad
    de los Individuos.
   |
   | Es ampliamente usada para la Representación Cromosómica **(véase Model/ChromosomalRepresentation)**
    de tipo Binario **(ó Binary)**, aunque su uso no se limita sólo a esta codificación. 
   |
   | Con respecto del cálculo del :math:`\sigma_{share}`, éste se hace tomando en cuenta el número máximo 
    permitido de genes diferentes entre dos cromosomas cualesquiera.
   | Dicha cantidad es deducida solicitándole al usuario únicamente el porcentaje máximo permitido, con base
    en éste se determina entonces el número en concreto.
"""


def calculate_sigma_share(population,sharing_function_parameters):
    """
       Basándose en las indicaciones mencionadas anteriormente, se
       lleva a cabo la implementación de la obtención del valor Sigma Share.
    """
        
    #Aquí se almacena el tamaño total del cromosoma.
    distance = 0.0

    #A continuación se obtienen las longitudes de los subcromosomas
    #(véase Model/ChromosomalRepresentation).
    length_subchromosomes = sharing_function_parameters["length_subchromosomes"]

    #Se obtiene de la sección View el parámetro asociado al porcentaje de tolerancia,
    #es decir, la tolerancia máxima de genes del cromosoma visto como porcentaje
    #para considerar a dos cromosomas dentro del mismo Niche.
    percentage_of_acceptance = sharing_function_parameters["percentage_of_acceptance"]
 
    #Se suman las longitudes de los subcromosomas y se almacena el resultado
    #en la variable distance.
    for current_length in length_subchromosomes: 
        distance += current_length

    #Se regresa el número máximo real de genes en el cromosoma que permiten
    #considerar una distancia como válida, es decir, que se encuentra en el mismo Niche.
    return int(distance*percentage_of_acceptance)


def calculate_distance(individual_i,individual_j,sharing_function_parameters):
    """
       Con base en la información proporcionada anteriormente, se implementa
       el cálculo de la distancia entre dos Individuos apoyándose de la técnica
       conocida como Distancia de Hamming **(ó Hamming Distance)**.
    """

    #Aqui se almacenará la distancia de Hamming.
    hamming_distance = 0.0
    
    #Se toman los cromosomas de los Individuos participantes.
    chromosome_i = individual_i.get_complete_chromosome()
    chromosome_j = individual_j.get_complete_chromosome()
    
    #Se obtiene la longitud de una de las cadenas cromosómicas, la cual es la misma
    #en ambos Individuos.
    length_chromosome = len(chromosome_i)

    #Por cada gen en los cromosomas se hace lo siguiente:
    for x in range (length_chromosome):
 
        #Se obtiene el gen de cada Individuo localizado en la misma posición
        #en el cromosoma.
        gen_i = chromosome_i[x]
        gen_j = chromosome_j[x]

        #Se realiza la comparación pertinente, si sus alelos son diferentes
        #se actualiza el valor de la Distancia de Hamming.
        if gen_i != gen_j:
           hamming_distance += 1

    #Se regresa la distancia de Hamming.
    return hamming_distance
