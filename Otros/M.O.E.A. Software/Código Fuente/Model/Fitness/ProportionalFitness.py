#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


"""
   | Se desarrolla la asignación de Fitness conocida como Proportional **(ó Proporcional)**.
   | La función **(ó fórmula)** utilizada es la siguiente:
   .. centered:: :math:`Fitness(Individuo) = \\frac{F_0(Individuo)}{\sum_{i=1}^{tama\\tilde{n}o\_poblaci\\acute{o}n}F_0(Individuo_i)}`
   | Donde:
   |     :math:`F_0` es conocido como el valor de la función objetivo del Individuo. Nótese 
   |     que :math:`F_0` debe ser proporcional al Fitness del Individuo.
   |
   | De acuerdo a la información provista anteriormente, la asignación es llamada así porque, 
    como dice el nombre, el Fitness de un Individuo corresponde a la parte proporcional
    de la cantidad total de :math:`F_0` de la Population **(ó Población)**.
   | De esta manera es posible ajustar los valores para que no existan Fitness dispares.
   | Con respecto de :math:`F_0` es importante considerar que, dado que se está manejando
    un sistema multi objetivo puede haber más de un valor en existencia,  por ello se necesita 
    una cantidad que conjunte estas evaluaciones el cual es el rank, sin embargo el rank es inversamente
    proporcional a la calidad de un Individuo.
   | Entonces se debe hacer una modificación para garantizar que exista un valor
    proporcional al Fitness del Individuo, por lo cual :math:`F_0` se reescribe así:
   .. centered:: :math:`F_0(Individuo) = tama\\tilde{n}o\_poblaci\\acute{o}n - rank(Individuo)`
   | Reescribiendo la fórmula inicial se tiene lo siguiente:
   .. centered:: :math:`Fitness(Individuo) = \\frac{tama\\tilde{n}o\_poblaci\\acute{o}n - rank(Individuo)}{\sum_{i=1}^{tama\\tilde{n}o\_poblaci\\acute{o}n}[tama\\tilde{n}o\_poblaci\\acute{o}n - rank(Individuo_i)]}`
   | Con esta actualización ya es posible obtener un Fitness acorde al rank del Individuo sin alterar
    la esencia de la técnica.
"""


def assign_fitness(population,fitness_parameters):
    """
       Se implementa la asignación de Proportional Fitness **(ó Fitness Proporcional)**
       con base en la información especificada con anterioridad.
    """

    #Este valor almacenará la suma de F0 de cada Individuo.
    total_values = 0.0

    #Este valor almacenará el Fitness total de la Población.
    total_fitness = 0.0

    #Se obtiene el número de Individuos de la Población.
    population_size = population.get_size()

    #Primero se obtiene la suma de F0 de todos los Individuos.
    for individual in population.get_individuals():
        total_values += population_size - individual.get_rank()

    #Usando la cantidad anterior, se hace lo siguiente para cada Individuo:
    for individual in population.get_individuals():

        #Se calcula el Fitness de manera proporcional.
        current_fitness = (population_size - individual.get_rank())/total_values

        #Se actualiza el Fitness del Individuo.
        individual.set_fitness(current_fitness)

        #Se agrega el Fitness actual al total de Fitness de la Población.
        total_fitness += current_fitness

 
    #Se actualiza el Fitness de la Población.   
    population.set_total_fitness(total_fitness)

    #Se actializan propiedades relativas al Fitness para cada Individuo.
    population.calculate_population_properties()
