#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


"""
   | Se implementa la asignación de Fitness conocida como Linear Ranking **(ó Ranking Lineal)**.
   | Es denominada así porque el Fitness se asigna con una función lineal que tiene como
    fundamento la posición que ocupa el Individuo dentro de la Población.   
   | El procedimiento es: tomando en cuenta el ranking asignado a los Individuals 
    **(ó Individuos)** por la clase Community **(véase Model/Community/Community.py)** 
    se ordenan de acuerdo a este valor y entonces el Fitness se basa en la posición 
    que cada uno de los Individuos ocupa. Más en específico, el Fitness está proporcionado 
    por la siguiente fórmula:  
   .. centered:: :math:`Fitness(Individuo) = 2 - SP + \\frac{2 \\cdot (SP - 1) \\cdot posici\\acute{o}n(Individuo)}{tama\\tilde{n}o\_poblaci\\acute{o}n - 1}`
   | Donde:
   |       **SP (Selective Pressure ó Presión Selectiva)** es un valor que oscila entre 1 y 2.
   |       **Posición(Individuo)** es la que ocupa el Individuo de acuerdo al rank.  
   |
   | Haciendo un análisis somero en la fórmula, se puede apreciar que los 
    Individuos con mejor Fitness serán aquéllos que se encuentren en las últimas posiciones, 
    sin embargo los rankings que se manejan en este proyecto son inversamente proporcionales 
    a la calidad de los Individuos **(véase Model/Community/Community.py)**; 
    por ello es importante ordenar a los Individuos de manera descendente para que la operación tenga sentido.
   | La función encargada de esto se llama sort_individuals y está en **Model/Community/Population/Population.py**.
"""


def assign_fitness(population,fitness_parameters):
    """
       Se realiza la implementación del Fitness de tipo Linear Ranking
       **(ó Ranking Lineal)** tomando en cuenta los datos proporcionados
       en la parte superior.
    """

    #Se crea una variable para ir obteniendo el Fitness
    #de todos los Individuos y sumarlo aquí.
    total_fitness = 0

    #Se toma el valor de SP.
    sp = fitness_parameters["sp_linear_ranking_fitness"] 

    #Se ordenan los Individuos con base en el rank en orden descendente, 
    #esto significa que Individuos con alto rank van a la izquierda
    #y por lo tanto en este caso se les asigna Fitness bajo. Por el contrario
    #a los que están a la derecha se les asigna alto Fitness.
    population.sort_individuals("get_rank",True)

    #Se mantiene la posición del primer elemento.
    posicion = 1
    
    #Por cada Individuo en la Población se hace lo siguiente:     
    for individual in population.get_individuals():

        #Se le asigna el Fitness con base en la fórmula ya especificada.
        current_fitness = 2.0 - sp + 2.0 * (sp - 1.0) * (posicion/(population.get_size() - 1.0))
        individual.set_fitness(current_fitness)

        #Se actualiza el Fitness total.
        total_fitness += current_fitness        

        #Se actualiza la posición.
        posicion += 1
  
    #Con las siguientes directivas, se actualiza el Fitness total de la Población
    #y se calculan propiedades grupales (véase Community/Population/Population.py).
    population.set_total_fitness(total_fitness) 
    population.calculate_population_properties()
