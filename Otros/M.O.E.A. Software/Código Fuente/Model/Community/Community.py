#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


import random as aleatorio
import Population.Population as poblacion


class Community:
      """
         | Proporciona toda la infraestructura lógica para poder construir poblaciones y operar con éstas,
          además de transacciones relacionadas con sus elementos de manera individual.
         | Se le llama Community porque aludiendo a su significado una Community **(ó Comunidad)**
          consta de al menos una Population **(o Población)**. De esta manera se deduce que en algún momento
          habrán métodos que involucren a más de una población.

         :param vector_functions: Lista que contiene las funciones objetivo previamente 
                                  saneadas por Controller/Controller.py.
         :param vector_variables: Lista que contiene las variables de decisión previamente 
                                  saneadas por Controller/Controller.py.
         :param available_expressions: Diccionario que contiene algunas funciones escritas como azúcar sintáctica
                                       para que puedan ser utilizadas más fácilmente por el usuario y evaluadas
                                       más ŕapidamente en el programa **(véase Controller/XML/PythonExpressions.xml)**.
         :param number_of_decimals: El número de decimales que tendrán las soluciones; con este número se determina
                                    en gran medida el tamaño del cromosoma.
         :param representation_instance: Instancia de la técnica de representación que eligió el usuario
                                         **(véase Controller/Verifier.py)**.
         :param representation_parameters: Diccionario que contiene todos los parámetros adicionales a la técnica
                                           de representación considerada por el usuario.
         :param fitness_instance: Instancia de la técnica de Fitness que eligió el usuario
                                  **(véase Controller/Verifier.py)**.
         :param fitness_parameters: Diccionario que contiene todos los parámetros adicionales a la técnica
                                    de Fitness seleccionada por el usuario.
         :param sharing_function_instance: Instancia de la técnica de Sharing Function seleccionada por el usuario
                                           **(véase Controller/Verifier.py)**.
         :param sharing_function_parameters: Diccionario que contiene todos los parámetros adicionales a la técnica
                                             de Fitness seleccionada por el usuario.
         :param selection_instance: Instancia de la técnica de selección **(Selection)** elegida por el usuario
                                    **(véase Controller/Verifier.py)**.
         :param selection_parameters: Diccionario que contiene todos los parámetros adicionales a la técnica
                                      de selección **(Selection)** usada por el usuario.
         :param crossover_instance: Instancia de la técnica de cruza **(Crossover)** tomada por el usuario
                                    **(véase Controller/Verifier.py)**.
         :param crossover_parameters: Diccionario que contiene todos los parámetros adicionales a la técnica
                                      de cruza **(Crossover)** manejada por el usuario.
         :param mutation_instance: Instancia de la técnica de mutación **(Mutation)** tomada por el usuario
                                   **(véase Controller/Verifier.py)**.
         :param mutation_parameters: Diccionario que contiene todos los parámetros adicionales a la técnica
                                     de mutación **(Mutation)** seleccionada por el usuario.
         
         :type vector_functions: List		
         :type vector_variables: List
         :type available_expressions: Dictionary
         :type number_of_decimals: Integer
         :type representation_instance: Instance
         :type representation_parameters: Dictionary
         :type fitness_instance: Instance
         :type fitness_parameters: Dictionary
         :type sharing_function_instance: Instance
         :type sharing_function_parameters: Dictionary
         :type selection_instance: Instance
         :type selection_parameters: Dictionary
         :type crossover_instance: Instance
         :type crossover_parameters: Dictionary
         :type mutation_instance: Instance
         :type mutation_parameters: Dictionary
         :returns: Model.Community.Community
         :rtype: Instance
      """


      def __init__(self,vector_functions,vector_variables,available_expressions,number_of_decimals,representation_instance,representation_parameters,
                   fitness_instance,fitness_parameters,sharing_function_instance,sharing_function_parameters,selection_instance,selection_parameters,
                   crossover_instance,crossover_parameters,mutation_instance,mutation_parameters):

          #Se almacenan todos los elementos en atributos privados para
          #su posterior uso. Dado que se crea una Community por cada MOEA, conviene
          #tener las características irrepetibles para un desempeño mayor.
          self.__vector_functions = vector_functions
          self.__vector_variables = vector_variables
          self.__available_expressions = available_expressions
          self.__number_of_decimals = number_of_decimals
          self.__representation_instance = representation_instance
          self.__representation_parameters = representation_parameters
          self.__fitness_instance = fitness_instance
          self.__fitness_parameters = fitness_parameters
          self.__sharing_function_instance = sharing_function_instance 
          self.__sharing_function_parameters = sharing_function_parameters
          self.__selection_instance = selection_instance
          self.__selection_parameters = selection_parameters
          self.__crossover_instance = crossover_instance
          self.__crossover_parameters = crossover_parameters
          self.__mutation_instance = mutation_instance
          self.__mutation_parameters = mutation_parameters
          
          #Elemento que albergará el tamaño de cromosomas por cada función objetivo.
          self.__length_chromosomes = []

          #Se añade el vector de variables a los parámetros de Sharing Function, ya que este valor se utilizará
          #para el cálculo de Sigma Share (véase Model/SharingFunction).         
          self.__sharing_function_parameters["vector_variables"] = self.__vector_variables


      def init_population(self,population_size):
          """
             Crea una Población de manera aleatoria.

             :param population_size: El tamaño de la Población. 

             :type population_size: Integer
             :returns: Model.Community.Community.Population
             :rtype: Instance
          """

          #Se ejecuta la función "calculate_length_subchromosomes", la cual regresa el tamaño del cromosoma
          #por cada función objetivo, creando así un super cromosoma que constará de todos los tamaños de los subcromosomas. 
          #El resultado depende de la técnica de representación utilizada (véase Model/ChromosomalRepresentation). 
          self.__length_subchromosomes = getattr(self.__representation_instance,"calculate_length_subchromosomes")(self.__vector_variables,self.__number_of_decimals,self.__representation_parameters)              

          #Se agrega el tamaño de los subcromosomas como parámetro adicional para las técnicas de Sharing Function,
          #de la cual se hablará más adelante.
          self.__sharing_function_parameters["length_subchromosomes"] = self.__length_subchromosomes

          #A continuación se crea una instancia de la clase Population, cuyos elementos aún no se inicializan.
          population = poblacion.Population(population_size,self.__vector_functions,self.__vector_variables,self.__available_expressions,self.__number_of_decimals)

          #Entonces, con base en el resultado de self.__length_subchromosomes se inicializan los Individuos
          #de la Población, indicando además el tamaño de cada subcromosoma y por ende, el tamaño del super
          #cromosoma.
          for x in range (population_size):

              #Se manda llamar la función "create_chromosome" dependiendo de la representación elegida (véase
              #Model/ChromosomalRepresentation).
              complete_chromosome = getattr(self.__representation_instance,"create_chromosome")(self.__length_subchromosomes,self.__vector_variables,self.__number_of_decimals,self.__representation_parameters)
              
              #Se crea un individio con base en el cromosoma creado.
              population.add_individual(x,complete_chromosome)
  
          return population


      def create_population(self,set_chromosomes):
          """
             Crea una población usando un conjunto de cromosomas como base.

             :param set_chromosomes: Conjunto de cromosomas. 

             :type set_chromosomes: List
             :returns: Model.Community.Population
             :rtype: Instance
          """

          #Se crea una instancia de la población (Population) con sus elementos aún no inicializados.
          population = poblacion.Population(len(set_chromosomes),self.__vector_functions,self.__vector_variables,self.__available_expressions,self.__number_of_decimals)

          #Se inicializan cada individuo con un elemento del conjunto de cromosomas.
          for x in range(len(set_chromosomes)):
              population.add_individual(x,set_chromosomes[x])

          return population

    
      def evaluate_population_functions(self,population):
          """
             | Evalúa cada uno de los subcromosomas de los individuos de la 
              población **(Population)**.
             | De manera adicional obtiene el listado de los valores extremos tanto
              de variables de decisión como de funciones objetivo para el 
              cálculo del sigma share **(véase el método __using_sharing_function)**. 
           
             :param population: La población sobre la que se hará la operación. 
             :type population: Instance
          """

          #Se obtiene la longitud del vector de funciones objectivo para poder obtener los valores
          #máximo y múnimo de cada una de las funciones.
          length_vector_functions = population.get_length_vector_functions()

          #Se obtienen las estructuras donde se almacenarán los valores mínimo y máximo para cada variable
          #de decisión y lo mismo para cada función objetivo respectivamente (estos valores se suelen utilizar
          #para el cálculo del sigma share, el cual es un factor determinante en el Sharing Function, véase
          #Model/SharingFunction).
          decision_variables_extreme_values = population.get_decision_variables_extreme_values()
          objective_functions_extreme_values = population.get_objective_functions_extreme_values()
          
          #Se toman los individuos de la Población.
          individuals = population.get_individuals()
          for individual in individuals:

              #Por cada Individuo se toma su correspondiente cromosoma (que será en realidad el súper cromosoma).
              complete_chromosome = individual.get_complete_chromosome()          

              #A continuación se devuelven las variables de decisión evaluadas por cada individuo con ayuda del método
              #"evaluate_subchromosomes". La obtención de las variables de decisión dependerá de la 
              #representación usada (véase Model/ChromosomalRepresentation).
              decision_variables = getattr(self.__representation_instance,"evaluate_subchromosomes")(complete_chromosome,self.__length_subchromosomes,self.__vector_variables,self.__number_of_decimals,self.__representation_parameters)

              #Al final en el Individuo se evalúan las funciones objetivo con base en las variables de decisión recién obtenidas.
              #(véase Model/Community/Population/Individual.py).
              individual.evaluate_functions(decision_variables)

              #Por cada Individuo se obtienen sus variables de decisión evaluadas, así como las
              #respectivas funciones objetivo.
              current_evaluated_variables = individual.get_decision_variables()
              current_evaluated_functions = individual.get_evaluated_functions()

              #A continuación se obtienen los valores máximo y mínimo para cada 
              #variable de decisión. Dado que para las variables de decisión se usa 
              #un diccionario como almacenamiento entonces se obtienen las llaves del diccionario
              #que son precisamente los identificadores de las variables.
              for variable_name in current_evaluated_variables.keys():

                  #Se obtiene el valor correspondiente a la variable de decisión actual.
                  current_variable_value = current_evaluated_variables[variable_name]

                  #Se toman los valores mínimo y máximo actuales de la variable de decisión
                  #en cuestión.
                  current_extreme_values = decision_variables_extreme_values[variable_name]
                  current_minimal_value = current_extreme_values[0]
                  current_maximal_value = current_extreme_values[1]
                                 
                  #Si el valor de la variable actual es menor al que estaba almacenado entonces se
                  #hace una actualización para obtener el valor mínimo.
                  if current_variable_value < current_minimal_value:
                     decision_variables_extreme_values[variable_name][0] = current_variable_value 

                  #Si el valor de la variable actual es mayor al que estaba almacenado entonces se
                  #hace una actualización para obtener el valor máximo.
                  if current_variable_value > current_maximal_value:
                     decision_variables_extreme_values[variable_name][1] = current_variable_value

              #Ahora se realiza la actualización para los valores mínimo y máximo de cada
              #función objetivo.
              for x in range (length_vector_functions):
               
                  #Se obtiene el valor de la función objetivo actual.
                  current_function_value = current_evaluated_functions[x] 

                  #A continuación se almacenan los valores mínimo y máximo actuales
                  #de la variable de decisión actual.
                  current_extreme_values = objective_functions_extreme_values[x]
                  current_minimal_value = current_extreme_values[0]
                  current_maximal_value = current_extreme_values[1]

                  #Si el valor actual es menor al que estaba guardado, se hace la actualización
                  #correspondiente para el valor mínimo.
                  if current_function_value < current_minimal_value:
                     objective_functions_extreme_values[x][0] = current_function_value 

                  #Si el valor actual es mayor al que estaba guardado, se hace la actualización
                  #correspondiente para el valor máximo.
                  if current_function_value > current_maximal_value:
                     objective_functions_extreme_values[x][1] = current_function_value

          #Al final se reinsertan en la población los valores actualizados para los valores mínimos y máximos
          #de tanto las variables de decisión y las funciones objetivo.
          population.set_decision_variables_extreme_values(decision_variables_extreme_values)
          population.set_objective_functions_extreme_values(objective_functions_extreme_values)


      def __compare_dominance(self,current,challenger,allowed_functions):
          """
             .. note:: Este método es privado.
 
             Permite realizar la comparación de las funciones objetivo de los 
             individuos current y challenger tomadas una a una para indicar así quién es el dominado y quién
             es el que domina. Cabe mencionar que más apropiadamente se le conoce como dominancia
             fuerte de Pareto.

             :param current: El Individuo inicial para comprobar dominancia.
             :param challenger: El Individuo que reta al inicial para comprobar dominancia.
             :param allowed_functions: Lista que indica cuáles son las funciones objetivo que deben 
                                       compararse.

             :type current: Instance
             :type challenger: Instance
             :type allowed_functions: List
             :returns: True si current domina a challenger, False en otro caso.
             :rtype: Boolean
          """
          
          #Aquí se almacenará el resultado.
          result = False

          #Aquí se almacenan los contadores para cuando un valor es menor a otro (lt, less than)
          #y un valor es menor o igual a otro (let, less equal than).
          lt = 0
          let = 0

          #Se toman las funciones de ambos individuos.
          current_evaluated_functions = current.get_evaluated_functions()
          challenger_evaluated_functions = challenger.get_evaluated_functions()

          #Aquí se indica las posiciones de las funciones objetivo que se deben comparar en caso
          #de que allowed_functions NO contenga la palabra "All".
          if allowed_functions != "All":
             current_evaluated_functions = [current_evaluated_functions[i] for i in allowed_functions] 
             challenger_evaluated_functions = [challenger_evaluated_functions[i] for i in allowed_functions] 

          #A continuación se comṕaran las funciones objetivo tomadas una a una considerando ya las que
          #fueron filtradas por la lista allowed_functions.
          for x in range(len(current_evaluated_functions)):

                 #Se toman los valores correspondientes a la posición indicada.
                 current_value = current_evaluated_functions[x]
                 challenger_value = challenger_evaluated_functions[x]
                 
                 #Aquí radica la comparación fuerte de Pareto, para que current domine a challenger
                 #éste tiene que ser en todas sus funciones objetivo menor e igual con respecto a challenger
                 #y existir al menos una función objetivo en la que sea estrictamente menor.
                 
                 #Se busca la condición contraria, que current_value sea mayor que challenger,
                 #en este caso automáticamente se regresa un resultado Falso.
                 if current_value > challenger_value:
                    return result

                 #Si current_value y challenger_value son
                 #estrictamente menores se cumple la condición <   
                 if current_value < challenger_value:
                    lt += 1

                 #Si current_value y challenger_value son iguales 
                 #se cumple la condición de <=
                 if current_value <= challenger_value:
                    let += 1
                       
          #Para que se pueda considerar dominancia y dado que ya se consideró
          #el caso en que el current_value es mayor que challenger, basta con
          #verificar que los contadores correspondientes sean mayores que 0. 
          if lt > 0 and let > 0:
             result = True
    
          #Se regresa el resultado.
          return result
          
               
      def calculate_population_pareto_dominance(self,population,allowed_functions):
          """
             Realiza la comparación de dominancia entre todos los elementos de la Población con base
             en la evaluación de sus funciones objetivo.
             
             :param population: La Población sobre la que se hará la operación.
             :param allowed_functions: Lista que indica las funciones objetivo permitidas para hacer la 
                                       comparación.

             :type population: Instance
             :type allowed_functions: List
          """

          #Se toman los individuos de la Población.
          individuals = population.get_individuals()

          #A continuación se hace una comparación de todos los Individuos contra todos; es por ello que
          #se crea un ciclo anidado paara poder hacer tarl operación.
          for x in range(population.get_size()):

              #Se obtiene el individuo current
              current = individuals[x]
              
              for y in range(population.get_size()):      

                  #Aquí se garantiza que un mismo individuo no se puede comparar consigo mismo.
                  if y != x:

                     #Se obtiene el individuo challenger.
                     challenger = individuals[y]

                     #Se ejecuta la operación de comparación entre current y challenger.
                     dominance_condition = self.__compare_dominance(current,challenger,allowed_functions)
                    
                     #Si se llega al resultado True, significa que current domina a challenger
                     #o equivalentemente challenger es dominado por current, por lo cual se actualizan sus
                     #respectivos contadores que controlan el número de individuos que dominan y son dominados.
                     #(véase Model/Community/Population/Individual.py).
                     if dominance_condition == True:
                        #Se actualiza el valor de current que indica que ahora domina a uno más.
                        current.set_pareto_dominates(current.get_pareto_dominates() + 1)

                        #Se actualiza el valor de challenger que indica que ahora es dominado por uno más.
                        challenger.set_pareto_dominated(challenger.get_pareto_dominated() + 1)
 

      def assign_goldberg_pareto_rank(self,population,additional_info = False,allowed_functions = "All"):
          """
             | Asigna una puntuación **(ó rank)** a cada uno de los Individuos de una Población con base en su dominancia
              de Pareto.
             | En términos generales, el algoritmo trabaja con niveles, es decir, primero toma los Individuos no
              dominados y les asigna un valor 0, luego los elimina del conjunto y nuevamente aplica la 
              operación sobre los no dominados del nuevo conjunto, a los que les asigna el valor 1, y así
              sucesivamente hasta no quedar Individuos.
             | Esta técnica es usada principalmente por N.S.G.A. II.

             :param population: La Población sobre la que se hará la operación.
             :param additional_info: Un valor que le indica a la función que debe regresar información 
                                     adicional.
             :param allowed_functions: Lista que contiene las posiciones de las funciones que son admisibles 
                                       para hacer comparaciones. Por defecto tiene el valor "All".
 
             :type population: Instance
             :type additional_info: Boolean
             :type allowed_functions: List
             :returns: Si additional_info es True: un arreglo con dos elementos: en el primero 
                       se almacena una lista con los niveles de dominancia disponibles, mientras que el 
                       segundo consta de una estructura que contiene todos los posibles niveles y asociados 
                       a éstos, los cromosomas de los Individuos que los conforman.
                       Si additional_info es False: el método es void **(no regresa nada)**.
             :rtype: List
          """

          #Contiene los cromosomas de los Individuos del nivel 0.
          f1 = []
          
          #Contiene los identificadores asociados a los Individuos que conforman el 
          #nivel "i" actual.
          current_fi = []

          #Aquí se alojarán los niveles de dominancia que no estén vacíos.
          pareto_fronts_list = []

          #En esta estructura se almacenarán los identificadores de los Individuos que están
          #siendo dominados por un Individuo "p".
          sp = {}
          
          #Se crea una estructura donde se guardarán los niveles, donde para cada nivel se almacenan
          #los cromosomas de los Individuos que constituyen cada nivel.
          pareto_fronts = {}
      
          #Se obtiene el tamaño de la Población.
          population_size = population.get_size()
 
          #Se obtienen los Individuos de una Población.
          individuals = population.get_individuals()

          #Esta variable almacena el nivel de dominancia actual.
          current_front = population_size

          #Por cada Individuo en la Población se hace lo siguiente.
          for x in range (population_size):

              #Este número indicará el número de soluciones que 
              #dominan a una solución "x".
              np = 0

              #Se crea en la estructura apropiada una referencia de 
              #los Individuos que dominará la solución "x".
              sp[x] = []

              #Se obtiene el Individuo actual.
              current_individual = individuals[x]

              #Se verifica el proceso de dominancia con los demás Individuos.
              for y in range (population_size):

                  #La dominancia no tiene sentido para el mismo Individuo, de modo que
                  #se descarta.
                  if x != y:
                     
                     #Se obtiene el Individuo que será comparado con el Individuo x.
                     challenger = individuals[y]

                     #Se verifica la dominancia de x con y. De ser positiva la operación, se agrega
                     #el identificador "y" a la lista de los elementos dominados por el Individuo "x".
                     if self.__compare_dominance(current_individual,challenger,allowed_functions) == True:
                        sp[x].append(y)

                     #En caso de ser negativo se verifica que "y" domine a "x", por lo que de ser 
                     #verdadero se incrementa el número de soluciones que dominan a "x".
                     elif self.__compare_dominance(challenger,current_individual,allowed_functions) == True:        
                          np += 1

              #Se actualiza la información del número de dominados para una solución "x"
              #en la estructura apropiada.
              individuals[x].set_pareto_dominated(np)

              #Se busca el valor np más bajo, ya que no necesariamente es 0.
              if np < current_front:
                 current_front = np 
              
          #Se obtienen los Invididuos cuyo np haya sido el más bajo,
          #esto corresponde al primer nivel de dominancia 0.
          for identifier in range(population_size):
             
              #Se obtiene el Individuo actual.
              current_individual = individuals[identifier]

              #Si el número de individuos que dominan al Individuo actual
              #es el mínimo entonces se agrega en la estructura f1.
              if current_individual.get_pareto_dominated() == current_front:

                 #Se actualiza el ranking del Individuo de la estructura f1 al 
                 #frente actual + 1                   
                 current_individual.set_rank(current_front + 1)

                 #Se añade el cromosoma correspondiente a la estructura f1.
                 f1.append(current_individual.get_complete_chromosome())      

                 #Se añade el identificador del Individuo correspondiente a la 
                 #estructura f1.
                 current_fi.append(identifier)
                 
          #El frente de dominancia de nivel 0 es el que se conforma con los cromosomas de los 
          #Individuos que no están dominados.
          pareto_fronts[current_front] = f1

          #Se añade a la lista el nivel de dominancia inicial.
          pareto_fronts_list.append(current_front)
          
          #A continuación se incrementa el nivel de dominancia actual en una unidad.
          current_front += 1
           
          #Mientras la lista con los identificadores no sea vacía
          #se hace lo siguiente:
          while current_fi != []:
                #print "entro en el fi porque hay cosas"
                #Las siguientes estructuras albergarán
                #los identificadores y cromosomas de los Individuos
                #de los siguientes niveles de dominancia respectivamente.
                h_ids = []
                h_chromosomes = []

                #Se toman los identificadores del conjunto actual. 
                for z in current_fi:

                    #Se obtiene el conjunto de identificadores relativos a las 
                    #soluciones que domina el Individuo asociado al identificador "z".
                    current_sp = sp[z]

                    #Se usa cada identificador "k".
                    for k in current_sp:

                        #A continuación se obtiene el Individuo correspondiente
                        #al identificador "k".
                        q = individuals[k]#population_dict[k]

                        #Se disminuye en una unidad el valor de los Individuos
                        #que dominan a q.
                        nq = q.get_pareto_dominated() - 1 
                        q.set_pareto_dominated(nq)

                        #Si dicho valor es 0 significa que es parte del nivel de dominancia actual
                        #por lo que debe de agregarse su cromosoma en la estructura h_chromosome y 
                        #su identificador en h_id.
                        if nq == 0:
                      
                           #Se actualiza el número de elementos que dominan a la solución actual.
                           q.set_pareto_dominated(current_front)

                           #Se actualiza el rango actual
                           q.set_rank(current_front + 1)

                           #Se agrega el identificador.
                           h_ids.append(k)
 
                           #Se agrega el cromosoma.
                           h_chromosomes.append(q.get_complete_chromosome())

                #Puede darse el caso en que un nivel de dominancia se encuentre vacío, 
                #por ello es que se verifica que el nivel actual no esté vacío.                                  
                if h_chromosomes != []:

                   #Se agrega el nivel actual con el resultado de la lista h_chromosome
                   pareto_fronts[current_front] = h_chromosomes

                   #Este valor se agrega a una lista que indica que un nivel de dominancia no está
                   #vacío.
                   pareto_fronts_list.append(current_front)

                #Se actualiza el nivel de dominancia actual.
                current_front += 1 
                   
                #La estructura de identificadores pasa a ser el nuevo current_fi para que puedan
                #verificarse nuevos elementos.
                current_fi = h_ids
        
          #Al final se regresa la lista que contiene la lista de niveles de dominancia disponibles
          #y la estructura con los niveles de dominancia y sus respectivos elementos.
          if additional_info == True:
             return [pareto_fronts_list,pareto_fronts]


      def assign_fonseca_and_flemming_pareto_rank(self,population,allowed_functions = "All"):
          """
             | Asigna una puntuación **(ó rank)** a cada uno de los Individuos de una Población 
              con base en su dominancia de Pareto.
             | A grandes rasgos, el algoritmo asigna un rank que consiste en:
             .. centered:: :math:`rank(Individuo) = n\\acute{u}mero\_soluciones\_que\_dominan(Individuo) + 1`
             | Esta técnica es usada principalmente por M.O.G.A.

             :param population: La Población sobre la que se hará la operación.
             :param allowed_functions: Lista que contiene las posiciones de las funciones que son admisibles 
                                       para hacer comparaciones. Por defecto tiene el valor "All".
 
             :type population: Instance
             :type allowed_functions: List
          """

          #Se calcula la dominancia en la Población.
          self.calculate_population_pareto_dominance(population,allowed_functions)

          #Dado que los Individuos ya tienen asignado en suas atributos el número de Individuos que los dominan
          #entonces el rank de cada uno consiste en este valor más uno.
          for individual in population.get_individuals():
              individual.set_rank(individual.get_pareto_dominated() + 1)


      def assign_zitzler_and_thiele_pareto_rank(self,population,allowed_functions = "All"):
          """
             | Asigna una puntuación (rank) a cada uno de los Individuos de una Población con 
              base en su dominancia de Pareto.
             | A manera de esbozo, el algoritmo asigna un rank que consiste en una razón:
             .. centered:: :math:`rank(Individuo) = \\frac{n\\acute{u}mero\_soluciones\_dominadas(Individuo)}{tama\\tilde{n}o\_poblaci\\acute{o}n} + 1`
             | Esta técnica es usada principalmente por S.P.E.A. II

             :param population: La Población sobre la que se hará la operación.
             :param allowed_functions: Lista que contiene las posiciones de las funciones que son admisibles 
                                       para hacer comparaciones. Por defecto tiene el valor "All".
 
             :type population: Instance
             :type allowed_functions: List
          """
          
          #Se toma el tamaño de la Población.
          population_size = population.get_size()

          #Se calcula la dominancia de Pareto en la Población.
          self.calculate_population_pareto_dominance(population,allowed_functions)

          #Finalmente por cada elemento se realiza la operación de Ranking antes descrita.
          for individual in population.get_individuals():
              individual.set_rank((individual.get_pareto_dominates()/float(population_size)) + 1)

          
      def assign_population_fitness(self,population):
          """
             Aplica la asignación de Fitness para una Población dada usando como
             base el Ranking de cada Individuo **(véase Model/Fitness)**.
            
             :param population: La población sobre la que se hará la operación.
           
             :type population: Instance
          """

          #Se ejecuta el método "assign_fitness" usando la instancia previamente creada para el tipo de
          #Fitness elegido por el usuario (véase Controller/Verifier.py).
          getattr(self.__fitness_instance,"assign_fitness")(population,self.__fitness_parameters)
  

      def __using_sharing_function(self,individual_i,individual_j,alpha_share,sigma_share):
          """
             .. note:: Este método es privado.

             | Devuelve un valor que ayuda al cálculo del Sharing Function.
             | A grandes rasgos el sharing function sirve para hacer una selección más precisa de los
              mejores Individuos cuando se da el caso de que tienen el mismo número de Individuos dominados.

             :param individual_i: Individuo sobre el que se hará la operación.
             :param individual_j: Individuo sobre el que se hará la operación.
             :param alpha_share: El valor necesario para poder calcular la distancia entre Individuos.
             :param sigma_share: El valor necesario para poder calcular la distancia entre Individuos.
             
             :type individual_i: Instance
             :type individual_j: Instance
             :type alpha_share: Float
             :type sigma_share: Float
             :returns: El resultado que contribuirá al sharing function. 
             :rtype: Float
          """

          #Aquí se colocará el resultado del cálculo de la distancia
          result = 0.0

          #Se calcula la distancia entre los individuos usando la técnica que el usuario eligió en la sección gráfica
          #(véase Model/SharingFunction).
          dij = getattr(self.__sharing_function_instance,"calculate_distance")(individual_i,individual_j,self.__sharing_function_parameters)

          #De acuerdo a la técnica, si la distancia resulta menor a sigma se hace la siguiente operación.
          if dij < sigma_share:
             result = 1.0 - (dij/sigma_share)**alpha_share

          #Se regresa el resultado
          return result
        

      def calculate_population_niche_count(self,population):
          """
             Calcula el valor conocido como niche count que no es mas que la suma de los sharing function
             de todos los individuos j con el individuo i, con i != j.

             :param population: Conjunto sobre el que se hará la operación.
             
             :type population: Instance
          """

          #De acuerdo al trabajo escrito y a la documentación el valor de alpha típicamente
          #se asigna a 1, no obstante en este proyecto se le da la libertad al usuario de
          #seleccionar el valor libremente. Aquí se obtiene dicho valor con base en la información
          #ingresada por el usuario.           
          alpha_share = self.__sharing_function_parameters["alpha_sharing_function"]

          #A continuación se hace el cálculo del Sigma Share para poder obtener el Niche Count,
          #esto tomando en cuenta el tipo de distancia que haya elegido el usuario.
          sigma_share = getattr(self.__sharing_function_instance,"calculate_sigma_share")(population,self.__sharing_function_parameters)

          #Se aplica un recorrido de los Individuos de la Población con ellos mismos
          #para calcular el Niche Count de cada uno.
          for individual_i in population.get_individuals():
 
              #El valor mínimo de Niche Count para un Individuo será 1.
              result = 1.0
              for individual_j in population.get_individuals():

                  #Así se garantiza que no se hará sharing function de los individuos con ellos mismos.
                  if individual_i != individual_j:

                     #Se calcula el niche count para cada individuo_i de la población
                     result += self.__using_sharing_function(individual_i,individual_j,alpha_share,sigma_share)
        
              #Al final se añade este valor al individuo i
              individual_i.set_niche_count(result)


      def calculate_population_shared_fitness(self,population):
          """
             Calcula el Shared Fitness **(ó Fitness Compartido)** de cada uno
             de los Individuos de la Población.

             :param population: Conjunto sobre el que se hará la operación.
             
             :type population: Instance
          """
          
          for individual in population.get_individuals():
             
              #El cálculo del sharing function por individuo es: fitness / niche count. Se hace
              #esto por cada Individuo.
              individual.set_fitness(individual.get_fitness()/individual.get_niche_count())          
          
  
      def execute_selection(self,parents):
          """
             Realiza la ejecución de la técnica de selección por medio de una instancia que
             se creó previamente **(véase Controller/Verifier.py)**.
 
             :param parents: El conjunto de individuos sobre el cual se aplicará la técnica
            
             :type parents: Instance
             :returns: Una lista con los cromosomas de aquellos individuos seleccionados.
             :rtype: List
          """

          #Se toma la instancia previamente creada para realizar la ejecución de la técnica (véase Model/Operator/Selection).
          #Aunado a esto se toman los parámetros de la selección que se guardaron en la declaración de la clase y se manejan aquí.
          return getattr(self.__selection_instance,"execute_selection_technique")(parents,self.__selection_parameters)
      

      def execute_crossover_and_mutation(self,selected_parents_chromosomes):
          """
             Realiza la cruza y mutación de los Individuos. Para el caso de la cruza ésta se lleva a cabo siempre
             entre dos individuos, mientras que la mutación es unaria.

             :param selected_parents_chromosomes: El conjunto de cromosomas sobre los cuales se aplicarán dichos operadores genéticos.
            
             :type selected_parents_chromosomes: List
             :returns: Una instancia del tipo Model.Community.Population.
             :rtype: Instance   
          """

          #Se toma el tamaño de la población (que es el equivalente a tomar el tamaño de los individuos seleccionados), también
          #se inicializa una población para que ahí se almacenen los hijos mutados.
          size = len(selected_parents_chromosomes)          
          children = poblacion.Population(size,self.__vector_functions,self.__vector_variables,self.__available_expressions,self.__number_of_decimals)

          #Si se tiene una población impar simplemente se añade un elemento al azar de los seleccionados automáticamente
          #a la siguiente generación no sin antes haber sido mutado.
          if size % 2 != 0:
             size -= 1  
             index = aleatorio.randint(0,size)
             lucky_chromosome = selected_parents_chromosomes[index]
             selected_parents_chromosomes.remove(selected_parents_chromosomes[index])
             modified_lucky_chromosome = getattr(self.__mutation_instance,"execute_mutation_technique")(lucky_chromosome,self.__mutation_parameters)
             children.add_individual(size,modified_lucky_chromosome)
          
          #Tomando siempre un conjunto de cromosomas par, la cruza se realiza de la siguiente manera:
          count = 0
          for x in range(1,size,2):

              #Se toman dos cromosomas consecutivos.
              chromosome_a = selected_parents_chromosomes[x - 1]
              chromosome_b = selected_parents_chromosomes[x]

              #Se realiza la cruza sobre éstos, usando la instancia que se creó previamente con la técnica de cruza seleccionada
              #(véase Model/Operator/Crossover y Controller/Verifier.py), así como los parámetros que
              #se guardaron en la definición de la clase; la técnica de cruza devolverá 2 hijos.
              [child_1,child_2] = getattr(self.__crossover_instance,"execute_crossover_technique")(chromosome_a,chromosome_b,self.__crossover_parameters)

              #Ahora cada hijo es mutado de manera individual, utilizando una instancia de la técnica de mutación que fue elegida
              #por el usuario en la sección gráfica (véase Model/Operator/Mutation y Controller/Verifier.py) y los parámetros
              #que fueron guardados al inicio de la declaración de la clase.
              modified_child_1 = getattr(self.__mutation_instance,"execute_mutation_technique")(child_1,self.__mutation_parameters)
              modified_child_2 = getattr(self.__mutation_instance,"execute_mutation_technique")(child_2,self.__mutation_parameters)

              #Se agregan los cromosomas a la población creada con anterioridad.
              children.add_individual(x - 1,modified_child_1)
              children.add_individual(x,modified_child_2)
              count +=2

          return children
   
      
      def get_best_individual(self,population):
          """
             Obtiene el mejor individuo dentro de una población. Para estos fines el mejor individuo es aquél que
             tenga mejor dominancia.

             :param population: La población sobre la cual se hará la búsqueda.
            
             :type population: Instance
             :returns: El Individuo que cumple con la característica de la mayor dominancia.
             :rtype: Instance    
          """

          #Se guarda una copia de la población para no alterar la original. 
          sorted_population = population

          #Se manda llamar a un método de la población que ordena los individuos de acuerdo a algún criterio
          #(véase Model/Community/Population.py). El parámetro False determina el orden descendente del ordenamiento.
          sorted_population.sort_individuals("get_pareto_dominated",False)

          #Se toma el primer individuo de los individuos.
          individuals = sorted_population.get_individuals()
          best_individual = individuals[0]
          return best_individual


      def __get_best_individual_results(self,population):
          """
             .. note:: Este método es privado.
             
             Obtiene los valores de las variables de decisión y de las funciones objetivo
             por cada individuo.

             :param population: Una lista que contiene los mejores individuos por generación.

             :type population: List
             :returns: Una lista que contiene por un lado la tupla (generacion, funciones)
                       y por otro la tupla (generación, variables). Esto por cada generación.
             :rtype: List   
          """

          #Se crean los elementos donde al final se llenará la información.
          generations = []		
          decision_variables = []
          objective_functions = []

          #Por cada individuo se hace lo siguiente:
          for x in range (len(population)):
              individual = population[x]

              #Se agrega la generación
              generations.append(x + 1)

              #Se agrega la función objetivo. 
              objective_functions.append(individual.get_evaluated_functions())

              #Se agrega la variable de decisión.
              decision_variables.append(individual.get_decision_variables().values())
        
          #Se regresa la tupla (generaciones, funciones) y (generaciones, variables).
          return [generations,objective_functions],[generations,decision_variables]


      def __get_pareto_results(self,population):
          """
             .. note:: Este método es privado.
             
             | Obtiene el frente de Pareto, el complemento del frente de Pareto y el óptimo de Pareto.
             | Para una mejor orientación léase la parte escrita del proyecto.

             :param population: La Población sobre la cual se obtendrán estos elementos.

             :type population: Instance
             :returns: Una lista que contiene el frente de Pareto, su complemento y el óptimo de Pareto.
             :rtype: List   
          """
     
          #Se crean las estructuras donde se guardarán el frente de Pareto, el complemento del frente de Pareto
          #y el óptimo de Pareto.
          pareto_front = []
          pareto_optimal = []
          pareto_complement = []

          #Se toman los individuos de la población.
          #Además se toma un individuo de muestra.
          individuals = population.get_individuals()
          sample = individuals[0]
          
          #Con base en la muestra se crean casillas para cada una de las funciones objetivo para el
          #frente de Pareto y su complemento.
          for function in sample.get_evaluated_functions():
              pareto_front.append([])
              pareto_complement.append([]) 
                   
          #Con base en la muestra también se crean casillas para cada una de las variables de decisión
          #para el óptimo de Pareto.
          for variable in sample.get_decision_variables().values():
              pareto_optimal.append([])

          #Por cada individuo se hace lo siguiente:
          for individual in individuals:
              
              #Si el individuo no tiene elementos que lo dominen, significa que es parte
              #del frente de Pareto, por lo que entonces se hace lo siguiente:
              individual_functions = individual.get_evaluated_functions()
              if individual.get_pareto_dominated() == 0:   

                 #Primero se agregan sus evaluaciones en las funciones objetivo a la estructura
                 #del frente de Pareto.
                 for x in range(len(pareto_front)):
                     pareto_front[x].append(individual_functions[x])

                 #A continuación se agregan las evaluaciones en las variables de decisión 
                 #a la estructura del óptimo de Pareto.
                 individual_decision_variables = individual.get_decision_variables().values()
                 for x in range(len(pareto_optimal)):
                     pareto_optimal[x].append(individual_decision_variables[x])

              #Si el individuo tiene al menos algún elemento que lo domine, significa que es del complemento
              #del frente de Pareto, por lo que simplemente se agregan las funciones objetivo a la 
              #respectiva estructura.
              else:
                 for x in range(len(pareto_complement)):
                     pareto_complement[x].append(individual_functions[x])

          #Al final se regresa la tupla (frente de Pareto, complemento del frente de Pareto, óptimo de Pareto).
          return [pareto_front,pareto_complement,pareto_optimal]


      def get_results(self,best_individual_along_generations,external_set_population):
          """
             Recolecta la información y la almacena en una estructura que contiene dos categorías principales: 
             funciones objetivo y variables de decisión. Por cada una existen las subcategorías Pareto y mejor 
             individuo, en referencia al óptimo o frente de Pareto **(según corresponda)** y a los valores del mejor 
             individuo por generación **(véase View/Additional/ResultsGrapher/GraphFrame.py)**.

             :param best_individual_along_generations: Una lista que contiene los mejores individuos por generación.
             :param external_set_population: La población sobre la cual se efectuarán las operaciones.
 
             :type best_individual_along_generations: List
             :type external_set_population: Instance
             :returns: Un diccionario con los elementos mostrados en la descripción.
             :rtype: Dictionary  
          """

          #Se crea la estructura final donde se almacenará toda la información.
          information = {}          

          #Se obtienen los valores para los mejores individuos por generación.
          objective_functions, decision_variables = self.__get_best_individual_results(best_individual_along_generations)

          #Se obtienen el frente de Pareto, su complemento y el óptimo de Pareto.
          #Por una petición de la Dra. Katya Rodríguez Vázquez se omite el complemento de Pareto en las
          #impresiones finales, por ello es que se solicitará el complemento aquí por si en algún momento el usuario lo
          #necesita pero no se va a utilizar en la sección de impresión (View/Additional/ResultsGrapher/GraphFrame.py)
          #dado que este método no regresará esa parte.
          pareto_front, pareto_complement, pareto_optimal = self.__get_pareto_results(external_set_population)

          #Se crea la primera categoría (funciones objetivo) de la información final y se llena con los datos mostrados a continuación.
          information["objective_functions"] = {           
                                                "pareto": {
                                                           "front": pareto_front,
                                                           #No se va a regresar el complemento de Pareto.
                                                           #"complement": pareto_complement
                                                          },

                                                "best individual": {
                                                                    "functions": objective_functions,
                                                                   }
                                               }

          #Se crea la segunda categoría (variables de decisión) de la información final y se llena con los datos mostrados a continuación.
          information["decision_variables"] = {
                                               "pareto": {
                                                          "optimal": pareto_optimal
                                              	         },

                                               "best individual": {
                                                                   "variables": decision_variables,
                                                                  }
                                              }

          return information
