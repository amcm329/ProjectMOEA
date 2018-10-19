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
   | Se concreta el método conocido como Float Point Mutation **(ó Mutación de Punto Flotante)**.
   | El procedimiento es el siguiente:
   * Se trata cada gen individualmente y se modifica de acuerdo a una probabilidad de Mutación asignada, si ésta es suficiente se procede a hacer el cambio, en otro caso se deja el alelo asociado al gen intacto.
   * Retomando el caso en que se puede modificar el alelo del gen se verifica los límites de la variable de decisión que está ligada a éste, así como la precisión decimal. Entonces se crea el nuevo número con la precisión decimal requerida y se sustituye por el anterior.
"""


def execute_mutation_technique(chromosome,mutation_parameters):
    """
       Utilizando los datos de la parte superior, se desarrolla la función
       conocida como Float Point Mutation **(ó Mutación de Punto Flotante)**.
    """

    #Aquí se almacenará el cromosoma mutado.
    mutated_chromosome = []   
   
    #Se obtienen las variables de los parámetros como son la probabilidad de 
    #mutación, la precisión decimal y el vector de variables.
    mutation_probability = mutation_parameters["probability_mutation_general"]
    number_of_decimals = mutation_parameters["number_of_decimals_floatpoint_mutation"]
    vector_variables = mutation_parameters["vector_variables_floatpoint_mutation"]["vector_variables"]

    #Dado que se trata de un cromosoma con representación de Punto Flotante
    #para mantener la precisión decimal es importante pasarle un formato; esto
    #se realiza usando una cadena especial como ésta.
    precision_string = "{0:." + str(number_of_decimals) + "f}"

    #Por cada gen en el cromosoma se realiza lo siguiente:
    for x in range(len(chromosome)):
        #Se obtiene el gen actual.
        gen = chromosome[x]

        #Se crea el número que servirá de verificación 
        #para la probabilidad de cruza.
        number = aleatorio.random()
             
        #Si el número en cuestión es menor o igual que el parámetro de la
        #probabilidad de cruza entonces se procede a cambiar el alelo asociado
        #al gen actual.
        if number <= mutation_probability:

           #Se toma el vector de variables de la posición asociada al gen
           #(ya que se trata de una representación de Punto Flotante, la 
           #correspondencia con el cromosoma es biunívoca y por ende es 
           #plausible este paso).
           current_variable =  vector_variables[x]

           #Se toma el rango asociado a la variable.
           variable_range = current_variable[1]

           #Se obtienen los límites inferior y superior que vienen en
           #el rango.
           lower_value = variable_range[0] 
           upper_value = variable_range[1]

           #Se crea un número nuevo que tenga como límites los mencionados
           #anteriormente. 
           new_number = aleatorio.uniform(lower_value,upper_value)

           #El nuevo alelo es reemplazado en la posición indicada.
           mutated_chromosome += [float(precision_string.format(new_number))] 
            
        #En caso de que la operación inherente a la probabilidad de cruza no
        #se haya cumplido, el gen actual no se modifica.
        else:
            mutated_chromosome += [gen]       
    
    #Al final se regresa el cromosoma con los genes mutados.      
    return mutated_chromosome
