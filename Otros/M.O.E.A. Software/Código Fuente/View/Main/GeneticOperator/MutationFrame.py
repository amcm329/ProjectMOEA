#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


import Tkinter as tk
from TemplateGeneticOperator.TemplateGeneticOperatorFrame import TemplateGeneticOperatorFrame 


class MutationFrame(TemplateGeneticOperatorFrame):
      """
         | Esta clase proporciona la infraestructura gráfica para que el usuario pueda 
          elegir técnicas y características relativas a la Mutación de Individuos.
         | También hereda atributos de la clase TemplateGeneticOperatorFrame para facilitar
          la carga automática de elementos en el Frame y su consecuente recolección de información.

         :param parent: Frame padre al que pertenece.
         :param name: Identificador **(único)** que tendrá el Frame.
         :param features: Conjunto de técnicas con sus respectivos parámetros para que
                          se puedan cargar automáticamente en este Frame **(véase
                          Controller/XMLParser.py)**.

         :type parent: Tkinter.Frame
         :type name: String
         :type features: Dictionary
         :returns: Tkinter.Frame
         :rtype: Instance
      """


      def __init__(self,parent,name,features):
          #El Frame donde se cargarán los elementos pertenece a la clase Padre.
          TemplateGeneticOperatorFrame.__init__(self,parent,name,features,True)

          #Se colocarán atributos exclusivos de esta clase, junto con sus valores por defecto.
          #Para este caso se tiene:
          #mutation_probability (probabilidad de mutación). Es menester mencionar que ésta maneja
          #valores entre 0 y 1.
          self.__default_mutation_probability = "0.10"

          #A continuación se crea la infraestructura gráfica para el elemento exclusivo de la clase.
          #También se le añade su valor por defecto.
          self.__mutation_probability_label = tk.Label(self,text = "Probability:")
          self.__mutation_probability_entry = tk.Entry(self,relief = "sunken")  
          self.__mutation_probability_entry.insert(tk.END,self.__default_mutation_probability)   
          self.__mutation_probability_label["font"] = self.name_font
          self.__mutation_probability_entry["font"] = self.value_font    
          
          #La clase Padre contiene un atributo título, el cual es creado pero no colocado, esto para que se puedan
          #agregar libremente tantos elementos como se desee entre éste y los elementos dinámicos.
          self.title_label.grid(row = self.row_position,column = 0,columnspan = 2,pady = (10,1),sticky = tk.N + tk.S)
          #También se maneja una variable que indica la posición en la que se va a agregar cada elemento, esto con la 
          #finalidad de que no se traslapen.
          self.row_position += 1

          #A continuación se colocan los elementos gráficos relativos a la probabilidad de mutación.    
          self.__mutation_probability_label.grid(row = self.row_position,column = 0,padx = (1,9),pady = (8,5),sticky = tk.E)
          self.__mutation_probability_entry.grid(row = self.row_position,column = 1,pady = (8,5),sticky = tk.W)           
          self.row_position += 1
          
          #Se actualiza la variable de colocación y se colocan los elementos genéricos.
          self.grid_widgets()
          
        
      def restore_settings(self):
          """
             Ejecuta el método de la clase Padre, el cual restaura los valores por 
             defecto de los elementos dinámicos y estáticos del Frame.
          """

          #Primero se limpia y se restaura el valor del elemento exclusivo
          #de la clase.
          self.__mutation_probability_entry.delete(0,tk.END)
          self.__mutation_probability_entry.insert(tk.END,self.__default_mutation_probability)   

          #Posteriormente se hace la misma operación para todos los elementos genéricos usando
          #la función Padre.
          TemplateGeneticOperatorFrame.restore_settings(self)
   
          
      def get_information(self):
          """
             Recolecta la información genérica **(usando el método de la clase Padre)**, y también
             se le añade aquélla recolectada exclusivamente en esta clase.

             :returns: | Un diccionario que contiene:
                       | **Métodos genéricos,**
                       | **Probabilidad de mutación.**
             :rtype: Dictionary
          """

          #Primero (con ayuda del método de la clase Padre) se obtiene la información genérica.
          mutation_information = TemplateGeneticOperatorFrame.get_information(self)
         
          #Posteriormente se anexa la información contenida en los parámetros de esta clase 
          #exclusivamente, en este caso, de la probabilidad de mutación.
          mutation_information["probability_mutation_general"] = self.__mutation_probability_entry.get()
          return mutation_information
