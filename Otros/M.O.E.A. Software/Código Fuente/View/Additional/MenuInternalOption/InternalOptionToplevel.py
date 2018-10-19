#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


import ttk
import Tkinter as tk

from InternalOptionTab.MOPExampleFrame import MOPExampleFrame
from InternalOptionTab.FeatureFrame import FeatureFrame
from InternalOptionTab.PythonExpressionFrame import PythonExpressionFrame


class InternalOptionToplevel(tk.Toplevel):
      """
         | Contiene un Menú pequeño con pestañas que indican las
          características internas del sistema a las que puede tener acceso el 
          usuario.
         | En su mayoría se trata de características que muestran los métodos,
          técnicas y sistemas auxiliares que garantizan un manejo más armonioso 
          del programa y si así lo desea el usuario, modificarlos para ajustar
          su desempeño.

         :param parent: El elemento Padre al que pertenece la actual
                        ventana independiente **(Toplevel)**.
         :param path_image_logo: La ruta al logotipo que se usa en esta ventana 
                                 independiente.
         :param features: Un diccionario que contiene las características necesarias
                          que serán mostradas en esta ventana independiente. 
         :param custom_function: Una variable que contiene una función, la cual
                                 redefinirá más apropiadamente el comportamiento de
                                 la actual Ventana Principal con respecto de su Frame Padre.
 
         :type parent: Tkinter.Menu
         :type path_image_logo: String
         :type features: Dictionary
         :type custom_function: Instance
         :returns: La ventana independiente que contiene la información
                   señalada.
         :rtype: Tkinter.Toplevel
      """


      def __init__(self,parent,path_image_logo,features,custom_function):
          #Se declaran las medidas de ancho y largo que llevará la ventana independiente.
          self.__width = 650
          self.__height = 460

          #Se guarda una referencia al Padre del Toplevel actual.
          self.__parent = parent

          #Se crea una variable asociada a la función personalizada.
          self.__custom_function = custom_function

          #Se inicializa el Toplevel (ventana independiente) actual.
          tk.Toplevel.__init__(self,parent)

          #Por defecto el Toplevel aparece en la esquina superior izquierda, de modo
          #que para poderlo llenar apropiadamente de la información relevante, se oculta
          #para que no se vea estropeada la experiencia de usuario.
          self.withdraw()

          #Se modifica la función que antecede al evento de cerrar la ventana.
          self.protocol("WM_DELETE_WINDOW", lambda: self.close()) 

          #Esta opción indica que la ventana independiente se mostrará delante de
          #su Padre.
          self.transient()
          
          #El elemento gráfico principal en esta ventana será el que tiene la posibilidad
          #de usar pestañas; se trata del Notebook.
          self.__notebook = ttk.Notebook(self)

          #Se crea el Frame que tendrá los M.O.P.'s (Multi Objective Problems) precargados 
          #Para facilitar la experiencia de usuario.
          self.__example_frame = MOPExampleFrame(self,features["M.O.P. Examples"])

          #Se crea el Frame que contendrá expresiones de azúcar sintáctica para
          #diseñar y evaluar funciones objetivo más complejas.
          self.__python_expression_frame = PythonExpressionFrame(self,features["Python Expressions"])

          #Se crea el Frame donde se mostrarán todas las técnicas disponibles
          #así como los parámetros que emplean.   
          self.__feature_frame = FeatureFrame(self,features["Features"])
          
          #A continuación se añaden cada uno de los Frames anteriores en el Notebook
          #usando pestañas para diferenciar un contenido de otro.
          self.__notebook.add(self.__example_frame,text = "M.O.P. Examples")
          self.__notebook.add(self.__python_expression_frame,text = "Python Expressions")
          self.__notebook.add(self.__feature_frame,text = "Features")
          
          #Se coloca el Notebook en el contenedor Padre (Toplevel).
          self.__notebook.pack(side = tk.TOP,fill = tk.BOTH,expand = True)

          #Con la información debidamente cargada, se procede a centrar la ventana independiente
          #con respecto de la ventana principal.
          self.__center()

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


      def close(self):
          """
             .. note:: Este método es privado.
             
             Cierra y elimina todo rastro de esta ventana independiente.
          """

          #Antes de cerrarse esta ventana independiente se ejecuta
          #la función que se pasó como parámetro en el constructor.          
          self.__custom_function()

          #Simplemente se destruye la ventana independiente.
          self.destroy()
