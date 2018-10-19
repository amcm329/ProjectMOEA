#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


"""
   | Se desarrolla la técnica M.O.E.A. que lleva por nombre M.O.G.A. 
    **(Multi Objective Genetic Algorithm ó Algoritmo Genético Multi Objetivo)**.
   | Su funcionamiento es el siguiente: 
   |
   | 1.- Se crea la Población Padre, se evalúan las funciones objetivo de sus correspondientes Individuos.

   | 2.- Se asigna a los Individuos un Ranking **(Fonseca & Flemming)** y posteriormente se calcula el Niche Count de la Población Padre.

   | 3.- Tomando en cuenta los valores del punto 2 se obtiene el Fitness para cada Individuo y posteriormente su Shared Fitness.

   | 4.- Se aplica el operador de selección sobre la Población Padre para determinar los elegidos para dejar descendencia.

   | 5.- Se crea la Población Hija, se evalúan las funciones objetivo de sus correspondientes Individuos.

   | 6.- Se asigna a los Individuos un Ranking **(Fonseca & Flemming)** y posteriormente se calcula el Niche Count de la Población Hija.

   | 7.- Tomando en cuenta los valores del punto 6 se obtiene el Fitness para cada Individuo y posteriormente su Shared Fitness.

   | 8.- La Población Hija pasará a ser la nueva Población Padre.

   | 9.- Se repiten los pasos 4 a 8 hasta que se haya alcanzado el número límite de generaciones **(iteraciones)**.
   |
   | Como se puede apreciar, la implementación de este algoritmo es muy sencilla, además 
    se rige casi en su totalidad por el Shared Fitness **(ó Fitness Compartido)**, por lo 
    que la Presión Selectiva **(ó Selective Pressure)** incluida dependerá en gran medida
    de la función de Distancia que se utilice, así como de la magnitud indicada por
    el usuario.
   | Finalmente es menester mencionar que para esta implementación el Ranking utilizado debe ser
    estrictamente el de Fonseca & Flemming **(véase Model/Community/Community.py)**.
"""


def execute_moea(execution_task_count,generations_queue,generations,population_size,vector_functions,vector_variables,available_expressions,number_of_decimals,
                 community_instance,algorithm_parameters,representation_instance,representation_parameters,fitness_instance,fitness_parameters,
                 sharing_function_instance,sharing_function_parameters,selection_instance,selection_parameters,crossover_instance,crossover_parameters,
                 mutation_instance,mutation_parameters):
    """
       Tomando como referencia el pseudocódigo antes citado, se elabora la implementación
       de M.O.G.A. **(Multi Objective Genetic Algorithm ó Algoritmo Genético Multi Objetivo)**.
    """
   
    #Se crea una instancia de Community ya que la mayoría de los métodos auxiliares
    #residen allí.
    comunidad = getattr(community_instance,"Community")(vector_functions,vector_variables,available_expressions,number_of_decimals,
                                                        representation_instance,representation_parameters,fitness_instance,fitness_parameters,
                                                        sharing_function_instance,sharing_function_parameters,selection_instance,selection_parameters,
                                                        crossover_instance,crossover_parameters,mutation_instance,mutation_parameters)

    #Se crea una estructura para almacenar al mejor Individuo por generación.
    best_individual_along_generations = []

    #Se inicializa la Población Padre.
    parents = comunidad.init_population(population_size)

    try: 
        #Se evalúan las funciones objetivo en la Población Padre.
        comunidad.evaluate_population_functions(parents)

        #Se asigna el Ranking de Fonseca & Flemming en los Individuos de la Población Padre.
        comunidad.assign_fonseca_and_flemming_pareto_rank(parents)
              
        #Se calcula el Niche Count de los Individuos de la Población Padre.
        comunidad.calculate_population_niche_count(parents)
 
        #Se asigna el Fitness a los Individuosde la Población Padre (se recomienda el Lineal Scaled Fitness).
        comunidad.assign_population_fitness(parents)
 
        #Se calcula el Shared Fitness de cada Individuo de la Población Padre.
        comunidad.calculate_population_shared_fitness(parents)

        for x in range (1,generations + 1):
            #Esta estructura se usa para enviarle una señal a la sección View
            #con el fin de indicarle el avance que se verá reflejado en un GenerationSignalToplevel.
            #Es importante que lo que se añada al generations_queue sea una tupla de tipo
            #(execution_task_count,generación_actual).
            generations_queue.append((execution_task_count,x))

            #Se seleccionan los candidatos para formar a la nueva Población Hija.
            selected_parents_chromosomes = comunidad.execute_selection(parents)

            #Se aplica cruza y mutación sobre los candidatos anteriores para conformar a la 
            #nueva Población Hija.
            children = comunidad.execute_crossover_and_mutation(selected_parents_chromosomes)

            #Se evalúan las funciones objetivo de los Individuos de la Población Hija.
            comunidad.evaluate_population_functions(children)

            #Se asigna el Ranking (Fonseca & Flemming) a los Individuos de la 
            #Población Hija.
            comunidad.assign_fonseca_and_flemming_pareto_rank(children)
               
            #Se calcula el Niche Count de la Población Hija.
            comunidad.calculate_population_niche_count(children)
 
            #Se obtiene el Fitness de cada Individuo en la Población
            #Hija (se recomienda Linear Scaled Fitness).
            comunidad.assign_population_fitness(children)
 
            #Se asigna el Shared Fitness a los Individuos de la Población.
            comunidad.calculate_population_shared_fitness(children)

            parents.sort_individuals("get_fitness",True)   
          
            #Se obtiene el mejor Individuo en la generación actual.
            best_individual_along_generations.append(comunidad.get_best_individual(children))

            #La Población Hija pasa a ser la nueva Población Padre.
            parents = children

    except Exception, e:
           #En caso de un error interno las generaciones automáticamente llegan a su límite
           #para cerrar la ventana en la parte de View.
           generations_queue.append((execution_task_count,generations))

           #Posteriormente se regresa el siguiente diccionario con la información relativa
           #al origen del error.
           error = {
                    "response": "ERROR",
                    "class": "MOGA", 
                    "method": "execute_moea",
                    "message": "An error has occurred during execution of MOGA algorithm",
                    "type": (str(e))
                   }   

           return error

    #Los resultados tienen el formato precisado dentro de la función get_results que se encuentra
    #en Model/Community/Community.py. Es sumamente importante que el usuario revise esta función
    #ya que de ésta depende la graficación de resultados (véase View/Additional/ResultsGrapher/ResultsGrapherToplevel.py).
    #El conjunto que almacena todos los Individuos para impresión de resultados es el de la Población Padre.
    results = comunidad.get_results(best_individual_along_generations,parents) 

    #Se regresan dichos resultados.
    return results
