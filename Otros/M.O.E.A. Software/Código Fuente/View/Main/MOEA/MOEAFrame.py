#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


import Tkinter as tk
from AlgorithmFrame import AlgorithmFrame
from SharingFunctionFrame import SharingFunctionFrame


class MOEAFrame(tk.Frame):
      """
         Unifica los Frames AlgorithmFrame y SharingFunctionFrame, 
         la razón de ésto es para facilitar el acomodo de componentes de manera 
         individual, para así garantizar un acceso asequible a la información.

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
          #Ambos Frames estarán contenidos en éste.
          tk.Frame.__init__(self,parent,relief = "groove")

          #Se declaran instancias de ambos Frames.
          self.__algorithm_frame = AlgorithmFrame(self,"MOEA",features["features"]["MOEA"])
          self.__sharing_function_frame = SharingFunctionFrame(self,"Sharing Function",features["features"]["Sharing Function"])

          #Se colocan dentro del Frame Padre
          self.__sharing_function_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True)
          self.__algorithm_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True)

     
      def restore_settings(self):
          """
             Restaura los valores por defecto en cada Frame.
          """

          #Se ejecuta la función correspondiente de cada Frame.
          self.__sharing_function_frame.restore_settings()
          self.__algorithm_frame.restore_settings()
          

      def get_information(self):
          """
             Toma la información solicitada en cada Frame y después
             la unifica para regresar un sólo conjunto de información.

             :returns: Un diccionario con la información de AlgorithmFrame y SharingFunctionFrame.
             :rtype: Dictionary
          """

          #Se toma un diccionario vacío y se le concatena la información
          #recabada por cada Frame.
          moea_information = {}
          moea_information.update(self.__sharing_function_frame.get_information())
          moea_information.update(self.__algorithm_frame.get_information())
          return moea_information
