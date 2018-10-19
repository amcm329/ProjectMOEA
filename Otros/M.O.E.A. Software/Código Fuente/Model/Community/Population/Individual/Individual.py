#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


class Individual:
      """
         | La base de toda operación lógica.
         | Consiste en una abstracción de un elemento simple en función de un ecosistema.
          Si bien la parte esencial es el cromosoma, en esta implementación se añaden algunos elementos extra
          con la finalidad de facilitar ciertas operaciones.

         :param complete_chromosome: El cromosoma que conformará al Individuo.
         :param vector_functions: Lista que contiene a las funciones objetivo.
         :param available_expressions: Diccionario que contiene algunas funciones escritas como azúcar sintáctica
                                       para que puedan ser utilizadas más fácilmente por el usuario y evaluadas
                                       más ŕapidamente en el programa **(véase Controller/XML/PythonExpressions.xml)**.
         :param number_of_decimals: El número de decimales que deberá tener cada solución, influye en el
                                    comportamiento del cromosoma.

         :type complete_chromosome: Array
         :type vector_functions: List
         :type available_expressions: Dictionary
         :type number_of_decimals: Integer

         :returns: Model.Community.Population.Individual
         :rtype: Instance
      """


      def __init__(self,complete_chromosome,vector_functions,available_expressions,number_of_decimals):
          #Se almacenan los atributos para poder usarlos posteriormente.
          self.__complete_chromosome = complete_chromosome
          self.__vector_functions = vector_functions
          self.__available_expressions = available_expressions

          #Debido a un problema con la precisión decimal en Python, cualquier número
          #que requiera de cierta expansión decimal debe apoyarse de la siguiente cadena.
          self.__precision_string = "{0:." + str(number_of_decimals) + "f}"

          #La siguiente variable contendrá variables de decisión para ser evaluadas.
          self.__decision_variables = {}

          #Aquí se almacenarán las funciones objetivo ya evaluadas.
          self.__evaluated_functions = [0]*len(vector_functions)

          #Los siguientes atributos auxilian en las comparaciones hechas para poder encontrar al
          #mejor Individuo (véase Model/Community/Community.py).
          self.__dominates = 0
          self.__is_dominated = 0
          self.__rank = 0
          self.__fitness = 0.0
          self.__niche_count = 0.0

          #La siguiente variable se utiliza sobre todo en técnicas de Selección (ó Selection).
          self.__expected_value = 0.0


      def get_complete_chromosome(self):
          """
             Regresa el cromosoma del Individuo.
 
             :returns: El cromosoma.
             :rtype: Array
          """

          #Regresa el valor de la variable asociada al cromosoma.
          return self.__complete_chromosome


      def get_vector_functions(self):
          """
             Obtiene el vector de funciones objetivo.
 
             :returns: El vector de funciones objetivo.
             :rtype: List
          """

          #Se regresa el vector.
          return self.__vector_functions


      def get_decision_variables(self):
          """
             Da el vector de variables de decisión.
 
             :returns: El vector de variables de decisión.
             :rtype: List
          """

          #Se regresa el vector.
          return self.__decision_variables

           
      def get_evaluated_functions(self):
          """
             Regresa las funciones objetivo evaluadas.
 
             :returns: Las funciones objetivo evaluadas.
             :rtype: List
          """

          #Se regresa el valor de esta variable.
          return self.__evaluated_functions
      

      def get_pareto_dominates(self):
          """
             Regresa el número de soluciones que son dominadas por 
             el actual Individuo.
 
             :returns: El número de soluciones dominadas.
             :rtype: Integer
          """

          #Se regresa este atributo.
          return self.__dominates


      def set_pareto_dominates(self,value):
          """
             Actualiza el número de soluciones dominadas por el
             Individuo actual.
 
             :param value: El valor a actualizar.
             :type value: Integer
          """

          #Se actualiza al valor correspondiente.
          self.__dominates = value     


      def get_pareto_dominated(self):
          """
             Regresa el número de soluciones que dominan al 
             Individuo actual.
 
             :returns: El número de soluciones que dominan a la actual.
             :rtype: Integer
          """

          #Se regresa el valor
          return self.__is_dominated


      def set_pareto_dominated(self,value):
          """
             Actualiza el número de soluciones que dominan a la
             solución actual.
 
             :param value: El valor a actualizar.
             :type value: Integer
          """

          #Se actualiza el valor.
          self.__is_dominated = value     

      
      def get_rank(self):
          """
             Regresa la puntuación **(rank)** que se le designó al Individuo
             **(véase Model/Community/Community.py)**.
 
             :returns: El rango.
             :rtype: Float
          """

          #Se regresa el rango.
          return self.__rank


      def set_rank(self,rank):
          """
             Actualiza el rango del Individuo.
 
             :param rank: El valor a actualizar.
             :type rank: Float
          """

          #Se actualiza al valor actual.
          self.__rank = rank


      def get_fitness(self):
          """
             Regresa el Fitness del Individuo.
 
             :returns: El Fitness.
             :rtype: Float
          """

          #Se regresa el valor.
          return self.__fitness


      def set_fitness(self,value):
          """
             Actualiza el valor del Fitness.
 
             :param value: El valor a actualizar.
             :type value: Float
          """

          #Se actualiza el valor.
          self.__fitness = value     

     
      def get_niche_count(self):
          """
             Regresa el valor niche para el Individuo.
 
             :returns: El tamaño niche.
             :rtype: Float
          """

          #Se regresa el valor.
          return self.__niche_count
 

      def set_niche_count(self,value):
          """
             Actualiza el valor niche.
 
             :param value: El valor a actualizar.
             :type value: Float
          """

          #Se actualiza el valor
          self.__niche_count = value

     
      def get_expected_value(self):
          """
             | Se obtiene el valor esperado del Individuo.
             | Por definición, el valor esperado es el número de posibles
              hijos que puede tener un Individuo. Mientras más apto, más 
              hijos.
 
             :returns: El valor esperado.
             :rtype: Float
          """

          #Se regresa el valor esperado del Individuo.
          return self.__expected_value


      def set_expected_value(self,value):
          """
             Actualiza el valor esperado del Individuo.
 
             :param value: El valor a actualizar.
             :type value: Float
          """

          #Se actualiza el valor.
          self.__expected_value = value
   

      def __evaluate_single_function(self,function,expressions): 
          """
             .. note:: Este método es privado.

             Evalúa una función objetivo.
 
             :param function: La función que será evaluada.
             :param expressions: El diccionario que ayuda a evaluar la función.
                                 Expressions = variables + constantes + funciones built-in. 

             :type function: String
             :type expressions: Dictionary
             
             :returns: La función evaluada.
             :rtype: Float
          
          """ 
           
          #Se regresa la función evaluada (las llaves de enmedio de la función
          #sirven para no contaminar la variable expressions).
          evaluation = eval(function,{},expressions)

          #Se le da el formato de la precisión decimal a la función recién
          #evaluada.
          return float(self.__precision_string.format(evaluation))


      def evaluate_functions(self,decision_variables):
          """
             Evalúa todas las funciones objetivo.

             :param decision_variables: El vector de variables de decisión.
 
             :type decision_variables: List
          """

          #Se guardan las variables de decisión
          self.__decision_variables = decision_variables

          #La evaluación de una función se apoya de un diccionario que contiene las
          #variables de decisión y cualquier otra constante definida por el usuario
          #(véase Controller/XML/PythonExpressions.xml).
          #Aquí entonces se llena dicho diccionario.
          all_expressions = {}
          all_expressions.update(self.__decision_variables)
          all_expressions.update(self.__available_expressions)

          #Finalmente se evalúan las funciones objetivo una a una y el resultado
          #se agrega a los contenedores creados previamente.          
          for x in range (len(self.__vector_functions)):
              function = self.__vector_functions[x]
              result = self.__evaluate_single_function(function,all_expressions)
              
              #A estos contenedores se agregan las funciones objetivo recién evaluadas.
              self.__evaluated_functions[x] = result


      def print_info(self):
          """
             Imprime las características básicas del Individuo **(en consola)**.
          """

          print "    Complete chromosome: " + str(self.__complete_chromosome)
          print "    Decision variables: " + str(self.__decision_variables)
          print "    Vector Functions: " + str(self.__vector_functions)
          print "    Evaluated functions (same position than Vector Functions): " + str(self.__evaluated_functions)
          print "    Rank:    " + str(self.__rank) + ". Fitness: " + str(self.__fitness) + ". Expected value: " + str(self.__expected_value)
          print "    Pareto dominates: " + str(self.__dominates) + ". Pareto is dominated: " + str(self.__is_dominated) + ". Niche count: " + str(self.__niche_count)
          print "\n"
