#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


import Tkinter as tk

from AboutToplevel import AboutToplevel 
from InternalOptionToplevel import InternalOptionToplevel
 

class MenuInternalOption(tk.Menu):
      """
         | Se crea el Menú de Opciones Internas o Menú Secundario.
         | Básicamente se trata de una serie de características que, aunque no
          forman parte esencial del programa, sí ofrecen alternativas que pueden
          facilitar la experiencia de usuario.
         | Este menú será atado al Frame Principal y desde allí el usuario podrá
          tener acceso a las opciones que aquí se describen.
         
         :param parent: El Frame Padre al que pertenece esta implementación.
         :param path_image_logo: La ruta al logotipo que se usa en esta ventana independiente.
         :param features: Un diccionario con las características que deberá tener cada una
                          de las opciones listadas.

         :type parent: Tkinter.Frame
         :type path_image_logo: String
         :type features: Dictionary 
         :returns: Tkinter.Menu
         :rtype: Instance
      """


      def __init__(self,parent,path_image_logo,features):

          #Se guarda la referencia al Frame Padre.
          self.__parent = parent

          #Se guarda una referencia al logotipo del proyecto.
          self.__path_image_logo = path_image_logo
 
          #Se crea el Menú Secundario de opciones.
          tk.Menu.__init__(self,parent)

          #Las siguientes variables se utilizan para garantizar
          #que sólo un Toplevel (ventana independiente) de cada categoría será creado y mostrado
          #(por defecto se pueden crear y mostrar tantos Toplevel como se desee.
          self.__about_toplevel_count = 0
          self.__internal_option_toplevel_count = 0 

          #Se obtienen las características que llevarán cada una de las secciones
          #del menú.
          self.__internal_option_features = features
          
          #Esta línea permite separar una opción del Menú Secundario de otra.
          self.__file_menu = tk.Menu(self,tearoff = 0)

          #La primera opción es Exit y como dice su nombre termina el programa.
          self.__file_menu.add_command(label = "Exit",command = parent.quit)

          #Esta línea permite separar una opción del Menú Secundario de otra.
          self.__edit_menu = tk.Menu(self,tearoff = 0)

          #La segunda opción corresponde a las Opciones Internas del programa, las cuales consisten en
          #los M.O.P.'s (Multi Objective Problems), Features que son las características del sistema 
          #y Python Expressions que son las expresiones de azúcar sintáctica necesarias para la 
          #evaluación de las funciones objetivo.
          self.__edit_menu.add_command(label = "Options",command = self.__launch_internal_option_toplevel)

          #Esta línea permite separar una opción del Menú Secundario de otra.
          self.__help_menu = tk.Menu(self,tearoff = 0)

          #La tercera opción corresponde a About, la ventana independiente (Toplevel) que contendrá
          #información básica del programa, así como datos de los desarrolladores y de contacto.
          self.__help_menu.add_command(label = "About...",command = self.__launch_about_toplevel)

          #A continuación se añaden al Menú Secundario las opciones 
          #descritas con anterioridad.
          self.add_cascade(label = "File",menu = self.__file_menu) 
          self.add_cascade(label = "Edit",menu = self.__edit_menu)
          self.add_cascade(label = "Help",menu = self.__help_menu)

          #El Menú Secundario es atado al Frame Principal.
          parent.config(menu = self)


      def about_toplevel_custom_close(self):
          """
             Indica que la única instancia que debe crearse
             para la opción About está disponible.
          """
         
          #Se decrementa el contador asociado en una unidad.
          self.__about_toplevel_count -= 1


      def internal_option_toplevel_custom_close(self):
          """
             Indica que la única instancia que debe crearse
             para la opción Options está disponible.
          """
         
          #Se decrementa el contador asociado en una unidad.
          self.__internal_option_toplevel_count -= 1


      def __launch_internal_option_toplevel(self):
          """
             .. note:: Este método es privado.
  
             Abre la ventana independiente **(Toplevel)** Internal Options
             **(o simplemente Options)**.
             También verifica que se abra una y sólo una instancia de 
             dicha ventana.
          """

          #Si el contador asociado es 0, significa que no se ha creado ninguna instancia
          #y se procede a crear una.
          if self.__internal_option_toplevel_count == 0:

             #Se crea un apuntador a la función que decrementa el contador asociado, 
             #esto para que, cuando se cierre el Toplevel actual, se decremente y entonces
             #esta sección reconocerá que se puede volver a crear una y sólo una instancia.
             internal_option_custom_function = self.internal_option_toplevel_custom_close

             #El contador asociado se incremente indicando que por el momento no se puede
             #crear otra instancia.
             self.__internal_option_toplevel_count += 1
 
             #Se crea la instancia Internal Options.
             InternalOptionToplevel(self.__parent,self.__path_image_logo,self.__internal_option_features,internal_option_custom_function)
          

      def __launch_about_toplevel(self):
          """
             .. note:: Este método es privado.

             Abre la ventana independiente **(Toplevel)** About.
             También verifica que se abra una y sólo una instancia de 
             dicha ventana.
          """

          #Si el contador asociado es 0, significa que no se ha creado ninguna instancia
          #y se procede a crear una.
          if self.__about_toplevel_count == 0:

             #Se crea un apuntador a la función que decrementa el contador asociado, 
             #esto para que, cuando se cierre el Toplevel actual, se decremente y entonces
             #esta sección reconocerá que se puede volver a crear una y sólo una instancia.
             about_custom_function = self.about_toplevel_custom_close

             #El contador asociado se incremente indicando que por el momento no se puede
             #crear otra instancia.
             self.__about_toplevel_count += 1 

             #Se crea la instancia About.
             AboutToplevel(self.__parent,self.__path_image_logo,about_custom_function) 
