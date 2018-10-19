#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


import tkFont as tkf
import Tkinter as tk


class ErrorFrame(tk.Frame):
      """
         | Este Frame surge si durante el proceso interno en el Modelo **(véase Model/MOEA)**
          se suscita algún error del cual el método no se pueda recuperar.
         | Entonces aquí se desplegará toda la información relativa a la falla, asímismo
          funciona como medida de contingencia para darle una salida al programa y evitar
          que se quede atorado.
         
         :param parent: Frame padre al que pertenece.
         :param final_results: Diccionario que contiene en este caso las características
                               alusivas a la falla **(véase Model/MOEA)**.

         :type parent: Tkinter.Frame
         :type final_results: Dictionary
         :returns: Tkinter.Frame
         :rtype: Instance
      """
      

      def __init__(self,parent,final_results):
          #El Frame Padre sobre el cual se almacenarán todos los elementos.
          tk.Frame.__init__(self,parent)

          #Se cargan algunas fuentes para darle formato a los elementos en el Frame.
          self.__title_font = tkf.Font(family = "Helvetica",size = 13,weight = "bold")
          self.__value_font = tkf.Font(family = "Helvetica",size = 11)

          #Se crean las etiquetas alusivas al Message y su contenido.
          self.__message_title_label = tk.Label(self,text = "Message:")
          self.__message_value_label = tk.Label(self,text = final_results["message"] + ".")

          #Se les da formato a las etiquetas anteriores.
          self.__message_title_label["font"] = self.__title_font
          self.__message_value_label["font"] = self.__value_font

          #Se colocan las etiquetas del Message y su contenido.
          self.__message_title_label.grid(row = 0,column = 0,padx = (25,9),pady = (40,10),sticky = tk.W)
          self.__message_value_label.grid(row = 0,column = 1,padx = (1,1),pady = (40,10),sticky = tk.W)
       
          #Se crean las etiquetas concernientes a la Class donde ocurrió 
          #el error, así como su contenido.
          self.__class_title_label = tk.Label(self,text = "Class:")
          self.__class_value_label = tk.Label(self,text = final_results["class"] + ".")
              
          #Se les da formato a las etiquetas anteriores.
          self.__class_title_label["font"] = self.__title_font
          self.__class_value_label["font"] = self.__value_font

          #Se colocan las etiquetas del Class y su contenido.  
          self.__class_title_label.grid(row = 1,column = 0,padx = (25,9),pady = (1,10),sticky = tk.W)
          self.__class_value_label.grid(row = 1,column = 1,padx = (1,1),pady = (1,10),sticky = tk.W)
       
          #Se colocan las etiquetas relacionadas con el Method y su contenido.
          self.__method_title_label = tk.Label(self,text = "Method:")
          self.__method_value_label = tk.Label(self,text = final_results["method"] + ".")

          #Se le da el formato adecuado a dichas etiquetas.
          self.__method_title_label["font"] = self.__title_font
          self.__method_value_label["font"] = self.__value_font

          #Las etiquetas del Method y su contenido se colocan en el Frame.
          self.__method_title_label.grid(row = 2,column = 0,padx = (25,9),pady = (1,10),sticky = tk.W)
          self.__method_value_label.grid(row = 2,column = 1,padx = (1,1),pady = (1,10),sticky = tk.W)
       
          #Se crean las etiquetas ligadas al Type y su contenido.
          self.__type_title_label = tk.Label(self,text = "Type:")
          self.__type_value_label = tk.Label(self,text = final_results["type"] + ".")

          #Se le da formato a dichas etiquetas.
          self.__type_title_label["font"] = self.__title_font
          self.__type_value_label["font"] = self.__value_font

          #Se colocan las etiquetas del Type y su respectivo contenido.
          self.__type_title_label.grid(row = 3,column = 0,padx = (25,9),pady = (1,10),sticky = tk.W)
          self.__type_value_label.grid(row = 3,column = 1,padx = (1,1),pady = (1,10),sticky = tk.W)
