#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


import Tkinter as tk
from PopulaceFrame import PopulaceFrame
from FitnessFrame import FitnessFrame


class PopulationFrame(tk.Frame):
      """
         Unifica y mantiene un control sobre las clases PopulaceFrame y 
         FitnessFrame, esto con el fin de poder colocar los elementos apropiadamente y 
         agilizar el intercambio de información con el usuario.

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
          #Se crea el Frame que albergará a PopulaceFrame y FitnessFrame.
          tk.Frame.__init__(self,parent,relief = "groove")
          
          #Se crean los Frames correspondientes a cada una de las clases contenidas.
          self.__populace_frame = PopulaceFrame(self,"Population",features["features"]["Population"])
          self.__fitness_frame = FitnessFrame(self,"Fitness",features["features"]["Fitness"])

          #Se colocan dichos frames en el Frame Padre, el cual se encuentra en esta clase.
          self.__populace_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True)
          self.__fitness_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True)
              
     
      def restore_settings(self):
          """
             Restaura los valores por defecto en ambos Frames.
          """

          #Se ejecuta la función correspondiente en cada Frame.
          self.__populace_frame.restore_settings()
          self.__fitness_frame.restore_settings()
     

      def get_information(self):
          """
             Toma la información propiciada en cada Frame y después
             la unifica para regresar un sólo conjunto de información.

             :returns: Un diccionario con la información de PopulaceFrame y FitnessFrame.
             :rtype: Dictionary
          """
          
          #Se crea un diccionario y sobre el cual se adjuntará la información
          #rescatada de cada uno de los Frames.
          population_information = {}
          population_information.update(self.__populace_frame.get_information())
          population_information.update(self.__fitness_frame.get_information())
          return population_information             
