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


class SelectionFrame(TemplateGeneticOperatorFrame):
      """
         | Esta clase proporciona la infraestructura gráfica para que el usuario pueda 
          elegir métodos y características relacionadas con la Selección de Individuos.
         | También hereda atributos de la clase TemplateGeneticOperatorFrame para facilitar
          la carga de elementos en el Frame y su correspondiente recolección de información.

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
          #El Frame de esta clase no será otro que el Frame de la clase Padre.
          TemplateGeneticOperatorFrame.__init__(self,parent,name,features)

          #La clase Padre contiene un elemento que será el título pero internamente no se coloca, esto
          #para que en la clase actual se decida dónde colocarlo, pues pueden haber elementos intermedios
          #entre el título y la sección dinámica
          self.title_label.grid(row = self.row_position,column = 0,columnspan = 2,pady = (10,1),sticky = tk.N + tk.S)
          #La clase Padre también contiene un atributo que nos indica el renglón actual para poder colocar
          #algún elemento y que no se traslape uno con otro.
          self.row_position += 1

          #Al final de manera genérica se colocan los elementos genéricos dinámicos y estáticos.
          self.grid_widgets()

   
      def restore_settings(self):
          """
             Ejecuta el método de la clase Padre, el cual restaura los valores por 
             defecto de los elementos dinámicos y estáticos del Frame.
          """

          TemplateGeneticOperatorFrame.restore_settings(self)


      def get_information(self):
          """
             Recolecta la información relativa a esta clase haciendo uso del método
             de la clase Padre.

             :returns: Diccionario con información de los métodos genéricos.
             :rtype: Dictionary
          """
        
          return TemplateGeneticOperatorFrame.get_information(self)
