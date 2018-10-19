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
   | Se determina la técnica conocida como Stochastic Universal Sampling 
    **(ó Muestreo Estocástico Universal)**.
   | Primero que nada es menester mencionar que es necesario el uso del Expected Value **(ó Valor Esperado)** de cada Individuo.
   | Para fines concernientes a este proyecto, se trata del número de "hijos" que un Individuo puede ofrecer. Éste se calcula de la siguiente forma:
   .. centered:: :math:`Valor\_Esperado(Individuo) = \\frac{tama\\tilde{n}o\_poblaci\\acute{o}n \cdot Fitness(Individuo)}{\sum_{i=1}^{tama\\tilde{n}o\_poblaci\\acute{o}n}Fitness(Individuo_i)}`
   | Con base a lo anterior, el método consiste en lo siguiente:
   * Se selecciona un valor aleatorio entre 0 y 1, a éste se le llamará Pointer **(ó Puntero)**
   * De manera secuencial se seleccionarán tantos Individuos como el tamaño de la Población, los cuales deben estar igualmente espaciados en su Valor Esperado tomando como referencia el valor de Pointer.
   | Es importante aclarar el segundo punto, así que se abordará desde una perspectiva computacional:
   * Se deben tener variables adicionales que indiquen la acumulación tanto del Pointer **(CP, Cumulative Pointers)** como de los Valores Esperados **(CEV, Cumulative Expected Value)** así como al Individuo actual que está siendo seleccionado **(I)**.
   * Para averiguar si un Individuo está igualmente espaciado en su Valor Esperado con respecto de los demás basándose en Pointer, basta con corroborar que: 
   .. centered:: :math:`CP + Pointer > CEV + EV`
   * Si la condición descrita es verdadera los valores EV e I deben actualizarse **(I se ajusta al siguiente Individuo)** ya que esto indica que se buscará al siguiente Individuo espaciado equitativamente con el valor Pointer. No se hace nada si la condición es falsa.
   * Independientemente del valor de la condición anterior, CP y CEV deben actualizarse durante todo el ciclo.
   | Cabe mencionar que si la lista de Individuos se agota, se puede volver a iterar 
    desde el inicio teniendo cautela en conservar CEV y CP.
"""


def execute_selection_technique(population,selection_parameters):
    """
       De acuerdo a la información provista anteriormente, se implementa
       el método conocido como Stochastic Universal Sampling **(ó Muestreo Estocástico Universal)**.
    """

    #Se crea una estructura para almacenar los cromosomas de los
    #Individuos seleccionados. A su vez se crea la variable Pointer.
    chromosome_set = []
    pointer = aleatorio.random()

    #Se inicializan las variables correspondientes a la acumulación de Pointers
    #y Valores Esperados respectivamente.
    cumulative_pointers = 0
    cumulative_expected_value = 0
    
    #Con este valores se seleccionarán los Individuos y determinará si son aptos para
    #la etapa de reproducción.
    population_count = 0
    population_selected = 0

    #Se obtiene el tamaño de la Población y los Individuos, no sin antes habiéndolos 
    #desordenado primero para garantizar una selección más justa.  
    population_size = population.get_size() 
    population.shuffle_individuals()
    individuals = population.get_individuals()
    
    #Se toma el primer Individuo como referencia para poder comenzar la
    #operación.
    current_individual = individuals[0]      

    #El siguiente proceso se realizará hasta que se hayan seleccionado 
    #para la reproducción tantos Individuos como el tamaño de la Población.
    while population_selected < population_size:
          #Se toma el Valor Esperado del Individuo actual.
          current_expected_value = current_individual.get_expected_value()

          #Si el Pointer es mayor que el Valor Esperado del actual Individuo considerando los valores
          #acumulados entonces se actualiza el candidato, pues lo anterior indica que se debe tomar el
          #siguiente Individuo espaciado con el valor Pointer.
          if cumulative_pointers + pointer > cumulative_expected_value + current_expected_value:
             #Se actualiza el apuntador al siguiente Individuo.
             population_count += 1   

             #Se actualiza el Valor Esperado Acumulado
             cumulative_expected_value += current_expected_value

             #Se selecciona el Individuo siguiente(se puede ver que usa el operador '%' 
             #para hacer cíclica la elección en caso de que se haya agotado la lista previamente).
             current_individual = individuals[population_count % population_size]
          
          #Independientemente de la operación anterior, se actualizan lod siguientes valores para permitir
          #seguir obteniendo Individuos hasta que se satisfaga la demanda.
          population_selected += 1
          cumulative_pointers += pointer

          #Se agrega el cromosoma del Individuo seleccionado actualmente.
          chromosome_set.append(current_individual.get_complete_chromosome())
             
    return chromosome_set
