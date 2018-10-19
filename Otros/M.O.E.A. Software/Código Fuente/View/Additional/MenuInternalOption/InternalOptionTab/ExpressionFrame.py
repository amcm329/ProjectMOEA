#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


import tkFont as tkf
import Tkinter as tk
import tkMessageBox as tkm


class ExpressionFrame(tk.Frame):
      """
         | Ofrece opciones simples para mostrar y añadir expresiones
          de Python. 
         | Lo anterior ocurre ya que al momento de crear y evaluar funciones objetivo 
          hay algunas palabras reservadas que no pueden ser usadas en Python 
          directamente si no se hace un renombramiento apropiado.
         | Dicha información se encuentra en 
         | **Controller/XML/PythonExpressions.xml**

         :param parent: El elemento Padre al que pertenece el actual
                        Frame.
         :param features: Un diccionario que contiene las características necesarias
                          que serán mostradas en este Frame. 
 
         :type parent: Tkinter.Toplevel
         :type features: Dictionary
         :returns: El Frame que contiene la información señalada.
         :rtype: Tkinter.Frame
      """
      

      def __init__(self,parent,features):

          #Se crea el Frame sobre el cual descansará toda la infraestructura gráfica. 
          tk.Frame.__init__(self,parent)

          #El primer Frame se crea para contener información introductoria sobre las expresiones.
          #El segundo Frame contiene a los botones que realizarán acciones correspondientes
          #a la inserción y guardado de expresiones en el archivo Controller/XML/PythonExpressions.xml.
          #El tercer Frame contiene las expresiones previamente cargadas en el archivo
          #antes mencionado.
          self.__information_frame = tk.Frame(self)
          self.__buttons_frame = tk.Frame(self)
          self.__expressions_frame = tk.Frame(self)

          #Se obtienen las expresiones previamente colocadas en el archivo 
          #pertinente.
          self.__current_expressions = features[0]()

          #Se obtiene la función que guarda los cambios.
          self.__save_function = features[1]

          #Se obtienen los íconos para que se puedan colocar como Buttons (botones)
          self.__images = features[2]
          
          #Se obtiene el ícono para eliminar un elemento.
          self.__delete_image = self.__images["delete_mini"]

          #Esta variable permitirá almacenar las casillas para no perder control sobre éstas 
          #y saber en qué posición se encuentran.
          #En realidad por cada posición habrá una tupla (etiqueta,expresión normal,etiqueta,expresión de Python,botón eliminar).
          #Se describirá cada uno en su momento.
          self.__rows = []

          #Esta variable es creada para poder tener una referencia rápida del renglón actual
          #sobre el cual se puede hacer una inserción o eliminación de elementos.
          self.__current_row = 0

          #A continuación se crean las tipografías que serán empleadas para mostrar
          #la información pertinente.
          self.__title_font = tkf.Font(family = "Helvetica",size = 11,weight = "bold")
          self.__name_font = tkf.Font(family = "Helvetica",size = 10,weight = "bold")
          self.__value_font = tkf.Font(family = "Helvetica",size = 10)

          #A continuación se desarrollan Labels (etiquetas) que contendrán la información
          #básica del comportamiento de esta sección. 
          self.__information_1_label = tk.Label(self.__information_frame,text = "When you try to create or evaluate certain objective functions there are some reserved ")
          self.__information_2_label = tk.Label(self.__information_frame,text = "words that cannot be used in Python directly unless you rename them propertly. This ")
          self.__information_3_label = tk.Label(self.__information_frame,text = "section offers the required infrastructure in order to add as many reserved words as ")
          self.__information_4_label = tk.Label(self.__information_frame,text = "possible. If a reserved word is already stored in certain library, then the container library ")
          self.__information_5_label = tk.Label(self.__information_frame,text = "must be added within the reserved word (library.function), as an example here are listed ")
          self.__information_6_label = tk.Label(self.__information_frame,text = "some constants and functions located at the \"math\" library.")                  
          self.__information_7_label = tk.Label(self.__information_frame,text = "See the file Controller/XML/PythonExpressions.xml for a better orientation.")                  

          #A las Labels antes mencionadas se les da el formato adecuado.
          self.__information_1_label["font"] = self.__name_font         
          self.__information_2_label["font"] = self.__name_font
          self.__information_3_label["font"] = self.__name_font
          self.__information_4_label["font"] = self.__name_font
          self.__information_5_label["font"] = self.__name_font
          self.__information_6_label["font"] = self.__name_font
          self.__information_7_label["font"] = self.__name_font

          #Se colocan los Labels en cuestión en su Frame padre (__information_frame).
          self.__information_1_label.grid(row = 0,column = 0,columnspan = 4,padx = (5,1),pady = (10,1),sticky = tk.W)
          self.__information_2_label.grid(row = 1,column = 0,columnspan = 4,padx = (5,1),pady = (1,1),sticky = tk.W)
          self.__information_3_label.grid(row = 2,column = 0,columnspan = 4,padx = (5,1),pady = (1,1),sticky = tk.W)
          self.__information_4_label.grid(row = 3,column = 0,columnspan = 4,padx = (5,1),pady = (1,1),sticky = tk.W)
          self.__information_5_label.grid(row = 4,column = 0,columnspan = 4,padx = (5,1),pady = (1,1),sticky = tk.W)
          self.__information_6_label.grid(row = 5,column = 0,columnspan = 4,padx = (5,1),pady = (1,1),sticky = tk.W)
          self.__information_7_label.grid(row = 6,column = 0,columnspan = 4,padx = (5,1),pady = (1,1),sticky = tk.W)
 
          #A continuación se crean los Buttons (botones) para agregar una expresión, así como
          #guardar los cambios hechos por el usuario.
          self.__add_expression_button = tk.Button(self.__buttons_frame,text="Add Expression")
          self.__save_changes_button = tk.Button(self.__buttons_frame,text="Save Changes")

          #A dichos Buttons se les asigna el formato apropiado.
          self.__add_expression_button["font"] = self.__title_font
          self.__save_changes_button["font"] = self.__title_font

          #A cada uno de estos Buttons se le asigna una función que se activará
          #cada vez que el usuario dé click en éstos.
          self.__add_expression_button.bind("<ButtonRelease-1>",self.__add_expression)
          self.__save_changes_button.bind("<ButtonRelease-1>",self.__save_changes)
          
          #Las siguientes opciones permiten centrar los Buttons considerando el redimensionamiento
          #de la ventana independiente.
          self.__buttons_frame.grid_columnconfigure(0,weight = 1)
          self.__buttons_frame.grid_columnconfigure(1,weight = 1)
          
          #Si los datos no incluyen una llave que se llame "recent", significa que
          #se colocan en el Frame, en otro caso se omite esta operación debido
          #a un fallo en la lectura del archivo .xml que alimenta esta sección.
          if not(self.__current_expressions.has_key("recent")): 

             #Se colocan los Buttons a manera de grid (malla).
             self.__add_expression_button.grid(row = 0,column = 0,padx = (1,55),pady = (14,14),sticky = tk.E)
             self.__save_changes_button.grid(row = 0,column = 1,pady = (14,14),sticky = tk.W)
 
             #Se cargan las expresiones que se encuentren previamente 
             #en el archivo Controller/XML/PythonExpressions.xml.
             self.__load_expressions()

          #Se colocan los Frames en el Frame padre.    
          self.__information_frame.pack()
          self.__buttons_frame.pack()
          self.__expressions_frame.pack()


      def get_current_elements(self):
          """
             Regresa el número actual de casillas en el Frame.
             
             :returns: Cantidad de elementos en la estructura rows, donde se guardan las casillas **(Entry's)**.
             :rtype: Integer
          """

          #Se regresa la longitud de la estructura self.__rows.
          return len(self.__rows)   


      def __load_expressions(self):
          """
             .. note:: Este método es privado.

             | Carga las expresiones a manera de contenido gráfico
              en el Frame.
             | Dichas expresiones son tomadas del archivo 
              **Controller/XML/PythonExpressions.xml.**
          """

          #Tomando la estructura localizada en la variable self.__current_expressions
          #Se toman los elementos llave-valor y esta tupla es la que se le 
          #pasa como parámetro a la función pertinente.
          for current_expression in self.__current_expressions.keys():

              #Se obtiene el valor con base en la llave.
              current_python_expression = self.__current_expressions[current_expression]

              #Se manda llamar a la función que realiza una inserción con base
              #en una expresión.
              self.__insert_expression([current_expression,current_python_expression]) 
      

      def __add_expression(self,event):
          """
             .. note:: Este método es privado.

             Inserta una casilla que conforma una expresión
             dentro del Frame.

             :param event: Identificador del elemento gráfico que activó la función.
             :type event: String
          """

          #Se manda llamar a la función que inserta una 
          #expresión.
          self.__insert_expression()      


      def __insert_expression(self,expression = None):
          """
             .. note:: Este método es privado.

             | Coloca en el Frame una colección de elementos:
             | [etiqueta para expresión normal, expresión normal, etiqueta para expresión de Pyrhon, expresión de Python, botón para eliminar]
             | Si el parámetro expression es **None**, se añade la casilla vacía, de lo contrario se 
              agrega ésta con la información pertinente.
    
             :param expression: Un arreglo con dos elementos, el primero contiene la expresión normal
                                mientras que el segundo maneja la información de la expresión equivalente
                                en Python.
             :type expression: Array
          """  

          #Se crea la Label que hace referencia a la expresión normal.
          current_expression_label = tk.Label(self.__expressions_frame,text = "Expression: ")
          current_expression_label["font"] = self.__name_font

          #Se crea un Entry que contiene información de la 
          #expresión normal.
          current_expression_entry = tk.Entry(self.__expressions_frame,width = 9,relief = "sunken")
          current_expression_entry["font"] = self.__value_font
                
          #Se crea la Label que hace referencia a la expresión 
          #equivalente en Python.
          current_python_expression_label = tk.Label(self.__expressions_frame,text = "Python Expression: ")
          current_python_expression_label["font"] = self.__name_font

          #Se crea un Entry que contiene información relativa a la 
          #expresión equivalente en Python.
          current_python_expression_entry = tk.Entry(self.__expressions_frame,width = 9,relief = "sunken")
          current_python_expression_entry["font"] = self.__value_font
          
          #Si la expresión es no vacía se añade la información
          #pertinente a los Entrys.
          if expression != None:
             current_expression_entry.insert(tk.END,expression[0])
             current_python_expression_entry.insert(tk.END,expression[1])

          #Se inserta el Label de la expresión normal de acuerdo 
          #a la posición que le corresponda.
          current_expression_label.grid(row = self.__current_row,column = 0,padx = (1,4),pady = (1,5),sticky = tk.N + tk.S + tk.W)

          #Se inserta el Entry de la expresión normal acuerdo a la posición 
          #que le corresponda.
          current_expression_entry.grid(row = self.__current_row,column = 1,padx = (1,11),pady = (1,10),sticky = tk.N + tk.S + tk.W)

          #Se inserta el Label de la expresión de Python actual de acuerdo
          #a la posición que le corresponda.
          current_python_expression_label.grid(row = self.__current_row,column = 2,padx = (1,4),pady = (1,5),sticky = tk.N + tk.S + tk.W)

          #Se inserta el Entry de la expresión de Python de acuerdo a 
          #la posición que le corresponda.
          current_python_expression_entry.grid(row = self.__current_row,column = 3,padx = (1,9),pady = (1,5),sticky = tk.N + tk.S + tk.W)

          #Se crea el botón para eliminar la variable de decisión.
          current_delete_button = tk.Button(self.__expressions_frame, background = "white",image = self.__delete_image)
          current_delete_button["font"] = self.__value_font
              
          #Al botón le es añadido un evento, quiere decir que cada vez que
          #se presione éste, se mandará llamar a una función, en este caso
          #es la función para eliminar la variable de decisión.
          current_delete_button.bind("<ButtonRelease-1>",self.__delete_single_expression)

          #Se coloca el botón junto con los otros Labels y Entrys .
          current_delete_button.grid(row = self.__current_row,column = 4,pady = (1,5),sticky = tk.E)

          #Se lleva un control de los elementos de la colección con esta variable.
          columns = [
                     current_expression_label,
                     current_expression_entry,
                     current_python_expression_label,
                     current_python_expression_entry,
                     current_delete_button
                    ]

          #La estructura columns con los elementos ya creados se añade a la súper estructura self.__rows
          self.__rows.append(columns)

          #Se actualiza la variable que indica que en qué renglón se pueden agregar nuevos
          #elementos.
          self.__current_row += 1


      def __delete_single_expression(self,event):
          """
             .. note:: Este método es privado.

             Elimina una expresión y todos los elementos gráficos que la acompañan.
             También elimina todo rastro que se encuentre en las estructuras lógicas.
            
             :param event: Identificador del elemento gráfico que activó la función.
             :type event: String
          """

          #Aquí se guardará la referencia al renglón actual una vez que se ha eliminado
          #la casilla.
          local_current_row = 0

          #Se obtiene la posición del botón de borrar que activó la función.
          variable_information = event.widget.grid_info()
               
          #Se obtiene la posición dentro de la estructura lógica.
          variable_location = int(variable_information["row"])

          #Todos los elementos de dicha posición son eliminados mediante la opción destroy.
          for element in self.__rows[variable_location]:
              element.destroy()

          #También se eliminan las referencias, esto en la parte lógica.             
          del self.__rows[variable_location]

          #A continuación se hace un reacomodo de las posiciones en el Frame para que no se dejen
          #huecos. Como son 5 elementos con cada casilla, todos se reacomodan.
          for row in self.__rows:

              #Los elementos son colocados en forma de malla (grid).
              row[0].grid(row = local_current_row,column = 0,padx = (1,4),pady = (1,5),sticky = tk.N + tk.S + tk.W)
              row[1].grid(row = local_current_row,column = 1,padx = (1,11),pady = (1,10),sticky = tk.N + tk.S + tk.W)
              row[2].grid(row = local_current_row,column = 2,padx = (1,4),pady = (1,5),sticky = tk.N + tk.S + tk.W)
              row[3].grid(row = local_current_row,column = 3,padx = (1,9),pady = (1,5),sticky = tk.N + tk.S + tk.W)
              row[4].grid(row = local_current_row,column = 4,pady = (1,5),sticky = tk.E)
    
              #Se actualiza la referencia del renglón actual.
              local_current_row += 1  

          #La variable self.__current_row se actualiza al total de elementos que quedan.
          self.__current_row = local_current_row       
          

      def __get_information(self):
          """
             .. note:: Este método es privado.

             Toma la información del Frame **(en específico de las casillas)** 
             y regresa las expresiones con sus respectivos equivalentes en Python.
             
             :returns: Una lista que contiene arreglos de dos elementos donde el primero es
                       la expresión normal mientras que el segundo es la expresión equivalente en
                       Python.
             :rtype: List 
          """

          #Aquí se almacenarán las expresiones resultantes.
          vector_expressions = []

          #Se realiza un recorrido sobre la estructura que contiene las variables (self.__rows) 
          for row in self.__rows:

              #En cada renglón se obtienen la expresión normal y su equivalente
              #en Python.
              expression = row[1].get()
              python_expression = row[3].get()
              
              #Habiendo tomado estos elementos, se guardan los valores recabados en la
              #estructura correspondiente.
              vector_expressions.append([expression,python_expression])
              
          #Se regresa la esructura antes mencionada.
          return vector_expressions


      def __save_changes(self,event):
          """
             .. note:: Este método es privado.

             Toma la información existente en las casillas y procede a sobreescribir
             el archivo **Controller/XML/PythonExpressions.xml** con la información
             recién recabada.
            
             :param event: Identificador del elemento gráfico que activó la función.
             :type event: String
          """
 
          #Primero se muestra un mensaje de advertencia al usuario, indicando que el cambio al archivo
          #corre bajo su propio riesgo.
          result = tkm.askquestion("Save changes","If you change the file PythonExpressions.xml is at your own risk, do you wish to continue?",icon = "warning",parent = self)	

          #Si el usuario acepta entonces ocurre lo siguiene.
          if result == "yes":
             
             #Se obtiene la información de las casillas.
             final_information = self.__get_information()

             #Se manda a sobreescribir el archivo Controller/XML/PythonExpressions.xml
             #(véase Controller/XMLParser.py) y se obtiene su código de verificación.
             verifier_code = self.__save_function(final_information)

             #Las siguientes variables contienen información sobre el 
             #estado de la transacción, la primera es el título que se adhiere a una ventana de alerta,
             #mientras que la segunda contiene la información del estado de la transacción.
             results_title = "Success"
             results_message = "Changes saved succesfully."

             #Si el código de verificación es distinto de "OK", entonces
             #se cambia la información en las variables descritas anteriormente.
             if verifier_code != "OK":

                #El título ahora tendrá la palabra errror.
                results_title = "ERROR"

                #El contenido del mensaje ahora indica que ha habido un error durante la 
                #transacción.
                results_message = "At least one error occurred during the operation. Check your inputs."
             
             #A continuación se muestra la ventana de alerta con la información
             #de las variables actualizadas.
             tkm.showinfo(results_title,results_message,parent = self)
