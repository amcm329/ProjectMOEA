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
   | Se desarrolla la técnica conocida como Torneo Probabilístico **(ó Probabilistic Tournament)**.
   | Tal como lo sugiere el nombre, la selección será llevada a cabo en forma de competencia
    directa entre los Individuos. 
   | Tradicionalmente se comparan sus Fitness y de esta manera el Individuo ganador es aquél con 
    la cantidad mayor de Fitness, pero dado que se maneja un esquema probabilístico la decisión 
    no depende totalmente del factor antes mencionado.
   |
   | De esta manera se pueden recapitular los siguientes pasos:
   * Tomar k :math:`(2 \\leqslant k \\leqslant tama\\tilde{n}o\_poblaci\\acute{o}n)` Individuos de la Población.
   * Realizar el torneo de manera secuencial entre los elementos seleccionados anteriormente, esto es, tomar el elemento A y enfrentarlo con B, al resultado de la batalla anterior enfrentarlo con C y así sucesivamente.
    Para ello por cada encuentro se crea un número aleatorio entre 0 y 1, si el número es menor a 0.5 
    se toma al elemento con menor Fitness, de lo contrario se elige al de mayor Fitness.
    La operación se lleva a cabo hasta que se tenga un ganador de los k Individuos.
   | Los dos pasos anteriores se repiten hasta que se hayan obtenido tantos Individuos 
    como el tamaño de la Población. 
"""


def execute_selection_technique(population,selection_parameters):
    """
       Tomando en cuenta las bases descritas previamente, se implementa
       el método conocido como Probabilistic Tournament **(ó Torneo Probabilístico)**.
    """

    #Se almacenan los cromosomas de los elementos seleccionados.
    chromosome_set = []

    #Se lleva un contador de los elementos seleccionados.
    population_count = 0

    #Se obtienen el tamaño de la Población, así como los Individuos
    #para ser elegidos.
    population_size = population.get_size()
    individuals = population.get_individuals()

    #Se obtiene el parámetro de la cantidad de contrincantes por cada enfrentamiento.
    contenders_amount = selection_parameters["contenders_amount_probabilistic_tournament"]
    
    #El proceso se realizará hasta haber tomado tantos elementos como
    #el tamaño de la población.
    while population_count < population_size:

          #La selección se dividirá en pequeños torneos de tamaño "contenders_amount".
          #Éstos son seleccionados al azar, una vez que se completan los participantes, 
          #se procede a obtener el mejor individuo para ese torneo.
          tournament = []

          #Aquí se agregan los concursantes al torneo.
          for x in range(contenders_amount):
              index = aleatorio.randint(0,population_size - 1)
              tournament.append(individuals[index])

          #En esta sección se toma el ganador del torneo.
          #La idea es la siguiente:
          #Se ponen a competir a los concursantes secuencialmente, de tal manera que el ganador de una
          #ronda anterior competirá con el siguiente individuo en el torneo.
          #Dado que es un torneo probabilístico, se erigirá al ganador de cada ronda con 
          #base en un valor aleatorio entre 0 y 1; si el valor es menor a 0.5 se toma al Individuo 
          #con menor Fitness, en otro caso el que tenga mayor Fitness habrá ganado.
          #Este procedimiento se prosigue hasta obtener un sólo ganador, del cual se 
          #extraerá su cromosoma para la parte de la reproducción.
          best = tournament[0]
          for x in range (1,len(tournament)):

              #Se almacenan los valores del contrincante, así como el Fitness de éste y del
              #mejor Individuo hasta el momento.
              contender = tournament[x]
              individual_higher_fitness = best
              individual_lower_fitness = contender
              
              #Si el Fitness del contrincante es mayor que el del mejor Individuo,
              #Se hace una actualización en las variables concernientes.
              if contender.get_fitness() > best.get_fitness():
                 individual_lower_fitness = best
                 individual_higher_fitness = contender
                   
              #Se crea el número aleatorio, así como la asignación del 
              flip = aleatorio.random()
              
              #Si el número aleatorio es menor a 0.5, se elige el contrincante
              #de menor Fitness, en otro caso se selecciona el de mayor Fitness.
              if flip < 0.5: 
                 best = individual_lower_fitness

              else:
                 best = individual_higher_fitness

          #Se agrega el cromosoma del ganador a la estructura pertinente.              
          chromosome_set.append(best.get_complete_chromosome())

          #Se incrementa el contador de los elementos seleccionados hasta
          #el momento. 
          population_count+=1

    return chromosome_set
