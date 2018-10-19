#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"
 

"""
   En esta parte se lleva a cabo la implementación del M.O.E.A. denominado
   N.S.G.A. II **(Non-dominated Sorting Genetic Algorithm ó Algoritmo Genético 
   de Ordenamiento No Dominado)**.

   La forma de proceder del método es la siguiente:

   1.- Se crea una Población Padre **(de tamaño n)**, a la cual se le evalúan las funciones objetivo de sus Individuos, se les asigna un Ranking **(Goldberg)** y posteriormente se les otorga un Fitness.

   2.- Con base en la Población Padre se aplica el operador de Selección para elegir a los Individuos que serán aptos para reproducirse.

   3.- Usando a los elementos del punto 2, se crea una Población Hija **(de tamaño n)**. 
 
   4.- Se crea una súper Población **(llamémosle S, de tamaño 2n)** que albergará todos los Individuos tanto de la Población Padre como Hija; a *S* se le evalúan las funciones objetivo de sus Individuos, se les asigna un Ranking **(Goldberg)** y posteriormente se les otorga un Fitness. 

   5.- La súper Población *S* se divide en subcategorías de acuerdo a los niveles de dominancia que existan, es decir, existirá la categoría de dominancia 0, la cual almacena Individuos que tengan una dominancia de 0 Individuos **(ningún Individuo los domina)**, existirá la categoría de dominancia 1 con el significado análogo y así sucesivamente hasta haber cubierto todos los niveles de dominancia existentes.

   6.- Se construye la nueva Población Padre, pare ello constará de los Individuos de *S* donde la prioridad será el nivel de dominancia, es decir, primero se añaden los elementos del nivel 0,luego los del nivel 1 y así en lo sucesivo hasta haber adquirido n elementos.
Se debe aclarar que la adquisición de Individuos por nivel debe ser total, esto significa que no se pueden dejar Individuos sueltos para el mismo nivel de dominancia. 

   Supongamos que a un nivel k existen tantos Individuos que su presunta adquisición supera el tamaño n, en este caso se debe hacer lo siguiente:
    
    6.1.- Se crea una Población provisional **(Prov)** con los Individuos del nivel k, se evalúan las funciones objetivo a cada uno de sus Individuos, se les asigna un Ranking **(Goldberg)** y posteriormente se les asigna el Fitness.

    Con los valores anteriores se calcula el Niche Count **(véase Model/SharingFunction)** de los Individuos; una vez hecho ésto se seleccionan desde Prov los Individuos faltantes con los mayores Niche Count, esto hasta completar el tamaño n de la nueva Población Padre.

   7.- Al haber conformado la nueva Población Padre, se evalúan las funciones objetivo de sus Individuos, se les asigna el Ranking correspondiente **(Goldberg)** y se les atribuye su Fitness.

   8.- Se repiten los pasos 2 a 7 hasta haber alcanzado el límite de generaciones **(iteraciones)**.

   | Como su nombre lo indica, la característica de este algoritmo es la clasificación 
    de los Individuos en niveles para su posterior selección.

   | Esto al principio propicia una Presión Selectiva moderada por la ausencia de elementos 
    con dominancia baja que suele existir en las primeras generaciones, sin embargo en iteraciones 
    posteriores se agudiza la Presión Selectiva ya que eventualmente la mayoría de los Individuos 
    serán alojados en las primeras categorías de dominancia, cubriendo casi instantáneamente 
    la demanda de Individuos necesaria en el paso 6, por lo que las categorías posteriores serán 
    cada vez menos necesarias con el paso de los ciclos.

   | Por otra parte la fusión de las Poblaciones en *S* garantiza que siempre se conserven a 
    los mejores Individuos independientemente de la generación transcurrida, a eso se le llama Elitismo.
   | Por cierto que en el algoritmo original no existe un nombre oficial para *S* sino más bien se señala como
    una estructura genérica, sin embargo se le ha formalizado con un identificador para guiar apropiadamente al 
    usuario en el flujo del algoritmo.
 
   | Para finalizar se señala que el uso del ranking de Goldberg **(véase Model/Community/Community.py)** 
    es indispensable.
"""


def execute_moea(execution_task_count,generations_queue,generations,population_size,vector_functions,vector_variables,available_expressions,number_of_decimals,
                 community_instance,algorithm_parameters,representation_instance,representation_parameters,fitness_instance,fitness_parameters,
                 sharing_function_instance,sharing_function_parameters,selection_instance,selection_parameters,crossover_instance,crossover_parameters,
                 mutation_instance,mutation_parameters):
    """
       Con base en los datos recabados se desarrolla la técnica M.O.E.A.
       que lleva por nombre N.S.G.A. II **(Non-dominated Sorting Genetic Algorithm ó
       Algoritmo Genético de Ordenamiento No Dominado)**- 
    """
    
    #Se crea una instancia de Community ya que la mayoría de los métodos auxiliares
    #residen allí.
    comunidad = getattr(community_instance,"Community")(vector_functions,vector_variables,available_expressions,number_of_decimals,
                                                        representation_instance,representation_parameters,fitness_instance,fitness_parameters,
                                                        sharing_function_instance,sharing_function_parameters,selection_instance,selection_parameters,
                                                        crossover_instance,crossover_parameters,mutation_instance,mutation_parameters)

    #Se crea una estructura para almacenar al mejor Individuo por generación.
    best_individual_along_generations = []

    #Se crea la Población Padre.
    parents = comunidad.init_population(population_size)

    try: 
        #Se evalúan las funciones objetivo de los Individuos de la Población
        #Padre.
        comunidad.evaluate_population_functions(parents)

        #Se asigna el Ranking (Goldberg) correspondiente a los Individuos de la
        #Población Padre. 
        comunidad.assign_goldberg_pareto_rank(parents)

        #Usando el Ranking, se asigna el Fitness a los Individuos de la 
        #Población Padre.
        comunidad.assign_population_fitness(parents)
 
        #El siguiente procedimiento se realizará hasta haber alcanzado
        #el número límite de generaciones.
        for x in range (1,generations + 1):
            #Esta estructura se usa para enviarle una señal a la sección View
            #con el fin de indicarle el avance que se verá reflejado en un GenerationSignalToplevel.
            #Es importante que lo que se añada al generations_queue sea una tupla de tipo
            #(execution_task_count,generación_actual).
            generations_queue.append((execution_task_count,x))

            #Se seleccionan los Individuos de la Población Padre elegidos para reproducirse-
            selected_parents_chromosomes = comunidad.execute_selection(parents)
 
            #Con base en los seleccionados en el paso anterior, se crea la Población Hija.
            children = comunidad.execute_crossover_and_mutation(selected_parents_chromosomes)

            #El primer paso del algoritmo consiste en fusionar las poblaciones Padre e
            #Hija en una súper Poblacion, para ello se hace lo siguiente:
            #Se crea una estructura para almacenar los cromosomas de los Individuos.
            parents_and_children = []

            #Los cromososmas de los Individuos de la Población Padre son añadidos
            #a dicha estructura.
            for parent in parents.get_individuals():
                parents_and_children.append(parent.get_complete_chromosome())

            #Los cromososmas de los Individuos de la Población Hija son añadidos
            #a dicha estructura.
            for child in children.get_individuals():
                parents_and_children.append(child.get_complete_chromosome())

            #La súper Población de tamaño 2n es creada. Como dato de implementación tiene sentido 
            #que la súper Poblacion tenga tamaño de 2n y entonces tenga una dominancia máxima de 2n - 1.
            new_population = comunidad.create_population(parents_and_children)
 
            #Se evalúan las funciones objetivo de los Individuos de la súper
            #Población.
            comunidad.evaluate_population_functions(new_population)

            #Se asigna el Ranking (Goldberg) a los Individuos de la 
            #súper Población.
            [auxiliar_pareto_fronts,pareto_fronts] = comunidad.assign_goldberg_pareto_rank(new_population,True)

            #Dado que debe haber n seleccionados y la súper Población consta de 2n Individuos se debe aplicar
            #un filtro, de modo que esta estructura albergará a los elegidos.
            chosen = []

            #Ahora se van tomando los cromosomas que pertenezcan primero al nivel de dominancia 0 (no hay ningún 
            #Individuo que los domine), luego a los del nivel de dominancia 1 (hay 1 Individuo que los domina) y así 
            #sucesivamente hasta haber seleccionado n elementos.
            #Cabe mencionar que se deben seleccionar los elementos del nivel completo siempre y cuando su tamaño no
            #exceda n.
            #Con esta variable se obtiene el nivel actual de dominancia.
            current_front_index = 0

            while len(chosen) != parents.get_size():

                  #Se obtiene el de nivel de dominancia actual.
                  current_front = auxiliar_pareto_fronts[current_front_index]

                  #Se verifica que los Individuos del nivel actual no sobrepasen el tamaño n,
                  #en caso de no rebasar el límite se agregan todos a la estructura chosen.
                  if len (chosen) + len(pareto_fronts[current_front]) <= parents.get_size():
                     for current_chromosome in pareto_fronts[current_front]:
                         chosen.append(current_chromosome)
  
                  #En caso de que, al momento de seleccionar un nivel k de dominancia, los elementos de la Población
                  #excedan el tamaño n, entonces se hace lo siguiente:
                  else:

                       #Es menester mencionar que en algunos casos la diferencia puede ser mucha porque no se entró en 
                       #el primer if, lo que significa que de entrada los primeros niveles de dominancia pueden ser tener 
                       #demasiados Individuos, mas que n. Por esa razón con el transcurso de las generaciones, sólo
                       #se verificará el nivel 0 de dominancia, a lo más, el nivel 1 y todos esos Individuos
                       #se agregarán en esta sección de código.
                       #Aquí se calcula el número de individuos que exceden a la población.
                       difference = parents.get_size() - len(chosen)
                      
                       #Lo que se hará entonces es agregar todos los Individuos del nivel de dominancia actual
                       #hasta cumplir con el tamaño n.
                       #Para ello se debe crear una Población Provisional aparte y
                       #asignarle un Niche Count para que puedan ser seleccionados los faltantes.  
                       provisional = comunidad.create_population(pareto_fronts[current_front])
 
                       #Se evalúan las funciones objetivo de los Individuos de la Población
                       #provisional.
                       comunidad.evaluate_population_functions(provisional)

                       #Se asigna el Ranking de Goldberg para los Individuos de la Población
                       #provisional.
                       comunidad.assign_goldberg_pareto_rank(provisional)

                       #Con base en el Ranking se asigna un Fitness a dichos Individuos.
                       comunidad.assign_population_fitness(provisional)

                       #Ahora se calcula el Niche Count de la Población.
                       comunidad.calculate_population_niche_count(provisional)

                       #Con base en este valor se ordenan a los Individuos de manera
                       #ascendente (un menor niche count significa que una solución tiene 
                       #menos vecinos por ende es más probable que dicha solución
                       #sea no dominada).
                       provisional.sort_individuals("get_niche_count",False)

                       #Se toman los Individuos de la Población provisional.
                       individuals = provisional.get_individuals()

                       #A continuación se añaden los elementos faltentes a la estructura
                       #chosen.
                       for x in range (difference):
                           chosen.append(individuals[x].get_complete_chromosome())

                  current_front_index += 1

            #Se crea la nueva Población Padre asociada a los elementos 
            #de la estructura chosen.
            parents = comunidad.create_population(chosen)

            #Se evalúan las funciones objetivo de los Individuos de la 
            #nueva Población Padre.
            comunidad.evaluate_population_functions(parents)

            #Se asigna el Ranking (Goldberg) a los Individuos de la 
            #nueva Población Padre.
            comunidad.assign_goldberg_pareto_rank(parents)

            #Se asigna el Fitness con base en el Ranking a los Individuos
            #de la nueva Población Padre.
            comunidad.assign_population_fitness(parents)

            #Se añade el mejor Individuo por generación a la estructura creada para tal fin.
            best_individual_along_generations.append(comunidad.get_best_individual(parents))

    except Exception, e:
           #En caso de un error interno las generaciones automáticamente llegan a su límite
           #para cerrar la ventana en la parte de View.
           generations_queue.append((execution_task_count,generations))

           #Posteriormente se regresa el siguiente diccionario con la información relativa
           #al origen del error.
           error = {
                    "response": "ERROR",
                    "class": "NSGAII", 
                    "method": "execute_moea",
                    "message": "An error has occurred during execution of NSGAII algorithm",
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
