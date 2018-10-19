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
   | Se implementa el método de selección conocido como Roulette **(ó Ruleta)**. También es llamado 
    Proportional Selection **(ó Selección Proporcional)**.
   | En la función se distinguen dos etapas principales: construir la ruleta y "ponerla a girar" para que se elija el elemento.
   * Para la primera etapa se toma como base el Valor Esperado **(ó Expected Value)** de cada Individuo **(véase Model/Community/Population/Individual.py)**. 
    El Valor Esperado para fines de este proyecto es el número de "hijos" que un Individuo puede ofrecer. Éste se calcula de la siguiente forma:
   .. centered:: :math:`Valor\_Esperado(Individuo) = \\frac{tama\\tilde{n}o\_poblaci\\acute{o}n \cdot Fitness(Individuo)}{\sum_{i=1}^{tama\\tilde{n}o\_poblaci\\acute{o}n}Fitness(Individuo_i)}`
   | Al final aquéllos con Valores Esperados altos tendrán lugar a mayores espacios en la ruleta y por ende su probabilidad de elección aumenta.
   * Para recorrer la ruleta en realidad se toma un valor aleatorio entre 0 y la suma de los Valores Esperados. Entonces se van sumando los Valores  Esperados de los Individuos hasta que se exceda el valor aleatorio mencionado antes. Aquel elemento cuyo Valor Esperado haya excedido la suma se considera el elegido y es seleccionado para la etapa de cruza.
   | Para la selección de Individuos se efectúa la segunda operación tantas veces como el tamaño de la Población. 
   | Cabe mencionar que el Valor Esperado ya se calcula de manera automática en este proyecto **(véase Model/Community/Population/Population.py)**.
"""


def execute_selection_technique(population,selection_parameters):
    """
       De acuerdo al proceso descrito anteriormente, se implementa
       la técnica conocida como Roulette **(ó Ruleta)**.
    """

    #Aquí se almacenarán los cromosomas de los Individuos elegidos.
    chromosome_set = []

    #Se obtienen los valores del tamaño de la Población y el
    #valor esperado de la Población para construir la ruleta.
    population_size = population.get_size()
    total_expected_value = population.get_total_expected_value()

    #A continuación se obtienen los Individuos de la Población.
    my_population = population.get_individuals()
    
    #El siguiente procedimiento se realiza tantas veces como el 
    #tamaño de la Población.
    for x in range (population_size):
        #Se crea el número aleatorio para "girar la ruleta".
        random_expected = aleatorio.uniform(0,total_expected_value)

        #Count es una variable que mantiene control cuando se dé el caso
        #en que todos los elementos se han recorrido y aún no se excede el
        #valor del número aleatorio.
        count = 0

        #Aquí se almacenará el Individuo elegido.
        individual = ""
        
        #En esta variable se almacenará la suma acumulada de los Fitness de los 
        #Individuos.
        cumulative_sum = 0.0

        #Esta sección es la equivalente a girar la ruleta, es decir, sumar
        #el Valor Esperado de cada Individuo hasta encontrar al Individuo cuya
        #suma exceda el valor aleatorio. Dicho Individuo será el seleccionado.
        while cumulative_sum < random_expected and count < population_size:
              #Se selecciona el Individuo actual.
              individual = my_population[count]
             
              #Se acumula la suma con el Valor Esperado del Individuo actual.
              cumulative_sum += individual.get_expected_value()

              #Se actualiza el contador de Individuos para el caso de emergencia
              #antes mencionado.
              count += 1
        
        #Se agrega el cromosoma del Individuo cuyo Valor Esperado 
        #excedió al número aleatorio.
        chromosome_set.append(individual.get_complete_chromosome())

    return chromosome_set
