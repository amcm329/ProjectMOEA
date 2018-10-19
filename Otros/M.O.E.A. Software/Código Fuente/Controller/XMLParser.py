#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


import os
import xml.etree.ElementTree as et


class XMLParser:
      """
         | Permite leer y escribir a archivos .xml **(los que se localizan en Controller/XML)**, 
          los cuales tienen almacenados: 
         * Los nombres de las técnicas con sus parámetros que se encuentran disponibles en la sección Model **(Features.xml)**.
         * La colección de palabras reservadas para poder emplear funciones y constantes auxiliares en las funciones objetivo **(PythonExpressions.xml)**.
         * El conjunto de M.O.P.'s **(Multi-Objective Problems, localizados en MOPExamples.xml)**.
         |
         | Dichos archivos proporcionan la información necesaria a la interfaz gráfica **(véase View/MainWindow.py)**.

         :returns: Controller.XMLParser
         :rtype: Instance
      """


      def indent(self,element,level = 0):
          """
             Indenta **(coloca espacios)** apropiadamente
             en un documento .xml para poder distinguir más
             rápidamente los distintos niveles que existen en éste.

             :param element: Una línea del archivo .xml
             :param level: El nivel en el que se está haciendo 
                           el proceso de identado.
       
             :type element: String
             :type level: Integer
          """

          #El procedimiento se hace de manera recursiva.
          #Se empieza con el nivel 0 colocando un salto de línea
          #para poder agregar los elementos pertinentes uno debajo del otro
          #en un mismo nivel.
          i = "\n" + level * "      "

          #Aquí se distinguen dos casos, o se trata de un contenido padre
          #(puede tener contenidos anidados y por ende, otros niveles) o un
          #contenido hijo (no hay más contenidos anidados).
          #Para este caso se trata de un contenido padre.
          if len(element):

             #Un contenido siempre tiene una etiqueta de inicio y otra de fin que
             #lo caracteriza; es por ello que también se aplica indentado a 
             #estos elementos. 
             #Aquí se aplica indentado a la etiqueta de inicio.             
             if not element.text or not element.text.strip():
                element.text = i  + "      "
                
             #A continuación se aplica indentado a la etiqueta de fin.
             if not element.tail or not element.tail.strip():
                element.tail = i
                
             #Se obtiene el número de elementos del contenido 
             #actual.
             length_element = len(element)

             #A continuación se hace el indentado del contenido
             #hijo que tiene el contenido actual.
             for x in range (length_element):
                 
                 #Se obtiene el elemento actual.
                 subelement = element[x]

                 #Se manda llamar a la función recursiva incrementando el nivel
                 #en una unidad.
                 self.indent(subelement,level + 1)

                 #Dentro del contenido se tiene especial cuidado en el último elemento listado
                 #ya que si se trata de éste se tiene que realizar un indentado especial pues
                 #se trata de la transición entre ese contenido y uno nuevo independientemente 
                 #del nivel, entonces mientras no se trate de ese elemento se aplica un indentado
                 #normal.
                 if not subelement.tail or not subelement.tail.strip():

                    #Si no se trata del último elemento en el contenido entonces se aplica un
                    #indentado normal.
                    if x != length_element - 1:
                       subelement.tail = i + "      "

                    #Si se trata del último elemento en el contenido entonces se aplica un
                    #indentado especial.
                    else: 
                       subelement.tail = i

          #Aquí se hace el indentado del contenido hijo.
          else:
              if level and (not element.tail or not element.tail.strip()):
                 element.tail = i


      def load_xml_features(self,features_filename):
          """
             Realiza la lectura del archivo que contenga el listado 
             de técnicas y sus parámetros disponibles **(véase Model)** 
             y carga todos los elementos que se encuentran en éste.

             :param features_filename: Nombre del archivo en cuestión.

             :type features_filename: String
             :returns: Un diccionario que contiene todos los elementos
                       del archivo.
             :rtype: Dictionary
          """

          #Aqui se almacenarán todos los elementos.
          category_features = {}

          #Se obtiene la ruta (path) completa del archivo.
          path = os.path.dirname(__file__)

          #Con base en la ruta se obtiene el documento .xml 
          #y se transforma en una estrctura de tipo árbol.
          tree = et.parse(path + "/XML/" + features_filename)

          #Se obtiene la raíz de dicho árbol.
          root = tree.getroot()

          #Si se observa el archivo .xml correspondiente, éste se encuentra
          #dividido en categorías.
          #Entonces la búsqueda se hace por cada categoría.
          for category in root:

              #Se obtiene el nombre de la categoría.
              category_name = category.get("name")

              #Cada categoría se encuentra organizada en divisiones,
              #aquí se hace dicho almacenamiento.
              division_settings = {}
    
              #Así la búsqueda continúa por divisiones.
              for division in category:

                  #Se obtienen tanto el nombre de la categoría como la ruta
                  #(path) de cada división.
                  division_name = division.get("name")
                  division_path = division.get("path")
                  
                  #Cada división es constituida por técnicas, de modo que
                  #aquí se almacenan dichos valores.
                  techniques = {}

                  #Entonces la búsqueda prosigue por cada técnica.
                  for technique in division:

                      #Se obtiene el nombre de la técnica, así como 
                      #la clase a la que pertenece (en Model) y 
                      #su clasificación (binaria o de punto flotante, aunque
                      #pueden haber más si el usuario las desarrolla).
                      technique_name = technique.get("name")        
                      technique_class = technique.get("class")
                      technique_classification = technique.get("classification")

                      #Cada técnica tiene asociada un conjunto de parámetros,
                      #aquí se almacenan dichos valores.
                      parameters = []

                      #Entonces se continúa con los parámetros.
                      for parameter in technique:

                          #Se obtiene el nombre del parámetro, su tipo (bool, integer, float point),
                          #el nombre de la variable asociada al parámetro, sus rangos
                          #inferior (valor mínimo) y superior (valor máximo) así como el valor que se
                          #espera tenga por defecto el parámetro.
                          parameter_name = parameter.get("name")
                          parameter_type = parameter.get("type")
                          parameter_variable = parameter.get("variable")
                          parameter_lower_range = parameter.get("lower_range")
                          parameter_upper_range = parameter.get("upper_range")
                          parameter_default_value = parameter.get("default")
                           
                          #Se añade a la estructura de parámetros los elementos
                          #descritos previamente.  
                          parameters.append({
                                             "name": parameter_name,
                                             "type": parameter_type,
                                             "variable": parameter_variable,
                                             "lower_range": parameter_lower_range,
                                             "upper_range": parameter_upper_range,
                                             "default": parameter_default_value 
                                            })

                      #Se añade a la estructura de técnicas la técnica actual con su
                      #clase asociada (en Model), el listado de parámetros y la 
                      #clasificación (bool, integer, float point) correspondiente.
                      techniques[technique_name] = {
                                                    "class": technique_class,
                                                    "parameters": parameters,
                                                    "classification": technique_classification
                                                   }
            
                  #Se añade a la división actual la estructura de técnicas disponibles junto con
                  #la ruta establecida.
                  try:
                      #El path de la clase Community sólo existe en una de las divisiones
                      #de tal manera que esta sección de código se construye para poder
                      #capturar este valor, si no existe entonces se realiza lo que está en la
                      #sección except.
                      community_path = division.get("community_path")
 
                      division_settings[division_name] = {
                                                          "path": division_path,
                                                          "community_path": community_path,
                                                          "techniques": techniques
                                                         }              
  
                  except:
                         #Si no se encuentra el valor para community_path entonces
                         #el proceso se realiza normalmente.
                         division_settings[division_name] = {
                                                             "path": division_path,
                                                             "techniques": techniques
                                                            }              
  
              #A la categoría actual se le añade la división correspondiente.
              category_features[category_name] = division_settings    
  
          #Finalmente se regresa la estructura con los datos pertinentes.
          return category_features


      def load_xml_mop_examples(self,features_filename):
          """
             | Lleva a cabo la lectura del archivo que contenga el listado de 
              M.O.P.'s **(Multi-Objective Problems)** y carga todos los elementos que se 
              encuentran en éste.
             |
             | Un M.O.P es una mezcla de variables de decisión y funciones objetivo ya estudiadas,
              se utilizan para reproducir su comportamiento y así garantizar, además de un correcto
              funcionamiento del programa, una opción rápida para probar las técnicas que se ofrecen.

             :param features_filename: Nombre del archivo en cuestión.

             :type features_filename: String
             :returns: Un diccionario que contiene todos los elementos
                       del archivo.
             :rtype: Dictionary
          """

          #Aquí se almacenarán todos los elementos.
          mop_examples = {}
  
          #Se obtiene la ruta (path) del archivo .xml en
          #cuestión.
          path = os.path.dirname(__file__)

          #Se obtiene el documento .xml con base en el path anterior
          #y se descarga éste en forma de estructura de árbol.
          tree = et.parse(path + "/XML/" + features_filename)

          #Se obtiene la raíz de la estructura anterior.
          root = tree.getroot()

          #El archivo se encuentra dividido en M.O.P.'s, entonces
          #se hace la búsqueda basándose en esta categoría.
          for mop in root:  

              #Se obtiene el nombre del M.O.P., el nombre casi siempre consta de los 
              #autores que lo diseñaron.
              mop_name = mop.get("name")
        
              #Cada M.O.P. consta de funciones y variables, entonces se
              #crean estructuras que almacenarán los elementos pertinentes.
              functions = []
              variables = []

              #Se hace una búsqueda sobre los elementos que contiene el
              #M.O.P.
              for element in mop:
                  
                  #Si se trata de una función se obtiene su contenido y
                  #se almacena en la estructura señalada.
                  if element.tag == "Function":
                     function_name = element.get("value")
                     functions.append(function_name)

                  #Si se trata de una variable se obtiene su contenido, así como
                  #sus rangos inferior y superior, entonces se añade en la estructura
                  #señalada.
                  elif element.tag == "Variable":
                       variable_name = element.get("value")
                       variable_lower_range = element.get("lower_range")  
                       variable_upper_range = element.get("upper_range")
                       variables.append([variable_name,variable_lower_range,variable_upper_range])

              #Al M.O.P. actual le es añadido un arreglo de dos elementos, el primero contiene las 
              #funciones mientras que el segundo las variables.
              mop_examples[mop_name] = [functions,variables]

          #Finalmente se regresa la estructura principal.
          return mop_examples


      def load_xml_python_expressions(self,features_filename):
          """
             | Realiza la lectura del archivo que contenga el listado 
              de expresiones en Python y carga todos los elementos que se 
              encuentran en éste.
             |
             | La idea detrás de esto es que, al momento de crear y/o evaluar
              funciones objetivo existen algunas palabras reservadas que no pueden 
              ser usadas directamente como son las funciones trigonométricas, por eso
              es que estas expresiones sirven como intermediarias entre el usuario y
              el intérprete de Python. 
             |
             | En ocasiones a este tipo de expresiones, no sólo en el ámbito actual
              sino en general, se les conoce como azúcar sintáctica.

             :param features_filename: Nombre del archivo en cuestión.

             :type features_filename: String
             :returns: Un diccionario que contiene todos los elementos
                       del archivo.
             :rtype: Dictionary
          """

          #Aquí se almacenarán todos los elementos.
          expressions = {}

          #Se obtiene la ruta (path) correspondiente al archivo
          #en cuestión.
          path = os.path.dirname(__file__)

          #Con base en el path anterior, se toma el documento .xml
          #y se obtiene en forma de estructura de árbol.
          tree = et.parse(path + "/XML/" + features_filename)

          #Se obtiene la raíz de dicha estructura.
          root = tree.getroot()
  
          #Cada elemento de este documento es una función,
          #entonces se itera sobre los elementos.
          for function in root:

              #La función tiene dos elementos, la expresión normal (entendida por el usuario),
              #y la expresión en Python (la que "entenderá" el intérprete de Python).
              #Se obtiene la expresión normal.
              name = function.get("name")

              #Se obtiene la expresión en Python.
              python_expression = function.get("value")

              #En la estructura se aloja la información correspondiente. 
              expressions[name] = python_expression
          
          #Al final se devuelve el diccionario.
          return expressions        


      def write_xml_python_expressions(self,features_filename,features):
          """
             | Sobreescribe el archivo donde se encuentra el listado de expresiones
              en Python.
             | El objetivo es que, una vez ejecutándose el programa y a través del menú
              pertinente **(véase View/Additional/MenuInternalOption/InternalOptionTab/PythonExpressionFrame.py)**,
              el usuario pueda añadir o eliminar las expresiones de Python que desee.
             |
             | En ocasiones a este tipo de expresiones, no sólo en el ámbito actual 
              sino en general, se les conoce como azúcar sintáctica.

             :param features_filename: Nombre del archivo en cuestión.
             :param features: La estructura que contiene las expresiones para ser guardadas
                              en el archivo .xml.

             :type features_filename: String
             :type features: List
          """
   
          #Se obtiene la ruta (path) del archivo en cuestión.
          path = os.path.dirname(__file__)

          #A continuación se toma el documento .xml y se crea una estructura
          #en forma de árbol.
          tree = et.parse(path + "/XML/" + features_filename)

          #Se obtiene la raíz de dicha estructura.
          root = tree.getroot()

          #Dado que es responsabilidad entera del usuario decidir sobre el contenido del
          #archivo, basta con obtener el contenido actual del archivo y eliminar todo,
          #ésto para garantizar que no existan duplicados o algún otro tipo de inconvenientes. 
          previous_elements = root.findall("Function")

          #Aquí se elimina del documento todo el contenido actual.
          for element in previous_elements:
              root.remove(element)

          #Se toman las expresiones que serán insertadas.
          for feature in features:

              #Se obtienen la expresión normal (la que entiende el usuario) seguida de la 
              #aexpresión en Python (la que entiende sólo el intérprete).
              name = feature[0]
              value = feature[1]	          

              #A continuación se añade un nuevo nodo al documento que está representado por una
              #estructura en forma de árbol.
              new_child = et.SubElement(root,"Function name=\"" + name + "\" value=\"" + value + "\"")

          #Se manda llamar a la función que imprime apropiadamente la estructura de un árbol,
          #ya que por defecto todos los elementos se colocan seguidos unos de otros sin espacios.
          self.indent(root)

          #Se escribe la estructura en forma de árbol en el documento .xml
          #pertinente.
          tree.write(path + "/XML/" + features_filename)
