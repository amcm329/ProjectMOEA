#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


import Tkinter as tk
import tkFont as tkf
import tkMessageBox as tkm


class FunctionFrame(tk.Frame):
      """
         | Esta clase proporciona una base gráfica para que el usuario pueda
          agregar tantas functiones objetivo como desee.
         | A grandes rasgos el usuario podrá agregar casillas donde se colocarán las funciones
          objetivo, esto utilizando un botón. De igual manera, las casillas pueden ser eliminadas
          usando un ícono que estará cerca de cada una de éstas.
         | Importante es mencionar que las funciones deben estar escritas en sintaxis de Python.

         :param parent: Frame padre al que pertenece.
         :param features: Conjunto de técnicas con sus respectivos parámetros para que
                          se puedan cargar automáticamente en este Frame **(véase
                          Controller/XMLParser.py)**.

         :type parent: Tkinter.Frame
         :type features: Dictionary
         :returns: Tkinter.Frame
         :rtype: Instance
      """


      def __init__(self,parent,features):
          #Primero se crea el contenedor (Frame) sobre el cual se 
          #agregará toda la infraestructura gráfica
          tk.Frame.__init__(self,parent,relief = "groove")               

          #Se declaran tipografías que servirán para identificar a los elementos en 
          #el Frame.
          self.__title_font = tkf.Font(family = "Helvetica",size = 11,weight = "bold")
          self.__value_font = tkf.Font(family = "Helvetica",size = 10)
       
          #Esta Frame usará íconos, en específico para poder identificar la función
          #de eliminación de cada casilla, entonces se cargan automáticamente todas
          #las imágenes disponibles y aquí se decide cuál usar (véase View/Image y View/MainWindow.py)
          self.__images = features["images"]

          #Se obtiene el ícono para borrar una casilla y se asigna a una variable.
          self.__delete_image = self.__images["delete"]
          
          #Esta variable permitirá almacenar las casillas para no perder control sobre éstas 
          #y saber en qué posición se encuentran.
          #En realidad por cada posición habrá una tupla (casilla,opciones de maximizar y minimizar,botón eliminar).
          #Se describirá cada uno en su momento.
          self.__rows = [] 

          #Se mantiene un control de las posiciones en las que se van a agregar o borrar tuplas.
          self.__current_row = 0

          #Las opciones de maximizar y minimizar sirven para indicarle al programa si lo que
          #se desea es encontrar el máximo o el mínimo de una función. Esta variable permite almacenar las 
          #referencias a estas opciones por cada variable.
          self.__rows_checkbuttons_variables = []
          
          #Se crea la infraestructura básica para los elementos estáticos.
          #El botón para agregar funciones (casillas donde se insertarán las funciones).
          #Una etiqueta de advertencia donde se indique que todas las funciones deben estar escritas
          #en la sintaxis de Python.
          #Etiquetas Function, Maximize y Minimize para identificar estas secciones en la pantalla.
          self.__advisory_label = tk.Label(self,text = "Important: All functions must be written in Python syntax.")
          self.__add_function_button = tk.Button(self,text = "Add Function")
          self.__function_name_label = tk.Label(self,text = "Function")
          self.__minimize_label = tk.Label(self,text = "Minimize")
          self.__maximize_label = tk.Label(self,text = "Maximize")

          #Se le añade el formato apropiado a los elementos creados anteriormente.
          self.__advisory_label["font"] = self.__title_font
          self.__add_function_button["font"] = self.__title_font
          self.__function_name_label["font"] = self.__title_font 
          self.__minimize_label["font"] = self.__title_font
          self.__maximize_label["font"] = self.__title_font

          #Al botón para agregar funciones se le añade el evento para agregar una función.
          self.__add_function_button.bind("<ButtonRelease-1>",self.__add_function)

          #Se colocan los elementos en el Frame.
          self.__grid_widgets()

          #El Frame siempre estará inicializado con una función disponible.                 
          self.insert_function()
          

      def get_current_elements(self):
          """
             Regresa el número actual de casillas en el Frame.
             
             :returns: Cantidad de elementos en la estructura rows, donde se guardan las casillas (Entries).
             :rtype: Integer  
          """

          #Se regresa la longitud de la estructura self.__rows.
          return len(self.__rows)   


      def __grid_widgets(self): 
          """
             .. note:: Este método es privado.

             Coloca elementos en el Frame.
          """  
          
          #En términos generales, todos los elementos del Frame se colocan en modo grid, esto significa
          #que se le tiene que indicar el renglón y la columna en la que serán puestos.
          #Existen otros parámetros para ajustar mejor la colocación, columnspan permite que el elemento 
          #se traslape tantas columnas como sea necesario, pad da una separación entre el actual y el siguiente
          #elemento gráfico (padx -> horizontal, pady -> vertical); sticky permite alinear los elementos a una orientación
          #determinada.
          #Entonces se empieza por la etiqueta de advertencia. 
          self.__advisory_label.grid(row = self.__current_row,column = 0,columnspan = 4,pady = (1,15),sticky = tk.N + tk.S)
          self.__current_row += 1          

          #A continuación se agrega el botón para agregar funciones.
          self.__add_function_button.grid(row = self.__current_row,column = 0,columnspan = 4,pady = (1,15),sticky =  tk.N + tk.S)
          self.__current_row += 1          

          #Entonces se agregan las funciones para colocar las etiquetas correspondientes a las secciones de Function,
          #Maximize y Minimize.
          self.__function_name_label.grid(row = self.__current_row,column = 0,padx = (1,25),pady = (1,7))
          self.__minimize_label.grid(row = self.__current_row,column = 1,pady = (1,6))
          self.__maximize_label.grid(row = self.__current_row,column = 2,pady = (1,6))
          self.__current_row += 1
          

      def insert_function(self,function = None):  
          """
             | Coloca en el Frame una colección de elementos:
             | [casilla para insertar funcion, opción de maximizar, opción de minimizar, botón para eliminar]
             | Si el parámetro function es **None**, se agrega la casilla vacía, de lo contrario se 
              añade ésta con la función.
    
             :param function: Una función para ser insertada en el primer elemento de la colección.
             :type function: String
          """  

          #Se lleva un control de los elementos de la colección con esta variable.
          columns = []

          #Se crea el Entry (casilla) donde se insertaría la función.
          current_function_entry = tk.Entry(self,relief = "sunken")
          current_function_entry["font"] = self.__value_font
       
          #Si el parámetro function no es None, se inserta éste en el Entry anterior.
          if function != None: 
             current_function_entry.insert(tk.END,function)

          #Se coloca ésta casilla en el grid y se guarda su referencia en la estructura columns
          current_function_entry.grid(row = self.__current_row,column = 0,pady = (1,5),sticky = tk.N + tk.S + tk.W)
          columns.append(current_function_entry)
         
          #Las opciones de Maximize y Minimize se rigen bajo Checkbuttons, cuos valores
          #deben almacenarse en una variable, entonces esta es la variable.
          current_checkbutton_variable = tk.IntVar()

          #Se crea el Checkbutton para Maximize, se coloca en el Frame y se guarda su referencia en la estructura columns.
          current_minimize_checkbutton = tk.Checkbutton(self,variable = current_checkbutton_variable,onvalue = 0,offvalue = 1)
          current_minimize_checkbutton["font"] = self.__value_font
          current_minimize_checkbutton.grid(row = self.__current_row,column = 1,pady = (1,5),sticky = tk.N + tk.S)
          
          #Se crea el Checkbutton para Minimize, se coloca en el Frame y se guarda su referencia en la estructura columns.
          current_maximize_checkbutton = tk.Checkbutton(self,variable = current_checkbutton_variable,onvalue = 1,offvalue = 0)
          current_maximize_checkbutton["font"] = self.__value_font
          current_maximize_checkbutton.grid(row = self.__current_row,column = 2,pady = (1,5),sticky = tk.N + tk.S)
          
          #La opción se Minimize siempre se activa por defecto.
          current_minimize_checkbutton.select()          

          #Se añaden ambos Checkbuttons en la estructura columns.
          columns.append(current_minimize_checkbutton)
          columns.append(current_maximize_checkbutton)
                 
          #A continuación se crea el botón para eliminar una función. Se carga el ícono que se encuentra en
          #View/Image.
          current_function_button = tk.Button(self,background = "white",image = self.__delete_image)
          current_function_button["font"] = self.__value_font

          #A continuación al botón se le adhiere el evento para borrar la función.
          current_function_button.bind("<ButtonRelease-1>",self.__delete_single_function)

          #Se agraga el botón al Frame y se guarda su referencia en la estructura columns.
          current_function_button.grid(row = self.__current_row,column = 3,pady = (1,5),sticky = tk.E)
          columns.append(current_function_button)

          #A la estructura actual se le añade la variable que almacena las decisiones para los Checkbuttons.
          self.__rows_checkbuttons_variables.append(current_checkbutton_variable)

          #A la variable actual se le agrega el resultado de la estructura columns.
          self.__rows.append(columns)

          #Se actualiza el contador del renglón (row) actual.
          self.__current_row += 1

      
      def __add_function(self,event):
          """
             .. note:: Este método es privado.

             Agrega una casilla al Frame. Esta función se usa si 
             fue ejecutada por un evento.
            
             :param event: Identificador del elemento gráfico que activó la función.
             :type event: String
          """
           
          #Se manda llamar a la función de inserción. 
          self.insert_function()
 
             
      def __delete_single_function(self,event):
          """
             .. note:: Este método es privado.

             Elimina una casilla y todos los elementos gráficos que la acompañan.
             También elimina todo rastro que se encuentre en las estructuras lógicas.
            
             :param event: Identificador del elemento gráfico que activó la función.
             :type event: String
          """

          #Si hay más de una casilla en el Frame se hace la operación de eliminación.
          if len(self.__rows) > 1:
             #La lista de rows (la que tiene las referencias a los elementos gráficos)
             #empieza en 0, entonces hay que hacer un corrimiento de "local_current__row" elementos
             #para poder seleccionar la posición de la casilla que será eliminada.
             #Esto es con respecto de self.__widgets_frame ya que es ahí donde se va a poner la 
             #información pertinente.
             local_current_row = 3
             
             #Se obtiene la posición del botón de borrar que activó la función.
             function_information = event.widget.grid_info()

             #Se obtiene la posición dentro de la estructura lógica.
             function_location = int(function_information["row"]) - local_current_row

             #Todos los elementos de dicha posición son eliminados mediante la opción destroy.
             for element in self.__rows[function_location]:
                 element.destroy()
             
             #También se eliminan las referencias, tanto de la parte de la casilla como de la
             #variable que mantenía los valores para Maximize o Minimize.
             del self.__rows[function_location]
             del self.__rows_checkbuttons_variables[function_location]

             #A continuación se hace un reacomodo de las posiciones en el Frame para que no se dejen
             #huecos. Como son 4 elementos con cada casilla, todos se reacomodan.
             for row in self.__rows:
                 row[0].grid(row = local_current_row,column = 0,pady = (1,5),sticky = tk.N + tk.S + tk.W)
                 row[1].grid(row = local_current_row,column = 1,pady = (1,5),sticky = tk.N + tk.S)
                 row[2].grid(row = local_current_row,column = 2,pady = (1,5),sticky = tk.N + tk.S)
                 row[3].grid(row = local_current_row,column = 3,pady = (1,5),sticky = tk.N + tk.S + tk.E)                
                 local_current_row += 1   

             #La variable self.__current_row se actualiza al total de elementos que quedan.
             self.__current_row = local_current_row
           
          #En caso de que un sólo elemento en el Frame, se activa un mensaje de advertencia
          #y no se ejecuta la operación.  
          else:
               tkm.showwarning("Warning", "At least one objective function must be available.")


      def restore_settings(self):
          """
             Restaura el contenido del Frame a sus valores por defecto.
             Esto significa que borrará cualquier contenido que se encuentre en existencia y 
             dejará una casilla vacía.
          """

          #Primero se eliminan todos los elementos gráficos (a partir de las etiquetas).
          for row in self.__rows:
              for element in row:
                  element.destroy()

          #Posteriormente todas las estructuras que contienen las referencias lógicas se limpian.
          self.__rows = []
          self.__rows_checkbuttons_variables = []

          #Se actualiza el contador de los renglones (rows) a su valor por defecto.
          self.__current_row = 3


      def insert_mop_example(self,functions):
          """
             | Inserta un M.O.P (Multi Objective Problem) que no es más que un conjunto de 
              funciones para que se pueda hacer más rápidamente una prueba.
             | Previo a ésto se limpia el Frame para insertar únicamente el M.O.P.
             | **(véase Controller/XML/MOPExample.xml)**
             | **(véase View/Additional/MenuInternalOption/InternalOptionFrame.py)**.
             
             :param functions: Conjunto de funciones para insertar en el Frame.
             :type functions: List
          """
          #Primero se limpia cualquier rastro de elementos anteriores existentes.
          self.restore_settings()

          #Después se añade una casilla por cada función (con ésta previamente insertada).
          for function in functions:
              self.insert_function(function)


      def get_information(self):
          """
             Toma la información del Frame y regresa las funciones objectivo que 
             el usuario insertó.

             :returns: Un diccionario que contiene una lista con las funciones escritas.
             :rtype: Dictionary 
          """

          #Aquí se almacenarán las funciones resultantes.
          vector_functions = []

          #Se realiza un recorrido sobre la estructura que contiene las funciones (self.__rows) 
          for x in range(len(self.__rows)):
              current_row = self.__rows[x]
              #Se toma el primer elemento de cada uno, que es un Entry, por lo que se extrae
              #la información.
              current_function = current_row[0].get()

              #A su vez se extrae la selección de Minimize o Maximize de la lista pertinente.
              maximize_function = self.__rows_checkbuttons_variables[x].get()
       
              #Si el valor es Maximize, dado que el programa está hecho para minimizar,
              #se multiplica por un -1 toda la función ya que maximizar una función es 
              #equivalente a minimizar el mínimo.
              if maximize_function == 1:
                 current_function = "-1*(" + current_function + ")"
               
              #Se añade la función a la estructura vector_functions. 
              vector_functions.append(current_function)              

          return {
                  "vector_functions": vector_functions
                 }
