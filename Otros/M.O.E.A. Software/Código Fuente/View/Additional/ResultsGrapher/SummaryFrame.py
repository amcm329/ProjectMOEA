#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


import Tkinter as tk
from ContentFrame import ContentFrame


class SummaryFrame(tk.Frame):
      """
         | Unifica dos elementos: Canvas y ContentFrame. La razón de esto es que, en promedio la
          información mostrada por ContentFrame rebasará el tamaño de la ventana de la información 
          final **(véase View/Additional/ResultsGrapher/ResultsGrapherTopLevel.py)**, es entonces 
          que se deben agregar barras de desplazamiento para poder acceder al contenido que quedaría oculto.
         | Uno de los elementos en Tkinter más sencillos que cumplen con este cometido es un
          Canvas. Luego entonces esa es la razón de tal fusión.

         :param parent: Frame padre al que pertenece.
         :param renamed_objective_functions: Diccionario de funciones objetivo renombradas 
                **(véase View/Additional/ResultsGrapher/ResultsGrapherToplevel.py)**.
         :param renamed_decision_variables: Diccionario de variables de decisión renombradas  
                **(véase View/Additional/ResultsGrapher/ResultsGrapherToplevel.py)**.
         :param main_features: Diccionario que contiene, entre otras cosas, los nombres de los
                parámetros asociados a cada técnica.
         :param gathered_information: Diccionario que contiene todas las configuraciones 
                recabadas ingresadas por el usuario **(véase View/Main/MainWindow.py)**.

         :type parent: Tkinter.Frame
         :type renamed_objective_functions: Dictionary
         :type renamed_decision_variables: Dictionary
         :type main_features: Dictionary
         :type gathered_information: Dictionary
         :returns: Tkinter.Frame
         :rtype: Instance
      """


      def __init__(self,parent,renamed_objective_functions,renamed_decision_variables,main_features,gathered_information):
          #Se crea el Frame Padre sobre el cual se colocará el Canvas que a su vez contendrá al ContentFrame..
          tk.Frame.__init__(self,parent,bd = 4,relief = "groove")
          
          #A continuación se crea el Canvas, así como sus dos barras de desplazamiento (horizontal y vertical).
          #Adicionalmente se añaden parámetros a loas barras de desplazamiento para que sean reconocidas de acuerdo
          #a su orientación (horizontal o vertical).
          self.__canvas = tk.Canvas(self)
          self.__vertical_scrollbar = tk.Scrollbar(self,orient = tk.VERTICAL,command = self.__canvas.yview)
          self.__horizontal_scrollbar = tk.Scrollbar(self,orient = tk.HORIZONTAL,command = self.__canvas.xview)

          #Las siguientes opciones son añadidas al Canvas para que reconozca que ahora tendrá dos barras de desplazamiento.
          self.__canvas.configure(yscrollcommand = self.__vertical_scrollbar.set)
          self.__canvas.configure(xscrollcommand = self.__horizontal_scrollbar.set)

          #Se crea el Frame que maneja el contenido del Task (véase View/Additional/ResultsGrapher/ResultsGrapherToplevel.py).
          self.__content_frame = ContentFrame(self.__canvas,renamed_objective_functions,renamed_decision_variables,main_features,gathered_information) 

          #A dicho Frame le es anexada la función que permitirá actualizar las barras de desplazamiento de acuerdo a sl 
          #contenido de éste. Posteriormente se coloca en el Padre (que será el Canvas).  
          self.__content_frame.bind("<Configure>",self.__update_scrollbar)
          self.__content_frame.pack(side = tk.TOP,fill = tk.X,expand = True)

          #Esta instrucción le indica al Canvas que creé una ventana en donde se almacenará el ContentFrame.
          self.__canvas.create_window((0,0),window = self.__content_frame,anchor = tk.NW)
         
          #A continuación se coloca el Canvas en el Frame Padre.   
          self.__canvas.grid(row = 0,column = 0,columnspan = 2,rowspan = 2,sticky = tk.N + tk.S + tk.W + tk.E)

          #Ahora se colocan las barras de desplazamiento en el Frame Padre.
          self.__vertical_scrollbar.grid(row = 0,column = 2,sticky = tk.N + tk.S)
          self.__horizontal_scrollbar.grid(row = 2,column = 0,sticky = tk.E + tk.W)

          #Estas dos opciones sirven para poder colocar apropiadamente el Canvas y las barras de desplazamiento
          #Básicamente indican que el tamaño de cierta columna o renglón se traslapa con la siguiente en "weight"
          #unidades.
          self.grid_rowconfigure(0,weight = 1)
          self.grid_columnconfigure(0,weight = 1)
            

      def __update_scrollbar(self,event):
          """
             .. note:: Este método es privado.  

             Actualiza la barra de desplazamiento de acuerdo al número de elementos
             existentes en el Frame, esto para poder hacer un recorrido apropiado de 
             la barra.

             :param event: Elemento que ejecutó esta función.
             :type event: String
          """

          #Ajusta la barra de desplazamiento de acuerdo al número de elementos (la cantidad de valores en el ContentFrame en este caso)
          #que se encuentran presentes.
          self.__canvas.configure(scrollregion = self.__canvas.bbox("all"))
