#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


"""
   | La Distancia Euclidiana **(ó Euclidean Distance)** es una implementación 
    de cálculo de distancia entre dos Individuos que pertenece a la subcategoría 
    Phenotypic Similarity **(ó Similaridad Fenotípica)**.
   | Esta versión está dirigida para las Funciones Objetivo **(ó Objective Functions)**
    que poseen cada uno de los Individuos **(ó Individuals)** de una Población **(ó Population)**.
   |
   | Primero que nada para obtener el cálculo de :math:`\sigma_{share}` la operación está regida por la siguiente
    fórmula:
   .. centered:: :math:`\sigma_{share} = \frac{\sum_{j=1}^{n\acute{u}m\_funciones\_objetivo}(max(F_j) - min(F_j))}{tama\tilde{n}o\_poblaci\acute{o}n - 1}`
   | Lo anterior significa que se van a obtener los valores máximo y mínimo de cada función objetivo, 
    se restan entre sí y al resultado anterior se le divide entre el tamaño de la Población menos uno; esto por cada generación.
   |
   | La forma de hacer el cálculo de la distancia es la siguiente:
   | Supongamos que tenemos los vectores :math:`U = (u_1,u_2,...,u_n)` y :math:`V = (v_1,v_2,...,v_n)`. Entonces la Distancia Euclidiana se define como:
   .. centered:: :math:`d_E(U,V) = \sqrt{(v_1 - u_1)^2 + (v_2 - u_2)^2 + ... + (v_n - u_n)^2}`
   | Para los fines que nos conciernen, los vectores :math:`U\ y\ V` serán las evaluaciones en las funciones objetivos 
    de cada Individuo participante.
   |
   | Finalmente es menester mencionar que, aunque tradicionalmente esta técnica se usa para Representaciones Cromosómicas
    **(véase Model/ChromosomalRepresentation)** de tipo FloatPoint **(ó Punto Flotante)**, en sentido estricto no se encuentra
    limitada sólo a este tipo de codificación.
"""


def calculate_sigma_share(population,sharing_function_parameters):
    """
       Tomando como referencia la información antes mencionada para el cálculo del 
       Sigma Share, se realiza la implementación correspondiente.
    """
        
    #Aquí se almacenará el valor del Sigma Share.
    sigma_share = 0.0

    #Por cada función objetivo se realiza la resta entre el máximo valor
    #y el mínimo y se añade dicho resultado a la variable sigma_share.
    for value in population.get_objective_functions_extreme_values():
        sigma_share += value[1] - value[0]
                         
    #Al final el valor recabado hasta el momento se divide entre el tamaño de la 
    #Población menos uno.
    return sigma_share / (population.get_size() - 1)


def calculate_distance(individual_i,individual_j,sharing_function_parameters):
    """
       Apoyándose de la técnica conocida como Distancia Euclidiana 
       **(ó Euclidean Distance)** se implementa el cálculo de la distancia 
       para dos Individuos cualesquiera.
    """

    #Se crea una variable que almacenará la suma de los valores al cuadrado.
    sum_squared = 0.0

    #Se obtienen los vectores de las funciones objetivo evaluadas de cada Individuo, así como
    #la longitud de éstos.
    individual_i_functions = individual_i.get_evaluated_functions()
    individual_j_functions = individual_j.get_evaluated_functions()
    
    length_functions = len(individual_i_functions)
    
    #El siguiente ciclo realiza la suma de las evaluaciones de las funciones objetivo 
    #de los Individuos en las mismas posiciones. Por cada posición dichos valores son restados
    # y elevados al cuadrado antes de ser sumados.
    for position in range(length_functions):
        sum_squared += (individual_i_functions[position] - individual_j_functions[position])**2
    
    #Al valor sum_squared se le obtiene la raiz cuadrada, con lo cual 
    #se conforma la Distancia Euclidiana lo cual es lo que se regresa.
    return sum_squared**(1.0/2.0)   
