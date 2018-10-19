#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


"""
   Se desarrolla la implementación de la técnica M.O.E.A. conocida como S.P.E.A. II
   **(Strength Pareto Evolutionary Algorithm ó Algoritmo Evolutivo de Fuerza de Pareto)**.

   El funcionamiento del algoritmo es el siguiente:

   | 1.- Se inicializa una Población llamada *P* y un conjunto inicialmente vacío llamado *E* **(E albergará Individuos también)**; ambos son de tamaño n.

   | 2.- Se asigna el Fitness a los Individuos de *P* y *E* **(para ello se evalúan las funciones objetivo de los Individuos de ambos conjuntos y se asigna el Ranking Zitzler & Thiele)**.

   | 3.- A continuación se funden *P* y *E* en una súper Población **(llamémosle S también señalado en el algoritmo como Mating Pool, de tamaño n)**.Para ello primero se añaden los Individuos *NO DOMINADOS* de *P* en *S* y posteriormente los *NO DOMINADOS* de *E* en *S*.
   |  Aquí se distinguen dos casos:
   *   Si llegasen a faltar Individuos se añaden al azar Individuos *DOMINADOS* de *P* en *S* hasta completar la demanda.
   *   Si después de la fusión el número de Individuos supera a n, entonces se hace un truncamiento en *S* hasta ajustar su tamaño a n.

   | 4.- *S* será la nueva *E*, además se crea la Población Hija de la recién creada *E* **(E-Child)**.

   | 5.- E-Child será la nueva P.

   | 6.- Se repiten los pasos 2 a 5 hasta que se haya alcanzado el límite de generaciones **(iteraciones)**.

   | Finalmente lo que se regresa es *E*, ya que ahí es donde se han 
    almacenado los mejores Individuos de todas las generaciones.
   |
   | La característica de este algoritmo es que tiene una Presión Selectiva alta ya que 
    se da prioridad a los Individuos no dominados **(de ahí el nombre de 
    Fuerza de Pareto ó los más fuertes con respecto al principio de Pareto)**, 
    y el hecho de mezclar a *E* y *P* en una súper Población garantiza la conservación 
    de los mejores Individuos sin importar el transcurso de las generaciones 
    **(a eso se le conoce como Elitismo)**, pero también da una tolerancia, aunque mínima, a los
    Individuos de menor calidad como en el punto 3.
   | Además al momento de actualizar *S* a *E* y E-Child a *P* se tiene una especie de 
    seguro de vida, es decir, si en algún momento la Población E-Child llegara a 
    tener una calidad baja se tiene el respaldo de *E* para una generación posterior
    para formar *S*.
   |
   | Se debe tener en cuenta que el algoritmo originalmente no contempla ni una súper 
    Población *S* ni E-Child sino que en los pasos 3 y 4 se utiliza solamente *E* para referirse tanto a E-child como a *S*,
    sin embargo para no confundir al usuario en la funcionalidad del método se decidió colocar contenedores 
    extra para poder diferenciar más precisamente a los elementos involucrados.
   |
   | Algo muy importante a mencionar es que en el paso 1 y al momento de crear la Población E-Child
    es necesario evaluar las funciones objetivo, asignar un Ranking y posteriormente un Fitness 
    para que se puedan aplicar los operadores geneticos **(véase Model/GeneticOperator)**, para este caso 
    el Ranking es estrictamente el de Zitzler & Thiele; la descripción completa de éste se 
    encuentra en **Model/Community/Community.py**.
"""


def execute_moea(execution_task_count,generations_queue,generations,population_size,vector_functions,vector_variables,available_expressions,number_of_decimals,
                 community_instance,algorithm_parameters,representation_instance,representation_parameters,fitness_instance,fitness_parameters,
                 sharing_function_instance,sharing_function_parameters,selection_instance,selection_parameters,crossover_instance,crossover_parameters,
                 mutation_instance,mutation_parameters):
    """
       Con base en la información señalada se lleva a cabo la implementación del
       M.O.E.A. conocido como S.P.E.A. II **(Strength Pareto Evolutionary Algorithm ó
       Algoritmo Evolutivo de Fuerza de Pareto)**.
    """

    #Se crea una instancia de Community ya que la mayoría de los métodos auxiliares
    #residen allí.
    comunidad = getattr(community_instance,"Community")(vector_functions,vector_variables,available_expressions,number_of_decimals,
                                                        representation_instance,representation_parameters,fitness_instance,fitness_parameters,
                                                        sharing_function_instance,sharing_function_parameters,selection_instance,selection_parameters,
                                                        crossover_instance,crossover_parameters,mutation_instance,mutation_parameters)

    #Se crea una estructura para almacenar al mejor Individuo por generación.
    best_individual_along_generations = []

    #De acuerdo al algoritmo se inicializan la Población P (llamada simplemente P) y 
    #el conjunto externo E (llamado simplemente E).
    population_p = comunidad.init_population(population_size)
    external_set_e = comunidad.init_population(population_size)

    try:
        #Se evalúan las funciones objetivo de los Individuo en el
        #conjunto externo E, también se les asigna el correspondiente
        #Ranking (Zitzler & Thiele) y posteriormente se calcula el Fitness.
        comunidad.evaluate_population_functions(external_set_e)
        comunidad.assign_zitzler_and_thiele_pareto_rank(external_set_e)
        comunidad.assign_population_fitness(external_set_e)   

        #El procedimiento se lleva a cabo hasta haber alcanzado el número
        #límite de generaciones.
        for x in range (1,generations + 1):
            #Esta estructura se usa para enviarle una señal a la sección View
            #con el fin de indicarle el avance que se verá reflejado en un GenerationSignalToplevel.
            #Es importante que lo que se añada al generations_queue sea una tupla de tipo
            #(execution_task_count,generación_actual).
            generations_queue.append((execution_task_count,x))

            #El algoritmo estrictamente menciona que en este paso se calcule el Fitness de P y E,
            #sin embargo como alternativa técnica el Fitness de E se calcula fuera del ciclo
            #y aquí sólo se calcula el de P. 
            #Cabe mencionar que para el cálculo del Fitness antes se deben evaluar las funciones
            #objetivo y calcular el Ranking (Zitzler & Thiele).
            comunidad.evaluate_population_functions(population_p)
            comunidad.assign_zitzler_and_thiele_pareto_rank(population_p)
            comunidad.assign_population_fitness(population_p)

            #El primer paso consiste en juntar a P y E en una súper Población de tamaño n, para ello
            #se auxilia de esta variable.
            external_set_e_list = []

            #Primero se añaden los Individuos no dominados de P a la estructura
            #antes mencionada.
            for current_individual in population_p.get_individuals():
                if current_individual.get_pareto_dominated() == 0:
                   external_set_e_list.append(current_individual)
             
            #Dado que, según el algoritmo, E debe estar vacía en la primera iteración, 
            #es hasta la segunda generación que se agregan los elementos de E a la 
            #estructura esternal external_set_e_list.
            if x > 1:
               for current_individual in external_set_e.get_individuals():
                   if current_individual.get_pareto_dominated() == 0:
                      external_set_e_list.append(current_individual)
      
            #Si faltan elementos a la súper Población,los faltantes se añaden de P.
            #Cabe mencionar que tienen que añadirse los dominados.
            if len(external_set_e_list) < population_size:   
               #Aquí se calcula la diferencia de los que faltan.
               difference = population_size - len(external_set_e_list)

               #Esta variable indica cuántos elementos no dominados se van
               #agregando
               auxiliar = 0 
  
               #Aquí se van seleccionando al azar los Individuos dominados de P y agregándose a la 
               #súper Población.
               for current_individual in population_p.get_individuals():
                   if current_individual.get_pareto_dominated() > 0 and auxiliar < difference:
                      external_set_e_list.append(current_individual)
                      auxiliar += 1
         
            #Dado que la súper Población debe ser de tamaño n, si despues de haber anadido 
            #todos los elementos de E y P hay un excedente entonces se hace truncamiento 
            #hasta que el tamaño sea n.
            if len(external_set_e_list) > population_size: 
                  external_set_e_list = external_set_e_list[0:population_size]
         
            #Se crea una nueva Población E con base en los elementos seleccionados previamente.
            #Aquí se añadirán los cromosomas para después crear la Población.
            auxiliar_external_set_e = []

            #Se añaden los cromosomas de los Individuos seleccionados en la súper Población. 
            for element in external_set_e_list:
                auxiliar_external_set_e.append(element.get_complete_chromosome())
              
            #Se crea la nueva Población E .
            external_set_e = comunidad.create_population(auxiliar_external_set_e)
        
            #Se evalúan funciones objetivo de los Invididuos en E, se les asigna
            #un Ranking (Zitzler & Thiele) y se les asigna el Fitness.
            comunidad.evaluate_population_functions(external_set_e)
            comunidad.assign_zitzler_and_thiele_pareto_rank(external_set_e)
            comunidad.assign_population_fitness(external_set_e)

            #Se crea la Población Hija de E (llamda E-Child), cabe mencionar que a E también se le llama 
            #"Mating Pool".
            selected_parents_chromosomes = comunidad.execute_selection(external_set_e)
            external_set_e_child = comunidad.execute_crossover_and_mutation(selected_parents_chromosomes)

            #Se evalúan funciones objetivo de los Invididuos en E-Child, se les asigna
            #un Ranking (Zitzler & Thiele) y se les asigna el Fitness.  
            comunidad.evaluate_population_functions(external_set_e_child)
            comunidad.assign_zitzler_and_thiele_pareto_rank(external_set_e_child)
            comunidad.assign_population_fitness(external_set_e_child)

            #Ahora E-Child pasará a ser P.
            population_p = external_set_e_child

            #Se agrega el mejor Individuo por generación a la estructura creada para ello.
            best_individual_along_generations.append(comunidad.get_best_individual(external_set_e))
    
    except Exception, e: 
           #En caso de un error interno las generaciones automáticamente llegan a su límite
           #para cerrar la ventana en la parte de View.
           generations_queue.append((execution_task_count,generations))

           #Posteriormente se regresa el siguiente diccionario con la información relativa
           #al origen del error.
           error = {
                    "response": "ERROR",
                    "class": "SPEAII", 
                    "method": "execute_moea",
                    "message": "An error has occurred during execution of S.P.E.A. II algorithm",
                    "type": (str(e))
                   }   

           return error
 
    #Los resultados tienen el formato precisado dentro de la función get_results que se encuentra
    #en Model/Community/Community.py. Es sumamente importante que el usuario revise esta función
    #ya que de ésta depende la graficación de resultados (véase View/Additional/ResultsGrapher/ResultsGrapherToplevel.py).
    #El conjunto que almacena los elementos para impresión de resultados es E.
    results = comunidad.get_results(best_individual_along_generations,external_set_e)

    #Se regresan dichos resultados.
    return results
