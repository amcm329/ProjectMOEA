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
   | Se implementa el método conocido como Binary Mutation **(ó Mutación Binaria)**.
   | El procedimiento es el siguiente:
   * Se trata cada gen individualmente y se modifica de acuerdo a una probabilidad de Mutación asignada, si ésta es suficiente se procede a hacer el cambio, en otro caso se deja el alelo asociado al gen intacto.
   * Retomando el caso en que se puede modificar el alelo del gen se verifica su valor actual y ya que se maneja una representación Binaria su transformación es muy simple: si se encuentra un 0, el alelo toma el valor 1 y viceversa.
"""


def execute_mutation_technique(chromosome,mutation_parameters):
    """
       Usando la información mostrada anteriormente, se desarrolla la función
       conocida como Binary Mutation **(ó Mutación Binaria)**.
    """

    #Aquí se almacenará el cromosoma mutado.
    mutated_chromosome = []  

    #Se obtiene el valor que representará a la probabilidad de Mutación
    #establecida por el usuario.
    mutation_probability = mutation_parameters["probability_mutation_general"]
    
    #Por cada gen en el cromosoma se realiza lo siguiente:
    for gen in chromosome: 

        #Se crea el número que servirá de verificación 
        #para la probabilidad de cruza.
        number = aleatorio.random()

        #Si el número en cuestión es menor o igual que el parámetro de la
        #probabilidad de cruza entonces se procede a cambiar el alelo asociado
        #al gen actual.
        if number <= mutation_probability:
           
           #Dado que se trata de una representación Binaria, la transformación
           #es muy simple, si hay un 0 entonces el nuevo alelo asociado al gen se
           #transfomará en 1 y viceversa.
           if gen == 0:
              mutated_chromosome += [1]
        
           elif gen == 1:
              mutated_chromosome += [0]
    
        #En caso de que la operación inherente a la probabilidad de cruza no
        #se haya cumplido, el gen actual no se modifica.     
        else:
            mutated_chromosome += [gen]       
             
    #Finalmente se regresa el cromosoma mutado. 
    return mutated_chromosome
