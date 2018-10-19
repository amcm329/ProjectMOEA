#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


import Tkinter as tk
from TemplatePopulation.TemplatePopulationFrame import TemplatePopulationFrame 


class FitnessFrame(TemplatePopulationFrame):
      """ 
         | Esta clase proporciona la infraestructura gráfica para que el usuario pueda 
          elegir métodos concernientes a la asignación del Fitness para la Población.
         | Además hereda atributos de la clase TemplatePopulationFrame para facilitar
          la colocacion y extracción de información pertinente para el usuario.

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
          #Se inicializa la clase Padre que a su vez es un Frame en el que se basará esta
          #clase.
          TemplatePopulationFrame.__init__(self,parent,name,features)
   
          #Si se verifica la clase padre el atributo del título no se coloca en ningún lado, esto es porque se 
          #deja al usuario que lo coloque donde sea para que se puedan agregar más elementos entre éste y los parámetros
          #dinámicos.
          self.title_label.grid(row = self.row_position,column = 0,columnspan = 2,pady = (17,1),sticky = tk.N + tk.S)   

          #La clase Padre tiene un atributo row_position el cual funge como puntero para poder colocar elementos en grid
          #y que no se traslapen; aquí se le indica entonces que antes de colocar los elementos dinámicos ya hay un elemento
          #colocado previamente (el título).
          self.row_position += 1
          self.grid_widgets()


      def restore_settings(self):
          """
             Llamar al método de la clase Padre, el cual restaura los valores por 
             defecto de los elementos dinámicos y estáticos del Frame.
          """
          TemplatePopulationFrame.restore_settings(self)


      def get_information(self):
          """
             Llama al método de la clase Padre, el cual recopila toda la información
             elegida por el usuario y la regresa en forma de diccionario.

             :returns: Diccionario con información de los métodos genéricos.
             :rtype: Dictionary
          """
          return TemplatePopulationFrame.get_information(self)
