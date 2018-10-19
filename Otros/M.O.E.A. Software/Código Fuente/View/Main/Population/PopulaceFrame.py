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


class PopulaceFrame(TemplatePopulationFrame):
      """ 
         | Esta clase proporciona la infraestructura gráfica para que el usuario pueda 
          elegir métodos y características concernientes a la conformación de la Población.
         | También hereda atributos de la clase TemplatePopulationFrame con el fin de 
          establecer una forma más rápida y ordenada de colocar componentes y recolectar
          la información de éstos.

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
          #Se crea un Frame que contendrá todos los elementos, para esto se llama al Frame
          #de la clase Padre.
          TemplatePopulationFrame.__init__(self,parent,name,features)
        
          #Los elementos a añadir por parte de esta clase serán:
          #number_of_generations (número de generaciones).
          #population_size (tamaño de la población).
          #number_of_decimals (número de decimales).
          #Las siguientes variables se crean para añadir valores por defecto
          #a sus correspondientes componentes gráficos.
          self.__default_population_size = "100"
          self.__default_number_of_generations = "100"
          self.__default_number_of_decimals = "7"          

          #Se crea la infraestructura gráfica para el número de generaciones. Constará
          #de un Label y un Entry.
          self.__number_of_generations_label = tk.Label(self,text = "Number of Generations:")
          self.__number_of_generations_entry = tk.Entry(self,relief = "sunken")
          self.__number_of_generations_label["font"] = self.name_font
          self.__number_of_generations_entry["font"] = self.value_font    
          self.__number_of_generations_entry.insert(tk.END,self.__default_number_of_generations)

          #Se crea la infraestructura gráfica para el tamaño de la población. Constará
          #de un Label y un Entry.
          self.__population_size_label = tk.Label(self,text = "Population Size:")
          self.__population_size_entry = tk.Entry(self,relief = "sunken")
          self.__population_size_entry.insert(tk.END,self.__default_population_size)
          self.__population_size_label["font"] = self.name_font
          self.__population_size_entry["font"] = self.value_font    
   
          #Se crea la infraestructura gráfica para el número de decimales. Constará
          #de un Label y un Entry.
          self.__number_of_decimals_label = tk.Label(self,text = "Number of Decimals:")
          self.__number_of_decimals_entry = tk.Entry(self,relief = "sunken")
          self.__number_of_decimals_entry.insert(tk.END,self.__default_number_of_decimals)
          self.__number_of_decimals_label["font"] = self.name_font
          self.__number_of_decimals_entry["font"] = self.value_font    
   
          #Se coloca el atributo del título que se encuentra en la clase Padre.
          self.title_label.grid(row = self.row_position,column = 0,columnspan = 2,pady = (17,1),sticky = tk.N + tk.S)   
          #Esta variable pertenece a la clase Padre y permite llevar un control 
          #sobre el orden en el que se agregan los elementos. Sirve para colocar elementos intermedios entre el título y
          #los elementos dinámicos del Frame. 
          self.row_position += 1
          
          #De manera intermedia, se colocan en el Frame los atributos correspondientes
          #sólo a la clase PopulaceFrame. Se comienza con el numero de generaciones 
          self.__number_of_generations_label.grid(row = self.row_position,column = 0,padx = (1,9),pady = (8,5),sticky = tk.E)
          self.__number_of_generations_entry.grid(row = self.row_position,column = 1,pady = (8,5),sticky = tk.W)
          self.row_position += 1
          
          #A continuación se coloca el componente para el tamaño de la población.
          self.__population_size_label.grid(row = self.row_position,column = 0,padx = (1,9),pady = (1,5),sticky = tk.E)
          self.__population_size_entry.grid(row = self.row_position,column = 1,pady = (1,5),sticky = tk.W)
          self.row_position += 1
          
          #Finalmente se coloca el componente relativo al número de decimales.
          self.__number_of_decimals_label.grid(row = self.row_position,column = 0,padx = (1,9),pady = (1,5),sticky = tk.E)
          self.__number_of_decimals_entry.grid(row = self.row_position,column = 1,pady = (1,5),sticky = tk.W)
          self.row_position += 1
          
          #Ahora se colocan los elementos genéricos, tanto estáticos como dinámicos.
          self.grid_widgets()
      

      def restore_settings(self):
          """
             Por un lado, restaura el contenido de los elementos pertenecientes sólo 
             a esta clase, y por el otro, activa el método de la clase Padre que realiza
             una restauración de los elementos genéricos.
          """

          #Primero se elimina el contenido actual para los elementos pertenecientes sólo 
          #a la clase PopulaceFrame.             
          self.__number_of_generations_entry.delete(0,tk.END)
          self.__population_size_entry.delete(0,tk.END)
          self.__number_of_decimals_entry.delete(0,tk.END)

          #A continuación se insertan los valores por defecto para dichos elementos.
          self.__number_of_generations_entry.insert(tk.END,self.__default_number_of_generations)
          self.__population_size_entry.insert(tk.END,self.__default_population_size)
          self.__number_of_decimals_entry.insert(tk.END,self.__default_number_of_decimals)

          #Finalmente se ejecuta la función que restaura los elementos genéricos dinámicos y
          #estáticos.
          TemplatePopulationFrame.restore_settings(self)    


      def get_information(self):
          """
             Recolecta la información genérica **(usando el método de la clase Padre)**, y también
             se le añade aquélla recolectada exclusivamente en esta clase.

             :returns: | Un diccionario que contiene:
                       | **Métodos genéricos,**
                       | **Número de Generaciones,**
                       | **Tamaño de la Población,**
                       | **Número de Decimales.**
             :rtype: Dictionary
          """

          #Con ayuda de la clase Padre se recoge la información genérica.
          populace_information = TemplatePopulationFrame.get_information(self)

          #Aunada a ésta, se agrega la información suscitada en esta clase.
          populace_information["number_of_generations"] = self.__number_of_generations_entry.get()
          populace_information["population_size"] = self.__population_size_entry.get()
          populace_information["number_of_decimals"] =  self.__number_of_decimals_entry.get()
          
          return populace_information
