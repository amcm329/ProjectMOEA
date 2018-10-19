#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


import math as matematicas
import random as aleatorio


"""
   | Este script contiene todas las funcionalidades requeridas para que se pueda hacer uso de una
    codificación de tipo Binary **(ó Binaria)**; ésto significa que los alelos que
    conforman al cromosoma serán exclusivamente 0 ó 1. 
"""


def calculate_length_subchromosomes(vector_variables,number_of_decimals,representation_parameters):
    """
       | Esta es la implementación del método para la codificación en binario.
        A grandes rasgos primero se determina el número de bits que se deben tomar en cuenta
        para representar la magnitud de una determinada variable de decisión.
       | Haciendo esto para todas las variables de decisión se obtienen las longitudes
        de todos los subcromosomas. 
       | Esta función se implementa obligatoriamente.
    """

    #Dado que se tiene que contemplar la expansión decimal para cada magnitud 
    #de cada variable de decisión, se hace esta operación para poder calcular el número real
    #de bits necesarios para cada variable de decisión.
    true_number_of_decimals = 10**number_of_decimals

    #Se declaran algunas variables para poder realizar las operaciones
    #del cálculo de bits totales.
    lower_limit = -1
    upper_limit = -1
    amount = -1
    how_many_bits_around = -1
    how_many_bits_real = -1

    #Aquí se almacenarán las longitudes de cada subcromosoma.
    length_subchromosomes = []

    #Por cada variable de decisión se hace lo siguiente:
    for single_variable in vector_variables:
        #Se obtiene el nombre de la variable de decisión, así como
        #sus límites.
        variable_range = single_variable[1]
        lower_limit = variable_range[0]
        upper_limit = variable_range[1]

        #A continuación se obtiene la magnitud total (en decimal) de la
        #variable de decisión actual, es decir, se calcula el espacio total
        #de búsqueda considerando la precisión decimal e incluyendo el 0.
        amount = (upper_limit - lower_limit)*true_number_of_decimals

        #A la cantidad determinada con anterioridad se le aplica logaritmo
        #en base dos para poder determinar el número de bits necesarios
        #para representar en binario la magnitud de la variable de decisión actual.
        how_many_bits_around = matematicas.log(amount,2) 

        #En caso de que el número de bits no sea entero, se le aplica la función
        #ceil (ó techo) para poder tener un poco más de tolerancia en la representación.
        how_many_bits_real = int(matematicas.ceil(how_many_bits_around))

        #Finalmente se agrega esta cantidad de bits a la estructura indicada.
        length_subchromosomes.append(how_many_bits_real)

    #Se regresa una lista con todas las cantidades.
    return length_subchromosomes


def create_chromosome(length_subchromosomes,vector_variables,number_of_decimals,representation_parameters):
    """
       | Crea un cromosoma binario completo con base en las longitudes de los subcromosmas.
       | Este método debe implementarse obligatoriamente.
    """

    #Aquí se almacenarán todos los alelos de todos los subcromosomas.
    final_chromosome = []

    #A grandes rasgos se agregarán a final_chromosome números al azar
    #entre 0 y 1, tantos números como el tamaño de cada una de las longitudes.
    for length_subchromosome in length_subchromosomes:
      
        #Entonces por cada longitud de subcromosoma se agregarán
        #los alelos. 
        for x in range(0,length_subchromosome):
            number = aleatorio.randint(0,1)
            final_chromosome.append(number)

    #Se regresa el súper cromosoma.
    return final_chromosome


def binary_to_decimal(chromosome):
    """
       | Método que convierte un número binario a decimal.
       | Este es un ejemplo de método que se puede agregar
        adicionalmente siempre y cuando se implementen las 
        funciones que se han mencionado ya.

       :param chromosome: El cromosoma sobre el cual se hará
                          la evaluación.

       :type chromosome: List
       :return: La representación en decimal del número binario.
       :rtype: Integer
    """
 
    #Este número será la evaluación en decimal.
    number = 0

    #Se toma el máximo exponente del número decimal.
    length_chromosome = len(chromosome) - 1

    #Ahora se van haciendo sumas de potencias de 2 por
    #cada alelo del cromosoma.
    for i in range (length_chromosome,-1,-1):
        number += chromosome[length_chromosome - i]*(2**i)
          
    #Se regresa el número ya convertido a decimal.
    return number


def evaluate_subchromosomes(complete_chromosome,length_subchromosomes,vector_variables,number_of_decimals,representation_parameters): 
    """
       | Realiza una evaluación de los subcromosomas para la codificación binaria **(ó Binary)**.
       | En términos generales se toma cada porción del subcrosomoma **(tomando en 
        cuenta que previamente se calcularon sus longitudes)** y así se convierte a 
        decimal, considerando la expansión numérica.
       | Posteriormente para obtener el número final se hace lo siguiente:
       .. centered:: :math:`Conversi\\acute{o}n(subcromosoma) = A + DN(subcromosoma) \\cdot \\frac{B - A}{2^M - 1}`
       | Donde:
       |       **A** es el límite inferior que toma la variable de decisión.
       |       **B** es el límite superior que toma la variable de decisión.
       |       **M** es la longitud del subcromosoma asociado a la variable de decisión.
       |       **DN (Decimal number)** es el número en decimal del subcromosoma asociado a la variable de decisión.

    """

    #Las siguientes variables permitirán almacenar los límites de 
    #inferior y superior de cada subcromosoma.
    lower_limit = 0
    upper_limit = 0

    #Aquí se almacenarán las variables de decisión con su respectiva
    #evaluación.
    decision_variables = {}    

    #La cadena de precisión sirve para delimitar el número de decimales
    #a los solicitados por el usuario.
    precision_string = "{0:." + str(number_of_decimals) + "f}"

    #La codificación de gray evita la epístasis (se generen números que no están
    #considerados dentro de los rangos de las variables de decisión). El usuario
    #puede optar por permitir o denegar esta opción desde la sección View (ó Vista).
    gray_coding = representation_parameters["gray_coding_binary_representation"]

    
    for i in range (0,len(length_subchromosomes)):
        #Se obtiene la longitud del subcromosoma actual.
        m = length_subchromosomes[i]

        #Se obtiene el nombre de la variable de decisión actual, así como
        #sus límites inferior y superior.
        single_variable = vector_variables[i]
        variable_name = single_variable[0]
        variable_range = single_variable[1]        
        a = variable_range[0]
        b = variable_range[1]

        #Se actualiza el límite superior para poder obtener el subcromosoma adecuado.
        upper_limit += m
        subchromosome = complete_chromosome[lower_limit:upper_limit]

        #Si la opción de la codificación de Gray está activada se procede a hacer
        #la operación. A grandes rasgos dicha codificación consiste en tomar el primer
        #alelo y hacer la operación XOR con el siguiente, del resultado hacer XOR con el
        #siguiente y así sucesivamente hasta haber manipulado todos los alelos originales.
        if gray_coding == True:
           gray_subchromosome = [subchromosome[0]]
           for j in range (1,len(subchromosome)):
               gray_subchromosome.append(subchromosome[j]^subchromosome[j-1])
                     
           subchromosome = gray_subchromosome   
                          
        #El subcromosoma en binario se convierte a decimal (esto representa
        #sólo la magnitud de la variable de decisión actual mas no el número).
        decimal_number = binary_to_decimal(subchromosome)

        #Esta es la operación que permite obtener el número real correspondiente
        #a la variable de decisión, se hace un ajuste tomando en cuenta los límites
        #inferior y superior de la variable de decisión actual, así como la longitud
        #total del subcromosoma.
        number = a + decimal_number*((b-a)/((2.0**m) - 1))
        
        #Se agrega el valor ya convertido a decimal, siendo antes formateado por 
        #la cadena de precisión para tener la expansión decimal adecuada.      
        decision_variables[variable_name] = float(precision_string.format(number))

        #Se actualizan los límites para poder elegir al siguiente subcromosoma.
        lower_limit = upper_limit

    return decision_variables
