#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


import ttk
import tkFont as tkf
import Tkinter as tk
import tkMessageBox as tkm

import os
import threading as hilo
from os import path,listdir 
from collections import deque

from Controller.Controller import Controller

from Additional.GenerationSignal.GenerationSignalToplevel import GenerationSignalToplevel
from Additional.ResultsGrapher.ResultsGrapherToplevel import ResultsGrapherToplevel
from Additional.MenuInternalOption.MenuInternalOption import MenuInternalOption
from Main.Home.HomeFrame import HomeFrame
from Main.DecisionVariable.DecisionVariableFrame import DecisionVariableFrame
from Main.ObjectiveFunction.ObjectiveFunctionFrame import ObjectiveFunctionFrame
from Main.Population.PopulationFrame import PopulationFrame
from Main.GeneticOperator.GeneticOperatorFrame import GeneticOperatorFrame
from Main.MOEA.MOEAFrame import MOEAFrame


class MainWindow:
      """
         | Mezcla todas las estructuras gráficas que forman parte de la sección View **(ó vista)**.
         | Se trata de una Ventana que contendrá todas las opciones necesarias para que
          el usuario pueda ejecutar a voluntad M.O.E.A.'s **(Multi Objective Evolutionary Algorithm
          ó Algoritmo Evolutivo Multi Objetivo)**
         |
         | El flujo que se suele seguir es el siguiente:
         * El usuario ingresa las características que desea que contenga el M.O.E.A. que será ejecutado.

         * Posteriormente el Controller **(ó Controlador, véase Controller/Controller.py)** verifica la consistencia de los datos anteriores para que no haya conflicto en el lado del Model **(ó Modelo)**.

         * Si no existe problema alguno se prosigue con el proceso, en otro caso se arroja un mensaje de error.

         * Siguiendo con el flujo normal se ejecutará una instancia del M.O.E.A. solicitado en la capa de Model **(ó Modelo)**, la cual tendrá una ventana asociada en View **(ó Vista)** que indicará el progreso del primero.

         * Cuando una instancia termine de ejecutarse, la ventana del progreso desaparece y en su lugar se muestra otra conteniendo los resultados del M.O.E.A. **(véase View/Additional/ResultsGrapher/ResultsGrapherToplevel.py)**.
        
         | Es importante mencionar que esta clase y el proyecto en general están diseñados para que 
          se puedan crear varias instancias simultáneamente, con ello se espera aprovechar al máximo los recursos
          computacionales en los que el proyecto fuera a ejecutarse.

         :returns: Tkinter.Frame
         :rtype: Instance
      """


      def __init__(self):
          #***********************************************************************#
          #Las siguientes variables determinan la composición y funcionamiento del
          #Frame Principal que es donde reside toda la carga gráfica del proyecto:
          #***********************************************************************#
          
          #Se inicializa el Frame Principal de todo el proyecto.
          #Sobre éste se colocarán otros Frames y elementos adicionales.
          self.__root = tk.Tk()   
  
          #Este es el título que llevará el Frame Principal.
          self.__root.title("M.O.E.A. Software")   

          #Este será el path (ruta) donde se hará referencia a cada
          #imagen para que se utilice en la interfaz gráfica.
          self.__image_path = ""
 
          #La siguiente variable contiene la ruta del logotipo que se usará en toda la 
          #interfaz gráfica.
          self.__path_image_logo = ""

          #Se hace una consideración a la carga de imágenes con respecto del sistema operativo usado.
          #Por defecto el sistema hace la carga de imágenes para los sistemas GNU/Linux, pero si falla entonces
          #se hace la carga para los sistemas Windows.
          try:

              #Se crea el path para los sistemas GNU/Linux.
              self.__image_path = self.resource_path("{0}/Image/".format(path.dirname(path.realpath(__file__))))
 
          except: 

              #Se crea el path para los sistemas Windows.
              self.__image_path = self.resource_path("{0}\\Image\\".format(path.dirname(path.realpath(__file__)))) 
 
          #A continuación se actualiza el logo de la interfaz gráfica de acuerdo al sistema
          #operativo usado.
          if os.name != "nt":
             #Se actualiza el logo de acuerdo a un sistema Linux.
             self.__path_image_logo = "@" + self.__image_path + "unam_shield.xbm"
    
          else:
             #Se actualiza el logotipo de acuerdo a un sistema Windows.
             self.__path_image_logo = self.__image_path + "unam_shield.ico"         

          #Se obtienen los valores de las dimensiones de la 
          #pantalla para que el Frame Principal quede enmedio.
          screen_width = self.__root.winfo_screenwidth()
          screen_height = self.__root.winfo_screenheight()

          #Estas variables se crean para ajustar las posiciones
          #del Frame Principal a la mitad.
          nuevo_w = (screen_width - 850)/2
          nuevo_h = (screen_height - 700)/2

          #Finalmente se colocará el Frame Principal en las posiciones 
          #obtenidas previamente.
          self.__root.geometry("850x700+{0}+{1}".format(nuevo_w,nuevo_h))

          #Esta línea de código cambia la tipografia de los mensajes de alerta.
          self.__root.option_add("*Dialog.msg.font","Helvetica")
       
          #*************************************************************#
          #La siguiente variable determina al Controller (ó Controlador):
          #*************************************************************#

          #La siguiente variable es una instancia al Controller (ó Controlador),
          #el cual permite la comunicación adecuada con Model (ó Modelo), a través
          #de funcionalidades que ya están implementadas en el primero.
          self.__controller = Controller()
          
          #***************************************************************#
          #Las siguientes variables manejan las cuestiones multi-threading
          #(ó Multi-hilo) del programa al momento de ejecutar M.O.E.A.S.:
          #***************************************************************#
          
          #Esta estructura permite obtener los resultados que los procesos 
          #haan descargado previamente aquí.
          self.__results_queue = deque()

          #Esta estructura obtiene el progreso actual de cada uno de los
          #procesos.
          self.__generations_queue = deque()

          #Aquí se almacenan las ventanas asociadas a los procesos, las cuales
          #indican el progreso (en generaciones) que llevan éstos.
          self.__stored_generations_signals = {}

          #Esta variable servirá como un candado para que sólo el primer proceso
          #active la verificación de las colas (Queues). El candado se desactivará
          #cuando el último proceso termine su ejecución.
          self.__check_queues_flag = False
 
          #Esta variable es un identificador para los procesos en ejecución.
          self.__execution_task_count = 0

          #Se cargan las imágenes para los Frames de la Ventana Principal.
          self.__images_data = self.__load_images()
 
          #**********************************************************************************#
          #Las siguientes variables contienen características que llevará el Menú secundario
          #perteneciente al Frame Principal:
          #**********************************************************************************#

          #Las siguientes variables proporcionan el formato para las opciones
          #del Menú secundario.
          self.__notebook_font = tkf.Font(family = "Helvetica",size = 10)
          self.__notebook_style = ttk.Style()
          self.__notebook_style.configure('.',font = self.__notebook_font)

          #Esta variable tendrá los ejemplos de M.O.P. (Multi Objective Problems), que
          #son una combinación de funciones objetivo y variables de decisión ya estudiadas.
          self.__examples = self.__controller.load_mop_examples()

          #Se cargan las opciones (features) que cada Frame posee como
          #técnicas asociadas y sus correspondientes parámetros.
          self.__main_features = self.__controller.load_features()
          
          #La siguiente variable conformará al Menú Secundario, el cual a su vez
          #consta de 3 secciones:
          #M.O.P. Examples, donde se puede ver y seleccionar los M.O.P.s existentes.
          #Python Expressions, donde se pueden ver las expresiones de azúcar sintáctica
          #implementadas hasta el momento.
          #Features, donde se pueden ver las opciones extras para cada Frame
          #de la Ventana Principal. 
          self.__menu_frame = MenuInternalOption(self.__root,self.__path_image_logo,{
                                                                                     "M.O.P. Examples": [
                                                                                                         self.__examples,
                                                                                                         self.load_mop_example
                                                                                                        ],

                                                                                     "Python Expressions": [
                                                                                                            self.__controller.load_python_expressions,
                                                                                                            self.__controller.save_python_expressions,
                                                                                                            self.__images_data,
                                                                                                           ],
   
                                                                                     "Features": self.__main_features  
                                                                                    })

          #****************************************************************************#
          #Las siguientes variables contienen Frames asociados con la Ventana Principal:
          #****************************************************************************#

          #En esta estructura se almacenarán los Frames y sus instancias ya inicializadas.
          self.__frames = {}

          #En esta estructura se guardarán los Frames y sus posiciones de acuerdo al
          #Frame de Opciones.
          self.__frames_index = {}

          #En esta lista se declaran los nombres que tendrán los Frames en la
          #Ventana Principal, también se declaran sus instancias asociadas (aún sin inicializar).
          self.__frames_instances = [
                                     ("Home",HomeFrame),
                                     ("Decision Variables",DecisionVariableFrame),
                                     ("Objective Functions",ObjectiveFunctionFrame),
                                     ("Population Settings",PopulationFrame),
                                     ("Genetic Operators Settings",GeneticOperatorFrame),
                                     ("MOEAs Settings",MOEAFrame)
                                    ]

          #En este diccionario se indica si un Frame necesita o no de imágenes.
          self.__frames_using_images = {
                                        "Home": True,
                                        "Decision Variables": True,
                                        "Objective Functions": True,
                                        "Population Settings": False,
                                        "Genetic Operators Settings": False,
                                        "MOEAs Settings": False
                                       }

          #Las siguientes variables permiten mantener un control 
          #sobre el Frame que estará colocado en la Ventana Principal
          #así como las posiciones (índices) que éstas les corresponden.
          self.__prior_frame_index = 0
          self.__current_frame_index = 0
          self.__prior_frame_name = self.__frames_instances[0][0]
          
          #*******************************************************************#
          #Las siguientes variables se relacionan con las secciones de las que 
          #constará el Frame Principal:
          #*******************************************************************#

          #El Frame Principal estará compuesto de 3 secciones gráficas:
          #Frame de Ejecución, donde estarán los botones de ejecución de M.O.E.A. 
          #y limpieza de campos
          #Frame de Opciones, aquí descansarán todas los Frames disponibles que contendrán
          #opciones para ejecutar M.O.E.A.S.
          #Ventana Principal, en realidad es un Frame que contendrá la información gráfica
          #del Frame que fuese seleccionado en el Frame de Opciones.
          
          #****Primer Frame, Frame de Ejecución***.

          #Se crea el Frame asociado a dicha sección.
          self.__execution_frame = tk.Frame(self.__root,bd = 4,relief = "groove")

          #A continuación se define la tipografía que llevarán los Buttons.
          self.__execution_font = tkf.Font(family = "Helvetica",size = 11,weight = "bold")

          #Se crea el Button relacionado con la restauración y limpieza de campos. 
          self.__delete_button = tk.Button(self.__execution_frame,relief = "raised",text = "Restore Settings ")

          #Se crea el Button que iniciará el procedimiento de ejecución de M.O.E.A.s
          self.__init_process_button = tk.Button(self.__execution_frame,relief = "raised",text = "Init Process ")
 
          #A ambos Buttons se les asigna el formato pertinente.
          self.__delete_button["font"] = self.__execution_font
          self.__init_process_button["font"] = self.__execution_font
          
          #Al Button de restauración se le liga el evento correspondiente.
          self.__delete_button.bind("<ButtonRelease-1>",self.__restore_settings)

          #Al Button de ejecución se le añade el evento correspondiente.
          self.__init_process_button.bind("<ButtonRelease-1>",self.__init_procedure)

          #Las siguientes opciones permiten centrar los botones considerando el redimensionamiento
          #de la Ventana Principal.
          self.__execution_frame.grid_columnconfigure(0,weight = 1)
          self.__execution_frame.grid_columnconfigure(1,weight = 1)

          #Si los datos provenientes del archivo .xml relacionado con las técnicas disponibles
          #contienen una llave llamada "recent" significa que el archivo está corrupto por lo que
          #se omiten los botones "Restore Settings" y "Init Process" pues no tiene sentido iniciar
          #un proceso si no se tienen las técnicas correctas.          
          if not(self.__main_features.has_key("recent")):
             #Se colocan los Buttons a manera de grid (malla).
             self.__delete_button.grid(row = 0,column = 0,padx = (1,55),pady = (14,14),sticky = tk.E)
             self.__init_process_button.grid(row = 0,column = 1,pady = (14,14),sticky = tk.W)

          #El Frame de Ejecución es añadido al Frame Principal.
          self.__execution_frame.pack(side = tk.BOTTOM,fill = tk.X)
          
          #****Segundo Frame, Frame de Opciones****.
          
          #Se crea el Frame que estará asociado a dicha sección.
          self.__settings_frame = tk.Frame(self.__root,bd = 4,relief = "groove")

          #A continuación se crea la tipografía que llevarán los elementos en la 
          #Listbox.
          self.__settings_font = tkf.Font(family = "Helvetica",size = 10,weight = "bold")

          #Se crea la Listbox.
          self.__settings_frame_listbox = tk.Listbox(self.__settings_frame,selectmode = "single",width = 24)

          #Se le añade el formato a la Listbox y por ende, a todos sus elementos.
          self.__settings_frame_listbox["font"] = self.__settings_font

          #Se crea un contador para poder identificar la posición del Frame.
          count = 0

          #Si los datos tomados del archivo .xml relacionado con los métodos disponibles
          #no tienen la llave "recent" entonces se procede a hacer la carga de opciones
          #que se mostrarán en el Frame de Settings.
          if not(self.__main_features.has_key("recent")):
            
             #Por cada Frame se realiza lo siguiente:
             for element in self.__frames_instances: 

                 #Se añade a la lista de índices el contador actual.      
                 self.__frames_index[element[0]] = count

                 #Se añade a la Listbox la opción actual de Frame.
                 self.__settings_frame_listbox.insert(tk.END,element[0]) 

                 #Se incrementa el contador para la siguiente posición del Frame.
                 count += 1
          
             #A la Listbox se le liga la función con la que se cambiará de Frame.
             self.__settings_frame_listbox.bind("<ButtonRelease-1>",self.__update_frame)

             #Las siguientes opciones sirven para resaltar la actual selección de
             #Frame de color verde.
             self.__settings_frame_listbox.itemconfig(0,background = "green")
             self.__settings_frame_listbox.itemconfig(0,selectbackground = "green")

          #Se coloca el Listbox en el Frame contenedor.
          self.__settings_frame_listbox.pack(side = tk.LEFT)  

          #Se coloca el Frame de Opciones en el Frame Principal.
          self.__settings_frame.pack(side = tk.LEFT,fill = tk.Y)

          #Se coloca el ícono correspondiente para que toda la interfaz gráfica tenga el logotipo de la 
          #Universidad Nacional Autónoma de México y no la de TK como está por defecto.
          self.__root.wm_iconbitmap(bitmap = self.__path_image_logo)
          
          #Si hubo un problema al leer las técnicas disponibles para el usuario entonces
          #se arroja un mensaje de alerta para informar al usuario.
          if self.__main_features.has_key("recent"):
             message = self.__main_features["recent"]["message"]
             tkm.showwarning("Problem at Controller/XML.",message,parent = self.__root)

          #En caso de que las técnicas disponibles no presenten ninguna falla se realiza la
          #carga de los Frames con sus correspondientes datos.
          else: 
             #Aquí se inicializan los Frames de la Ventana Principal y también se coloca
             #el designado por default en el Frame Principal.
             self.__initialize_frames()
 
          #En caso de que el archivo relacionado con las expresiones de Python esté
          #corrupto se manda un mensaje de alerta para advertir al usuario.
          if self.__controller.load_python_expressions().has_key("recent"):
             message = self.__controller.load_python_expressions()["recent"]["message"]
             tkm.showwarning("Problem at Controller/XML.",message,parent = self.__root)
 
          #Si el archivo relativo a los M.O.P.'s (Multi-objective Problems) tiene irregularidades
          #se manda un mensaje de alerta para notificar al usuario.            
          if self.__examples.has_key("recent"):
             message = self.__examples["recent"]["message"]
             tkm.showwarning("Problem at Controller/XML.",message,parent = self.__root)


      def resource_path(self,relative_path):
          """
             Esta función se utiliza para poder crear ejecutables
             apropiadamente.
             A grandes rasgos el ejecutable se empaqueta en un directorio
             llamado _MEIPASS, entonces aquí se implementa la búsqueda
             de dicho archivo devolviendo un path **(ruta)**.

             :returns: La ruta del directorio _MEIPASS.
             :rtype: String
          """

          #PyInstaller crea un folder temporal y almacena el path en
          #el directorio _MEIPASS
          try:

              #Se devuelve el path del archivo _MEIPASS.
              base_path = sys._MEIPASS
          except Exception:
                 
              #En caso de una falla se devuelve la ruta del archivo
              #actual.              
              base_path = os.path.abspath(".")

          #Se hace uan concatenación del path de _MEIPASS 
          #con el path relativo y eso es lo que se regresa.
          return os.path.join(base_path, relative_path)

     
      def __load_images(self):
          """
             .. note:: Este método es privado.

             Carga las imágenes que se encuentran en el 
             directorio View/Images para que puedan ser
             usadas por los Frames. Es importante recalcar que el método
             sólo carga imágenee .gif ya que son la extensión más estable
             para que se muestren las imágenes en la interfaz gráfica.

             :returns: Un diccionario con todas las imágenes cargadas.
             :rtype: Dictionary
          """

          #Aquí se almacenarán las imágenes.
          images = {}

          #Por cada imagen en el path utilizado se hace la carga y se guarda
          #en el diccionario. Se debe recordar que sólo se pueden utilizar archivos .gif.          
          for image in listdir(self.__image_path):
              image_index = image.rfind('.') 

              #Se obtiene la extensión de la imagen.
              image_extension = image[image_index:len(image)]
              
              #Si la imagen es .gif entonces se carga.
              if image_extension == ".gif":
                 images[image[0:image_index]] = tk.PhotoImage(file = "{0}{1}".format(self.__image_path,image)) 

          #Se regresa el diccionario de imágenes.
          return images


      def __initialize_frames(self): 
          """
             .. note:: Este método es privado.
 
             Método que inicializa los Frames que se 
             colocarán en la Ventana Principal como opciones.
          """
              
          #Se ejecuta el siguiente ciclo para cargar cada uno de los 
          #Frames que se encuentran en la estructura __frames_instances.
          for element in self.__frames_instances:
              #Aquí se introducen características adicionales
              #que pudieran requerir el Frame actual.
              complete_features = {}

              #Se obtiene el nombre del Frame.
              name = element[0]

              #Se obtiene la instancia del Frame.
              frame_instance = element[1]

              #Si el Frame necesita que se le carguen imágenes
              #se añaden aquí usando la estructura complete_features.
              if self.__frames_using_images[name] == True:
                 complete_features["images"] = self.__images_data
              
              #Si el Frame se encuentra en la estructura __main_frames
              #significa que se le debe añadir algunos datos extra como son
              #las técnicas que dispone y sus parámetros auxiliándose de la 
              #estructura complete_features.
              if self.__main_features.has_key(name):
                 complete_features["features"] = self.__main_features[name]

              #Se añade el Frame a la estructura __frames, la cual será con la
              #que se controle la manipulación de éstos para que aparezcan o 
              #desaparezcan de la Ventana Principal.
              self.__frames[name] = frame_instance(self.__root,complete_features)
              
          #Por defecto se coloca el Frame correspondiente al "Home", donde 
          #estará almacenada la introducción al proyecto.
          self.__frames[self.__prior_frame_name].pack(expand = True,fill = tk.BOTH)
          
      
      def __update_frame(self,event):
          """
             .. note:: Este método es privado.

             Muestra en la Ventana Principal el Frame actual.

             :param event: El evento del elemento gráfico que 
                           activa la función.
 
             :type event: String
          """

          #De la lista que contiene las opciones de Frames se obtiene
          #el índice del seleccionado actualmente.
          selected_item = self.__settings_frame_listbox.curselection()

          #Se obtiene y adecua el índice con base en la variable
          #anterior.
          current_frame_index = int(selected_item[0])

          #Se obtiene el nombre del Frame que está asociado al índice
          #de las opciones de Frames.
          current_frame_name = self.__settings_frame_listbox.get(current_frame_index)

          #Se manda llamar a la función que hace el cambio
          #de Frame.
          self.__change_frame(current_frame_name)


      def __change_frame(self,current_frame_name):
          """
             .. note:: Este método es privado.

             Hace el cambio en la Ventana Principal ocultando un Frame y
             mostrando otro.
      
             :param current_frame_name: El Frame que se va a mostrar en 
                                        la Ventana Principal.

             :type current_frame_name: Tkinter.Frame
          """

          #Primero en la estructura que almacena los índices de los Frames
          #se obtiene el índice del Frame que se va a actualizar.
          self.__current_frame_index = self.__frames_index[current_frame_name]

          #En el menú de opciones de los Frames el que se oculta deja de seleccionarse y se coloca
          #en color blanco.
          self.__settings_frame_listbox.itemconfig(self.__prior_frame_index,selectbackground = "white")
          self.__settings_frame_listbox.itemconfig(self.__prior_frame_index,background = "white")
         
          #En el menú de opciones de los Frames el que se muestra se selecciona en color verde.
          self.__settings_frame_listbox.itemconfig(self.__current_frame_index,selectbackground = "green")
          self.__settings_frame_listbox.itemconfig(self.__current_frame_index,background = "green")
          
          #A continuación el Frame seleccionado se muestra no sin antes haber ocultado el
          #anterior.
          self.__frames[self.__prior_frame_name].pack_forget()	
          self.__frames[current_frame_name].pack(expand = True,fill = tk.BOTH) 
                    
          #Se actualizan las referencias al Frame que se oculta. 
          self.__prior_frame_index = self.__current_frame_index
          self.__prior_frame_name = current_frame_name 


      def load_mop_example(self,elements):
          """
             Carga el M.O.P **(Multi Objective Problem)** seleccionado
             a los Frames correspondientes **(Objective Functions y Decision Variables)**.
 
             :param elements: Un arreglo que contiene dos elementos, el primero son las
                              funciones objetivo precargadas mientras que el segundo son las
                              variables de decisión también precargadas. Ambas provienen del menú
                              secundario **(véase View/Additional/MenuInternalOption/InternalOptionTab/MOPExampleFrame.py,
                              Controller/XML/MOPExamples.xml)**.

             :type elements: Array   
          """

          #Se obtienen las funciones objetivo y las variables de decisión que han sido precargadas
          #en los sitios antes mencionados para ejemplificar y facilitar las pruebas al usuario.
          objective_functions = elements[0]
          decision_variables = elements[1]

          #El Frame de Objective Functions se carga con las funciones recién obtenidas.
          self.__frames["Objective Functions"].insert_mop_example(objective_functions)

          #El Frame de Decision Variables se carga con las variables y sus rangos recién
          #recolectados.
          self.__frames["Decision Variables"].insert_mop_example(decision_variables)

          #Adicional a lo anterior el Frame actualmente mostrado se renueva para que sea
          #el de Objective Functions. 
          self.__change_frame("Objective Functions")                       


      def __restore_settings(self,event):
          """
             .. note:: Este método es privado.

             Limpia y deja por defecto los valores estándar del Frame
             mostrado actualmente en la Ventana Principal.
             El método no aplica para regresar a M.O.P.'s **(Multi Objective Problems)**
             cargados anteriormente.

             :param event: El evento del elemento gráfico que acciona esta función.
        
             :type event: String
          """

          #Se busca en la lista de opciones de Frames el 
          #nombre asociado al índice actual.
          current_frame_name = self.__settings_frame_listbox.get(self.__current_frame_index)

          #Al final se busca el Frame indicado y se aplica 
          #la función de restauración.
          self.__frames[current_frame_name].restore_settings()


      def __get_information(self):
          """
             .. note:: Este método es privado.

             Método que obtiene los datos ingresados por el usuario
             de cada uno de los Frames asociados a esta Ventana Principal.

             :returns: Un diccionario con toda las preferencias del usuario recolectadas
                       para cada uno de los Frames disponibles.
             :rtype: Dictionary
          """
 
          #En este diccionario se almacenarán los datos recolectados.
          gathered_information = {}

          #Se recorren uno a uno los Frames que conforman la Ventana Principal.
          for frame in self.__frames.keys():

              #Se obtiene el Frame actual.
              current_frame = self.__frames[frame]

              #Se averigua si el Frame actual contiene el método "get_information"
              #implementado.
              invert_op = getattr(current_frame,"get_information",None) 

              #Si dicho método existe entonces se ejecuta el método para obtener
              #la información local, la cual es colocada en el diccionario de este
              #método.
              if callable(invert_op):
                 gathered_information[frame] = current_frame.get_information()
            
          #Se regresa la información en conjunto.  
          return gathered_information

          
      def __init_procedure(self,event):
          """
             .. note:: Este método es privado.

             | Inicia el procedimiento para ejecutar un M.O.E.A.
             | Los pasos que se realizan son:
             * Recolecta las preferencias ingresadas por el usuario en los Frames que conforman la Ventana Principal.
             * Se sanitizan dichos datos con ayuda del Controller.
             * En caso de no haber problemas con la sanitización, se ejecuta el proceso alojándolo en un hilo **(Thread)** para que permita seguir teniendo acceso a la Ventana Principal; por el contrario si hubo alguna falla regresa un mensaje de error.
             | Gracias a este método el proyecto entero tiene la característica de ser Multi-Hilo **(ó Multi-Threading)**, es decir,
              se pueden ejecutar varios procedimientos de manera independiente.

             :param event: El evento del elemento gráfico que activa esta función.

             :type event: String
          """      

          #Se obtienen todas las preferencias del usuario en esta variable.
          gathered_information = self.__get_information()

          #Con base en las solicitudes del usuario, estos valores son sanitizados en el Controller.
          sanitized_information = self.__controller.sanitize_settings(gathered_information,self.__main_features)

          #Si el Controller detecta al menos una anomalía en la consistencia y/o coherencia de los datos
          #devolverá un mensaje de error.
          if sanitized_information.has_key("recent"):

             #El Controller ya tiene asociada una estructura de mensajes de error, en esta
             #sección sólo se obtienen los mensajes importantes.
             #Aquí se obtiene el error completo.
             immediate_level = sanitized_information["recent"]

             #En este se obtiene el error que ha ocurrido inmediatamente.
             lower_level = sanitized_information["previous"][0]

             #En esta parte se obtiene el nombre del Frame en el que ocurrió el error.
             error_frame_name = immediate_level["frame"]

             #Para mejorar la detección de errores, se muestra en la Ventana Principal el
             #Frame en el que ocurrió el error inmediato.
             self.__change_frame(error_frame_name)

             #Finalmente se lanza el mensaje en una ventana independiente de emergencia.
             tkm.showerror("Error at {0}".format(error_frame_name),lower_level["message"])

          #En caso de que la sanitización haya resultado exitosa se procede a hacer
          #lo siguiente:
          else: 
               #Se incrementa el número de ejecución de proceso actual.
               self.__execution_task_count += 1

               #Se obtiene el número de generaciones de la estructura recién sanitizada.
               number_of_generations = sanitized_information["number_of_generations"]

               #Se crea la ventana asociada al proceso que indicará el progreso de éste
               #(véase View/Additional/GenerationSignal/GenerationSignalToplevel.py).
               current_generations_signal = GenerationSignalToplevel(self.__root,self.__path_image_logo,self.__execution_task_count)

               #Para poder eliminar la ventana asociada al proceso apropiadamente, esta se añade
               #en la estructura __stored_generations_signals.
               self.__stored_generations_signals[self.__execution_task_count] = current_generations_signal

               #Dentro de la misma estructura se inicializa el número de generaciones que tendrá el proceso y
               #se muestra en la pantalla dicha ventana.
               self.__stored_generations_signals[self.__execution_task_count].update_number_of_generations(number_of_generations)
               self.__stored_generations_signals[self.__execution_task_count].show()
               
               #A continuación se crea el hilo (Thread) que contendrá el proceso que será el encargado de ejecutar 
               #el M.O.E.A.
               current_process = hilo.Thread(target = self.__obtain_results,args = (self.__execution_task_count,self.__generations_queue,gathered_information,sanitized_information,))

               #Se inicia el hilo.
               current_process.start()
               
               #Si se trata del primer hilo en ejecutarse, activará una función que se dedicará a reviar las colas
               #(Queues) creadas para mantener control sobre los procesos y sus ventanas asociadas.
               if self.__check_queues_flag == False:
                  #Se manda llamar a la función check_queues.
                  self.__check_queues() 
                  #Para garantizar que sólo el primer hilo ejecute la función, se pone un
                  #candado a esta sección. Será desbloqueado hasta que no existan procesos
                  #corriendo.
                  self.__check_queues_flag == True
                  
          
      def __obtain_results(self,execution_task_count,generations_queue,gathered_information,sanitized_information):
          """
             .. note:: Este método es privado.

             Ejecuta un M.O.E.A.. Esta es la función que se coloca en un hilo
             para ser llevada a cabo de manera independiente con la finalidad 
             de dejar libre la Ventana Principal y de manera secundaria ejecutar
             varios procedimientos simultáneamente.
             
             :param execution_task_count: El número de proceso actual.
             :param generations_queue: Una referencia a una cola **(Queue)** donde los procesos escribirán su avance
                                       en cuanto a las generaciones transcurridas.
             :param gathered_information: La información que el usuario ingresó al momento de iniciar el proceso actual.
             :param sanitized_information: La información anterior sanitizada.

             :type execution_task_count: Integer
             :type generations_queue: Instance
             :type gathered_information: Dictionary
             :type sanitized_information: Dictionary
          """

          #Se manda llamar al método que está en Controller, la cual ejecuta un M.O.E.A.
          #En ese mismo método al final se regresan resultados los cuales se guardan en final_results.
          final_results = self.__controller.execute_procedure(execution_task_count,generations_queue,sanitized_information)

          #La función termina colocando en un queue (Cola) una terna de valores 
          #los cuales son (de izquierda a derecha):
          #El número del proceso.
          #La información que ingresó el usuario al momento de haber ejecutado el proceso actual.
          #Los resultados arrojados por el método.
          self.__results_queue.append((execution_task_count,gathered_information,final_results))
         
 
      def __check_queues(self):
          """
             .. note:: Este método es privado.

             Una vez iniciado un proceso que ejecuta un M.O.E.A., este método
             revisa periódicamente las colas **(Queues)** sobre las cuales los procesos
             escribirán todo tipo de información pertinente.
          """

          #Los elementos de __generations_queue para extraer serán tuplas
          #de tipo (proceso,generación actual). La idea es que en esta sección
          #se actualice el progreso en las ventanas asociadas a los procesos.
          #Entonces si hay elementos en la cola se hace lo siguiente:
          if self.__generations_queue:

             #Se obtiene el elemento en la cola.
             current_element = self.__generations_queue.pop()

             #El segundo elemento de la tupla corresponde a la generación actual.
             current_generation = current_element[1]
 
             #El primer elemento de la tupla se trata del número de proceso.
             current_execution_task_count = current_element[0]
        
             #Se revisa que la ventana asociada aún esté en el registro pertinente.
             if self.__stored_generations_signals.has_key(current_execution_task_count):

                #Si la identificación es positiva se actualiza ésta con el número 
                #de generación obtenido en la cola.
                status_code = self.__stored_generations_signals[current_execution_task_count].update_current_generation(current_generation)

                #Si se regresa un código 1 (véase View/Additional/GenerationSignal/GenerationSignal.py) 
                #significa que de alguna manera u otra el método en el proceso ha llegado a su fin, 
                #por lo que la ventana asociada debe cerrarse.
                if status_code == 1:
                   self.__stored_generations_signals[current_execution_task_count].close()

          #Los elementos de __results_queue albergarán los datos necesarios para poder
          #construir las gráficas. Se trata de una terna que consta de los siguientes
          #datos (de derecha a izquierda):
          #El número del proceso.
          #La información que ingresó el usuario al momento de haber ejecutado el proceso actual.
          #Los resultados arrojados por el método.
          #Entonces si hay elementos en la cola se hace lo siguiente:
          if self.__results_queue:
             #Se obtiene el elemento de la cola.
             current_element = self.__results_queue.pop()

             #El primer elemento es el número de proceso.
             current_execution_task_count = current_element[0]

             #El segundo elemento es la información que ingresó el usuario.
             current_gathered_information = current_element[1]

             #El tercer elemento son los resultados que arrojó el método envuelto 
             #en el proceso.
             current_final_results = current_element[2]

             #Dado que ya se devolvieron los resultados, aquí se elimina directamente
             #la ventana asociada al proceso.
             del self.__stored_generations_signals[current_execution_task_count]   

             #Finalmente, los resultados son graficados en una ventana independiente
             #(véase View/Additional/ResultsGrapher/ResultsGrapherToplevel.py).
             result_grapher = ResultsGrapherToplevel(self.__root,self.__path_image_logo,current_execution_task_count,self.__main_features,current_gathered_information,current_final_results)
                   
          #Mientras las ventanas asociadas a los procesos sigan "vivas",
          #se seguirá ejecutando este mismo método cada 10 milisegundos.
          if self.__stored_generations_signals != {}:
             self.__root.after(10,self.__check_queues)

          #Si ya no queda ninguna ventana asociada "viva" entonces el
          #método ya no se ejecuta y además se desbloquea el candado usado para el método
          #__init_procedure().
          else:
             self.__check_queues_flag == False
          

      def run(self):
          """
             Lanza la Ventana Principal.
          """
            
          #Con este comando se muestra la Ventana Principal.
          self.__root.mainloop()
