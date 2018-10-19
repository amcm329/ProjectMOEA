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
from ErrorFrame import ErrorFrame
from SummaryFrame import SummaryFrame
from GraphFrame import GraphFrame


class ResultsGrapherToplevel(tk.Toplevel):
      """
         | Esta clase lanza una ventana independiente que muestra los resultados arrojados por una configuración
          previa del usuario.
         |
         | Primero que nada es menester mencionar que una ventana independiente es un Toplevel en Tkinter,
          la cual es casi ajena a la Ventana Principal **(véase View/Main/MainWindow.py)**, pero si ésta última es
          cerrada, se eliminarán también las ventanas independientes creadas.
         |
         | Cada ventana independiente mostrará el número de Task, es decir, el orden en el que fue procesada la información
          con respecto de otros Tasks.
         |
         | Entiéndase por Task a una ejecución de algún algoritmo MOEA bajo un cierto conjunto de configuraciones iniciales.
          Así, los Tasks serán mostrados en una ventana independiente. La numeración de los Tasks irá siempre en orden progresivo,
          lo que significa que el número será reinicializado sólamente volviendo a ejecutar el programa principal.
         | De esta manera es posible tener varias ventanas independientes abiertas y en cuestiones más generales, es posible
          ejecutar varios Tasks simultáneamente, ya que el programa es multi-threading en ese sentido.
         |
         | Finalmente, la información será mostrada en dos pestañas: en una **(SummaryFrame)** se otorga un resumen de todas
          las funciones objetivo, variables de decisión, MOEA usado y configuraciones adicionales en el Task.
         | En la otra **(GraphFrame)** se colocan todas las gráficas pertinentes producto de la ejecución del MOEA con las
          funciones objectivo, variables de decisión y configuraciones ingresadas **(véase Model/Community/Community.py)**
          **(véase View/Additional/ResultsGrapher/GraphFrame.py)**.
         |         
         | Si por cualquier circunstancia llega a haber una falla interna durante la ejecución del proceso, ninguna de las dos
          pestañas será mostrada y en su lugar aparecerá una de error **(ErrorFrame)**, especificando además el tipo de error
          y en qué parte de Model **(ó Modelo)** ocurrió.

         :param parent: Frame padre al que pertenece.
         :param path_image_logo: La ruta al logotipo que se usa en esta ventana independiente.
         :param execution_task_count: Número que indica el actual Task en ejecución.
         :param main_features: Diccionario que contiene, entre otras cosas, los nombres de los
                parámetros asociados a cada técnica.
         :param gathered_information: Diccionario que contiene todas las configuraciones 
                recabadas ingresadas por el usuario **(véase View/Main/MainWindow.py)**.
         :param final_results: Diccionario que contiene la información procesada lista para graficar
                **(véase View/Additional/ResultsGrapher/GraphFrame.py)**.

         :type parent: Tkinter.Frame
         :type path_image_logo: String
         :type execution_task_count: Integer
         :type main_features: Dictionary
         :type gathered_information: Dictionary
         :type final_results: Dictionary
         :returns: Tkinter.Toplevel
         :rtype: Instance         
      """


      def __init__(self,parent,path_image_logo,execution_task_count,main_features,gathered_information,final_results):
          #Se crea un Toplevel (ventana independiente) sobre la cual se colocarán todos los elementos gráficos.
          tk.Toplevel.__init__(self,parent)

          #Se establecen las dimensiones del Toplevel. 
          self.__width = 600
          self.__height = 500

          #Se asignan las dimensiones al Toplevel; es importante destacar que este tamaño
          #es el que se coloca sólo al principio, el usuario puede modificar a voluntad estos valores.
          self.minsize(width = self.__width,height = self.__height)

          #Al Toplevel se le coloca el título, indicando el número de Task que le corresponde.
          self.title("Task {0}. Final results.".format(execution_task_count))

          #Esta opción indica que el TopLevel siempre se colocará enfrente con respecto de la ventana Padre.
          self.transient()

          #Cuando se declara un Toplevel, éste siempre es mostrado tenga información o no, entonces se oculta
          #automáticamente para que pueda ser actualizado apropiadamente y posteriormente se muestre.
          self.withdraw()

          #Se almacena la referencia a la ventana Padre.
          self.__parent = parent
          
          #A continuación se declara un elemento gráfico que puede albergar pestañas, el Notebook.
          self.__notebook = ttk.Notebook(self)

          #Si los resultados contienen una llave que se llama response, significa que hubo un error de ejecución
          #interna en el Model, de modo que el título de la ventana se cambia a la de error.
          if final_results.has_key("response"):
             #Al Toplevel se le coloca el título, indicando el número de Task que le corresponde.
             self.title("Task {0}. ERROR.".format(execution_task_count))
         
             #El Frame correspondiente al error suscitado es creado para indicar la información
             #procediente.	
             self.__error_frame = ErrorFrame(self,final_results)

             #Se añade al Notebook el Frame correspondiente al error y su descripción
             self.__notebook.add(self.__error_frame,text = " Error ")

             #Se centra el Toplevel con respecto de la ventana Padre.
             self.__center()   
             
          else: 
              #Si no hubo error interno en la ejecución del algoritmo, al Toplevel se le coloca el título,
              #indicando el número de Task que le corresponde.
              self.title("Task {0}. Final results.".format(execution_task_count))

              #Se declara estructuras que almacenan los datos llave - valor de las funciones objetivo y las 
              #variables de decisión renombradas.
              self.__renamed_objective_functions = {}
              self.__renamed_decision_variables = {}

              #Se declaran estructuras que almacenan sólo los nombres de las funciones objetivos y las 
              #variables de decisión renombradas.
              self.__renamed_objective_functions_list = []
              self.__renamed_decision_variables_list = []
          
              #Se almacenan las funciones objetivo y las variables de decisión que el usuario insertó y 
              #fueron procesadas en la capa Model.
              self.__objective_functions = gathered_information["Objective Functions"]["vector_functions"]
              self.__decision_variables = gathered_information["Decision Variables"]["vector_variables"]
        
              #Se renombran las funciones objetivo y las variables de decisión.
              self.__create_renamed_settings()
          
              #Se crean los Frames relativos al Summary (información general del Task) y Graph (gráficas de los resultados finales).
              self.__summary_frame = SummaryFrame(self,self.__renamed_objective_functions,self.__renamed_decision_variables,main_features,gathered_information)
              self.__graph_frame = GraphFrame(self,execution_task_count,self.__renamed_objective_functions_list,self.__renamed_decision_variables_list,final_results)
          
              #Se añaden al Notebook los Frames correspondientes, indicando en las pestañas el nombre de la sección.
              self.__notebook.add(self.__summary_frame,text = " Summary ")
              self.__notebook.add(self.__graph_frame,text = " Graphs ")

          #Se almacena en el Toplevel el Notebook completo.
          self.__notebook.pack(side = tk.TOP,fill = tk.BOTH,expand = True)

          #Se centra el Toplevel con respecto de la ventana Padre.
          self.__center()          

          #Se coloca el logotipo en esta ventana independiente.
          self.wm_iconbitmap(bitmap = path_image_logo)

          #Esta opción "materializa" el Toplevel, es decir, una vez que se ocultó, actualizó y centró en la ventana Padre, entonces es momento
          #de mostrarlo en la pantalla.
          self.deiconify()  


      def __create_renamed_settings(self):
          """
             .. note:: Este método es privado.
             
             | Tal como su nombre lo dice, renombra las funciones objetivo y variables de decisión
              para posteriormente almacenarlas en una estructura por cada tipo.
             | Renombrar una función o variable de decisión es hacer un mapeo que consista en:
             | Elemento_renombrado -> elemento original.
             | Para el caso de la función objetivo, el renombramiento se da anteponiendo la letra **F**
              seguido de la posición en la que fue insertada originalmente por el usuario.
             | El caso es análogo para la variable de decisión, sólo que la letra es **V**.
             | La idea de renombrar las funciones y variables surge como alternativa al momento de graficar los datos
              **(véase View/Additional/ResultsGrapher/GraphFrame.py)**, ya que el usuario puede ingresar
              funciones muy largas o variables con identificadores muy complejos y esto en la parte gráfica 
              se vería muy amontonado; por ello fue preferible mostrar la parte renombrada en la sección de 
              GraphFrame y colocar la muestra original en el SummaryFrame.         
          """   

          #A continuación se realiza el renombramiento de las funciones objetivo.
          for x in range (len(self.__objective_functions)):
              #Se crea la etiqueta de renombramiento y se toma la función actual.
              renamed_function = "F" + str(x + 1)
              current_function = self.__objective_functions[x]

              #La función renombrada se almacena en una lista y en un diccionario; en este último
              #La clave - valor es precisamente: Función renombrada -> función original.
              self.__renamed_objective_functions_list.append(renamed_function)
              self.__renamed_objective_functions[renamed_function] = current_function
                            
          #A continuación se realiza el renombramiento de las variables de decisión.
          for y in range (len(self.__decision_variables)):
              #Se crea la etiqueta de renombramiento y se toma la variable actual.
              renamed_variable = "V" + str(y + 1)
              current_variable = self.__decision_variables[y][0]
              current_range = self.__decision_variables[y][1]
 
              #La variable renombrada se almacena en una lista y en un diccionario; en este último
              #La clave - valor es precisamente: Variable renombrada -> variable original.
              self.__renamed_decision_variables_list.append(renamed_variable)
              self.__renamed_decision_variables[renamed_variable] = (current_variable,current_range)
         

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

          #A continuación se obtiene la geometría de la ventana independiente.
          #Ésta se obtiene de la forma A x B + C + D, donde A y B representan 
          #el ancho y largo respectivamente, mientras que C y D contienen el 
          #desplazamiento en el eje X (para C) & Y (para D) con respecto
          #del origen (esquina superior izquierda de la pantalla).
          #Es importante mencionar que estas características se toman cuando ya se
          #ha insertado la información pertinente en la ventana, esto para que 
          #se pueda conocer a priori el tamaño de la ventana que será en principio inmutable.
          current_geometry = self.winfo_geometry()
          current_geometry = current_geometry.replace('x','+').split('+')

          #Con base en la información anterior, se toman sólo el ancho y largo 
          #de la ventana independiente.
          current_width = int(current_geometry[0])
          current_height = int(current_geometry[1])
          
          #Ahora se obtiene la geometría de la ventana principal.
          #Ésta se obtiene de la forma A x B + C + D, donde A y B representan 
          #el ancho y largo respectivamente, mientras que C y D contienen el 
          #desplazamiento en el eje X (para C) & Y (para D) con respecto
          #del origen (esquina superior izquierda de la pantalla).
          parent_geometry = self.__parent.winfo_geometry()
          parent_geometry = parent_geometry.replace('x','+').split('+')

          #De la ventana principal se toman todos los datos.
          parent_width = int(parent_geometry[0])
          parent_height = int(parent_geometry[1])
          parent_offset_width = int(parent_geometry[2])
          parent_offset_height = int(parent_geometry[3])

          #Se calculan los desplazamientos de la ventana independiente tomando como referencia 
          #los tamaños de la ventana padre y la ventana independiente, y dado que tiene que quedar
          #exactamente en el centro, por eso es que se divide entre 2, para que quede el mismo espacio
          #tanto a la izquierda como a la derecha; tanto arriba como abajo.
          current_offset_width = parent_offset_width + (parent_width - current_width)/2 
          current_offset_height = parent_offset_height + (parent_height - current_height)/2

          #Al final se toman estos datos y se colocan en la geometría de la ventana independiente de la 
          #manera A x B + C + D descrita anteriormente.
          self.geometry('{0}x{1}+{2}+{3}'.format(current_width,current_height,current_offset_width,current_offset_height))
