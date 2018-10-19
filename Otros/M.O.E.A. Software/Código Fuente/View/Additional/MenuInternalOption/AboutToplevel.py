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


class AboutToplevel(tk.Toplevel):
      """
         Esta ventana independiente **(Toplevel)** proporciona
         información básica del programa así como de sus 
         desarrolladores.

         :param parent: El elemento Padre al que pertenece la actual
                        ventana independiente **(Toplevel)**.
         :param path_image_logo: La ruta al logotipo que se usa en esta ventana independiente.
         :param custom_function: Una variable que contiene una función, la cual
                                 redefinirá más apropiadamente el comportamiento de
                                 la actual Ventana Principal con respecto de su Frame Padre.
 
         :type parent: Tkinter.Menu
         :type path_image_logo: String
         :type custom_function: Instance
         :returns: Tkinter.Toplevel
         :rtype: Instance
      """


      def __init__(self,parent,path_image_logo,custom_function):

          #Las siguientes son las dimensiones de ancho y largo
          #respectivamente que tendrá esta ventana independiente.
          self.__width = 388
          self.__height = 270

          #Se guarda una referencia al Frame Padre.
          self.__parent = parent

          #Se inicializa el Toplevel (ventana independiente) actual.
          tk.Toplevel.__init__(self,parent)

          #Por defecto el Toplevel aparece en la esquina superior izquierda, de modo
          #que para poderlo llenar apropiadamente de la información relevante, se oculta
          #para que no se vea estropeada la experiencia de usuario.
          self.withdraw()

          #Se coloca el título que llevará esta ventana.
          self.title("About M.O.E.A. Software.")

          #Se modifica la función que antecede al evento de cerrar la ventana.
          self.protocol("WM_DELETE_WINDOW", lambda: self.__close(custom_function)) 

          #Esta opción indica que la ventana independiente se mostrará delante de
          #su Padre.
          self.transient()

          #A continuación se crean las tipografías que serán empleadas para mostrar
          #la información pertinente.
          self.__name_font = tkf.Font(family = "Helvetica",size = 10,weight = "bold")
          self.__value_font = tkf.Font(family = "Helvetica",size = 10)

          #Los siguientes Labels manejan aspectos muy generales del programa, como la versión
          #y en qué lenguaje de programación fue hecho.
          self.__outline_label = tk.Label(self,text = "Outline: ")
          self.__outline_1_label = tk.Label(self,text = "M.O.E.A. Software. Version 1.0.")
          self.__outline_2_label = tk.Label(self,text = "Made in Python, version 2.7.3.")

          #Se le da formato a las Labels de las características generales del programa.
          self.__outline_label["font"] = self.__name_font
          self.__outline_1_label["font"] = self.__value_font
          self.__outline_2_label["font"] = self.__value_font

          #Se colocan en el Toplevel los Labels de las características generales del programa.
          self.__outline_label.grid(row = 0,column = 0,padx = (32,9),pady = (10,2),sticky = tk.W)
          self.__outline_1_label.grid(row = 1,column = 1,padx = (1,1),pady = (5,2),sticky = tk.W)
          self.__outline_2_label.grid(row = 2,column = 1,padx = (1,1),pady = (5,2),sticky = tk.W)

          #Los siguientes Labels contienen información sobre los desarrolladores
          #del proyecto. 
          self.__developers_label = tk.Label(self,text = "Developers: ")
          self.__developers_1_label = tk.Label(self,text = u"PhD. Katya Rodríguez Vázquez.".encode("utf-8"))
          self.__developers_2_label = tk.Label(self,text = u"Aarón Martín Castillo Medina.".encode("utf-8"))

          #Se les da el formato adecuado a los Labels de los desarrolladores.          
          self.__developers_label["font"] = self.__name_font
          self.__developers_1_label["font"] = self.__value_font
          self.__developers_2_label["font"] = self.__value_font

          #Se colocan en el Toplevel los Labels de los desarrolladores.
          self.__developers_label.grid(row = 3,column = 0,padx = (32,9),pady = (10,2),sticky = tk.W)
          self.__developers_1_label.grid(row = 4,column = 1,padx = (1,1),pady = (5,2),sticky = tk.W)
          self.__developers_2_label.grid(row = 5,column = 1,padx = (1,1),pady = (5,2),sticky = tk.W)

          #Los siguientes Labels contienen información de la manera de contactar
          #a los desarrolladores del proyecto.
          self.__contact_label = tk.Label(self,text = "Contact: ")
          self.__contact_1_label = tk.Label(self,text = "katya.rodriguez@iimas.unam.mx")
          self.__contact_2_label = tk.Label(self,text = "amcm329@hotmail.com")

          #Se le da el formato apropiado a los Labels de la forma de contacto
          #de los desarrolladores.
          self.__contact_label["font"] = self.__name_font
          self.__contact_1_label["font"] = self.__value_font
          self.__contact_2_label["font"] = self.__value_font

          #Se colocan los Label de la forma de contacto de los desarrolladores.
          self.__contact_label.grid(row = 6,column = 0,padx = (32,9),pady = (10,2),sticky = tk.W)
          self.__contact_1_label.grid(row = 7,column = 1,padx = (1,1),pady = (5,2),sticky = tk.W)
          self.__contact_2_label.grid(row = 8,column = 1,padx = (1,1),pady = (5,2),sticky = tk.W)

          #Con la información debidamente cargada, se procede a centrar la ventana independiente
          #con respecto de la ventana principal.
          self.__center()

          #Con esta opción se indica que la ventana no puede ser redimensionada a otros valores mayores.       
          self.resizable(0,0)

          #Se coloca el logotipo en esta ventana independiente.
          self.wm_iconbitmap(bitmap = path_image_logo)

          #Al final muestra la ventana independiente.
          self.deiconify()
 

      def __center(self):
          """
             .. note:: Este método es privado.

             Centra la ventana independiente con respecto de la Ventana Principal.
             En otras palabras, la ventana independiente será colocada en el centro de la 
             Ventana Principal.
          """
  
          #Primero se actualizan las posiciones y dimensiones de la ventana principal (en caso 
          #de que alguien la haya redimensionado o movido de su posición original).
          self.update_idletasks()

          #Se obtiene la geometría de la ventana principal.
          #Ésta se obtiene de la forma A x B + C + D, donde A y B representan 
          #el ancho y largo respectivamente, mientras que C y D contienen el 
          #desplazamiento en el eje X (para C) & Y (para D) con respecto
          #del origen (esquina superior izquierda de la pantalla).
          parent_geometry = self.__parent.winfo_geometry()
          parent_geometry = parent_geometry.replace('x','+').split('+')
          parent_width = int(parent_geometry[0])
          parent_height = int(parent_geometry[1])
          parent_offset_width = int(parent_geometry[2])
          parent_offset_height = int(parent_geometry[3])

          #A continuación se obtiene la geometría de la ventana independiente.
          #Ésta se obtiene de la forma A x B + C + D, donde A y B representan 
          #el ancho y largo respectivamente, mientras que C y D contienen el 
          #desplazamiento en el eje X (para C) & Y (para D) con respecto
          #del origen (esquina superior izquierda de la pantalla).
          #Es importante mencionar que estas características se toman cuando ya se
          #ha insertado la información pertinente en la ventana, esto para que 
          #se pueda conocer a priori el tamaño de la ventana que será en principio inmutable.
          current_width = self.__width
          current_height = self.__height

          #Se calculan los desplazamientos de la ventana independiente tomando como referencia 
          #los tamaños de la ventana padre y la ventana independiente, y dado que tiene que quedar
          #exactamente en el centro, por eso es que se divide entre 2, para que quede el mismo espacio
          #tanto a la izquierda como a la derecha; tanto arriba como abajo.
          current_offset_width = parent_offset_width + (parent_width - current_width)/2 
          current_offset_height = parent_offset_height + (parent_height - current_height)/2

          #Al final se toman estos datos y se colocan en la geometría de la ventana independiente de la 
          #manera A x B + C + D descrita anteriormente.
          self.geometry('{0}x{1}+{2}+{3}'.format(current_width,current_height,current_offset_width,current_offset_height))


      def __close(self,custom_function):
          """
             .. note:: Este método es privado.
             
             Cierra y elimina todo rastro de esta ventana independiente.

             :param custom_function: Una variable que contiene una función que ha de 
                                     ejecutarse dentro de este método.

             :type custom_function: Instance
          """

          #Antes de cerrarse esta ventana independiente se ejecuta
          #la función que se pasó como parámetro.          
          custom_function()

          #Simplemente se destruye la ventana independiente.
          self.destroy()       
