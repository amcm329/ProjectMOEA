#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


import re
import random as aleatorio


class Verifier:
      """
         | Realiza principalmente la verificación y transformación adecuada de los datos 
          que el usuario introduce en **View/MainWindow.py** para alimentar a los algoritmos 
          que se encuentran en la sección Model **(más en concreto Model/MOEA)**.
         |
         | En caso de haber algún error regresa los mensajes de error adecuados para que puedan
          ser interpretados por la capa Vista y precisar al usuario el acontecimiento ocurrido.
         |
         | Por otra parte si se ha llevado a cabo la verificación correctamente se obtiene la información
          transformada apropiadamente.
         |
         | De manera secundaria también ofrece métodos de verificación para la extracción
          y colocación de datos en los archivos .xml **(véase XMLParser y el directorio Controller/XML)**.

         :returns: Controller.Verifier
         :rtype: Instance
      """


      def verify_load_xml_features(self,data):
          """
             Verifica que los datos obtenidos de las técnicas disponibles que alimentan 
             a la Ventana Principal **(véase View/MainWindow.py)** no tengan defectos.
             Este método se apoya de **load_xml_features** localizado en 
             **Controller/XMLParser.py**.

             :param data: Los datos que son leídos por el método **load_xml_features**
                          mencionado previamente.

             :type data: Dictionary
             :returns: Si los datos contienen algún error, un diccionario con las características
                       de la falla, en otro caso los datos mismos.
             :rtype: Dictionary
          """

          #Primero se crea un diccionario con el mensaje de error que contempla una posible
          #falla.
          error = {
                   "class": "Verifier",
                   "method": "__verify_load_xml_features",
                   "message": "The .xml file regarding the available techniques is malformed."
                  }

          #Del método load_xml_features se establece que si el tipo de la variable 
          #"data" NO es un diccionario entonces se determina que falló la carga de datos
          #y luego se regresa el diccionario de error con información actualizada.
          if type(data) != dict:
             error["frame"] = "Objective Functions"
             return {
                     "recent": error, 
                     "previous": []
                    }

          #Se regresa la variable que contiene ya sea el mensaje de error o los
          #datos correctos.
          return data


      def verify_load_xml_mop_examples(self,data):
          """
             | Revisa que los M.O.P.'s **(Multi-Objective Problems)**
              que se muestran en **View/MainWindow.py** a través de
             | **View/Additional/MenuInternalOption/InternalOptionTab/MOPExampleFrame.py** 
              estén libres de errores.
             | Este método se apoya de **load_mop_examples** localizado en 
              **Controller/XMLParser.py**.

             :param data: Los datos que son leídos por el método **load_mop_examples**
                          mencionado previamente.

             :type data: Dictionary
             :returns: Si los datos contienen algún error, un diccionario con las características
                       de la falla, en otro caso los datos mismos.
             :rtype: Dictionary
          """

          #Primero se crea un diccionario con el mensaje de error que contempla una posible
          #falla.
          error = {
                   "class": "Verifier",
                   "method": "__verify_load_xml_mop_examples",
                   "message": "The .xml file regarding the M.O.P.'s. is malformed."
                  }

          #Del método load_xml_mop_examples se concluye que si el tipo de la variable 
          #"data" NO es un diccionario entonces se determina que falló la carga de datos
          #y luego se regresa el diccionario de error con información actualizada.
          if type(data) != dict:
             error["frame"] = "Objective Functions"
             return {
                     "recent": error, 
                     "previous": []
                    }

          #Se regresa la variable que contiene ya sea el mensaje de error o los
          #datos correctos.
          return data


      def verify_load_xml_python_expressions(self,data):
          """
             | Revisa que las expresiones de Python estén libres de errores.
             | Este método se apoya de **load_python_expressions** localizado en 
              **Controller/XMLParser.py**.

             :param data: Los datos que son leídos por el método **load_python_expressions**
                          mencionado previamente.

             :type data: Dictionary
             :returns: Si los datos contienen algún error, un diccionario con las características
                       de la falla, en otro caso los datos mismos.
             :rtype: Dictionary
          """

          #Primero se crea un diccionario con el mensaje de error que surgiría en caso de una
          #falla.
          error = {
                   "class": "Verifier",
                   "method": "__verify_load_xml_python_expressions",
                   "message": "The .xml file for Python expressions is malformed."
                  }

          #Del método load_xml_python_expressions se aclara que si el tipo de la variable 
          #"data" NO es un diccionario entonces se determina que falló la carga de datos
          #y luego se regresa el diccionario de error con información actualizada.
          if type(data) != dict:
             error["frame"] = "Objective Functions"
             return {
                     "recent": error, 
                     "previous": []
                    }

          #Se regresa la variable que contiene ya sea el mensaje de error o los
          #datos correctos.
          return data


      def verify_write_xml_python_expressions(self,data):
          """
             Verifica la consistencia de los datos relativos a las
             expresiones de Python antes de ser escritos en el archivo .xml
             correspondiente.

             :param data: El conjunto de expresiones que serán almacenadas.
   
             :type data: List
             :returns: Un mensaje "OK" si la verificación fue satisfactoria,
                       y "ERROR" en caso de aparecer alguna falla.
             :rtype: String                                             
          """

          #Con esta estructura se verifica que no existan expresiones
          #repetidas
          repeated = {}

          #Por cada elemento de los datos se hace lo siguiente:
          for element in data:

              #El elemento se descompone en dos factores: la expresión original (la que
              #utiliza el usuario) y la expresión de Python (la que entiende este intérprete).
              expression = element[0].replace(" ","").replace("	","")
              python_expression = element[1].replace(" ","").replace("	","")
              
              #Si la expresión original o la expresión de Python son vacías o la expresión
              #original está repetida entonces se considera un error y debe mandarse el mensaje
              #correspondiente.
              if expression == "" or python_expression == "" or repeated.has_key(expression):
                 return "ERROR"
                
              #Aquí se almacena la expresión actual para considerar su conteo y por ende
              #su repetición.
              repeated[expression] = 1

          #Si no hubo ningún error se regresa el mensaje "OK", indicando que los datos no
          #tienen errores. 
          return "OK" 
                   

      def __verify_instance(self,name_class):
          """
             .. note:: Este método es privado.

             | Devuelve una instancia del nombre de la clase que se le pase
              como parámetro.
             | 
             | Esta funcionalidad es útil sobre todo para la sección Model ya que
              uno de los objetivos es proporcionar al usuario de una infraestructura 
              rápida con técnicas fácilmente intercambiables sin necesidad de estar
              importando explícitamente cada una de éstas.
             |
             | De esta forma con base en una instancia se puede ejecutar cualquier método
              de manera dinámica.

             :param name_class: el nombre de la clase **(con su ruta)** de la cual se
                                    desea obtener una instancia.

             :type name_class: String
             :returns: Una instancia de la clase solicitada si el proceso es exitoso,
                       en otro caso se obtiene un diccionario con los detalles de la
                       falla.
             :rtype: Instance/Dictionary
          """

          #Aquí se colocará la instancia resultante.
          instance = None

          try:
              #Se crea la instancia con base en la clase otorgada como parámetro.
              instance = __import__(name_class,globals(),locals(),["object"],-1) 
     
          except:

              #En caso de que haya un problema se asigna la instancia al siguiente
              #mensaje.
              instance = {
                          "class": "Verifier", 
                          "method": "__verify_instance",
                          "message": "A problem occured with instance {0}.".format(instance_class)
                         }  

          #Se regresa la variable instancia independientemente de su contenido.
          return instance


      def get_dynamic_function(self,complete_function):
          """
             Obtiene una instancia de una función en un String 
             de la forma **biblioteca.función**.
             Este método se usa para convertir las expresiones de Python
             en instancias que serán utilizadas al momento de evaluar  
             funciones objetivo **(véase View/Additional/MenuInternalOption/InternalOptionTab/PythonExpressionFrame.py,
             Controller/XML/PythonExpressions.xml)**.
 
             :param complete_function: un String preferentemente de la forma
                                       **biblioteca.función** **(el punto debe ir incluido)**.
 
             :type complete_function: String
             :returns: Una instancia de la función asociada a la biblioteca.
             :rtype: Instance
          """          

          #Aquí se almacenará la instancia.
          instance = None
 
          #Se coloca un bloque try para poder asegurarse de contemplar
          #todas las posibles fallas.
          try: 

              #Si existe un punto en el String entonces significa
              #que se puede separar en biblioteca y función.
              if '.' in complete_function:

                 #Se hace la separación en biblioteca y función.
                 splitted_function = complete_function.split('.')
                 library = splitted_function[0]
                 function = splitted_function[1]

                 #Se crea la instancia relativa a la biblioteca.
                 library_instance = self.__verify_instance(library)
 
                 #Con base en la instancia anterior se toma la función
                 #pertinente.
                 instance = getattr(library_instance,function)

              #En caso de que el String no cumpla con la 
              #característica de la separación simplemente se evalúa
              #el contenido
              else:               
                   instance = eval(complete_function)
           
          #En caso de cualquier falla durante el proceso 
          #se asigna la instancia a None.
          except:
                 instance = None

          #Al final se regresa la instancia.
          return instance


      def __cast_parameter(self,parameter_value,parameter_settings):
          """
             .. note:: Este método es privado.

             Verifica un parámetro asociado a alguna técnica.
             Primero asegura que el parámetro se pueda evaluar correctamente,
             posteriormente convierte apropiadamente el tipo de dato pasando 
             de String a Boolean, Integer ó Float según corresponda.

             :param parameter_value: El valor actual del parámetro.
             :param parameter_settings: Un diccionario que contiene el tipo del parámetro
                                        **(bool, integer ó float)** y el rango que debe tomar
                                        tanto inferior como superior.
                                       
             :type parameter_value: Float
             :type parameter_settings: Dictionary
             :returns: El valor saneado del parámetro si no hay fallas, pero si se encuentra
                       algún desperfecto entonces se regresa un diccionario con la información
                       detallada del desperfecto.
             :rtype: (Boolean, Integer, Float)/Dictionary                                  
          """

          #Aquí se almacenará el parámetro saneado (que ya se probó su tipo y responde
          #apropiadamente a los rangos establecidos).
          sanitized_parameter = None

          #Se obtiene el tipo de parámetro.
          parameter_type = parameter_settings["type"]

          #Se prepara un diccionario con información sobre el error
          #por si un desperfecto llega a ocurrir.
          error = {
                   "response": "ERROR",
                   "class": "Verifier", 
                   "method": "__cast_parameter"
                  }   

          #Se evalúa el parámetro actual con el valor actual y el tipo
          #que le corresponde.
          try:
              sanitized_parameter = eval(parameter_type)(parameter_value)
              
          except:

              #En caso de haber un error durante esta evaluación se regresa
              #un mensaje de error.
              error["message"] = "Invalid value for at least one of the additional parameters."
              return  error
       
          #Independientemente del tipo de parámetro, al haber pasado la prueba anterior
          #ahora es momento de identificar, con base en el tipo mencionado, el tipo
          #de transformación que se deba hacer, para ello se considera que existen
          #los tipos bool y float, el integer se considera un caso especial de float.
          #Entonces se procede a hacer lo siguiente:
          if parameter_type == "bool":
             
             #Se verifica que el valor sea True.
             if parameter_value.lower() == "true":
                sanitized_parameter = True

             #Se verifica que el valor sea False
             elif parameter_value.lower() == "false":
                  sanitized_parameter = False

             #Si existe algo adicional a estas dos opciones entonces
             #se manda un mensaje de error.
             else:
                 error["message"] = "Boolean value must be either True or False."
                 return  error

          else:
               #Se obtienen los rangos inferior y superior en los 
               #que debe oscilar el parámetro.
               parameter_lower_range = parameter_settings["lower_range"]
               parameter_upper_range = parameter_settings["upper_range"]

               #Se procede a hacer lo siguiente:
               #Se crean variables para indicar si el parámetro pasa o no la
               #prueba de los rangos inferior y superior.
               lower_flag = False
               upper_flag = False

               #Si el rango inferior del parámetro está definido y es mayor que el valor
               #actual del paŕametro entonces significa que hay un problema y se levanta la
               #correspondiente bandera.
               if parameter_lower_range != '-':
                  if sanitized_parameter < eval(parameter_type)(parameter_lower_range):
                     lower_flag = True 
  
               #Si el rango superior del parámetro está definido y es menor que el valor
               #actual del paŕametro entonces significa que hay un problema y se levanta la
               #correspondiente bandera.
               if parameter_upper_range != '-':
                  if sanitized_parameter > eval(parameter_type)(parameter_upper_range):
                     upper_flag = True 
  
               #Si al menos una de las banderas es True entonces se manda un mensaje
               #de error indicando que al menos uno de los rangos del parámetro es incorrecto.
               if lower_flag == True or upper_flag == True:
                  error["message"] = "Invalid range for at least one of the additional parameters."
                  sanitized_parameter = error         
        
          #Si se pasan todas las pruebas se regresa el parámetro saneado.
          return sanitized_parameter


      def sanitize_techniques(self,general_information,features):
          """
             | Realiza una verificación adicional concerniente al tipo de representación de todas las técnicas seleccionadas.
             | Lo anterior significa que, usando la Representación Cromosómica **(ó Chromosomal Representation,
              véase Model/ChromosomalRepresentation, View/Main/Population/PopulationFrame.py)**, todas las técnicas
              deben concordar con el mismo tipo de representación cromosómica que se haya seleccionado.
             | Para esta versión sólo están disponibles las representaciones binaria y de punto flotante.

             :param general_information: El listado de características disponibles **(véase XMLParser.py)**.
             :param features: La colección de datos que seleccionó el usuario en la sección View.

             :type general_information: Dictionary
             :type features: Dictionary
             :returns: Un diccionario el cual, si la verificación es exitosa, es el mismo general_informacion,
                       si por el contrario falla, entonces es un diccionario que contiene detalles del error.
             :rtype: Dictionary
          """

          #Se obtiene la representación cromosómica seleccionada por el usuario en View/MainWindow.py.
          chromosomal_representation = general_information["Population Settings"]["population_technique"]

          #Se selecciona la clasificación relativa a la representación cromosómica anterior.
          initial_classification = features["Population Settings"]["Population"]["techniques"][chromosomal_representation]["classification"]

          #Si llega a existir algún inconveniente en el proceso se prepara un diccionario
          #con información relativa a la falla.
          error = {
                   "response": "ERROR",
                   "class": "Verifier", 
                   "method": "sanitize_techniques",
                   "message": "According to the chromosomal representation, all the selected techniques must be of the same type ({0} in this case).".format(initial_classification)
                  }  
  
          #A continuación se hace la verificación de la clasificación con la
          #de todas las técnicas seleccionadas por el usuario.
          for category in general_information.keys():

              #Se elige la categoría actual (véase View/MainWindow, Controller/XML/Features.xml).
              current_category = general_information[category]

              #Por cáda técnica de la categoría actual se lleva a cabo lo siguiente:
              for technique in current_category.keys():

                  #Se garantiza que se esté revisando una técnica (puede
                  #estarse revisando un parámetro).
                  if "technique" in technique:

                     #Se obtiene la técnica actual.
                     technique_test = general_information[category][technique]

                     #Se otienen las técnicas seleccionadas por el usuario.
                     for section in features[category].keys():

                         #Se verifica que la técnica actual exista en las seleccionadas por
                         #el usuario.
                         if features[category][section]["techniques"].has_key(technique_test):
 
                            #Se obtiene la clasificación de la técnica seleccionada por el usuario.
                            technique_test_classification =  features[category][section]["techniques"][technique_test]["classification"]

                            #Si la clasificación inicial es distinta a la seleccionada por el usuario
                            #entonces hay un error y se regresa el mensaje pertinente.
                            if initial_classification != technique_test_classification and technique_test_classification != '-':
                               error["frame"] = category
                               return {
                                       "recent": error, 
                                       "previous": []
                                      }
       
          #Si no llega a existir algún error durante el proceso, simplemente
          #se regresa el diccionario original de información general.
          return general_information
    

      def sanitize_decision_variables(self,vector_variables):
          """
             | Verifica el conjunto de elementos de la categoría "Decision Variables"
              **(véase View/Main/DecisionVariable/DecisionVariableFrame.py)**, los cuales
              son precisamente las variables de decisión.
             | Primero se asegura que cada variable de decisión se pueda evaluar
              correctamente, posteriormente convierte apropiadamente el tipo
              de dato de sus respectivos rangos, pasando de String a Float.

             :param vector_variables: El vector que contiene las variables de 
                                      decisión con sus correspondientes rangos.
                                       
             :type vector_variables: Dictionary
             :returns: Un diccionario con las variables de decisión y sus 
                       rangos debidamente saneados.
             :rtype: Dictionary              
          """

          #Aquí se almacenarán las variables de decisión repetidas.
          repeated = []

          #Aquí se almacenarán las variables de decisión saneadas
          #(ya fueron probados tanto la estructura sintáctica del identificador
          #como su correcto valor dentro de los rangos especificados).
          sanitized_vector_variables = []

          #Se crea una expresión regular para verificar la correcta
          #sintaxis de los identificadores de las variables de decisión.
          valid_format = r"^[a-zA-Z](?:\w*_*)*$"

          #Se obtienen las variables de decisión.
          current_vector_variables = vector_variables["vector_variables"] 

          #Se obtiene la longitud de las variables de decisión.
          current_length = len(current_vector_variables)

          #En caso de que surja algún desperfecto durante el método
          #se prepara un diccionario con información relativa al error. 
          error = {
                   "response": "ERROR",
                   "frame": "Decision Variables", 
                   "class": "Verifier",
                   "method": "sanitize_decision_variables"
                  }

          #Por cada variable de decisión se realiza lo siguiente:
          for current_vector in current_vector_variables:

              #Se obtiene el identificador de la variable.
              variable = current_vector[0]

              #Se obtienen los rangos (inferior y superior) de la variable.
              ranges = current_vector[1]
      
              #Si el identificador de la variable es vacío se arroja un mensaje
              #de error.
              if variable == '': 
                 error["message"] = "At least one of the variables is empty."
                 return {
                         "recent": error, 
                         "previous": []
                        } 

              #Si al menos uno de los rangos es vacío, se arroja un mensaje
              #de error.
              if ranges[0] == '' or ranges[1] == '':           
                 error["message"] = "At least one of the ranges is empty."
                 return {
                         "recent": error, 
                         "previous": []
                        } 
      
              #Si el identificador de la variable no cumple con la sintaxis
              #adecuada (debe empezar con una letra) se regresa un mensaje de error
              if not(re.compile(valid_format).match(variable)):
                 error["message"] = "At least one of the variables is malformed."
                 return {
                         "recent": error, 
                         "previous": []
                        } 

              #Si la variable ya estaba repetida (en la estructura pertinente), entonces
              #se lanza un mensaje de error.
              if variable in repeated:
                 error["message"] = "At least one variable is repeated."
                 return {
                         "recent": error, 
                         "previous": []
                        } 
                  
              #Una vez que se aprobaron las pruebas básicas entonces se procede a hacer
              #la correcta conversión de valores.
              else:
                  #Aquí se almacenarán los valores de los rangos transformados.
                  lower_range = ""
                  upper_range = ""

                  #Se añade la variable en la estructura de repetidos para verificar
                  #que la siguiente variable se encuentre o no repetida.
                  repeated.append(variable)

                  #Se transforman los rangos (esto porque por defecto tienen el tipo 
                  #String y se desea que se transformen a Float).
                  try:
                      lower_range = float(eval(ranges[0]))
                      upper_range = float(eval(ranges[1]))
                            
                  except:

                        #Si ocurre algún error durante esta transformación se regresa
                        #un mensaje de error.
                        error["message"] = "Not a valid range for at least one of the variables."
                        return {
                                "recent": error, 
                                "previous": []
                               }
                   
                  #Pasando la prueba anterior, se verifica que el rango superior no sea menor que
                  #el rango inferior, pues de ser este el caso se retorna un mensaje de error.
                  if lower_range > upper_range:
                     error["message"] = "At least in one of the variables, lower range is greater than upper range."
                     return {
                             "recent": error, 
                             "previous": []
                            }

                  #Si se pasan todas las pruebas exitosamente entonces se agrega a la estructura final
                  #la variable de decisión y sus rangos saneados.
                  else:
                       sanitized_vector_variables.append([variable,[lower_range,upper_range]])                
               
          
          #Al final se obtiene un diccionario que incluye la estructura que almacena a todas
          #las variables de decisión y sus rangos saneados.   
          return {
                  "vector_variables": sanitized_vector_variables
                 }


      def sanitize_objective_functions(self,vector_variables,available_expressions,vector_functions):
          """
             Lleva a cabo el saneamiento de los elementos correspondientes a la categoría
             "Objective Functions" **(véase View/Main/ObjectiveFuncion/ObjectiveFunctionFrame.py)**, 
             los cuales son de hecho sólo las funciones objetivo.
             
             :param vector_variables: El vector de variables de decisión que el usuario
                                      ha ingresado.
             :param available_expressions: Un listado con las expresiones de Python
                                           disponibles **(véase Controller/XML/PythonExpressions.xml,
                                           View/Additional/MenuInternalOption/InternalOptionTab/PythonExpressionFrame.py)**.
             :param vector_functions: El vector de funciones objetivo ingresados por el usuario.

             :type vector_variables: Dictionary
             :type available_expressions: Dictionary
             :type vector_functions: Dictionary
             :returns: Si el proceso fue exitoso, se obtiene el mismo vector_functions,
                       en otro caso se regresa un diccionario con información detallada
                       sobre el errror encontrado.
             :rtype: List/Dictionary
          """

          #Se toman las variables de decisión ingresadas por el usuario,
          #ya que la prueba de las funciones objetivo se hará usando los primeros.
          vector_variables_test = vector_variables["vector_variables"]

          #Se obtienen las funciones objetivo.
          vector_functions_test = vector_functions["vector_functions"] 

          #Se obtienen las expresiones especiales de Python.
          expressions = available_expressions

          #En caso de una falla en el proceso, se prepara el mensaje de error con sus 
          #detalles.
          error = {
                   "response": "ERROR",
                   "class": "Verifier", 
                   "method": "sanitize_objective_functions",
                  }  

          #Para realizar las pruebas en las funciones objetivo, se deben
          #crear valores de prueba para las variables de decisión (por defecto
          #esa creación de valores se hace en Model/ChromosomalRepresentation).
          for current_vector in vector_variables_test:

              #Se toma el nombre de la variable.
              variable = current_vector[0]

              #Se obtienen sus rangos inferior y superior.
              ranges = current_vector[1]
              lower_limit = ranges[0]
              upper_limit = ranges[1]

              #Se aprovecha la estructura expressions y se agrega ahí la variable
              #con su valor de prueba.
              #Si al menos una de las variables de decisión ya estaba en expressions
              #se manda un mensaje de error (esto es por seguridad).
              if expressions.has_key(variable):
                     error["message"] = "At least one of the decision variables is repeated in the Python expressions."
                     return {
                             "recent": error, 
                             "previous": []
                            }              

              #Si no hay problema con las variable de decisión actual entonces
              #se agrega a la estructura.
              else:
                 expressions[variable] = aleatorio.uniform(lower_limit,upper_limit)
                 
          #A continuación se lleva a cabo la evaluación de funciones objetivo.
          try:

              #Primero se verifica que no esté vacía, de ser el caso entonces
              #se regresa un mensaje de error.
              for function in vector_functions_test:
                  if function == '':
                     error["message"] = "At least one of the functions is empty."
                     return {
                             "recent": error, 
                             "previous": []
                            }
      
                  #Ahora se realiza la evaluación de la función, si no hay
                  #falla en este proceso significa que ésta está bien formada
                  #sintácticamente hablando.
                  evaluated_function = eval(function,{},expressions)

          except:

              #Si por el contrario llega a existir alguna falla en el proceso entonces se 
              #retorna un mensaje de error.
              error["message"] = "At least one of the functions is malformed."
              return {
                      "recent": error, 
                      "previous":[]
                     }

          #Si se aprobaron todas las pruebas se regresa 
          #el mismo vector de funciones objetivo.
          return vector_functions


      def sanitize_population_settings(self,population_settings,features):
          """
             Verifica la consistencia y realiza el saneamiento de los datos
             que ingresó el usuario concernientes a la sección "Population Settings"
             **(véase View/Main/Population/PopulationFrame.py)**.
  
             :param population_settings: El listado de técnicas y sus parámetros que el usuario
                                         eligió en la sección correspondiente.
             :param features: El conjunto de las opciones disponibles 
                              para esta sección, así como sus características.

             :type population_settings: Dictionary
             :type features: Dictionary
             :returns: Un diccionario que, dependiendo de los resultados, puede contener
                       o información del error encontrado durante el procedimiento o 
                       todos los datos debidamente verificados y transformados.
             :rtype: Dictionary
          """

          #Se adjunta la ruta de la técnica de Fitness (véase Model/Fitness)
          #que el usuario ha seleccionado.
          fitness_class = population_settings["fitness_class"]

          #Ahora se almacena el nombre de la técnica de Fitness que el usuario
          #ha elegido.
          fitness_technique = population_settings["fitness_technique"]

          #A continuación se obtienen los parámetros asociados a la técnica
          #de Fitness seleccionada por el usuario.
          fitness_parameters = population_settings["fitness_parameters"]  

          #Se obtienen las características de los parámetros de la técnica
          #de Fitness que el usuario ha seleccionado.
          fitness_features = features["Population Settings"]["Fitness"]["techniques"][fitness_technique]["parameters"]

          #Es almacenada la ruta de la técnica de Representación Cromosómica
          #(Chromosomal Representation, véase Model/ChromosomalRepresentation)
          #que el usuario ha seleccionado.
          population_class = population_settings["population_class"]

          #Luego se recaba el nombre de la técnica de Representación Cromosómica
          #que el usuario ha elegido.
          population_technique = population_settings["population_technique"]

          #Entonces se adquieren los parámetros asociados a la técnica
          #de Representación Cromosómica seleccionada por el usuario.
          population_parameters = population_settings["population_parameters"]

          #Ahora se almacenan las características de los parámetros de la técnica
          #de Representación Cromosómica que el usuario ha seleccionado.
          population_features = features["Population Settings"]["Population"]["techniques"][population_technique]["parameters"]
          
          #Se guarda el nombre de la ruta de la clase Community (véase Model/Community/Community.py), 
          #la cual es la base para el proceso genético.
	  community_class = features["Population Settings"]["Population"]["community_path"]

          #En caso de que surja cualquier desperfecto durante el proceso
          #se prepara un mensaje de error para ser regresado por el método.
          error = {
                   "response": "ERROR",
                   "class": "Verifier", 
                   "method": "sanitize_population_settings"
                  }   
    
          #Aquí se almacenará el tamaño de la población saneado.
          sanitized_population_size = -1

          #En esta variable se guarda el valor saneado correspondiente
          #al número de decimales.
          sanitized_number_of_decimals = -1

          #Dentro de esta variable se guarda el valor relativo al número
          #de generaciones.
          sanitized_number_of_generations = -1
          
          #En las siguientes dos varibles se colocarán los valores 
          #saneados relativos a las técnicas de Representación Cromosómica 
          #y Fitness respectivamente, las cuales han sido seleccionadas 
          #por el usuario.
          sanitized_fitness_parameters = {}
          sanitized_population_parameters = {} 

          #En esta variable se colocarán todos los valores saneados finales.
          sanitized_population_settings = {}

          #Primero se obtiene una instancia de la clase Community.
          sanitized_community_instance = self.__verify_instance(community_class)

          #Si el tipo devuelto por el método es un diccionario significa que ha 
          #habido un error en el proceso y por ende se regresa la información
          #alusiva a éste.
          if type(sanitized_community_instance) == dict:
             error["frame"] = "Fitness"
             error["message"] = "Problem while creating community instance."
             return {
                     "recent": error, 
                     "previous": [sanitized_community_instance]
                    } 

          #En caso de no haber problema se almacena la instancia en la estructura
          #final.
          sanitized_population_settings["community_instance"] = sanitized_community_instance

          #Ahora toca el turno de obtener la instancia de la técnica de Fitness
          #elegida por el usuario.
          sanitized_fitness_instance = self.__verify_instance(fitness_class)

          #Nuevamente y por las mismas razones que en el caso anterior, si el
          #método pertinente devuelve un diccionario, entonces hubo una falla
          #y se regresan los detalles del desperfecto.
          if type(sanitized_fitness_instance) == dict:
             error["frame"] = "Fitness"
             error["message"] = "Problem while creating fitness instance."
             return {
                     "recent": error, 
                     "previous": [sanitized_fitness_instance]
                    } 

          #En caso de no haber falla entonces se adjunta la instancia 
          #en la estructura final y se prosigue con el método.
          sanitized_population_settings["fitness_instance"] = sanitized_fitness_instance

          #A continuación se obtiene la instancia para la técnica de Representación
          #Cromosómica seleccionada por el usuario.
          sanitized_representation_instance = self.__verify_instance(population_class)

          #Si se devuelve un diccionario en el método anterior, entonces hubo un error
          #en el proceso y se lanza un mensaje con los detalles del mismo.
          if type(sanitized_representation_instance) == dict:
             error["frame"] = "Population"
             error["message"] = "Problem while creating representation instance."
             return {
                     "recent": error, 
                     "previous": [sanitized_representation_instance]
                    } 

          #Si no hubo desperfecto alguno entonces se guarda la instancia en
          #la estructura pertinente y se continúa con el proceso.
          sanitized_population_settings["representation_instance"] = sanitized_representation_instance
    
          #Toca turno al saneamiento del valor relacionado con el número de generaciones.
          try:
              
              #Si el número de generaciones es menor o igual a 0 entonces se considera un error
              #y por ende se arroja un mensaje de falla.
              sanitized_number_of_generations = int(population_settings["number_of_generations"]) 
              if sanitized_number_of_generations <= 0:
                 error["frame"] = "Population"
                 error["message"] = "Invalid range for Number of Generations."
                 return {
                         "recent": error,
                         "previous": []
                        } 
         
              #Si el número de generaciones cumple con las características solicitadas
              #se recaba en la estructura final y se continúa con el método.
              sanitized_population_settings["number_of_generations"] = sanitized_number_of_generations 

          except: 

              #Si durante el procedimiento anterior se llega a este punto
              #significa que el valor ingresado para el número de generaciones
              #no era del tipo Integer y entonces se retorna un mensaje de error.
              error["frame"] = "Population"
              error["message"] = "Invalid Number of Generations."
              return {
                      "recent": error, 
                      "previous": []
                     } 
    
          #Se realiza el saneamiento del valor asociado al tamaño de la Población
          #(véase Model/Community/Population.py).
          try:

              #Se verifica que el tamaño no tenga un valor negativo o 0, de encontrarse
              #con alguno de estos casos se retornará un mensaje de error.
              sanitized_population_size = int(population_settings["population_size"])
              if sanitized_population_size <= 0:
                 error["frame"] = "Population"
                 error["message"] = "Invalid range for Population Size."
                 return {
                         "recent": error, 
                         "previous": []
                        } 

              #Si no hubo problemas durante el saneamiento se recolecta el dato
              #pertinente.
              sanitized_population_settings["population_size"] = sanitized_population_size 

          except:

              #Si hubo algún error durante el proceso de saneamiento significa
              #que el valor del tamaño de la Población no era de tipo Integer, por lo que
              #se regresa un mensaje de error.
              error["frame"] = "Population"
              error["message"] = "Invalid Population Size."
              return {
                      "recent": error,
                      "previous": []
                     }
     
          #Ahora se realiza el saneamiento del número de decimales que deben tener
          #las soluciones propuestas en una Población (véase Model/Community/Population.py).
          try:

              #Se verifica que el número de decimales no sea un número negativo, de encontrarse
              #con este desperfecto se arroja un mensaje de error.
              sanitized_number_of_decimals = int(population_settings["number_of_decimals"])
              if sanitized_number_of_decimals < 0:
                 error["frame"] = "Population"
                 error["message"] = "Invalid range For Number of Decimals."
                 return {
                         "recent": error,
                         "previous": []
                        }     

              #Si no hay fallas en el proceso entonces se recolecta el dato ya saneado.
              sanitized_population_settings["number_of_decimals"] = sanitized_number_of_decimals

          except: 

              #Si durante el procedimiento se haya un error, significa
              #que el número de decimales no era de tipo Integer por lo que
              #se arroja un mensaje con detalles de la falla.
              error["frame"] = "Population"
              error["message"] = "Invalid Number of Decimals."
              return {
                      "recent": error, 
                      "previous": []
                     }     
        
          #A continuación se revisan y sanean los parámetros correspondientes a la técnica
          #de Fitness que seleccionó el usuario.
          for parameter in fitness_features:

              #Se selecciona el nombre actual del parámetro.
              parameter_variable = parameter["variable"]

              #Se manda llamar a la función que sanea parámetros.
              sanitized_parameter = self.__cast_parameter(fitness_parameters[parameter_variable],parameter)   

              #Si el tipo del resultado obtenido es un diccionario, significa que
              #previamente se halló una falla en el proceso por lo que se regresará
              #un mensaje de error.
              if type(sanitized_parameter) == dict:
                 error["frame"] = "Fitness"
                 error["message"] = "Problem while sanitizing parameters."
                 return {
                         "recent": error, 
                         "previous": [sanitized_parameter]
                        }     

              #En caso de que no haya existido falla, se recolecta el parámetro saneado.
              sanitized_fitness_parameters[parameter_variable] = sanitized_parameter

          #Al final se recolecta la estructura que almacena los parámetros saneados.
          sanitized_population_settings["fitness_parameters"] = sanitized_fitness_parameters 

          #A continuación se lleva a cabo el proceso de saneamiento
          #para los parámetros relativos a la técnica de Representación
          #Cromosómica elegida por el usuario.
          for parameter in population_features:

              #Se selecciona el nombre actual del parámetro.
              parameter_variable = parameter["variable"]

              #Se manda llamar a la función que sanea parámetros.
              sanitized_parameter = self.__cast_parameter(population_parameters[parameter_variable],parameter)   

              #Si el tipo del resultado obtenido es un diccionario, significa que
              #previamente se halló una falla en el proceso por lo que se regresará
              #un mensaje de error.
              if type(sanitized_parameter) == dict:
                 error["frame"] = "Fitness"
                 error["message"] = "Problem while sanitizing parameters."
                 return {
                         "recent": error, 
                         "previous": [sanitized_parameter]
                        }     
              #En caso de que no haya existido falla, se recolecta el parámetro saneado.
              sanitized_population_parameters[parameter_variable] = sanitized_parameter

          #Al final se recolecta la estructura que almacena los parámetros saneados.
          sanitized_population_settings["representation_parameters"] = sanitized_population_parameters

          #Para concluir si no se encontró desperfecto en ninguna de las 
          #etapas anteriores se regresa el diccionario con la información
          #aprobada y convertida.
          return sanitized_population_settings

 
      def sanitize_genetic_operators_settings(self,genetic_operators_settings,features,vector_variables,number_of_decimals):
          """
             Revisa la integridad y sanea los datos que ingresó el usuario 
             concernientes a la sección "Genetic Operators Settings"
             **(véase View/Main/GeneticOperator/GeneticOperatorFrame.py)**.
  
             :param genetic_operators_settings: El listado de técnicas y sus parámetros que el usuario
                                                eligió en la sección correspondiente.
             :param features: El conjunto de las opciones disponibles 
                              para esta sección, así como sus características.
             :param vector_variables: El vector de variables de decisión.
             :param number_of_decimals: El número de decimales que llevará cada solución en 
                                        Population.

             :type genetic_operators_settings: Dictionary
             :type features: Dictionary
             :type vector_variables: List
             :type number_of_decimals: Integer
             :returns: Un diccionario que, dependiendo de los resultados, puede contener
                       o información del error encontrado durante el procedimiento o 
                       todos los datos debidamente verificados y transformados.
             :rtype: Dictionary
          """

          #Se obtiene la ruta de la clase del método de Selección (véase Model/Operator/Selection)
          #que ha seleccionado el usuario.
          selection_class = genetic_operators_settings["selection_class"]

          #Se adquiere el nombre de la técnica de Selección que el usuario
          #solicitó.
          selection_technique = genetic_operators_settings["selection_technique"]

          #Ahora se recaban los parámetros asociados a la técnica de Selección
          #que el usuario pidió.
          selection_parameters = genetic_operators_settings["selection_parameters"]

          #A continuación se extrae la información de los parámetros asociados 
          #a la técnica de Selección que el usuario seleccionó.
          selection_features = features["Genetic Operators Settings"]["Selection"]["techniques"][selection_technique]["parameters"]

          #Se almacena la ruta de la clase del método de Cruza (Model/Operator/Crossover)
          #que el usuario ha elegido.
          crossover_class = genetic_operators_settings["crossover_class"]

          #Se extrae el nombre de la técnica de Cruza que el usuario ha 
          #seleccionado.
          crossover_technique = genetic_operators_settings["crossover_technique"]

          #Ahora se extraen los parámetros relacionados con la técnica de Cruza
          #que el usuario ha pedido.
          crossover_parameters = genetic_operators_settings["crossover_parameters"]

          #Luego se obtiene la información relacionada con los parámetros relativos
          #al método de Cruza que el usuario ha precisado.
          crossover_features = features["Genetic Operators Settings"]["Crossover"]["techniques"][crossover_technique]["parameters"]

          #Se selecciona la ruta del método de Mutación (Model/Operator/Mutation) 
          #que ha elegido el usuario.
          mutation_class = genetic_operators_settings["mutation_class"]

          #Luego se selecciona el nombre de la técnica del método de Mutación
          #que el usuario ha precisado.
          mutation_technique = genetic_operators_settings["mutation_technique"]

          #A continuación se seleccionan los parámetros alusivos a la técnica 
          #de Mutación escogida por el usuario.
          mutation_parameters = genetic_operators_settings["mutation_parameters"]      

          #Entonces se toma información de las técnicas ligadas al método de 
          #Mutación que el usuario ha tomado.
          mutation_features = features["Genetic Operators Settings"]["Mutation"]["techniques"][mutation_technique]["parameters"]

          #En caso de la aparición de cualquier falla durante el procedimiento, se prepara
          #un diccionario con información alusiva al error.
          error = {
                   "response": "ERROR",
                   "class": "Verifier", 
                   "method": "sanitize_generic_operators_settings"
                  }   

          #Aquí se almacenará el valor saneado de la probabilidad de Cruza.
          sanitized_probability_crossover_general = -1 

          #En esta variable se guardará el valor saneado de la probabilidad de Mutación.
          sanitized_probability_mutation_general = -1

          #En las siguientes estructuras se almacenarán los parámetros 
          #relacionados con las técnicas de Selección, Cruza y Mutación respectivamente.
          sanitized_selection_parameters = {}
          sanitized_crossover_parameters = {}
          sanitized_mutation_parameters = {}

          #En esta estructura se almacenarán todos los valores saneadas.
          sanitized_genetic_operators_settings = {}
    
          #Ahora se obtiene una instancia de la técnica de Selección.
          sanitized_selection_instance = self.__verify_instance(selection_class)

          #Si el método regresa un diccionario, significa que hubo una falla y entonces
          #el proceso termina con un mensaje de error.
          if type(sanitized_selection_instance) == dict:
             error["frame"] = "Selection"
             error["message"] = "Problem while creating selection instance."
             return {
                     "recent": error, 
                     "previous": [sanitized_selection_instance]
                    }      

          #Si no hubo falla alguna entonces el método continua su proceso, habiendo antes
          #almacenado el valor en la estructura pertinente.
          sanitized_genetic_operators_settings["selection_instance"] = sanitized_selection_instance

          #Se obtiene una instancia del método de Cruza.
          sanitized_crossover_instance = self.__verify_instance(crossover_class)

          #Si el resultado anterior es un diccionario entonces hubo un error
          #en la creación de la instancia, por lo que el proceso concluye aquí
          #retornando un mensaje de error.
          if type(sanitized_crossover_instance) == dict:
             error["frame"] = "Crossover"
             error["message"] = "Problem while creating crossover instance."
             return {
                     "recent": error, 
                     "previous": [sanitized_crossover_instance]
                    }     

          #Al no haber falla alguna en la instancia, se prosigue con el método principal
          #almacenando la instancia en la estructura final.
          sanitized_genetic_operators_settings["crossover_instance"] = sanitized_crossover_instance

          #Ahora se obtiene una instancia del método de Mutación.
          sanitized_mutation_instance = self.__verify_instance(mutation_class)

          #Si se regresa un diccionario en vez de la instancia significa que 
          #hubo un error durante la creación de instancia, entonces 
          #se regresa un mensaje de error con lo cual concluye este método.
          if type(sanitized_mutation_instance) == dict:
             error["frame"] = "Mutation"
             error["message"] = "Problem while creating mutation instance."
             return {
                     "recent": error, 
                     "previous": [sanitized_mutation_instance]
                    }     

          #Si no se detecta falla alguna en el procedimiento se procede a almacenar
          #la instancia y se continúa con el método principal.
          sanitized_genetic_operators_settings["mutation_instance"] = sanitized_mutation_instance

          #A continuación se verifican los valores de los parámetros 
          #del método de Selección.           
          for parameter in selection_features:

              #Se obtiene el parámetro actual.
              parameter_variable = parameter["variable"]

              #Se sanea el parámetro actual.
              sanitized_parameter = self.__cast_parameter(selection_parameters[parameter_variable],parameter)   

              #Si el método regresa un diccionario, significa que hubo una falla con
              #el saneamiento de algún parámetro y el método principal termina arrojando
              #para ello un mensaje de error.
              if type(sanitized_parameter) == dict:
                 error["frame"] = "Selection"
                 error["message"] = "Problem while casting selection parameters."
                 return {
                         "recent": error, 
                         "previous": [sanitized_parameter]
                        }     

              #En caso contrario se almacena localmente el parámetro.
              sanitized_selection_parameters[parameter_variable] = sanitized_parameter

          #LLegando a este punto se almacena la estructura que contiene a los 
          #parámetros saneados dentro de la estructura principal.
          sanitized_genetic_operators_settings["selection_parameters"] = sanitized_selection_parameters 

          #A continuación se aplica el saneamiento de la probabilidad de Cruza.
          try:

              #Si la probabilidad de cruza es un valor que no está entre 0 y 1 se considera un error
              #por lo cual se arroja un mensaje de fall.              
              sanitized_probability_crossover_general = float(genetic_operators_settings["probability_crossover_general"])
              if sanitized_probability_crossover_general < 0.0 or sanitized_probability_crossover_general > 1.0:
                 error["frame"] = "Crossover"
                 error["message"] = "Invalid range for Crossover Probability."
                 return {
                         "recent": error, 
                         "previous": []
                        }

              #Si el valor cumple con los requisitos anteriormente mencionados entonces
              #se almacena en la estructura pertinente.
              sanitized_crossover_parameters["probability_crossover_general"] = sanitized_probability_crossover_general

          #Si durante el proceso se llega a esta excepción significa que el valor admitido
          #no era ni siquiera Float, por lo que el proceso principal concluye y se
          #regresa un mensaje con los detalles de la falla.
          except: 
              error["frame"] = "Crossover"
              error["message"] = "Invalid Crossover Probability."
              return {
                      "recent": error, 
                      "previous":[]
                     }      
  
          #Ahora es turno de la verificación de los valores
          #de los parámetros asociados a la técnica de Cruza.        
          for parameter in crossover_features:

              #Se obtiene el valor del parámetro actual.
              parameter_variable = parameter["variable"]

              #Se manda llamar a la función que sanea el parámetro.
              sanitized_parameter = self.__cast_parameter(crossover_parameters[parameter_variable],parameter)   

              #Si el método anterior regresa un diccionario, entonces
              #hubo un error durante el saneamiento y debe interrumpirse el 
              #proceso principal devolviendo el diccionario que contiene las fallas.
              if type(sanitized_parameter) == dict:
                 error["frame"] = "Crossover"
                 error["message"] = "Problem while sanitizing crossover parameters."
                 return {
                         "recent": error, 
                         "previous": [sanitized_parameter]
                        }      

              #Si no hay ninguna falla con el método entonces se almacena el parámetro
              #actual en la estructura correspondiente.
              sanitized_crossover_parameters[parameter_variable] = sanitized_parameter

          #Si en general no hubo problema alguno con ninguno de los parámetros
          #se almacena la estructura correspondiente en la estructura final.
          sanitized_genetic_operators_settings["crossover_parameters"] = sanitized_crossover_parameters 

          #Es momento de aplicar el saneamiento en la variable de 
          #probabilidad de Mutación.
          try:

              #Si el valor obtenido no oscila entre 0 y 1 entonces se considera fallido, por lo cual
              #se debe arrojar un mensaje de error, terminando así el método principal.
              sanitized_probability_mutation_general = float(genetic_operators_settings["probability_mutation_general"])
              if sanitized_probability_mutation_general < 0.0 or sanitized_probability_mutation_general > 1.0:
                 error["frame"] = "Mutation"
                 error["message"] = "Invalid range for Mutation Probability."
                 return {
                         "recent": error, 
                         "previous": []
                        }      

              #Si se cumplieron los requisitos para la probabilidad de Mutación entonces se 
              #guarda el valor resultante en la estructura principal.
              sanitized_mutation_parameters["probability_mutation_general"] = sanitized_probability_mutation_general
      
          #Si por alguna razón se atraviesa por el bloque except, significa que la probabilidad
          #de Mutación no era un valor de tipo Float, por ello es que el método principal
          #debe terminar regresando para ello la información detallada de la falla.
          except: 
              error["frame"] = "Mutation"
              error["message"] = "Invalid Mutation Probability."
              return {
                      "recent": error, 
                      "previous":[]
                     }      
     
          #A continuación se revisan los valores de los
          #parámetros para la técnica de Mutación seleccionada.
          for parameter in mutation_features:

              #se obtiene el valor del parámetro actual.
              parameter_variable = parameter["variable"]

              #Se aplica la función de saneamiento del parámetro actual.
              sanitized_parameter = self.__cast_parameter(mutation_parameters[parameter_variable],parameter)   

              #Si el método anterior devuelve un diccionario se trata entonces
              #de una falla, por lo que la función principal debe terminar regresando
              #entonces un diccionario con los detalles del error.
              if type(sanitized_parameter) == dict:
                 error["frame"] = "Mutation"
                 error["message"] = "Problem while sanitizing mutation parameters."
                 return {
                         "recent": error, 
                         "previous": [sanitized_parameter]
                        }      
           
              #Si no hubo falla alguna entonces se agrega el valor del parámetro
              #actual a la estructura local.    
              sanitized_selection_parameters[parameter_variable] = sanitized_parameter

          #Los siguientes valores se agregan tal cual se tomaron, éstos internamente son esenciales
          #para poder llevar a cabo la Mutación de Punto Flotante, su saneamiento no es necesario
          #ya que éstos fueron aplicados en métodos anteriores.
          sanitized_mutation_parameters["number_of_decimals_floatpoint_mutation"] = number_of_decimals
          sanitized_mutation_parameters["vector_variables_floatpoint_mutation"] = vector_variables

          #Al final se añaden todos los valores saneados de parámetros relativos a la Mutación
          #a la estructura principal.
          sanitized_genetic_operators_settings["mutation_parameters"] = sanitized_mutation_parameters 

          #Si no hubo falla alguna durante todo el procedimiento, se devuelve 
          #el diccionario con los valores de las tres técnicas (Selección, Cruza y Mutación)
          #saneados.
          return sanitized_genetic_operators_settings  
    

      def sanitize_moeas_settings(self,moeas_settings,features):
          """
             Verifica integridad y lleva a cabo el saneamiento de 
             los datos que ingresó el usuario concernientes a la 
             sección "MOEAs Settings" **(véase View/Main/MOEA/MOEAFrame.py)**.
  
             :param moeas_settings: El listado de técnicas y sus parámetros que el usuario
                                                eligió en la sección correspondiente.
             :param features: El conjunto de las opciones disponibles 
                              para esta sección, así como sus características.
             
             :type moeas_settings: Dictionary
             :type features: Dictionary
             :returns: Un diccionario que, dependiendo de los resultados, puede contener
                       o información del error encontrado durante el procedimiento o 
                       todos los datos debidamente verificados y transformados.
             :rtype: Dictionary
          """

          #Se obtiene la ruta del método de Sharing Function (ó Functión de Compartición,
          #véase Model/SharingFunction) que ha seleccionado el usuario.
          sharing_function_class = moeas_settings["sharing_function_class"]

          #Se adquiere el nombre del método de Sharing Function que el usuario
          #ha seleccionado.
          sharing_function_technique = moeas_settings["sharing_function_technique"]

          #Se recaban los valores de los parámetros asociados a la técnica de Sharing
          #Function que seleccionó el usuario.
          sharing_function_parameters = moeas_settings["sharing_function_parameters"]
  
          #Se almacena la información relacionada con los parámetros relacionados con la 
          #técnica de Sharing Function que el usuario ha elegido.
          sharing_function_features = features["MOEAs Settings"]["Sharing Function"]["techniques"][sharing_function_technique]["parameters"]

          #Se guarda la ruta de la técnica M.O.E.A (Multi-Objective Evolutionary Algorithm,
          #véase Model/MOEA) que el usuario ha seleccionado.
          moea_class = moeas_settings["moea_class"]

          #Devuelve el nombre del método M.O.E.A. que el usuario ha
          #elegido.
          moea_technique = moeas_settings["moea_technique"]

          #Otorga los valores de los parámetros de la función M.O.E.A.
          #propiciada por el usuario.
          moea_parameters = moeas_settings["moea_parameters"]

          #Se guarda información relativa a los parámetros asociados
          #al método M.O.E.A. que el usuario ha escogido.
          moea_features = features["MOEAs Settings"]["MOEA"]["techniques"][moea_technique]["parameters"]
 
          #En caso de haber algún error en este procedimiento, se prepara un mensaje 
          #de falla con los detalles sobre el desperfecto.
          error = {
                   "response": "ERROR",
                   "class": "Verifier", 
                   "method": "sanitize_moeas_settings"
                  }   

          #Aquí se colocará la información final.
          sanitized_moeas_settings = {}

          #Las siguientes estructuras almacenarán los parámetros
          #saneados, tanto para la técnica de Sharing Function seleccionada
          #como para la de M.O.E.A. utilizada, respectivamente.
          sanitized_sharing_function_parameters = {}
          sanitized_moea_parameters = {}

          #En esta variable se almacenará el valore alpha saneado, el cual
          #tiene participación en la técnica de Sharing Function.
          sanitized_alpha_sharing_function = -1
          
          #A continuación se obtiene una instancia de la técnica M.O.E.A.
          #seleccionada.
          sanitized_moea_instance = self.__verify_instance(moea_class)

          #Si el método anterior otorga un diccionario, significa que 
          #hubo una falla al momento de crear la instancia y entonces
          #el método debe interrumpirse, arrojando un mensaje de error.
          if type(sanitized_moea_instance) == dict:
             error["frame"] = "MOEA"
             error["message"] = "Problem while creating moea instance."
             return {
                     "recent": error, 
                     "previous": [sanitized_moea_instance]
                    } 

          #Al no haber falla en el proceso anterior se almacena la instancia en
          #la estructura final y se prosigue con el saneamiento.
          sanitized_moeas_settings["moea_instance"] = sanitized_moea_instance

          #A continuación se aplica la verificación y saneamiento
          #en los valores de los parámetros que acompañan a la 
          #técnica M.O.E.A. seleccionada.
          for parameter in moea_features:

              #Se toma el valor del parámetro actual.
              parameter_variable = parameter["variable"]

              #Se aplica el saneamiento del valor del parámetro actual.
              sanitized_parameter = self.__cast_parameter(moea_parameters[parameter],parameter)   

              #Si el resultado del método anterior es un diccionario, significa que 
              #hubo una falla en el procedimiento de saneamiento, por lo que el método
              #principal es interrumpido y se devuelve un diccionario con información
              #de la falla.
              if type(sanitized_parameter) == dict:
                 error["frame"] = "MOEA"
                 error["message"] = "Problem while sanitizing moea parameters."
                 return {
                         "recent": error, 
                         "previous": [sanitized_parameter]
                        } 

              #Al no haber problema con el saneamiento, se almacena el valor del parámetro
              #en la estructura provisional pertinente.
              sanitized_moea_parameters[parameter_variable] = sanitized_parameter

          #LLegados a este punto si no hubo ningún error con los parámetros, se almacena
          #la estructura local de parámetros saneados en la estructura principal.
          sanitized_moeas_settings["moea_parameters"] = sanitized_moea_parameters 

          #A continuación se aplica el saneamiento en el valor alpha de Sharing Function.
          try:

              #Si el valor de alpha es menor a 0, se considera un error por lo cual
              #el proceso actual es interrumpido y se devuelve el diccionario con los detalles
              #de la falla.
              sanitized_alpha_sharing_function = float(moeas_settings["alpha_sharing_function"])
              if sanitized_alpha_sharing_function < 0.0:
                 error["frame"] = "Sharing Function"
                 error["message"] = "Invalid range for Alpha Value."
                 return {
                         "recent": error, 
                         "previous": []
                        } 
           
          #Si durante el proceso anterior se llega a la sección except, significa que el valor
          #de alpha ni siquiera era un Float, por lo que se considera una falla, interrumpiendo
          #el procedimiento y entonces regresando un diccionario con la información del error.
          except:
              error["frame"] = "Sharing Function"
              error["message"] = "Invalid Alpha Value."
              return {
                      "recent": error, 
                      "previous": []
                     }    

          #Ahota se obtiene la instancia del método de Sharing Function.
          sanitized_sharing_function_instance = self.__verify_instance(sharing_function_class)

          #Si el método anterior devuelve un diccionario entonces ha ocurrido un
          #desperfecto en éste por lo cual se regresa un diccionario con la información
          #relativa a la falla.
          if type(sanitized_sharing_function_instance) == dict:
             error["frame"] = "Sharing Function"
             error["message"] = "Problem while creating sharing function instance."
             return {
                     "recent": error, 
                     "previous": [sanitized_sharing_funcion_instance]
                    }       

          #De no haber ocurrido ningún inconveniente se prosigue con el método, almacenando
          #el valor correspondiente en la estructura principal. 
          sanitized_moeas_settings["sharing_function_instance"] = sanitized_sharing_function_instance
    
          #Luego se verifican y sanean los valores de los parámetros 
          #relacionados con la técnica de Sharing Function empleada. 
          for parameter in sharing_function_features:

              #Se obtiene el valor del parámetro actual.
              parameter_variable = parameter["variable"]

              #Se aplica el método de saneamiento.
              sanitized_parameter = self.__cast_parameter(sharing_function_parameters[parameter_variable],parameter)   

              #Si el método anterior retorna un diccionario, significa que 
              #ha ocurrido un desperfecto, por lo cual la función principal se interrumpe
              #y regresa un diccionario con la información alusiva a la falla.
              if type(sanitized_parameter) ==  dict:
                 error["frame"] = "Sharing Function"
                 error["message"] = "Invalid range for parameter."
                 return {
                         "recent": error, 
                         "previous": [sanitized_parameter]
                        } 
              #Llegados a este punto signidica que el método no ha arrojado fallas, entonces
              #se almacena el valor del parámetro en la estructura local.
              sanitized_sharing_function_parameters[parameter_variable] = sanitized_parameter

          #Se almacenan el valor saneado alpha de Sharing Function en la estructura principal.
          sanitized_sharing_function_parameters["alpha_sharing_function"] = sanitized_alpha_sharing_function
          
          #Se almacena la estructura que contiene los parámetros saneados de la 
          #técnica de Sharing Function en la estructura principal. 
          sanitized_moeas_settings["sharing_function_parameters"] = sanitized_sharing_function_parameters
              
          #Al final si no ocurrió ninguna falla en el proceso total,
          #se devuelve la estructura principal.
          return sanitized_moeas_settings
