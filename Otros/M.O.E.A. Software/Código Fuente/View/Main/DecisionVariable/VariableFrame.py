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


class VariableFrame(tk.Frame):
      """
         | Proporciona bases gráficas para que el usuario pueda insertar
          variables de decisión, así como información relativa a éstas.
         | En términos generales, el usuario insertará casillas para ingresar variables
          de decisión, indicando también el valor mínimo y máximo que podrán tener.
         | Es importante comentar que todas las variables de decisión deben contener
          rangos finitos, es decir, no se contemplan valores infinitos, aunque algunos
          M.O.P.'s **(Multi Objective Problems ó Problemas Multi Objetivo)** manejan este tipo de rangos.         

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
          #Se crea un contenedor (Frame) sobre el cual descansará toda la 
          #infraestructura gráfica.
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
          #En realidad por cada posición habrá una tupla (casilla,rango mínimo,rango máximo,botón eliminar).
          #Se describirá cada uno en su momento.
          self.__rows = []

          #Se mantiene un control de las posiciones en las que se van a agregar o borrar tuplas.
          self.__current_row = 0
             
          #Se añaden elementos estáticos:
          #Un botón para añadir variables de decisión.
          #Una etiqueta para identificar la sección del nombre de la variable.
          #Una etiqueta para indicar la sección del rango inferior.
          #Una etiqueta para mostrar la sección del rango superior.
          self.__add_variable_button = tk.Button(self,text="Add Variable")
          self.__variable_name_label = tk.Label(self,text="Variable Name")
          self.__lower_range_label = tk.Label(self,text="Lower Range") 
          self.__upper_range_label = tk.Label(self,text="Upper Range")

          #Al botón para agregar las variables de decisión se le añade un evento
          #que es la acción de agregar una nueva casilla.
          self.__add_variable_button.bind("<ButtonRelease-1>",self.__add_variable)

          #Se le añade el formato apropiado a los elementos creados anteriormente.
          self.__add_variable_button["font"] = self.__title_font
          self.__variable_name_label["font"] = self.__title_font 
          self.__lower_range_label["font"] = self.__title_font
          self.__upper_range_label["font"] = self.__title_font

          #Se colocan los elementos estáticos en el Frame.
          self.__grid_widgets()

          #Inicialmente habrá una casilla disponible en el Frame.
          self.insert_variable()
          

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
          #Entonces se coloca el botón para agregar una variable de decisión.
          self.__add_variable_button.grid(row = self.__current_row,column = 0,columnspan = 4,pady = (15,15),sticky =  tk.N + tk.S)

          #Se incrementa en una unidad la variable self.__current_row para poder tener un apuntador actualizado del orden
          #en que se agregan las variables
          self.__current_row += 1
           
          #Se agregan las etiquetas que corresponderán a las secciones del nombre de la variable,
          #rango mínimo y rango máximo.  
          self.__variable_name_label.grid(row = self.__current_row,column = 0,pady = (1,10))
          self.__lower_range_label.grid(row = self.__current_row,column = 1,pady = (1,10))
          self.__upper_range_label.grid(row = self.__current_row,column = 2,pady = (1,10))

          #Se actualiza la variable self.__current_row.
          self.__current_row += 1

          
      def insert_variable(self,variable = None):  
          """
             | Coloca en el Frame una colección de elementos:
             | [casilla para insertar variable ,casilla de rango minimo, casilla de rango máximo, botón para eliminar]
             | Si el parámetro function es **None**, se añade la casilla vacía, de lo contrario se 
              agrega ésta con la variable y sus rangos.
    
             :param function: Una terna (nombre de la variable, rango máximo, rango mínimo)
              para ser insertada en las casillas correspondientes.
             :type function: String
          """  

          #Se lleva un control de los elementos de la colección con esta variable.
          columns = []

          #Se agregan las tres casillas correspondientes al nombre de la variable,
          #rango mínimo y rango máximo.
          for j in range(3):
              #Se crea una casilla.
              current_entry = tk.Entry(self,relief = "sunken")
              current_entry["font"] = self.__value_font
                
              #Si variable no es None, entonces se le añade el contenido 
              #a la casilla correspondiente.
              if variable != None:
                 current_entry.insert(tk.END,variable[j])

              #Se inserta el Entry actual de acuerdo a la posición que le corresponda.
              current_entry.grid(row = self.__current_row,column = j,padx = (1,10),pady = (1,5),sticky = tk.N + tk.S + tk.W)

              #Cada elemento se agrega a la estructura columns.
              columns.append(current_entry)
         
          #Se crea el botón para eliminar la variable de decisión.
          current_delete_button = tk.Button(self, background = "white",image = self.__delete_image)
          current_delete_button["font"] = self.__value_font
              
          #Al botón le es añadido un evento, quiere decir que cada vez que se presione éste, se
          #mandará llamar a una función, en este caso es la función para eliminar la variable de decisión.
          current_delete_button.bind("<ButtonRelease-1>",self.__delete_single_variable)

          #Se coloca el botón junto con los otros Entry's.
          current_delete_button.grid(row = self.__current_row,column = 3,pady = (1,5),sticky = tk.E)

          #Se añade el botón a la estructura columns.
          columns.append(current_delete_button)       

          #La estructura columns con los elementos ya creados se añade a la súper estructura self.__rows
          self.__rows.append(columns)

          #Se actualiza la variable que indica que en qué renglón se pueden agregar nuevos
          #elementos.
          self.__current_row += 1

         
      def __add_variable(self,event):
          """
             .. note:: Este método es privado.

             Agrega una casilla al Frame. Esta función se usa si 
             fue ejecutada por un evento.
            
             :param event: Identificador del elemento gráfico que activó la función.
             :type event: String
          """
           
          #Se manda llamar a la función de inserción. 
          self.insert_variable()


      def __delete_single_variable(self,event):
          """
             .. note:: Este método es privado.

             Elimina una casilla y todos los elementos gráficos que la acompañan.
             También elimina todo rastro que se encuentre en las estructuras lógicas.
            
             :param event: Identificador del elemento gráfico que activó la función.
             :type event: String
          """

          #Si hay más de una casilla en el Frame, se activa la sección de eliminación.
          if len(self.__rows) > 1:
             #La lista de rows (la que tiene las referencias a los elementos gráficos)
             #empieza en 0, entonces hay que hacer un corrimiento de "local_current__row" elementos
             #para poder seleccionar la posición de la casilla que será eliminada.
             #Esto es con respecto de self.__widgets_frame ya que es ahí donde se va a poner la 
             #información pertinente.
             local_current_row = 2

             #Se obtiene la posición del botón de borrar que activó la función.
             variable_information = event.widget.grid_info()
               
             #Se obtiene la posición dentro de la estructura lógica.
             variable_location = int(variable_information["row"]) - local_current_row

             #Todos los elementos de dicha posición son eliminados mediante la opción destroy.
             for element in self.__rows[variable_location]:
                 element.destroy()

             #También se eliminan las referencias, esto en la parte lógica.             
             del self.__rows[variable_location]

             #A continuación se hace un reacomodo de las posiciones en el Frame para que no se dejen
             #huecos. Como son 4 elementos con cada casilla, todos se reacomodan.
             for row in self.__rows:
                 row[0].grid(row = local_current_row,column = 0,padx = (1,10),pady = (1,5),sticky = tk.N + tk.S + tk.W)
                 row[1].grid(row = local_current_row,column = 1,padx = (1,10),pady = (1,5),sticky = tk.N + tk.S + tk.W)
                 row[2].grid(row = local_current_row,column = 2,padx = (1,10),pady = (1,5),sticky = tk.N + tk.S + tk.W)
                 row[3].grid(row = local_current_row,column = 3,pady = (1,5),sticky = tk.E)                
                 local_current_row += 1  

             #La variable self.__current_row se actualiza al total de elementos que quedan.
             self.__current_row = local_current_row       
          
          #Si hay sólo una casilla en el Frame, se activa un mensaje de advertencia, ya que
          #tiene que haber al menos una casilla disponible.
          else:
               tkm.showwarning("Warning", "At least one decision variable must be available.")


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

          #Se actualiza el contador de los renglones (rows) a su valor por defecto. 
          self.__current_row = 2


      def insert_mop_example(self,variables):
          """
             | Inserta un M.O.P (Multi Objective Problem) que no es más que un conjunto de 
              variables con sus rangos para que se pueda hacer más rápidamente una prueba.
             | Previo a ésto se limpia el Frame para insertar únicamente el M.O.P.
             | **(véase Controller/XML/MOPExample.xml)**
             | **(véase View/Additional/MenuInternalOption/InternalOptionFrame.py)**.
             
             :param functions: Conjunto de variables para insertar en el Frame.
             :type functions: List
          """

          #Primero se limpia el contenido actual en el Frame.
          self.restore_settings()

          #Después se añade una casilla por cada variable (con ésta previamente insertada).
          for variable in variables:
              self.insert_variable(variable)


      def get_information(self):
          """
             Toma la información del Frame y regresa las variables con sus rangos que 
             el usuario ingresó.

             :returns: Un diccionario que contiene una lista con las variables (y rangos) escritas.
             :rtype: Dictionary 
          """

          #Aquí se almacenarán las variables resultantes.
          vector_variables = []

          #Se realiza un recorrido sobre la estructura que contiene las variables (self.__rows) 
          for row in self.__rows:
              #En cada renglón se obtienen los primeros tres elementos que contendrán
              #el nombre de la variable, su rango mínimo y su rango máximo.
              variable = row[0].get()
              lower_range = row[1].get()
              upper_range = row[2].get()

              #Habiendo tomado estos elementos, se guardan los valores recabados en la
              #estructura correspondiente.
              vector_variables.append([variable,[lower_range,upper_range]])
              
          return {
                  "vector_variables": vector_variables
                 }
