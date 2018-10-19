#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


import math

from XMLParser import XMLParser
from Verifier import Verifier


class Controller:
      """
         | Proporciona la infraestructura adecuada para poder comunicar la sección Vista
          **(ó View)** con la sección Modelo **(ó Model)**, apoyándose de las clases XMLParser y Verifier.
         |
         | El ciclo normal consiste en proporcionar a la capa Vista **(ó View)** la información
          recabada en los archivos .xml con ayuda de la clase XMLParser con la finalidad de notificar
          al usuario de todas las técnicas disponibles.
         |  
         | Una vez ejecutada la opción de iniciar un proceso genético por el usuario, se recaban los
          datos ingresados por el usuario, los cuales pasan por un proceso de verificación y transformación
          empleando para ello los métodos de la clase Verifier. 
         |
         | En caso de haber al menos una falla en alguno de los procedimientos mencionados anteriormente
          se regresa un mensaje de error, en otro caso se pasa la información respectiva a la
          capa Model para que pueda operar con ésta.
         |  
         | En cualquiera de los dos casos anteriores se regresa la información resultante a la Vista.

         :returns: Controller.Controller
         :rtype: Instance
      """


      def __init__(self):

          #Se almacena el nombre del archivo .xml donde se 
          #almacenan los nombres de todas las técnicas con 
          #sus parámetros que se encuentran disponibles para el usuario.
          self.__features_filename = "Features.xml"

          #Se guarda el nombre del archivo .xml que contiene
          #los M.O.P.'s disponibles para el usuario.
          #Un M.O.P. (Multi-Objective Problem) es un conjunto de variables
          #de decisión y funciones objetivo cuyo resultado está bien
          #estudiado, se utiliza principalmente para comprobar que el
          #funcionamiento del proyecto es el óptimo y además proveer
          #al usuario de una alternativa rápida y concisa para utilizar
          #el proyecto.
          self.__mop_examples_filename = "MOPExamples.xml"

          #A continuación se toma el nombre del archivo que almacena las
          #expresiones especiales de Python. 
          #Esto sucede porque en ocasiones hay algunas funciones o constantes
          #especiales que el intérprete de Python no comprende directamente,
          #por ello es que se necesita establecer una relación entre las 
          #expresiones que ingresa el usuario y su equivalente en Python.
          #Por ello es que al crear o evaluar funciones objetivo se debe hacer
          #uso de estas expresiones.
          self.__python_expressions_filename = "PythonExpressions.xml"

          #Se obtiene una instancia de la clase que opera con archivos
          #.xml.
          self.__parser = XMLParser()

          #Se guarda una instancia de la clase que verifica y convierte 
          #apropiadamente los datos que el usuario ingresa para ejecutar
          #algún algoritmo M.O.E.A. (Multi-Objective Evolutionary Algorithm).
          self.__verifier = Verifier()


      def load_features(self):
          """ 
             | Regresa los datos correspondientes **(debidamente verificados)**
              a las técnicas disponibles para el usuario, los cuales se mostrarán
              en **View/MainWindow.py**.
             | **(véase View/Additional/MenuInternalOption/InternalOptionTab/FeatureFrame.py)**.
             | Esta técnica tiene como base los símiles que se encuentran en 
              **Controller/XMLParser.py** y **Controller/Verifier.py**.

             :returns: Una estructura con los métodos disponibles para el usuario.
             :rtype: Dictionary
          """

          #Aquí se almacenan los datos obtenidos por el método de Controller/XMLParser.py.
          data = None

          #Se ejecuta el método que obtiene los datos del archivo .xml correspondiente.
          #Lo que se extraiga se guarda en la variable creada anteriormente.
          try:
              data = self.__parser.load_xml_features(self.__features_filename)
     
          #Si por alguna razón ocurre una falla en la carga de datos se almacena
          #en la variable "data" el valor "ERROR", esto para indicar que ha habido
          #un desperfecto en el procedimiento.
          except:
              data = "ERROR"
       
          #Al final se regresan los datos verificados por el método
          #correspondiente de la clase Controller/Verifier.py
          return self.__verifier.verify_load_xml_features(data)    
          

      def load_mop_examples(self):
          """
             | Obtiene los datos correspondietes **(previamente verificados)**
              a los M.O.P.'s **(Multi-Objective Problems)** que se utilizan en
              en **View/MainWindow.py**
             | **(véase View/Additional/MenuInternalOption/InternalOptionTab/MOPExampleFrame.py)**.
             | Esta técnica tiene como base las análogas que se encuentran en 
              **Controller/XMLParser.py** y **Controller/Verifier.py**.

             :returns: Una estructura con los M.O.P.'s disponibles para el usuario.
             :rtype: Dictionary
          """

          #En esta variable se almacenan los datos cargados por el método
          #localizado en Controller/XMLParser.py.
          data = None

          #A continuación se lleva a cabo la carga correspondiente de los datos en el
          #archivo pertinente, almacenando éstos en la variable creada con anterioridad.
          try:
              data = self.__parser.load_xml_mop_examples(self.__mop_examples_filename)
          
          #En caso de existir alguna falla durante el proceso la variable data adquiere 
          #el valor "ERROR", para hacer énfasis en el desperfecto.
          except:
              data = "ERROR"
       
          #Se regresan los datos verificados auxiliándose del método localizado en 
          #Controller/Verifier.py.
          return self.__verifier.verify_load_xml_mop_examples(data)


      def load_python_expressions(self):
          """
             | Obtiene los datos correspondietes **(previamente verificados)**
              a las expresiones de Python, las cuales se usan para evaluar 
              funciones objetivo más eficientemente
             | **(véase View/Additional/MenuInternalOption/InternalOptionTab/PythonExpressionFrame.py)**.
             | Esta función se apoya de las homónimas localizadas en 
              **Controller/XMLParser.py** y **Controller/Verifier.py**.

             :returns: Una estructura con las expresiones de Python disponibles.
             :rtype: Dictionary
          """

          #En esta variable se almacenan los datos que se vayan a cargar con ayuda de 
          #la función ubicada en Controller/XMLParser.py.
          data = None

          #Ahora se ejecuta el método que carga los datos correspondientes, almacenando éstos
          #en la variable mencionada antes.
          try:
              data = self.__parser.load_xml_python_expressions(self.__python_expressions_filename)
          
          #Si durante el proceso llega a existir algún inconveniente entonces a la variable
          #"data" se le asigna el valor "ERROR" para enfatizar que hubo un contratiempo.
          except:
              data = "ERROR"
       
          #Para finalizar se regresa lo que se obtenga de ejecutar el método correspondiente 
          #que se encuentra en Controller/Verifier.py. 
          return self.__verifier.verify_load_xml_python_expressions(data)    
          
      
      def save_python_expressions(self,data):
          """
             Inserta las expresiones de Python que ha ingresado
             el usuario en el archivo .xml correspondiente.

             :param data: Un conjunto de las expresiones que ha ingresado el usuario.
                          Cada elemento es a su vez una lista con dos elementos, el primero
                          es la expresión original **(la que es comprensible por el 
                          usuario)**, mientras que la segunda es la expresión equivalente
                          en Python.
 
             :type data: List
             :returns: Mensaje "OK" si la inserción ha sido exitosa, mientras que en caso
                       de que haya habido un error entonces el mensaje es "ERROR".
             :rtype: String
          """

          #Se ejecuta la función pertinente (que reside en Controller/Verifier.py), la cual
          #revisa que los datos no tengan desperfectos.
          verifier_code =  self.__verifier.verify_write_xml_python_expressions(data)

          #Si el código que regresa la función es "OK", se realiza la operación de inserción
          #en el archivo correspondiente.
          if verifier_code == "OK": 
             self.__parser.write_xml_python_expressions(self.__python_expressions_filename,data)
          
          #Sin importar el código resultante, éste se regresa para que pueda ser usado en
          #otras secciones del programa (véase View/Additional/MenuInternalOption/InternalOptionTab/PythonExpressionFrame.py).
          return verifier_code


      def sanitize_settings(self,general_information,features):
          """
             Lleva a cabo la verificación y saneamiento de todos los datos
             que ha ingresado el usuario en la sección View **(véase View/MainWindow)**.

             :param general_information: El conjunto de datos que el usuario ha ingresado o
                                         seleccionado.
             :param features: Una colección de todos los elementos con sus características
                              disponibles para el usuario.

             :type general_information: Dictionary
             :type features: Dictionary
             :returns: El diccionario que contiene todos los datos debidamente saneados.
             :rtype: Dictionary
          """

          #Aquí se almacenan los resultados verificados y saneados.
          result = {}

          #Se prepara un diccionario con información genérica sobre algún error
          #que llegara a ocurrir en esta función.
          error = {
                   "response": "ERROR",
                   "class": "Controller",
                   "method": "__sanitize_settings",                
                  }

          #Se crean estructuras para guardar las expresiones de Python saneadas (convertidas a instancias).
          #La copia sirve para evitar la contaminación de dichas expresiones ya que se deberán usar para sanear
          #las funciones objetivo.
          sanitized_available_expressions = {}
          copy_sanitized_available_expressions = {} 

          #Se leen del archivo .xml correspondiente las expresiones personalizadas para Python.
          available_expressions = self.load_python_expressions()

          #Si llega a existir una falla en la lectura de dichas expresiones el proceso
          #se detiene inmediatamente no sin antes haber regresado un mensaje de error
          #con los elementos relativos a la falla.
          if available_expressions.has_key("recent"):
             error["frame"] = available_expressions["recent"]["frame"]
             error["message"] = "A problem with at least one of the Python expressions has occurred."
             available_expressions["previous"].append(available_expressions["recent"])
             available_expressions["recent"] = error
             return available_expressions

          #A continuación se transforman las expresiones de Python a instancias para que puedan ser reconocidas
          #independientemente de la biblioteca usada.
          #La variable copia es para mantener un registro limpio de dichas instancias ya que para hacer las pruebas
          #de calidad a las funciones objetivo se usará la otra variable y ésta quedará inevitablemente contaminada.
          for expression in available_expressions.keys():
              sanitized_expression = self.__verifier.get_dynamic_function(available_expressions[expression])
              sanitized_available_expressions[expression] = sanitized_expression
              copy_sanitized_available_expressions[expression] = sanitized_expression

          #Posteriormente se lleva a cabo el proceso de sanitización de los tipos de las técnicas, es decir,
          #las técnicas usadas deben ser o todas de tipo float o todas de tipo binario (aunque hay algunas que
          #pueden pertenecer a ambos tipos).
          #En caso de existir un desperfecto el proceso se interrumpe aquí, regresando un mensaje de error
          #con los detalles.
          sanitized_techniques = self.__verifier.sanitize_techniques(general_information,features)
          if sanitized_techniques.has_key("recent"):
             error["frame"] = sanitized_techniques["recent"]["frame"]
             error["message"] = "A problem with at least one selected technique has occurred."
             sanitized_techniques["previous"].append(sanitized_techniques["recent"])
             sanitized_techniques["recent"] = error
             return sanitized_techniques

          #Ahora se lleva a cabo la verificación y saneamiento de las variables de decisión (junto con sus
          #respectivos rangos).
          #En caso de existir algún error se interrumpe el proceso, regresando un mensaje con los 
          #detalles de la falla.
          sanitized_decision_variables = self.__verifier.sanitize_decision_variables(general_information["Decision Variables"]) 
          if  sanitized_decision_variables.has_key("recent"):
              error["frame"] = "Decision Variables"
              error["message"] = "A problem occurred while sanitizing decision variables."
              sanitized_decision_variables["previous"].append(sanitized_decision_variables["recent"])
              sanitized_decision_variables["recent"] = error
              return sanitized_decision_variables
	
          #A continuación se verifican y transforman las funciones objetivo.
          #Si llega a existir un desperfecto en el proceso se manda un mensaje de error 
          #con las fallas detalladas.
          sanitized_objective_functions = self.__verifier.sanitize_objective_functions(sanitized_decision_variables,copy_sanitized_available_expressions,general_information["Objective Functions"])
          if sanitized_objective_functions.has_key("recent"):
             error["frame"] = "Objective Functions"
             error["message"] = "A problem occurred while sanitizing objective functions."
             sanitized_objective_functions["previous"].append(sanitized_objective_functions["recent"])
             sanitized_objective_functions["recent"] = error
             return sanitized_objective_functions

          #Toca el turno de la verificación y transformación de datos correspondientes
          #a la categoría "Population Settings" que se encuentra en View/MainWindow.py.
          #En caso de encontrarse con algún error, el proceso se detiene en este punto
          #y se obtiene un mensaje de error con las características alusivas a éste.
          sanitized_population_settings = self.__verifier.sanitize_population_settings(general_information["Population Settings"],features)
          if sanitized_population_settings.has_key("recent"):
             error["frame"] = "Population Settings"
             error["message"] = "A problem occurred while sanitizing population settings."
             sanitized_population_settings["previous"].append(sanitized_population_settings["recent"])
             sanitized_population_settings["recent"] = error
             return sanitized_population_settings

          #Ahora se revisan y transforman los datos correspondientes a la categoría
          #"Genetic Operators Settings" que se encuentran en View/MainWindow.py, si
          #se recaba alguna falla en el procedimiento se detiene esta función regresando
          #un mensaje de error con las características del desperfecto.
          sanitized_genetic_operator_settings = self.__verifier.sanitize_genetic_operators_settings(general_information["Genetic Operators Settings"],features,sanitized_decision_variables,sanitized_population_settings["number_of_decimals"])
          if sanitized_genetic_operator_settings.has_key("recent"):
             error["frame"] = "Genetic Operators Settings"
             error["message"] = "A problem occurred while sanitizing genetic operator settings."
             sanitized_genetic_operator_settings["previous"].append(sanitized_genetic_operator_settings["recent"])
             sanitized_genetic_operator_settings["recent"] = error
             return sanitized_genetic_operator_settings

          #Para concluir se verifican y sanean los datos relacionados con la categoría
          #"MOEAs Settings" localizada en View/MainWindow.py. En caso de ocurrir un desperfecto
          #el proceso es interrumpido en este punto y se devuelve un mensaje de error con los
          #detalles alusivos a la falla.
          sanitized_moeas_settings = self.__verifier.sanitize_moeas_settings(general_information["MOEAs Settings"],features)
          if sanitized_moeas_settings.has_key("recent"):
             error["frame"] = "MOEAs Settings"
             error["message"] = "A problem occurred while sanitizing moeas settings."
             sanitized_moeas_settings["previous"].append(sanitized_moeas_settings["recent"])
             sanitized_moeas_settings["recent"] = error
             return sanitized_moeas_settings          
          
          #Llegados a este punto todos los elementos saneados se agregan en la
          #estructura creada explícitamente para ello.
          #Primero se adjuntan las expresiones de Python saneadas, es decir, se convierten
          #en instancias del tipo de función que representan.
          result.update({
                         "available_expressions": sanitized_available_expressions
                        })

          #A continuación se añaden las variables de decisión saneadas.
          result.update(sanitized_decision_variables)

          #Posteriormente se agregan las funciones objetivo saneadas. 
          result.update(sanitized_objective_functions)

          #Ahora se adjuntan los elementos saneados de la categoría
          #gráfica "Population Settings".
          result.update(sanitized_population_settings)

          #Luego se anexan los elementos saneados correspondientes
          #a la cateoría gráfica "Genetic Operator Settings".
          result.update(sanitized_genetic_operator_settings)

          #Entonces se colocan los elementos saneados alusivos a la 
          #categoría gráfica "MOEAs Settings".
          result.update(sanitized_moeas_settings)
 
          #Finalmente se regresa el diccionario con todos los elementos
          #de todas las categorías debidamente saneados.         
          return result
      
    
      def execute_procedure(self,execution_task_count,generations_queue,sanitized_information):
          """
             Realiza la ejecución de algún algoritmo M.O.E.A.
             **(Multi-Objective Evolutionary Algorithm)** y se encarga
             de obtener los resultados apropiadamente.

             :param execution_task_count: Una característica numérica que identifica inequívocamente
                                          a esta función que será ejecutada de las demás, ya que el objetivo
                                          del proyecto es poder ejecutar varios de estos métodos de manera
                                          concurrente **(véase View/Additional/ResultsGrapher/ResultsGrapherToplevel.py)**.
             :param generations_queue: Una instancia a una cola **(Queue)**, la cual servirá para
                                       escribir a esa estructura el número actual de generación
                                       por el que cursa el algoritmo. Esta acción es para fines de 
                                       concurrencia **(véase View/MainWindow.py)**.
             :param sanitized_information: Los parámetros que ingresó el usuario
                                           debidamente verificados y saneados.

             :type execution_task_count: Integer
             :type generations_queue: Instance
             :type sanitized_information: Dictionary
             :returns: Un diccionario con información de los resultados de haber
                       ejecutado el M.O.E.A. seleccionado por el usuario, la
                       estructura del mismo puede verse en **Model/Community/Community.py**.
             :rtype: Dictionary
          """
          
          #Tomando en cuenta la información saneada, ésta se separa apropiadamente
          #para que pueda pasarse como parámetros en el M.O.E.A.
          #Este es el número de generaciones.
          generations = sanitized_information["number_of_generations"]

          #Este es el tamaño de la población.
          population_size = sanitized_information["population_size"]

          #Se obtiene el vector de funciones objetivo.
          vector_functions = sanitized_information["vector_functions"]
   
          #Se obtiene el vector de variables de decisión.
          vector_variables = sanitized_information["vector_variables"]

          #Se obtienen las expresiones especiales de Python.
          available_expressions = sanitized_information["available_expressions"]

          #Aquí se almacena el número de decimales que llevarán las soluciones
          #de una Población (véase Model/Community/Population/Population.py).
          number_of_decimals = sanitized_information["number_of_decimals"]

          #A continuación se adquiere la instancia de la Comunidad
          #(véase Model/Community/Community.py).
          community_instance = sanitized_information["community_instance"]

          #Se almacenan los valores de la instancia del M.O.E.A.
          #seleccionado (véase Model/MOEA), así como de sus parámetros.
          algorithm_instance = sanitized_information["moea_instance"]
          algorithm_parameters = sanitized_information["moea_parameters"]

          #Se extraen los valores de la instancia de la técnica de Representación
          #Cromosómica elegida (Chromosomal Representation, véase Model/ChromosomalRepresentation), 
          #así como de sus parámetros.
          representation_instance = sanitized_information["representation_instance"]
          representation_parameters = sanitized_information["representation_parameters"]

          #Se obtienen los valores de la instancia de la técnica de Fitness
          #utilizada (véase Model/Fitness), así como de sus parámetros.
          fitness_instance = sanitized_information["fitness_instance"]
          fitness_parameters = sanitized_information["fitness_parameters"]

          #Ahora se extraen los valores de la instancia de la técnica de Sharing Function
          #(ó Función de Compartición, véase Model/SharingFunction) escogida, así como de sus parámetros.
          sharing_function_instance = sanitized_information["sharing_function_instance"]
          sharing_function_parameters = sanitized_information["sharing_function_parameters"]

          #Luego se guardan los valores de la instancia de la técnica de Selection
          #(ó Selección, véase Model/Operator/Selection) utilizada, así como de sus parámetros.
          selection_instance = sanitized_information["selection_instance"]
          selection_parameters = sanitized_information["selection_parameters"]

          #A continuación se guardan los valores de la instancia de la técnica de Crossover
          #(ó Cruza, véase Model/Operator/Crossover) empleada, así como de sus parámetros.
          crossover_instance = sanitized_information["crossover_instance"]
          crossover_parameters = sanitized_information["crossover_parameters"]

          #Posteriormente se almacenan los valores de la instancia de la técnica de Mutation
          #(ó Mutación, véase Model/Operator/Mutation) elegida, así como de sus parámetros.
          mutation_instance = sanitized_information["mutation_instance"]
          mutation_parameters = sanitized_information["mutation_parameters"]
             
          #Se manda ejecutar el método execute_moea de la instancia del
          #algoritmo que se creó previamente (véase Verifier.py).
          #La finalidad de esta implementación es obtener la ejecución de 
          #varios algoritmos de manera dinámica, es decir, sin necesidad 
          #de estar importando bibliotecas y colocando el código de manera
          #estática.
          final_results = getattr(algorithm_instance,"execute_moea")(execution_task_count,generations_queue,generations,population_size,
                                                                    vector_functions,vector_variables,available_expressions,number_of_decimals,
                                                                   community_instance,algorithm_parameters,representation_instance,representation_parameters,
                                                                 fitness_instance,fitness_parameters,sharing_function_instance,sharing_function_parameters,  			                                                  selection_instance,selection_parameters,crossover_instance,crossover_parameters,
                                                                  mutation_instance,mutation_parameters)

          #Nota: no es necesario agregar una capa de error en caso 
          #de recibir algo incorrecto, la misma sección Model se 
          #encarga de todo.
          #Al final se regresan los resultados de la ejecución del M.O.E.A.
          return final_results
