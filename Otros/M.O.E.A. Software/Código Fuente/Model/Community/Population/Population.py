#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


import random as aleatorio 
import operator as operador 
import Individual.Individual as individuo


class Population:
      """
         Consiste en un conjunto de instancias de la clase Individual, proporcionando además métodos y atributos que 
         se manifiestan tanto en grupo como de manera individual.

         :param population_size: El tamaño de la Población.
         :param vector_functions: Lista con las funciones objetivo.
         :param vector_variables: Lista con las variables de decisión y sus rangos.
         :param available_expressions: Diccionario que contiene algunas funciones escritas como azúcar sintáctica
                                       para que puedan ser utilizadas más fácilmente por el usuario y evaluadas
                                       más ŕapidamente en el programa **(véase Controller/XML/PythonExpressions.xml)**.
         :param number_of_decimals: Número de decimales que tendrá cada solución **(tanto en variables de decisión como
                                    funciones objetivo)**.

         :type population_size: Integer
         :type vector_functions: List
         :type vector_variables: List
         :type available_expressions: Dictionary
         :type number_of_decimals: Integer

         :returns: Model.Community.Population
         :rtype: Instance
      """


      def __init__(self,population_size,vector_functions,vector_variables,available_expressions,number_of_decimals):

          #Se almacenan los valores para que puedan ser usado posteriormente, a veces por clases externas .
          #Los siguientes atributos indican características básicas que tendrán los Individuos.
          self.__population_size = population_size
          self.__vector_functions = vector_functions
          self.__vector_variables = vector_variables 
          self.__available_expressions = available_expressions
          self.__number_of_decimals = number_of_decimals
          
          #La siguiente estructura almacenará a los Individuos, que no es otra cosa que un arreglo de tamaño
          #fijo.
          self.__population = [0.0]*self.__population_size  

          #El valor del tamaño del vector de funciones objetivo se usa muchas veces, por eso se pone como atributo.
          self.__length_vector_functions = len(vector_functions)

          #las siguientes variables contendrán números que se calcularán con métodos grupales
          self.__total_fitness = 0.0
          self.__total_expected_value = 0.0

          #Esta estructura almacena los valores mínimo y máximo respectivamente de cada 
          #variable de decisión. Se necesitan para poder obtener el valor sigma share.
          self.__decision_variables_extreme_values = {}

          #Dado que las variables de decisión se manejan como un diccionario para poder ser evaluados
          #más fácilmente ante las funciones objetivo, los valores extremos de cada una de las variables de
          #decisión también se manejan como un diccionario, con el identificador de cada variable de decisión
          #como llave.
          for variable in vector_variables:
              variable_name = variable[0]
              self.__decision_variables_extreme_values[variable_name] = [0,0]

          #Esta estructura almacena los valores mínimo y máximo respectivamente de cada 
          #función objetivo. Se necesitan para poder obtener el valor sigma share.
          self.__objective_functions_extreme_values = [[0,0]]*len(self.__vector_functions)


      def get_individuals(self):
          """
             Regresa los Individuos de la Población.
 
             :returns: Estructura que contiene a los Individuos de la Población.
             :rtype: Array
          """

          #Se regresa la estructura.
          return self.__population


      def get_size(self):
          """
             Otorga el tamaño de la Población.
 
             :returns: El tamaño de la Población.
             :rtype: Integer
          """
         
          #Se regresa el atributo concerniente al tamaño de la Población.
          return self.__population_size


      def get_length_vector_functions(self):
          """
             Regresa el número de elementos del vector de funciones objetivo.
 
             :returns: Número de funciones objetivo.
             :rtype: Integer
          """
         
          #Se obtiene el atributo relativo al tamaño del vector de funciones objetivo.
          return self.__length_vector_functions


      def get_vector_variables(self):
          """
             Regresa el vector de variables de decisión.
 
             :returns: Conjunto que contiene las variables de decisión con sus rangos.
             :rtype: List
          """

          #Se obtiene el atributo relativo a las variables de decisión.
          return self.__vector_variables


      def get_total_fitness(self):
          """
             Captura el Fitness total de la Población.
 
             :returns: El valor del Fitness poblacional.
             :rtype: Float
          """
         
          #Se regresa el valor concerniente al Fitness total de la Población.
          return self.__total_fitness


      def set_total_fitness(self,value):
          """
             Actualiza el Fitness total de la Población.
 
             :param value: El valor a actualizar.

             :type value: Float
          """
         
          #Se actualiza el valor de la variable correspondiente.
          self.__total_fitness = value


      def get_total_expected_value(self):
          """
             Regresa el valor esperado de la Población.
 
             :returns: El valor esperado.
             :rtype: Float
          """
         
          #Se regresa el valor esperado de la Población.
          return self.__total_expected_value


      def get_objective_functions_extreme_values(self):
          """
             Regresa el listado de los valores máximo y mínimo de las 
             funciones objetivo para el cálculo de sigma share.
 
             :returns: El listado con los valores máximo y mínimo para las
                       funciones objetivo.
             :rtype: List
          """
         
          #Se regresa el listado de las deltas.
          return self.__objective_functions_extreme_values


      def set_objective_functions_extreme_values(self,objective_functions_extreme_values):
          """
             Actualiza el listado de valores máximo y mínimo de las
             funciones objetivo para el cálculo de sigma share.
             
             :param objective_functions_extreme_values: Una lista con los valores máximo y mínimo
                                                        de cada una de las funciones objetivo.

             :type objective_functions_extreme_values: List
          """
         
          #Se actualiza el valor de la variable en cuestión.
          self.__objective_functions_extreme_values = objective_functions_extreme_values
 

      def get_decision_variables_extreme_values(self):
          """
             Regresa el listado de los valores máximo y mínimo de las 
             variables de decisión para el cálculo de sigma share.
 
             :returns: Una colección con los valores máximo y mínimo para las
                       variables de decisión.
             :rtype: Dictionary
          """
         
          #Se regresa el listado de las deltas.
          return self.__decision_variables_extreme_values


      def set_decision_variables_extreme_values(self,decision_variables_extreme_values):
          """
             Actualiza el listado de valores máximo y mínimo de las
             variables de decisión para el cálculo de sigma share.
             
             :param decision_variables_extreme_values: Un conjunto con los valores máximo y mínimo
                                                       de cada una de las variables de decisión.

             :type decision_variables_extreme_values: Dictionary
          """
         
          #Se actualiza el valor de la variable en cuestión.
          self.__decision_variables_extreme_values = decision_variables_extreme_values
 

      def add_individual(self,position,complete_chromosome):
          """
             Añade un Individuo a la Población.
              
             :param position: La posición dentro del arreglo de Individuos 
                              donde se colocará el nuevo elemento.
             :param complete_chromosome: El cromosoma del Individuo.

             :type position: Integer
             :type complete_chromosome: Array
          """

          #Se agrega dentro del arreglo de Individuos la instancia del Individuo nuevo.
          #Dado que todos los atributos para crear una instancia ya han sido capturados
          #sólo se necesita el nuevo cromosoma. Como se puede apreciar, este método en 
          #realidad sólo sustituye elementos, no agrega posiciones extra para colocas
          #nuevos individuos.
          self.__population[position] = individuo.Individual(complete_chromosome,self.__vector_functions,self.__available_expressions,self.__number_of_decimals)
          
      
      def calculate_population_properties(self):
          """
             Calcula atributos individuales con base en los valores de toda la Población.
          """

          #Por cada Individuo se hace lo siguiente:
          for individual in self.__population:

              #Se calcula el valor esperado de la Población, el cual consiste en: 
              #fitness/(fitness total/tamaño de la Población)
              try:
                  expected_value = individual.get_fitness()/(self.__total_fitness/self.__population_size)

              except:
                  expected_value = 0.0

              #Se agrega este valor calculado en el Individuo actual.
              individual.set_expected_value(expected_value)

              #Se calcula el valor esperado de la Población
              self.__total_expected_value += expected_value     


      def sort_individuals(self,method,is_descendent):
          """
             Ordena los Individuos de acuerdo a algún criterio dado.
         
             :param method: El método o atributo sobre el cual se hará la comparación.
             :param is_descendent: Indica si el ordenamiento es ascendente o descendente.
 
             :type method: String
             :type is_descendent: Boolean
          """

          #Se ordena la Población con base en "method" y el orden lo indica el atributo "is_descendant".
          self.__population.sort(key = operador.methodcaller(method),reverse = is_descendent)


      def shuffle_individuals(self):
          """
             Desordena los elementos de la Población.
          """

          #Se desordena la lista de Individuos.
          aleatorio.shuffle(self.__population)


      def print_info(self):
          """
             Imprime en texto las características de los Individuos
             de la Población, tanto grupales como individuales **(en consola)**.
          """

          print "Total fitness: " + str(self.__total_fitness)
          print "Total expected value: " + str(self.__total_expected_value)
          print "Individuals: "
          for x in range (self.__population_size):
              print "Number: " + str(x)

              #Se imprime cada Individuo.
              self.__population[x].print_info()      
