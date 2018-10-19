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


class CrossoverFrame(TemplateGeneticOperatorFrame):
      """
         | Esta clase proporciona la infraestructura gráfica para que el usuario pueda 
          elegir técnicas y características concernientes a la Cruza entre Individuos.
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
          #El Frame estará conformado por aquél de la clase Padre.
          TemplateGeneticOperatorFrame.__init__(self,parent,name,features)
          
          #El parámetro exclusivo de esta clase será: 
          #default_crossover_probability (probabilidad de cruza), es importante
          #destacar que ésta maneja valores entre 0 y 1.
          self.__default_crossover_probability = "0.60"
          
          #Para el parámetro descrito anteriormente se crea la infraestructura 
          #gráfica, en este caso constará de un Label y un Entry.
          self.__crossover_probability_label = tk.Label(self,text = "Probability:")   
          self.__crossover_probability_entry = tk.Entry(self,relief = "sunken")         
          self.__crossover_probability_entry.insert(tk.END,self.__default_crossover_probability)   
          self.__crossover_probability_label["font"] = self.name_font
          self.__crossover_probability_entry["font"] = self.value_font    
   
          #La clase Padre consta de un elemento gráfico que es el título, el cual se declara pero no se coloca, esto
          #es para que entre éste y los elementos dinámicos se pueda colocar lo que sea necesario. En este caso
          #se agrega el elemento crossover_probability.
          self.title_label.grid(row = self.row_position,column = 0,columnspan = 2,pady = (10,1),sticky = tk.N + tk.S)
 
          #Con este valor (que reside en la clase Padre) se tiene un control sobre en qué renglón colocar los elementos
          #para que no se sature un (renglón) con dos elementos distintos.
          self.row_position += 1
          
          #Ahora se coloca la infraestructura del elemento exclusivo de la clase. De hecho se colocan ambos Label y Entry.
          self.__crossover_probability_label.grid(row = self.row_position,column = 0,padx = (1,9),pady = (8,5),sticky = tk.E)
          self.__crossover_probability_entry.grid(row = self.row_position,column = 1,pady = (8,5),sticky = tk.W)
          self.row_position += 1

          #Finalmente se colocan los elementos genéricos.
          self.grid_widgets()
     
     
      def restore_settings(self):
          """
             Ejecuta el método de la clase Padre, el cual restaura los valores por 
             defecto de los elementos dinámicos y estáticos del Frame.
          """

          #Primero se limpia y se restaura el valor del elemento exclusivo
          #de la clase.
          self.__crossover_probability_entry.delete(0,tk.END)
          self.__crossover_probability_entry.insert(tk.END,self.__default_crossover_probability)   

          #Posteriormente se hace la misma operación para todos los elementos genéricos usando
          #la función Padre.
          TemplateGeneticOperatorFrame.restore_settings(self)

          
      def get_information(self):
          """
             Recolecta la información genérica **(usando el método de la clase Padre)**, y también
             se le añade aquélla recolectada exclusivamente en esta clase.

             :returns: | Un diccionario que contiene:
                       | **Métodos genéricos,**
                       | **Probabilidad de cruza.**
             :rtype: Dictionary
          """

          #Primero se obtiene la información genérica con ayuda del método de la clase Padre.
          crossover_information = TemplateGeneticOperatorFrame.get_information(self)

          #Luego a esa estructura se le añade la información de la clase actual, en este caso 
          #la probabilidad de cruza.
          crossover_information["probability_crossover_general"] = self.__crossover_probability_entry.get()
          return crossover_information
