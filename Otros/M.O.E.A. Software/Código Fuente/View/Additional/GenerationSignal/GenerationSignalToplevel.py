#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


import Tkinter as tk
import time as tiempo


class GenerationSignalToplevel(tk.Toplevel):
      """
         | Se trata de un Toplevel **(ventana independiente)** que muestra el progreso de las generaciones
          al momento de ejecutar un Task.
         | Esta ventana aunque es creada y mostrada en los procesos de la capa View, será en **Model/MOEA**
          en donde se utilice y actualice, ya que la idea es crear una "señal" que indique al usuario el progreso
          del MOEA en ejecución para que se dé una idea del desempeño del algoritmo.
         
         :param parent: Frame padre al que pertenece.
         :param path_image_logo: La ruta al logotipo que se usa en esta ventana independiente.
         :param execution_task_number: Número que indica el actual Task en ejecución 
                                       **(véase View/Additional/ResultsGrapher/ResultsGrapherToplevel.py)**.
         
         :type parent: Tkinter.Frame
         :type path_image_logo: String
         :type execution_task_number: Integer
         :returns: Tkinter.Toplevel
         :rtype: Instance         
      """


      def __init__(self,parent,path_image_logo,execution_task_number):  

          #Se declaran las medidas de ancho y largo que llevará la ventana independiente.
          self.__width = 335
          self.__height = 75

          #Se guarda una referencia a la ventana Padre.
          self.__parent = parent

          #Las siguiente variable sirve para determinar el número
          #total de generaciones. Esta información se mostrará en la ventana.
          self.__number_of_generations = -1

          #A continuación se crea un Toplevel sobre el cual se impregnará la información pertinente.
          tk.Toplevel.__init__(self,parent)

          #Por defecto, un Toplevel recién creado siempre se mostrará en pantalla, se haya o no insertado informacion.
          #Es por esto que, una vez construido se oculta automáticamente para poder rellenarlo de los datos necesarios
          #y posteriormente reactivarlo.
          self.hide()

          #Se colocan las medidas mínimas necesarias de largo y anchura para la ventana independiente. Esto en parte ayuda
          #a que el usuario NO redimensione la ventana.
          self.minsize(width = self.__width,height = self.__height)

          #Dado que se trata de una ventana independiente, trae consigo el ícono para cerrarse activo. Con la finalidad 
          #de evitar situaciones malintencionadas por parte del usuario, dicho ícono se desactiva, sustituyendo su función
          #asociada por una función "dummy" o que no hace nada.
          self.protocol("WM_DELETE_WINDOW", self.__do_nothing) 

          #Con esta opción se indica que la ventana no puede ser redimensionada a otros valores mayores.       
          self.resizable(0,0)

          #Con esta opción se le ordena a la ventana independiente que se muestre siempre delante de su ventana Padre,
          #en este caso, la ventana principal.
          self.transient()

          #Se le pone un título a la ventana independiente, el cual incluirá el número del Task actual.
          self.title("Executing task no.: {0}. Please wait.".format(execution_task_number))
       
          #Se crea una etiqueta que es la que almacenará el número de generación actual y el número de 
          #generaciones totales.
          self.__current_generation_label = tk.Label(self,font = "Helvetica")

          #Dicha etiqueta se coloca en la ventana independiente.
          self.__current_generation_label.pack(side = tk.BOTTOM,fill = tk.Y,expand = True)

          #Se coloca el logotipo en esta ventana independiente.
          self.wm_iconbitmap(bitmap = path_image_logo)

          
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
             Oculta y elimina toda referencia gráfica y lógica de la 
             ventana independiente, indicando así que el número de generaciones ha alcanzado
             su límite.
          """

          #Simplemente se destruye la ventana independiente.
          self.destroy()


      def hide(self):
          """
            Oculta la ventana independiente de la pantalla pero no la elimina de los registros
            gráficos.
          """
         
          #Esta función desaparece la ventana sin borrar su registro.
          self.withdraw()


      def update_number_of_generations(self,number_of_generations):
          """
             Actualiza el número total de generaciones. Generalmente esta función
             será llamada desde Controller/Controller.py ya que ahí es donde se decide
             si las configuraciones iniciales son adecuadas para poder ejecutar el algoritmo.

             :param number_of_generations: El número de generaciones total que tendrá el MOEA.
             
             :type number_of_generations: Integer. 
          """

          #Se actualiza el valor de las generaciones al que tiene la clase como atributo.
          self.__number_of_generations = number_of_generations

          
      def show(self):
          """
             Reactiva la ventana independiente, realizando además durante esta ejecución
             un par de consignas más para dar una experiencia de usuario suficiente y concisa.
          """
          
          #Primero se centra la ventana actual con respecto de la ventana Padre.
          self.__center()

          #A continuación se coloca en la ventana la siguiente etiqueta que indica que
          #el proceso fue aprobado por Controller y que comenzará en breve
          self.__current_generation_label.config(text = "Starting procedure...")

          #Ahora se materializa la ventana ya en el centro de la ventana Principal.
          self.deiconify()

          #Se hace un retraso de tiempo (en segundos) para dar la ilusión al usuario de que se están cargando configuraciones extra.
          #Lo cierto es que si no se pone este retraso, la carga es tan rápida que ni siquiera podría ver etiqueta alguna.
          tiempo.sleep(2)

          #Después de haber transcurrido el período de "espera", se coloca en la ventana la siguiente etiqueta que muestra
          #que el número de generaciones ya comienza a correr.
          self.__current_generation_label.config(text = "Now running generation 1 / {0}".format(self.__number_of_generations))

          #Por los mismos argumentos que en la parte descrita anteriormente, se coloca un retraso de un segundo para 
          #darle al usuario la sensación de que el proceso está siendo cargado apropiadamente.
          tiempo.sleep(1)
          
    
      def update_current_generation(self,current_generation):
          """
             | Actualiza la generación actual en la ventana independiente.
             | Típicamente esta función será usada en todos los algoritmos de la capa Model/MOEA, pues
              es allí donde se designará el progreso del algoritmo que a su vez se verá 
              reflejado en la capa de View.

             :param current_generation: La generación que está corriendo actualmente en el MOEA.s

             :type current_generation: Integer
             :returns: 1 si se  ha alcanzado la generación límite, 0 en otro caso.
             :rtype: Integer         
          """

          #Se actualiza la etiqueta de la ventana principal con base en el valor de la generación actual.
          self.__current_generation_label.config(text = "Now running generation {0} / {1}".format(current_generation + 1,self.__number_of_generations))   

          #Si la generación actual ha llegado al máximo de generaciones entonces se hace lo siguiente.
          if current_generation == self.__number_of_generations:

             #Se da una ventana de tiempo para que el usuario pueda ver que se ha llegado al final.
             tiempo.sleep(1)

             #Después se le notifica al usuario que se están procesando los datos recabados para poder ser graficados.
             #Cabe mencionar que dichas acciones NO se realizan aquí, nuevamente esto da la ilusión de tales operaciones
             #para dar una experiencia de usuario digna.
             self.__current_generation_label.config(text = "Processing data...")

             #Se realiza un retraso de tiempo para que el usuario perciba que el procesamiento de datos está tomando un poco de tiempo.
             tiempo.sleep(2)

             #Finalmente se oculta la ventana. NO se destruye porque de eso se encargará otra función (véase View/Main/MainWindow.py).
             self.hide()
            
             #Como se ha alcanzado la generación límite, se regresa 1.
             return 1

          #Si no se ha alcanzado la generación límite, se regresa 0.
          return 0
          

      def __do_nothing(self):
          """
             .. note:: Este método es privado.

             Simplemente es una función "dummy" que no realiza nada. 
             Es utilizada como sustituto de la función del ícono "Cerrar" y así evitar
             que el usario intencionadamente intente ocluir la ventana del número de generaciones.
          """ 

          #Así se indica en Python que la función no hará nada.        
          pass 
