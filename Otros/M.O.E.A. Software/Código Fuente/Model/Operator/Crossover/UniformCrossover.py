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
   | Se lleva a cabo la implementación de la técnica conocida como Uniform Crossover
    **(ó Cruza Uniforme)**.
   | Primero que nada esta operación está fabricada para usarse tanto con la Representación
    Cromosómica **(véase Model/ChromosomalRepresentation)**
    de tipo FloatPoint **(ó Punto Flotante)** como Binary **(ó Binaria)**.
   |
   | La característica de este procedimiento es crear nuevos Individuos intercambiando 
    secuencialmente los genes de sus padres; visto de una manera más estructurada consiste en lo siguiente:
   * Tenemos a los cromosomas de los padres Padre A: :math:`A_1A_2...A_n` 
    y Padre B: :math:`B_1B_2...B_n`
   * Ahora, cada hijo será construido con genes de uno y sólo uno de los padres a menos que se indique lo contrario; este movimiento será posible con una variable denominada Pmask **(Pm)** que toma valores de 0 a 1 y una probabilidad de Pmask **(Pp)** que también toma valores de 0 a 1. Entonces lo anterior se puede declarar así:   
    * Para el hijo :math:`(H_1)` que tomará sus genes del padre A **(PA)**: 
     Si :math:`Pm \leqslant Pp\ entonces\ H_1(i) = A_i,\ en\ otro\ caso\ H_1(i) = B_i; 1 \leqslant i \leqslant n`
    * Para el hijo :math:`(H_2)` que tomará sus genes del padre B **(PB)**: 
     Si :math:`Pm \leqslant Pp\ entonces\ H_2(i) = B_i,\ en\ otro\ caso\ H_1(i) = A_i; 1 \leqslant i \leqslant n`
   |
"""


def execute_crossover_technique(chromosome_a,chromosome_b,crossover_parameters):
    """
       Tomando en cuenta la información proporcionada con anterioridad, 
       se implementa el método conocido como Uniform Crossover **(ó Cruza Uniforme)**.
    """

    #Se obtiene el calor del parámetro para la probabilidad
    #de Cruza.
    crossover_probability = crossover_parameters["probability_crossover_general"]

    #Se crean referencias a los hijos.
    chromosome_child_1 = []
    chromosome_child_2 = []

    #Se toma un número que servirá para verificar 
    #la probabilidad de cruza.
    number = aleatorio.random()

    #Si el número recién creado es menor o igual que la probabilidad de cruza,
    #significa que se debe hacer la recombinación genética.
    if number <= crossover_probability:

       #Se adquiere el valor concerniente al pmask.
       crossover_pmask = crossover_parameters["pmask_uniform_crossover"]

       #La siguiente operación se hace para cada gen:
       for x in range(len(chromosome_a)):

           #Se crea un número aleatorio que servirá para verificar el valor del pmask.
           pmask = aleatorio.random()

           #Si el valor creado es menor o igual al pmask obtenido por parámetro,
           #significa que el gen actual de cada cromosoma será el gen del padre contrario.
           if pmask <= crossover_pmask:
              chromosome_child_1 += [chromosome_b[x]]
              chromosome_child_2 += [chromosome_a[x]]

           #Si la condición descrita es falsa entonces el gen actual constará del 
           #gen de su padre por defecto.
           else:
               chromosome_child_1 += [chromosome_a[x]]
               chromosome_child_2 += [chromosome_b[x]]
    
    #En el caso en que la condición descrita anteriormente sea false no se realiza
    #ninguna acción y los hijos resultan en copias idénticas de los padres.
    else:
         chromosome_child_1 = chromosome_a
         chromosome_child_2 = chromosome_b      
 
    #Se regresa el arreglo con los hijos.
    return [chromosome_child_1,chromosome_child_2]
