#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


"""
   | Se implementa la técnica M.O.E.A conocida como V.E.G.A. **(Vector Evaluated Genetic 
    Algorithm ó Algoritmo Genético de Vectores Evaluados)**.
   | La forma de proceder del algoritmo es la siguiente:
   |
   | 1.- Se crea la Población Padre (de tamaño :math:`n`).

   | 2.- Tomando en cuenta las :math:`k` funciones objetivo y la Población Padre, se crean :math:`k` subpoblaciones de tamaño :math:`n/k` cada una, si este número llega a ser irracional se pueden hacer ajustes con respecto de la distribución de los Individuos.

   | 3.- Por cada subpoblación, se aplica la técnica de Selección y obtienen los :math:`n/k` Individuos, terminado esto se deben unificar todos los seleccionados de nuevo en una súper Población.

   | 4.- Con la súper Población del paso 3, se crea a la Población Hija, la cual pasará a convertirse en la la nueva Población Padre.

   | 5.- Se repiten los pasos 2 a 4 hasta haber alcanzado el número de generaciones **(iteraciones)** límite.
   |
   | Como se puede apreciar es una implementación muy sencilla de optimización multiobjetivo,
    sin embargo el inconveniente que tiene es la fácil pérdida de material genético valioso.
   | Lo anterior significa que un Individuo que en una generación previa era el mejor para una
    función objetivo :math:`i` al momento de ser separado y seleccionado en una subpoblación :math:`j`
    (y por ende analizado bajo la función objetivo :math:`j`) puede ser muy malo en calidad y por tanto no ser seleccionado; 
    perdiéndose la ganancia genética hasta el momento obtenida para la función objetivo :math:`i;\ i \neq j`.
   |
   | Por ello es que se puede decir que V.E.G.A. genera soluciones promedio que destacan con una calidad media
    para todas las funciones objetivo.
   |
   | Finalmente hay que comentar que para este algoritmo no se requiere aplicar un Ranking específico, no obstante,
    se ha decidido utilizar el de Fonseca & Flemming **(véase Model/Community/Community.py)** pues es el más sencillo
    de implementar.
"""


def create_subpopulations(comunidad,main_population):
    """
       Método que divide a la Población principal en subpoblaciones
       de acuerdo al número de funciones objetivo.

       :param comunidad: Una instancia de Community para poder crear
                         poblaciones..
       :param main_population: La Población que será dividida.  

       :type comunidad: Instance
       :type main_population: Instance
       :returns: Una lista con las subpoblaciones **(de tipo Population)**.
       :rtype: List
    """

    #Aquí se almacenarán las subpoblaciones.
    subpopulations = []

    #Para averiguar de cuántos Individuos consta la Población.
    how_many_individuals = main_population.get_size()

    #Para averiguar cuántas funciones objetivo existen.
    how_many_objectives = main_population.get_length_vector_functions()

    #Se obtienen los Individuos de la Población.
    complete_population = main_population.get_individuals()
 
    #Las siguientes variables permiten agregar los Individuos a las poblaciones adecuadamente
    #sin cometer errores de repetición de elementos.
    lower_limit = 0
    upper_limit = 0

    #El siquiente ciclo se ejecutará de acuerdo al número de funciones objetivo que será
    #también el número de subpoblaciones.   
    for y in range (main_population.get_length_vector_functions()):

        #Para la función objetivo actual se calcula el número de Individuos que le
        #corresponde a su subpoblación asociada.
        #Deseable que se desordenen las cantidades de los individuos por objetivo.
        #Por ahora permanecen estáticas, tocandole la misma cantidad de Individuos
        #a cada subpoblación.
        individuals_per_objective = int(how_many_individuals/how_many_objectives)

        #Se actualiza el límite superior de Individuos permitido.
        upper_limit += individuals_per_objective   

        #Se toma la porción adecuada de Individuos de acuerdo a los límites
        #citados con anterioridad.   
        provisional_parents = complete_population[lower_limit:upper_limit]

        #Se inicializa una estructura que almacenará los cromosomas de los Individuos
        #pertenecientes a la subpoblación.
        chromosome_set = []

        #De acuerdo a los Individuos correspondientes a la subpoblación actual, se les
        #extrae el cromosoma y se almacenan en la estructura previa.
        for provisional_parent in provisional_parents:
            chromosome_set.append(provisional_parent.get_complete_chromosome())

        #Se procede a crear la subpoblación con el conjunto de cromosomas actual.
        subpopulation = comunidad.create_population(chromosome_set)          

        #Se añade la subpoblación actual al listado creado en un inicio.
        subpopulations.append(subpopulation)

        #Se actualiza el límite inferior para poder tomar otra porción diferente de Individuos
        #en la siguiente subpoblación.
        lower_limit = upper_limit

        #Se reduce la cantidad de Individuos disponibles.
        how_many_individuals -= individuals_per_objective

        #Se reduce la cantidad de funciones objetivo (y por ende de subpoblaciones) disponibles.
        how_many_objectives -= 1
     
    #Se regresa el listado de subpoblaciones. 
    return subpopulations


def execute_moea(execution_task_count,generations_queue,generations,population_size,vector_functions,vector_variables,available_expressions,number_of_decimals,
                 community_instance,algorithm_parameters,representation_instance,representation_parameters,fitness_instance,fitness_parameters,
                 sharing_function_instance,sharing_function_parameters,selection_instance,selection_parameters,crossover_instance,crossover_parameters,
                 mutation_instance,mutation_parameters):
    """
       De acuerdo a la información proporcionada con anterioridad, se 
       implementa el método que representa a la técnica M.O.E.A. conocida 
       como V.E.G.A. **(Vector Evaluated Genetic Algorithm ó Algoritmo 
       Genético de Vectores Evaluados)**.
    """ 

    #Se crea una instancia de Community ya que la mayoría de los métodos auxiliares
    #residen allí.
    comunidad = getattr(community_instance,"Community")(vector_functions,vector_variables,available_expressions,number_of_decimals,
                                                        representation_instance,representation_parameters,fitness_instance,fitness_parameters,
                                                        sharing_function_instance,sharing_function_parameters,selection_instance,selection_parameters,
                                                        crossover_instance,crossover_parameters,mutation_instance,mutation_parameters)

    #Se crea una estructura para almacenar al mejor Individuo por generación.
    best_individual_along_generations = []
  
    #El algoritmo V.E.G.A. requiere que se obtengan los puntos extremos del frente de Pareto, es decir,
    #los mejores resultados por cada función objetivo, por ello es que se almacena en esta estructura dichos
    #valores.
    special_individuals = []

    #Se crea la Población Padre.
    parents = comunidad.init_population(population_size)

    try:

        #El siguiente proceso ocurrirá hasta que se alcance el número
        #límite de generaciones.
        for x in range (1,generations + 1):

            #Esta estructura se usa para enviarle una señal a la sección View
            #con el fin de indicarle el avance que se verá reflejado en un GenerationSignalToplevel.
            #Es importante que lo que se añada al generations_queue sea una tupla de tipo
            #(execution_task_count,generación_actual).
            generations_queue.append((execution_task_count,x))

            #Se desordenan los Individuos para garantizar una división poblacional 
            #más aleatoria.
            parents.shuffle_individuals()

            #Se manda llamar al método para crear subpoblaciones.
            parents_subpopulations = create_subpopulations(comunidad,parents)

            #Aquí se almacenarán los cromosomas de todos los Individuos seleccionados
            #de todas las subpoblaciones.
            children_chromosomes = []

            #Una vez creadas las subpoblaciones, se procede a aplicar el método de Selección
            #de Individuos ara cada una de éstas.
            for y in range (len(parents_subpopulations)):

                #Se toma la subpoblación actual.
                current_subpopulation = parents_subpopulations[y] 

                #Se evalúan las funciones objetivo con base en las variables de decisión
                #de cada Individuo.
                comunidad.evaluate_population_functions(current_subpopulation)

                #Se asigna un Ranking a cada Individuo tomando como referencia sólo la función objetivo que 
                #representa la subpoblación.
                comunidad.assign_goldberg_pareto_rank(current_subpopulation,allowed_functions = [y])

                #Con base en el Ranking anterior, se le asigna el Fitness a los Individuos.
                comunidad.assign_population_fitness(current_subpopulation)

                #A continuación se lleva a cabo el proceso de Selección tomando en cuenta que devolverá tantos
                #cromosomas de Individuos como elementos haya en la subpoblación, por lo que no hay riesgo de
                #sobrepoblación.
                selected_parents_chromosomes = comunidad.execute_selection(current_subpopulation)

                #A la estructura children_chromosomes se le agrega los cromosomas de los elegidos de
                #la subpoblación actual.
                children_chromosomes += selected_parents_chromosomes     
           
            #Una vez obtenidos los cromosomas de los elegidos de las subpoblaciones, a la recién formada
            #súper Población "children" se le aplican los operadores de Cruza y Mutación.
            children = comunidad.execute_crossover_and_mutation(children_chromosomes)

            #Se evalúan las funciones objetivo de los Individuos de "children".
            comunidad.evaluate_population_functions(children)

            #Se asigna el Ranking a la Población "children".
            comunidad.assign_goldberg_pareto_rank(children)

            #Con base en el Ranking previo, se asigna el Fitness a la Población "children".
            comunidad.assign_population_fitness(children)

            #Se añade el mejor Individuo de la generación actual a la estructura previamente
            #creada para ello.
            best_individual_along_generations.append(comunidad.get_best_individual(children))

            #La Población Hija actual pasará a ser la nueva Población Padre para la 
            #siguiente generación.
            parents = children

        #Una vez concluido el proceso genético se procede a obtener los puntos extremos del frente de Pareto.
        #Para ello primero se almacenan los Individuos de la última generación.
        final_individuals = parents.get_individuals()

        #A continuación se obtiene la mejor solución por cada función objetivo.
        for x in range(len(vector_functions)):
 
            #Esta es la posición del mejor Individuo dentro de la estructura final_individuals.
            position = 0   
          
            #Ahora por cada Individuo se verifica que la solución sea la mejor.
            for y in range (parents.get_size()):

                #Si la posición del mejor Individuo no sea la posición del elemento actual
                #se hace lo siguiente:
                if position != y:

                   #Se obtiene el Individuo actual.
                   current_individual = final_individuals[y]

                   #Si el valor de la función objetivo del Individuo actual es menor que la del Individuo con la posición "position"
                   #entonces se actualiza este último valor.
                   if current_individual.get_evaluated_functions()[x] < final_individuals[position].get_evaluated_functions()[x]:
                      position = y

            #Al final se almacena el cromosoma de aquel Individuo en la posición "position"
            special_individuals.append(final_individuals[position].get_complete_chromosome())
                
        #Ahora para poder graficar los datos adecuadamente se debe crear una Población,
        #la cual constará de los mejores Individuos por función objetivo.
        special_population = comunidad.create_population(special_individuals)

        #Se evalúan las funciones objetivo de los Individuos de "special population".
        comunidad.evaluate_population_functions(special_population)

        #Se asigna el Ranking a la Población "special population".
        comunidad.assign_goldberg_pareto_rank(special_population)
    
    except Exception, e:
           #En caso de un error interno las generaciones automáticamente llegan a su límite
           #para cerrar la ventana en la parte de View.
           generations_queue.append((execution_task_count,generations))

           #Posteriormente se regresa el siguiente diccionario con la información relativa
           #al origen del error.
           error = {
                    "response": "ERROR",
                    "class": "VEGA", 
                    "method": "execute_moea",
                    "message": "An error has occurred during execution of V.E.G.A. algorithm",
                    "type": (str(e))
                   }   

           return error

    #Los resultados tienen el formato precisado dentro de la función get_results que se encuentra
    #en Model/Community/Community.py. Es sumamente importante que el usuario revise esta función
    #ya que de ésta depende la graficación de resultados (véase View/Additional/ResultsGrapher/ResultsGrapherToplevel.py).
    results = comunidad.get_results(best_individual_along_generations,special_population)
   
    #Se regresan dichos resultados.
    return results
