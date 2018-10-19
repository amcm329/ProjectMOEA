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
from IntroductionFrame import IntroductionFrame


class HomeFrame(tk.Frame):
      """
         | Unifica dos elementos: Canvas e IntroductionFrame.
         | La razón de haber hecho esto es que, cuando se añaden demasiados elementos al
          IntroductionFrame, se tiene que agregar una barra de desplazamiento para poder
          acceder a los que se encuentran hasta abajo. Dentro del ambiente de Tkinter, el
          elemento más sencillo para lograr esto es un Canvas, por ello se anida el
          IntroductionFrame al Canvas.

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
          #Se crea un Frame principal, el cual tendrá al Canvas como hijo que a su vez
          #tendra al IntroductionFrame como hijo.
          tk.Frame.__init__(self,parent,bd = 4,relief = "groove")

          #Este es el elemento gráfico que permite la inserción de una barra de desplazamiento.
          #Un Frame no puede contener tal elemento de manera nativa.
          self.__canvas = tk.Canvas(self)

          #A continuación se declara la barra de desplazamiento, se colocará de manera vertical y 
          #se asocia al Canvas.
          self.__scrollbar = tk.Scrollbar(self,orient = tk.VERTICAL,command = self.__canvas.yview)

          #Se configura al Canvas con las caracterísitas de la barra de desplazamiento.
          self.__canvas.configure(yscrollcommand = self.__scrollbar.set)

          #Para obtener el color del fondo del Frame Principal.
          features["parent_bg"] = parent.cget("bg")

          #Ahora se crea el IntroductionFrame cuyo Padre será el Canvas.
          self.__content_frame = IntroductionFrame(self.__canvas,self.move_to_section,features)  

          #Se le añade un evento al IntroductionFrame que activará la barra de desplazamiento cada vez que
          #el número de casillas sobrepase el límite del Frame.
          self.__content_frame.bind("<Configure>",self.__update_scrollbar)

          #Se coloca el Frame dentro del Canvas.
          self.__content_frame.pack(side = tk.TOP,fill = tk.X,expand = True)

          #La siguiente instrucción le indica al Canvas que cree una ventana que contenga al 
          #IntroductionFrame y que se desplazará hacia abajo y hacia la derecha cuando se quiera 
          #hacer desplazamiento con la barra.
          self.__canvas.create_window((30,0),window = self.__content_frame,anchor = tk.NW)
          
          #Estas opciones sirven para colocar apropiadamente el Canvas, son opciones
          #que permiten traslapar en este caso la columna y el renglón 0 en una unidad.
          self.grid_rowconfigure(0,weight = 1)
          self.grid_columnconfigure(0,weight = 1)
  
          #Se coloca el Canvas en referencia al contenedor Padre.
          self.__canvas.grid(row = 0,column = 0,sticky = tk.N + tk.S + tk.W + tk.E)
  
          #Se coloca el Scrollbar en referencia al contenedor Padre.
          self.__scrollbar.grid(row = 0,column = 1,sticky = tk.N + tk.S)    
                            
                       
      def __update_scrollbar(self,event = None):
          """
             .. note:: Este método es privado.  

             Actualiza la barra de desplazamiento de acuerdo al número de elementos
             existentes en el Frame, esto para poder hacer un recorrido apropiado de 
             la barra.

             :param event: Elemento que ejecutó esta función.

             :type event: String
          """

          #Ajusta la barra de desplazamiento con respecto del Frame.
          self.__canvas.configure(scrollregion = self.__canvas.bbox("all"))


      def restore_settings(self):
          """
             Restaura la configuración del Frame a la que tenía por
             defecto.
          """

          #Ajusta el Scrollbar asociado al Canvas hasta el principio de su
          #posición.
          self.__canvas.yview_moveto(0.0)
          

      def move_to_section(self,y_coordinate):
          """
             Mueve la barra de desplazamiento (y por ende el contenido)
             con base en la coordenada (en Y) que se le pase como parámetro.

             :param y_coordinate: Coordenada que se necesita para hace el
                                  desplazamiento. Oscila entre 0 y 1.

             :type y_coordinatet: Float
          """

          #Desde el Canvas se le ordena al Scrollbar que se mueva a la 
          #posición indicada.
          self.__canvas.yview_moveto(y_coordinate)
