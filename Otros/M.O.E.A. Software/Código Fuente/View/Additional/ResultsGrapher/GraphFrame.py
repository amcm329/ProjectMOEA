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
#Aunque no se usa FileDialog, se importa para que  el programa funcione en sistemas 
#operativos Windows.
import FileDialog

import matplotlib
#La siguiente línea de código sirve para eliminar el modo depurador de la biblioteca
#que enlaza Tkinter con Matplotlib
matplotlib.use("TkAgg",warn = False)

from matplotlib.figure import Figure
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from CustomNavigationToolbar2TkAgg import CustomNavigationToolbar2TkAgg


class GraphFrame(tk.Frame):
      """
         Proporciona un Frame que contiene gráficas alimentadas por los resultados obtenidos
         al ejecutar algún MOEA, el cual ha sido refinado por las configuraciones
         recabadas de la Ventana Principal **(véase Model/MOEA)**.

         :param parent: Frame padre al que pertenece.
         :param execution_task_count: Número que indica el actual Task en ejecución.
         :param objective_functions: Lista que contiene las funciones objetivo renombradas.
         :param decision_variables: Lista que contiene las variables de decisión renombradas.
         :param final_results: Diccionario que contiene la información para graficar. Se divide en dos categorías principales:
                               Frente de Pareto y Mejor Individuo por Generación.
                
         :type parent: Tkinter.Frame
         :type execution_task_count: Integer
         :type objective_functions: List
         :type decision_variables: List
         :type final_results: Dictionary
         :returns: Tkinter.Frame
         :rtype: Instance
      """
      
      def __init__(self,parent,execution_task_count,objective_functions,decision_variables,final_results):

          #Se crea el Frame sobre el cual se colcoarán todos los elementos gráficos.
          tk.Frame.__init__(self,parent,bd = 4,relief = "groove")
          
          #Primero que nada es importante mencionar que habrán dos categorías de gráficas principales:
          #las concernientes a las funciones objetivo y las que tienen que ver con variables de decisión.
          #El número de gráficas de cada categoría dependerá de ciertas condiciones que se muestran posteriormente.
          #Así, en todo el Frame habrán 3 secciones:
          #La primera es la sección donde habrán botones de selección (Checkbuttons) para poder intercalar las
          #categorías de funciones objetivo y variables de decisión.
          #La segunda es la seccción del OptionMenu, esto significa que, por cada categoría principal elegida mediante
          #los checkbuttons, puede darse el caso de que exista más de una gráfica de manera interna, por ello la sección
          #OptionMenu despliega un listado en el cual se colocan todas las gráficas posibles de una misma categoría.
          #Finalmente la tercera sección constituye la parte en la que se muestran las gráficas, esta porción de espacio
          #es controlada por los elementos de las secciones anteriores.
          #Entonces se declaran los Frames correspondientes a la primera y segunda sección.
          self.__checkbutton_frame = tk.Frame(self)
          self.__option_menu_frame = tk.Frame(self)

          #Con respecto del tipo de gráficas que se mostrarán, se enlistan de acuerdo a la categoría principal:
          #Funciones objetivo: frente de Pareto y el mejor Individuo por generación.
          #Variables de decisión: óptimo de Pareto y el mejor Individuo por generación.

          #Para indagar más en los conceptos frente de Pareto y óptimo de Pareto se recomienda leer simultáneamente el trabajo
          #escrito (no confundir con la documentación del programa).

          #Entonces por cada tipo de gráfica se declaran los colores y leyendas con los que se identificarán los puntos graficados:
          #Para el caso del mejor Individuo por generación (independientemente de la categoría) se toman los valores 
          #"variables" y "functions", para el óptimo de Pareto se toma "optimal", mientras que el resto son para el frente de Pareto.
          #A petición de la Dra. Katya Rodríguez Vázquez el complemento de Pareto no será mostrado, esto significa que
          #el método que provee la información (en Model/Community/Community.py) no incluirá dicha parte, sin embargo se mantienen
          #presentes las características visuales relativas al complemento por si en algún momento el usuario desea utilizarlas.
          self.__color = {
                          "variables":'b',
                          "functions":'r',
                          "front": 'r',
                          "optimal": 'g',
                          "complement": 'b',
                         }

          #La leyenda permite agregar a las gráficas el tipo de valor que se está graficando para así facilitar la comprensión
          #al usuario.
          self.__legend = {
                           "variables": "Best Value per Generation",
                           "functions": "Best Value per Generation",
                           "front": "Pareto Front",
                           "optimal": "Pareto Optimal",
                           "complement": "Pareto Complement"
                          }

          #Se declaran tipografías para las secciones de los Checkbuttons y los OptionMenus.
          checkbutton_font = tkf.Font(family = "Helvetica",size = 11,weight = "bold")
          option_menu_font = tkf.Font(family = "Helvetica",size = 11,weight = "bold")
          
          #Se guarda una referencia al Frame Padre.
          self.__parent = parent
          
          #Se almacena el número de Task.
          self.__execution_task_count = execution_task_count

          #Se obtiene la información principal arrojada por la ejecución de algún MOEA.
          #Se mencionó que contiene dos secciones principales, una es el mejor Individuo por generación y
          #el otro es el frente de Pareto (incluido el óptimo de Pareto).
          #En realidad por cada sección hay 2 estructuras: una lista que le corresponde a las variables de 
          #decisión y otra que tiene que ver con las funciones objetivo, así se puede elegir más rápidamente
          #el tipo de información para poder graficar.
          self.__final_results = final_results

          #Se guarda una referencia a la gráfica actual (sin importar la categoría o información que contenga).
          #Aquí se debe hacer hincapié en el hecho de que si se desea crear más de una gráfica independiente y
          #colocarlas en el mismo Frame, va a arrojar un error de programación ya que Matplotlib (la biblioteca 
          #de Python para crear gráficas) no permite este tipo de operaciones independientes. Por ello es que
          #se guarda la gráfica en un Canvas, ya que esta estructura se puede proliferar de manera independiente.
          #Así, los conceptos de gráfica y Canvas se referirán a la primera siendo almacenada en la segunda.
          self__current_canvas = ""
          
          #Aquí se guardan referencias a todos los posibles Canvas que se crean para la categoría de las funciones
          #objetivo, también se guardan referencias a la función objetivo actual seleccionada y su 
          #correspondiente listado (OptionMenu) que se materializará en caso de que haya más de 3 funciones objetivo.
          self.__objective_functions_canvas = {} 
          self.__objective_functions_canvas_list = [] 
          self.__current_objective_function_name = ""
          self.__objective_functions_option_menu = ""
          
          #Aquí se guardan referencias a todos los posibles Canvas que se crean para la categoría de las variables 
          #de decisión, también se guardan referencias a la variable de decisión actual seleccionada y su 
          #correspondiente listado (OptionMenu) que se materializará en caso de que haya más de 3 variables de decisión.
          self.__decision_variables_canvas = {}
          self.__decision_variables_canvas_list = []
          self.__current_decision_variable_name = ""
          self.__decision_variables_option_menu = ""
          
          #Si bien se menciona que hay dos tipos de gráficas, éstas no estarán siempre disponibles en todo momento, 
          #Para fines de este trabajo de tesis, la disección ocurre de la siguiente manera: si hay una función objetivo
          #se graficará esa función vs generación; en otro caso se graficarán las funciones F1,...,Fk para obtener el frente de 
          #Pareto.
          #Para el caso de las variables de decisión el caso es muy similar, con la salvedad de que en caso de que haya más de una 
          #variable de decisión, se graficarán las variables V1,...,Vk para obtener el óptimo de Pareto.
          #Nótese que en estos casos estamos tomando las variables y funciones renombradas, pero dado que las información
          #de final_results viene en el mismo orden en el que las funciones y variables fueron ingresadas por el usuario, 
          #sólo basta con fijarnos en la posición de la información para hacer un enlace automático entre los datos renombrados
          #y la información final.

          #Para el caso de las funciones objetivo se extraen diferentes datos según el número de éstas.
          if len(objective_functions) > 1: 
             self.__create_objective_functions_canvas(objective_functions,final_results["objective_functions"]["pareto"])
              
          else:
             self.__create_objective_functions_canvas(objective_functions,final_results["objective_functions"]["best individual"])
              
          #Ahora se hace lo mismo para las variables de decisión.
          if len(decision_variables) > 1: 
             self.__create_decision_variables_canvas(decision_variables,final_results["decision_variables"]["pareto"]) 

          else:
             self.__create_decision_variables_canvas(decision_variables,final_results["decision_variables"]["best individual"])

          #Una vez creadas las gráficas se actualizan los listados de Canvas y la función
          #objetivo actual
          self.__objective_functions_canvas_list = self.__objective_functions_canvas.keys()
          self.__current_objective_function_name = self.__objective_functions_canvas_list[0]
                          
          #Lo mismo ocurre para los Canvas y su variable de decisión actual.    
          self.__decision_variables_canvas_list = self.__decision_variables_canvas.keys()
          self.__current_decision_variable_name = self.__decision_variables_canvas_list[0]
          
          #Se coloca un Canvas por defecto (que será siempre un elemento de las funciones objetivo).
          self.__current_canvas = self.__objective_functions_canvas[self.__current_objective_function_name]
          
          #Las siguientes variables permiten tener un control de las elecciones que se susciten en
          #las secciones de los Checkbuttons y los OptionMenus. Esto con el fin de poder actualizar apropiadamente
          #cada elemento gráfico.
          self.__variable_checkbutton = tk.IntVar(self)       
          self.__variable_option_menu = tk.StringVar(self.__checkbutton_frame)

          #A continuación en la sección Checkbutton se crea el elemento que identificará la selección
          #para la categoría de las funciones objetivo, también se le da formato.
          #Asímismo la categoría de las funciones objetivo es elegida como la seleccionada por defecto.
          self.__objective_functions_checkbutton = tk.Checkbutton(self.__checkbutton_frame,text = "Objective Functions",variable = self.__variable_checkbutton,onvalue = 0,offvalue = 1,command = self.__change_canvas_category)
          self.__objective_functions_checkbutton["font"] = checkbutton_font
          self.__objective_functions_checkbutton.select()

          #A continuación en la sección Checkbutton se crea el elemento que identificará la selección
          #para la categoría de las variables de decisión, también se le da formato.
          self.__decision_variables_checkbutton = tk.Checkbutton(self.__checkbutton_frame,text = "Decision Variables",variable = self.__variable_checkbutton,onvalue = 1,offvalue = 0,command = self.__change_canvas_category)
          self.__decision_variables_checkbutton["font"] = checkbutton_font

          #Entonces ambos Checkbuttons se colocan en el Frame.
          self.__objective_functions_checkbutton.grid(row = 0,column = 0,padx = (1,40),pady = 13,sticky = tk.E)
          self.__decision_variables_checkbutton.grid(row = 0,column = 1,padx = (40,1),pady = 13,sticky = tk.W)
          
          #Se recordará que los OptionMenus sirven para mostrar un listado de de gráficas disponibles cuando existan más de 3 funciones
          #o variables.
          #En la siguiente secuencia se identifica esta condición para crear de manera procedural el OptionMenu relativo a cada 
          #categoría principal. En este caso se construye el OptionMenu para las funciones objetivo.
          if len(objective_functions) > 3:

             #A continuación se crea un OptionMenu que se carga con los identificadores de las gráficas extra, también se le añade
             #una función que cambiará de manera interna el Canvas.
             #Finalmente se le da formato al listado y se coloca en el Frame correspondiente.
             self.__objective_functions_option_menu = tk.OptionMenu(self.__option_menu_frame,self.__variable_option_menu,*self.__objective_functions_canvas_list,command = self.__change_inner_canvas)
             self.__objective_functions_option_menu["font"] = option_menu_font
             self.__variable_option_menu.set(self.__current_objective_function_name)
             self.__objective_functions_option_menu.grid(row = 1,column = 0,pady = (1,13),sticky = tk.S + tk.N)

          #Toca el turno a las variables de decisión para crear el OptionMenu correspondiente.
          if len(decision_variables) > 3:

             #A continuación se crea un OptionMenu que se carga con los identificadores de las gráficas extra, también se le añade
             #una función que cambiará de manera interna el Canvas.
             #Finalmente se le da formato al listado y se coloca en el Frame correspondiente.
             self.__decision_variables_option_menu = tk.OptionMenu(self.__option_menu_frame,self.__variable_option_menu,*self.__decision_variables_canvas_list,command = self.__change_inner_canvas)
             self.__decision_variables_option_menu["font"] = option_menu_font

             #Esta sección de código notifica al Frame que, a menos que exista ya el OptionMenu de las funciones objetivo,
             #no deberá colocarse éste OptionMenu. Esto significa que el OptionMenu de las funciones objetivo es el designado
             #por defecto.
             if self.__objective_functions_option_menu == "":
                self.__variable_option_menu.set(self.__current_decision_variable_name)
                self.__decision_variables_option_menu.grid(row = 1,column = 0,pady = (1,13),sticky = tk.S + tk.N)

          #Ocurre un efecto muy curioso al momento de usar Canvas, cuando se crea uno, se le indique o no, siempre
          #terminará adjuntádose al Frame principal; ésto ocasiona serios problemas de visualización de datos, por ello
          #es que todos salvo el que estaba por defecto se desactivan visualmente.
          #Primero toca el turno a las variables de decisión.
          for decision_variable_canvas in self.__decision_variables_canvas_list:
              current_decision_variable_canvas = self.__decision_variables_canvas[decision_variable_canvas]

              #La acción original que corresponde al botón para guardar la gráfica está obsoleta,
              #de modo que se actualiza la función que se encarga de esta acción con una que
              #se creó específicamente para este tipo de archivos (gráficas).   
              #Dado que no en todos los sistemas operativos se puede realizar esta acción, se coloca en
              #un bloque try-catch para evitar que el programa falle.
              #Se comenta porque aunque ya se encontró una manera distinta (y más poderosa) de realizarlo (en CustomNavigationToolbar2TkAgg.py),
              #no deja de ser una opción que no se encuentra implementada en las fuentes consultadas.
              #Es importante aclarar que esta función se lleva a cabo en sistemas GNU/Linux.
              #
              #current_decision_variable_canvas[1].bsave.configure(command = lambda: self.custom_save_figure_linux(current_decision_variable_canvas[0],"decision_variable"))
                      
              #Las siguientes líneas de código modifican las opciones asociadas a una barra de herramientas.
              #Esto se realiza cambiando la tupla de opciones por los valores que se deseen recordando que
              #en tupla (1,2,3,4):
              # tupla(1) = Nombre del elemento.
              # tupla(2) = Título que llevará la ventana asociada al elemento.
              # tupla(3) = Nombre de la imagen asociada al elemento.
              # tupla(4) = Nombre de la función asociada al elemento.
              #
              #Esta opción se lleva a cabo en sistemas operativos Windows.
              #
              #custom_toolitems = []
              #for x in range (8):
              #    custom_toolitems.append(current_decision_variable_canvas[1].toolitems[x])
              #               
              #custom_toolitems.append((u"Save",u"Save the figure",u"filesave","custom_save_figure_windows"))
              #custom_tooitems = tuple(custom_toolitems)
              #
              #current_decision_variable_canvas[1].toolitems = custom_toolitems
              #    
              #Esta función actualiza los valores de los elementos de la barra de navegación.
              #current_decision_variable_canvas[1]._init_toolbar()
                  
              #Se guardan los canvas (con sus respectivas barras de navegación) de todas
              #las gráficas, ya que las que se mostrarán por defecto serán las de las funciones
              #objetivo.
              current_decision_variable_canvas[1].pack_forget()
              current_decision_variable_canvas[0]._tkcanvas.pack_forget()

          #Ahora corresponde a las funciones objetivo, donde se desactivan todos menos el que está por defecto.
          for objective_function_canvas in self.__objective_functions_canvas_list:
              current_objective_function_canvas = self.__objective_functions_canvas[objective_function_canvas]
             
              #La acción original que corresponde al botón para guardar la gráfica está obsoleta,
              #de modo que se actualiza la función que se encarga de esta acción con una que
              #se creó específicamente para este tipo de archivos (gráficas).
              #Dado que no en todos los sistemas operativos se puede realizar esta acción, se colocan las instrucciones
              #necesarias para hacer las modificaciones pertinentes. Si bien ya se ha encontrado una manera más poderosa
              #de llevar a cabo esta acción (en CustomNavitagionToolbar2TkAgg.py) se dejan estas opciones comentadas
              #ya que hasta el momento son otras formas de resolver el mismo problema cuya construcción se realizó casi
              #sin apoyo ya que existe poca documentación al respecto.
              #La instrucción que se coloca a continuación se utiliza para cambiar el comportamiento del
              #botón en un sistema operativo GNU/Linux.
              #
              #current_objective_function_canvas[1].bsave.configure(command = lambda: self.custom_save_figure_linux(current_objective_function_canvas[0],"objective_function"))

              #Las siguientes líneas de código modifican las opciones asociadas a una barra de herramientas.
              #Esto se realiza cambiando la tupla de opciones por los valores que se deseen recordando que
              #en tupla (1,2,3,4):
              # tupla(1) = Nombre del elemento.
              # tupla(2) = Título que llevará la ventana asociada al elemento.
              # tupla(3) = Nombre de la imagen asociada al elemento.
              # tupla(4) = Nombre de la función asociada al elemento.
              #
              #La instrucción mostrada a continuación es usada para modificar el comportamiento antes mencionado
              #en un sistema operativo Windows. 
              #
              #custom_toolitems = []
              #for x in range (8):
              #    custom_toolitems.append(current_objective_function_canvas[1].toolitems[x])
                              
              #custom_toolitems.append((u"Save",u"Save the figure",u"filesave","custom_save_figure_windows"))
              #custom_tooitems = tuple(custom_toolitems)

              #current_objective_function_canvas[1].toolitems = custom_toolitems
                  
              #Esta función actualiza los valores de los elementos de la barra de navegación.
              #current_objective_function_canvas[1]._init_toolbar()

              #Se guardan casi todos los canvas (con sus respectivas barras de herramientas)
              #excepto el que se va a mostrar inicialmmente, esto para las funciones objetivo.
              if objective_function_canvas != self.__current_objective_function_name:    
                 current_objective_function_canvas[1].pack_forget()
                 current_objective_function_canvas[0]._tkcanvas.pack_forget()

          #Las siguientes opciones permiten centrar apropiadamente los Checkbuttons haciendo
          #un traslape de las columnas 0 y 1.
          self.__checkbutton_frame.grid_columnconfigure(0,weight = 1)
          self.__checkbutton_frame.grid_columnconfigure(1,weight = 1)     

          #La siguiente opción permite centrar los OptionMenu (si los hay), haciendo 
          #un traslape de la columna 0.
          self.__option_menu_frame.grid_columnconfigure(0,weight = 1)  

          #Se colocan los Frames relativos a Checkbuttons y OptionMenus en el Frame principal.
          self.__checkbutton_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True)
          self.__option_menu_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True)

          #Se actualiza el Canvas en la sección correspondiente del Frame principal.
          self.__change_canvas_category()
         

      def __create_objective_functions_canvas(self,objective_functions,collection_points):
          """
             .. note:: Este método es privado.

             Crea los Canvas para las funciones objetivo.

             :param objective_functions: Lista que contiene las funciones objetivo renombradas.
             :param collection_points: Diccionario que contiene los valores de las funciones objetivo
                    de todos los Individuos en la Población final.
                
             :type objective_functions: List
             :type collection_points: Dictionary
          """

          #Cuando se refiere a un Canvas en realidad se habla de dos elementos:
          #un Canvas y un NavigationToolBar, el segundo permite añadir opciones extra al Canvas
          #(y por lo tanto a la gráfica) tales como guardar el elemento, zoom, principalmente.
          #
          #Se crea la etiqueta que tendrán todas las imágenes de funciones objetivo por
          #defecto.
          image_text = "objective_functions"
          
          #La creación de un Canvas dependerá del número de funciones objetivo existentes.
          length_objective_functions = len(objective_functions)          

          #Si sólo hay una función objetivo se hará una gráfica Función vs Generación.
          if length_objective_functions == 1:
                
             #Se crean las etiquetas que llevará la gráfica.
             first_function = "Generations"
             second_function = objective_functions[0]

             #Este título servirá como la llave para el contenedor de Canvas de funciones objetivos.
             title = first_function + " vs " + second_function

             #Se crea una gráfica en dos dimensiones que estará contenida en un Canvas..
             canvas = self.__create_2d_canvas(first_function,0,second_function,1,collection_points)
   
             #Al Canvas se le añade su respectiva Barra de Navegación personalizada.
             toolbar = CustomNavigationToolbar2TkAgg(canvas,self,self.__parent,self.__execution_task_count,image_text)
             
             #Finalemente se agrega la tupla (canvas,barra de navegación) usando el título como llave.
             self.__objective_functions_canvas[title] = (canvas,toolbar)

          #Si hay 3 funciones objetivo  se hace una gráfica en tres dimensiones que estará contenida en 
          #un Canvas.
          elif length_objective_functions == 3:
               #Se toma la nomenclatura de las 3 funciones.
               first_function = objective_functions[0] 
               second_function = objective_functions[1]
               third_function = objective_functions[2]

               #Se crea el título que servirá como llave para poder almacenar su respectivo Canvas.
               title = first_function + " vs " + second_function + " vs " + third_function  

               #Se crea un Canvas de tres dimensiones.
               canvas = self.__create_3d_canvas(first_function,0,second_function,1,third_function,2,collection_points)

               #Se crea la Barra de Navegación personalizada aunada a dicho Canvas.
               toolbar = CustomNavigationToolbar2TkAgg(canvas,self,self.__parent,self.__execution_task_count,image_text)

               #Finalmente a la estructura pertinente se le agrega la tupla (canvas, barra de navegación).
               self.__objective_functions_canvas[title] = (canvas,toolbar)

          #Si hay dos funciones se crea un Canvas con ambos F1 y F2, pero si hay más de 3 funciones 
          #se van creando Canvas de dos dimensiones con las funciones tomadas dos a dos sin repetición.          
          elif length_objective_functions == 2 or length_objective_functions > 3:

               #Se toma un iterador que va recorriendo las funciones objetivo.
               for x in range (length_objective_functions):
                   for y in range(x,length_objective_functions):

                       #Con esto se evita que se grafiquen Fk con Fk
                       if x != y: 

                          #Se toma la nomenclatura de la primera y segunda funciones.
                          first_function = objective_functions[x] 
                          second_function = objective_functions[y]
 
                          #A continuación se crea el título que servirá como llave para poder
                          #identificar a su Canvas.      
                          title = first_function + " vs " + second_function

                          #Se crea el Canvas en dos dimensiones.
                          canvas = self.__create_2d_canvas(first_function,x,second_function,y,collection_points)
                               
                          #Se crea una Barra de Navegación (personalizada) anexada al Canvas.
                          toolbar = CustomNavigationToolbar2TkAgg(canvas,self,self.__parent,self.__execution_task_count,image_text)

                          #Finalmente se agrega a la estructura correspondiente la tupla (canvas, barra de navegación)
                          #usando el título como llave.
                          self.__objective_functions_canvas[title] = (canvas,toolbar)

         
      def __create_decision_variables_canvas(self,decision_variables,collection_points):
          """
             .. note:: Este método es privado

             Crea los Canvas para las variables de decisión.

             :param decision_variables: Lista que contiene las variables de decisión renombradas.
             :param collection_points: Diccionario que contiene los valores de las funciones objetivo
                    de todos los Individuos en la Población final.
                
             :type decision_variables: List
             :type collection_points: Dictionary
          """

          #Cuando se refiere a un Canvas en realidad se habla de dos elementos:
          #un Canvas y un NavigationToolBar, el segundo permite añadir opciones extra al Canvas
          #(y por lo tanto a la gráfica) tales como guardar el elemento, zoom, principalmente.
          #
          #Primero se establece el nombre que tendrán por defecto las imágenes asociadas a las gráficas
          #de esta categoría.
          image_text = "decision_variables"
          
          #La creación de un Canvas dependerá del número de variables de decisión existentes.
          length_decision_variables = len(decision_variables)

          #Si hay una sóla variable de decisión se grafica Variable vs Generaciones.
          if length_decision_variables == 1:

             #Se crean las etiquetas para la gráfica.
             first_variable = "Generations"
             second_variable = decision_variables[0] 

             #Se erige un título que servirá para identificar al actual Canvas en 
             #la estructura de Canvas de variables de decisión.
             title = first_variable + " vs " + second_variable

             #Se realiza la gráfica en dos dimensiones.
             canvas = self.__create_2d_canvas(first_variable,0,second_variable,1,collection_points)

             #Se crea una Barra de Navegación personalizada que irá atada al actual Canvas.
             toolbar = CustomNavigationToolbar2TkAgg(canvas,self,self.__parent,self.__execution_task_count,image_text)

             #Se agrega la tupla (canvas, barra de navegación) que irá 
             #identificada con el título antes creado.
             self.__decision_variables_canvas[title] = (canvas,toolbar)
                                    
          #Si hay 3 variables de decisión se crea una gráfica en 3 dimensiones.
          elif length_decision_variables == 3:
               #Se toman los nombres de las variables de decisión.
               first_variable = decision_variables[0] 
               second_variable = decision_variables[1]
               third_variable = decision_variables[2]

               #Se crea un título con el que se identificará al Canvas dentro de la estructura
               #que junta los Canvas de variables de decisión.
               title = first_variable + " vs " + second_variable + " vs " + third_variable

               #Se crea el Canvas en 3 dimensiones.     
               canvas = self.__create_3d_canvas(first_variable,0,second_variable,1,third_variable,2,collection_points)

               #Se construye la Barra de Navegación (personalizada) que irá anexada al actual Canvas.
               toolbar = CustomNavigationToolbar2TkAgg(canvas,self,self.__parent,self.__execution_task_count,image_text)

               #Finalmente en la estructura indicada se agrega la tupla (canvas, barra de navegación), la cual
               #tendrá al título como su llave.
               self.__decision_variables_canvas[title] = (canvas,toolbar)
               
          #Si hay dos variables se crea un Canvas con ambos V1 y V2, pero si hay más de 3 vaiables 
          #se van greando Canvas de dos dimensiones con las variables tomadas dos a dos sin repetición.          
          elif length_decision_variables == 2 or length_decision_variables > 3:

               #La siguiente sentencia de control permite ir tomando los elementos de la
               #lista de variables de decisión y comparar la lista consigo misma.
               for x in range (length_decision_variables):
                  for y in range(x,length_decision_variables):
                       
                      #Con esto se evita graficar elementos del estilo Vk vs Vk.
                      if x != y: 
                         #Se toman los nombres de las variables.
                         first_variable = decision_variables[x] 
                         second_variable = decision_variables[y]

                         #A continuación se hace un título que servirá como referencia para identificar
                         #al Canvas actual.
                         title = first_variable + " vs " + second_variable

                         #Se crea el Canvas en dos dimensiones.
                         canvas = self.__create_2d_canvas(first_variable,x,second_variable,y,collection_points)

                         #Se crea la Barra de Navegación personalizada concerniente al Canvas actual.
                         toolbar = CustomNavigationToolbar2TkAgg(canvas,self,self.__parent,self.__execution_task_count,image_text)

                         #En la estructura correspondiente se agregan la tupla (canvas, barra de navegación),
                         #usando el título previamente creado como llave.
                         self.__decision_variables_canvas[title] = (canvas,toolbar)
          

      def __create_2d_canvas(self,x_label,x_index,y_label,y_index,collection_points):
          """
             .. note:: Este método es privado.

             Crea una gráfica en 2 dimensiones que es envuelta en un Canvas.
             
             :param x_label: Nombre para el eje X de la gráfica. 
             :param x_index: Posición dentro de collection_points para los datos del eje X. 
             :param y_label: Nombre para el eje Y de la gráfica.  
             :param y_index: Posición dentro de collection_points para los datos del eje Y.
             :param collection_points: Diccionario que contiene los puntos a graficar.
   
             :type x_label: String
             :type x_index: Integer
             :type y_label: String
             :type y_index: Integer
             :type collection_points: Dictionary
             :returns: Canvas
             :rtype: matplotlib.backends.backend_tkagg.FigureCanvasTkAgg            
          """

          #Estructura para almacenar algunos puntos de muestra para obtener la leyenda.
          figure_points = []

          #Se crea la gráfica (Figure es una forma genérica de crear una gráfica).
          figure = Figure()

          #Se crea el Canvas Asociado a Figure.
          canvas = FigureCanvasTkAgg(figure,self)

          #Figure_legend será un espacio en el que se colocará la leyenda (coloración de los elementos de la gráfica
          #y su significado). Por otro lado, figure_graph es el espacio en el que se colocarä la gráfica. Entonces
          #se reserva el espacio para ambas secciones.
          figure_legend = figure.add_axes([0.134, 0.92, 0.775, 0.08],frameon = True)
          figure_graph = figure.add_axes([0.134, 0.14, 0.775, 0.69],frameon = True)

          #La graficación funciona por categorías, es decir, collection_points tiene a su vez subcategorías que a su vez contienen
          #listas de coordenadas. Esto es, hay una lista de coordenadas para X y una lista de coordenadas para Y, nuevamente por cada
          #subcategoría. Así, se recorren las subcategorías en el siguiente ciclo, y por cada una de éstas, se grafican las listas en X
          #e Y.
          for element_type in collection_points.keys():
              #Se toman los puntos de cada subcategoría.
              points = collection_points[element_type]
 
              #Se grafican los puntos, añadiendo el color que se tenía de acuerdo a las opciones 
              #que se especificaron al inicio de la clase.
              figure_graph.scatter(points[x_index],points[y_index],color = self.__color[element_type])

              #Se añade la información de leyenda para la sección correspondiente.
              current_element = figure_legend.scatter(points[0],points[1],color = self.__color[element_type],label = self.__legend[element_type])
              figure_points.append(current_element)

          #Se coloca la sección gráfica para la leyenda,         
          figure_legend.set_axis_off()
          figure_legend.legend(loc = "center",bbox_to_anchor = (0.5, -0.05),fancybox = True,shadow = True,ncol = len(collection_points.keys()),scatterpoints = 3)

          #Se coloca la gráfica. 
          figure_graph.set_xlabel(x_label,horizontalalignment = "center",size = 18,rotation = 0)
          figure_graph.set_ylabel(y_label,horizontalalignment = "right",size = 18,rotation =  0) 
          figure_graph.grid(True)

          #Se eliminan algunos datos residuales en la leyenda.
          for element in figure_points:
              element.remove()

          return canvas

               
      def __create_3d_canvas(self,x_label,x_index,y_label,y_index,z_label,z_index,collection_points):
          """
             .. note:: Este método es privado.

             Crea una gráfica en 3 dimensiones que es envuelta en un Canvas.
             
             :param x_label: Nombre para el eje X de la gráfica. 
             :param x_index: Posición dentro de collection_points para los datos del eje X.
             :param y_label: Nombre para el eje Y de la gráfica.  
             :param y_index: Posición dentro de collection_points para los datos del eje Y.
             :param z_label: Nombre para el eje Z de la gráfica.  
             :param z_index: Posición dentro de collection_points para los datos del eje Z.   
             :param collection_points: Diccionario que contiene los puntos a graficar.
   
             :type x_label: String
             :type x_index: Integer
             :type y_label: String
             :type y_index: Integer
             :type z_label: String
             :type z_index: Integer
             :type collection_points: Dictionary
             :returns: Canvas
             :rtype: matplotlib.backends.backend_tkagg.FigureCanvasTkAgg       
          """
         
          #Los siguientes elementos sirven para almacenar muestras de puntos y sus respectivas leyendas.
          points_legend = []
          labels_legend = []

          #Se crea un Figure (es una estructura más general para una gráfica).
          figure = Figure()

          #Se crea el Canvas, en el cual se incluirá el Figure.
          canvas = FigureCanvasTkAgg(figure,self)

          #Se crea una gráfica especial en 3d que será incluida en el Figure. Esto es porque la gráfica en 3d se moverá conforme
          #el usuario arrastre su contenido.
          figure_graph = Axes3D(figure)

          #La graficación funciona por categorías, es decir, collection_points tiene a su vez subcategorías que a su vez contienen
          #listas de coordenadas. Esto es, hay una lista de coordenadas para X, una para Y y una para Z, nuevamente por cada
          #subcategoría. Así, se recorren las subcategorías en el siguiente ciclo, y por cada una de éstas, se grafican las listas en X,
          # Y e Z.
          for element_type in collection_points.keys():

              #Primero se obtienen los puntos de una subcategoría dada.
              points = collection_points[element_type]

              #A continuación se realiza la graficación de todos los puntos para los 3 ejes.
              current_graph = figure_graph.scatter(points[x_index],points[y_index],points[z_index],c = self.__color[element_type])
             
              #Se agregan puntos de muestra para poder construir la leyenda.
              points_legend.append(matplotlib.lines.Line2D([0],[0],linestyle = "none",c = self.__color[element_type],marker = 'o'))
             
              #Se agregan las etiquetas de la leyenda.
              labels_legend.append(self.__legend[element_type])

          #Se agrega una leyenda a la gráfica con las muestras de los puntos y las etiquetas recolectadas.
          figure_graph.legend(points_legend,labels_legend,loc = 9,fancybox = True,shadow = True,ncol = len(collection_points.keys()),numpoints = 3)

          #Se colocan los nombres para los ejes X,y e Z.
          figure_graph.set_xlabel(x_label,horizontalalignment = "center",size = 18)
          figure_graph.set_ylabel(y_label,horizontalalignment = "center",size = 18)
          figure_graph.set_zlabel(z_label,horizontalalignment = "center",size = 18)  
 
          return canvas


      def __change_canvas_category(self):
          """
             .. note:: Este método es privado.

             Realiza el cambio de Canvas de la categoría de funciones objetivo 
             a la de variables y decision y viceversa, tomando en cuenta factores como por
             ejemplo si alguna de las dos categorías tiene un OptionMenu asociado **(para entonces
             colocarlo apropiadamente)** e identificando siempre el último Canvas seleccionado de 
             la categoría anterior para que cuando sea oportuno se vuelva a colocar.
          """

          #Las siguientes variables hacen referencia al OptionMenu actual y anterior
          #(si existen), así como al último Canvas seleccionado. Se declaran así para
          #que no exista distinción entre categorías y siempre se haga un cambio de 
          #forma genérica sin distinción alguna.
          prior_option_menu = ""
          current_option_menu = "" 
          current_variable_option_menu = ""

          #La siguiente variable contiene la elección hecha por el usuario
          #para cambiar de categoría.
          selected_variable_checkbutton = self.__variable_checkbutton.get()

          #Dado que un Canvas en realidad consta del Canvas y su barra de navegación
          #se desactivan entonces tales elementos actuales.

          #Aquí se desactiva la barra de navegación.
          self.__current_canvas[1].pack_forget()

          #Aquí se desactiva el Canvas.
          self.__current_canvas[0]._tkcanvas.pack_forget()

          #Si el usuario seleccionó la casilla de la función objetivo, significa que se 
          #van a actualizar las variables descritas en un principio, siendo las variables
          #antiguas aquéllas que tengan que ver con las variables de decisión y las actuales
          #con las funciones objetivo.
          if selected_variable_checkbutton == 0:
             prior_option_menu = self.__decision_variables_option_menu
             current_option_menu = self.__objective_functions_option_menu
             current_variable_option_menu = self.__current_objective_function_name
       
             #Se actualiza la variable current_canvas a la última que se eligió en la categoría de las
             #funciones objetivo.
             self.__current_canvas = self.__objective_functions_canvas[self.__current_objective_function_name]

          #Ahora en el caso contrario, si el usuario seleccionó la casilla de la variable de decisión,
          #de nueva cuenta se actualizarán las variables descritas al principio, sólo que ahora las actuales
          #serán las de variables de decisión, mientras que las antiguas serán las de funciones objetivo.   
          else:
             prior_option_menu = self.__objective_functions_option_menu
             current_option_menu = self.__decision_variables_option_menu
             current_variable_option_menu = self.__current_decision_variable_name

             #Se actualiza la variable current_canvas a la última que se seleccionó en la categoría de las
             #variables de decisión
             self.__current_canvas = self.__decision_variables_canvas[self.__current_decision_variable_name]

          #Si la categoría de la selección antigua tiene un OptionMenu, éste se desactiva del Frame.
          if prior_option_menu != "":
             prior_option_menu.grid_forget()
             self.__option_menu_frame.pack_forget()

          #Si la categoría de la selección actual tiene un OptionMenu, éste se activa y coloca en el Frame.
          if current_option_menu != "":
             self.__variable_option_menu.set(current_variable_option_menu)
             self.__option_menu_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True)
             current_option_menu.grid(row = 1,column = 0,pady = (1,13),sticky = tk.S+tk.N)

          #Se actualizan las características tanto del Canvas actual de la categoría recién elegida
          #como de su respectiva barra de navegación. También se colocan en el Frame ambos.
          self.__current_canvas[1].update()
          self.__current_canvas[1].pack(side = tk.BOTTOM,fill = tk.BOTH,expand = True)
          self.__current_canvas[0]._tkcanvas.pack(side = tk.TOP,fill = tk.BOTH,expand = True)
          self.__current_canvas[0].show()
          
      
      def __change_inner_canvas(self,event):
          """
             .. note:: Este método es privado.

             Realiza el cambio de Canvas dentro de una misma categoría, esto
             en caso en que los datos hayan arrojado más de una gráfica. El cambio
             se hace con ayuda de su OptionMenu asociado.

             :param event: Elemento que ejecutó esta función.
             :type event: String
          """
          #Las siguientes variables nos ayudan a identificar la categoría sobre la cual
          #se tendría que hacer el cambio interno
          selected_variable_menu_option = self.__variable_option_menu.get()
          selected_variable_checkbutton = self.__variable_checkbutton.get()

          #Sin importar la categoría, dado que va a haber un cambio, el Canvas actual
          #se desactiva. Dado que el Canvas en realidad consta del Canvas y de su barra de
          #navegación, entonces ambos elementos deben desactivarse.

          #Se desactiva la barra de navegación
          self.__current_canvas[1].pack_forget()
 
          #Se desactiva el Canvas.
          self.__current_canvas[0]._tkcanvas.pack_forget()

          #Si se trata de un cambio interno de funciones objetivo se toma la función seleccionada
          #con ayuda del OptionMenu y se solicita dentro de la estructura correspondiente dicho Canvas.
          if selected_variable_checkbutton == 0:
             self.__current_objective_function_name = selected_variable_menu_option
             self.__current_canvas = self.__objective_functions_canvas[self.__current_objective_function_name]

          #Si se trata de un cambio interno de variables de decisión se toma la función seleccionada
          #con ayuda del OptionMenu y se solicita dentro de la estructura correspondiente dicho Canvas.
          else: 
             self.__current_decision_variable_name = selected_variable_menu_option
             self.__current_canvas = self.__decision_variables_canvas[self.__current_decision_variable_name]

          #Al final el nuevo Canvas almacenado en self.__current_canvas se actualiza y se coloca en el Frame
          #junto con su respectiva barra de navegación.
          self.__current_canvas[1].update()
          self.__current_canvas[1].pack(side = tk.BOTTOM,fill = tk.BOTH,expand = True)
          self.__current_canvas[0]._tkcanvas.pack(side = tk.TOP,fill = tk.BOTH,expand = True)
          self.__current_canvas[0].show()
