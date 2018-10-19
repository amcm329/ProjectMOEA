#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


import Tkinter as tk
from SelectionFrame import SelectionFrame
from CrossoverFrame import CrossoverFrame
from MutationFrame import MutationFrame


class GeneticOperatorFrame(tk.Frame):
      """
         Reúne y controla las clases SelectionFrame, CrossoverFrame y  
         MutationFrame con la finalidad de colocar los elementos gráficos apropiadamente y 
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
          tk.Frame.__init__(self,parent,relief = "groove")

          #Se crean las instancias de cada Frame.
          self.__selection_frame = SelectionFrame(self,"Selection",features["features"]["Selection"])
          self.__crossover_frame = CrossoverFrame(self,"Crossover",features["features"]["Crossover"]) 
          self.__mutation_frame = MutationFrame(self,"Mutation",features["features"]["Mutation"])
         
          #Ahora se colocan éstas en su frame Padre.
          self.__selection_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True)
          self.__crossover_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True)
          self.__mutation_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True)

     
      def restore_settings(self):
          """
             Realiza la restauración de información y contenido en
             cada uno de los Frames.
          """

          #Se ejecuta la función pertinente en cada Frame.
          self.__selection_frame.restore_settings()
          self.__crossover_frame.restore_settings()
          self.__mutation_frame.restore_settings()


      def get_information(self):
          """
             Toma la información propiciada en cada Frame y después
             la unifica para regresar un sólo conjunto de información.

             :returns: Un diccionario con la información de SelectionFrame, CrossoverFrame y MutationFrame.
             :rtype: Dictionary
          """

          #Se toma un diccionario vacío y se va llenando con la información recabada de 
          #cada Frame.
          genetic_operator_information = {}
          genetic_operator_information.update(self.__selection_frame.get_information())
          genetic_operator_information.update(self.__crossover_frame.get_information())
          genetic_operator_information.update(self.__mutation_frame.get_information())
          return genetic_operator_information
