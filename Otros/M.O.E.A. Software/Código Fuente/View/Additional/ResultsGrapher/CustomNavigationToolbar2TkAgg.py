#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


#Aunque no se usa FileDialog, se importa para que  el programa funcione en sistemas 
#operativos Windows.
import FileDialog
from tkFileDialog import asksaveasfilename
from tkMessageBox import showerror

import matplotlib
#La siguiente línea de código sirve para eliminar el modo depurador de la biblioteca
#que enlaza Tkinter con Matplotlib
matplotlib.use("TkAgg",warn = False)

from matplotlib.backends.backend_tkagg import NavigationToolbar2TkAgg


class CustomNavigationToolbar2TkAgg(NavigationToolbar2TkAgg):
      """
         | Proporciona una Barra de Navegación **(ó NavigationToolbar)** que se anexa a cada
          una de las gráficas con el fin de facilitar la exploración y almacenamiento de los
          datos obtenidos.
         | Por defecto la barra de navegación original se encuentra obsoleta a las necesidades
          inherentes a este proyecto, por ello es que se crea una barra personalizada que
          responde a requerimientos tales como la obtención apropiada de imágenes relativas
          a las gráficas así como su correcto funcionamiento sin importar el sistema operativo
          empleado.

         :param canvas: La estructura que contiene tanto a la gráfica como a la Barra de Navegación.
         :param window: El Frame que contiene a canvas.
         :param parent_frame: El Frame que contiene a window, en este caso ResultsGrapherToplevel.py.
         :param execution_task_count: Un identificador que precisa el número de tarea **(Task)** en ejecución
                                      **(véase View/Additional/ResultsGrapher/ResultsGrapherToplevel.py)**.
         :param image_text: El nombre que tendrán por defecto las imágenes resultantes al guardarse en el equipo
                            de cómputo.

         :type canvas:  matplotlib.backends.backend_tkagg.FigureCanvasTkAgg
         :type window: Tkinter.Frame
         :type parent_frame: Tkinter.Frame
         :type execution_task_count: Integer
         :type image_text: String
         :returns: matplotlib.backends.backend_tkagg.NavigationToolbar2TkAgg
         :rype: Instance
      """


      def __init__(self,canvas,window,parent_frame,execution_task_count,image_text):

          #Se almacenan los datos correspondientes al Frame Padre (para saber dónde colocar
          #la ventana de salvado de gráfica), el texto con el que se guardan  por defecto las
          #gráficas resultantes y el número de Task en ejecución para que se diferencie de
          #los demás, respectivamente.
          self.__parent = parent_frame
          self.__image_text = image_text
          self.__execution_task_count = execution_task_count

          #Se inicializa la clase Padre para poder tener acceso a los métodos de éste.
          NavigationToolbar2TkAgg.__init__(self,canvas,window)


      def save_figure(self,*args):
          """
             .. note:: Este método sobreescribe al original.
             
             | Arroja una ventana emergente modificada para guardar archivos, en este caso
              las gráficas.
             | Las modificaciones con respecto de la función original consisten en agregar
              un título para tener conocimiento de las imágenes del Task que se van a guardar.
             | Además se modifica el comportamiento de la ventana para adherirlo a la ventana
              del Task y no a la Ventana Principal.

             :param args: Un listado con parámetros que aunque no se ocupan en el método
                           se coloca porque así lo estructuraron los desarrolladores originales
                           de la biblioteca.
            
             :type args: Tuple
          """    

          #Las siguientes instrucciones colocan los posibles formatos en los que se 
          #puede guardar la gráfica.
          filetypes = self.canvas.get_supported_filetypes().copy()
          default_filetype = self.canvas.get_default_filetype()
          default_filetype_name = filetypes[default_filetype]

          del filetypes[default_filetype]
          sorted_filetypes = filetypes.items()

          sorted_filetypes.sort()
          sorted_filetypes.insert(0, (default_filetype, default_filetype_name))
          tk_filetypes = [(name, '*.%s' % ext) for (ext, name) in sorted_filetypes]

          #Se crea la ventana de diálogo (ya está fabricada, sólo cambian algunos parámetros).
          fname = asksaveasfilename(
                                    parent = self.__parent,
                                    title = "Task {0}. Save the current graph".format(self.__execution_task_count),
                                    filetypes = tk_filetypes,
                                    defaultextension = ".png",
                                    initialfile = self.__image_text
                                   )

          #Si la creación de la ventana de diálogo no regresa nada, 
          #la función termina.
          if fname == "" or fname == ():
             return

          #Si la creación de la ventana de diálogo arroja algo distinto del vacío (pudiendo ser la instancia
          #de la ventana de diálogo o un mensaje de error), entonces se tratan ambos casos.
          else:
              try:
                  #Si se regresa una instancia, se muestra en el Canvas correspondiente. 
                  self.canvas.print_figure(fname)

              except Exception, e:
                  #Si se regresa un mensaje de error, se manda una ventana de diálogo especial.
                  showerror("Error saving file", str(e))
