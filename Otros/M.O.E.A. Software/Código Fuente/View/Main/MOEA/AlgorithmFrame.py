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


class AlgorithmFrame(tk.Frame):
      """
         Esta clase proporciona una base gráfica para que el usuario pueda
         seleccionar técnicas con sus parámetros correspondientes **(si es que tienen)**
         referentes a los M.O.E.A.'s **(Multi-Objective Evolutionary Algorithms ó Algoritmos Evolutivos Multiobjetivo)**.
         
         :param parent: Frame padre al que pertenece.
         :param name: Identificador **(único)** que tendrá el Frame.
         :param features: Conjunto de técnicas con sus respectivos parámetros para que
                          se puedan cargar automáticamente en este Frame **(véase
                          Controller/XMLParser.py)**.

         :type parent: Tkinter.Frame
         :type name: String
         :type features: Dictionary
         :returns: Tkinter.Frame
         :rtype: Instance
      """


      def __init__(self, parent,name,features):
          #Se declara el Frame que contendrá todos los elementos gráficos.
          tk.Frame.__init__(self,parent,bd = 4,relief = "groove")
          
          #Se declaran tipografías que servirán para identificar tanto a los elementos 
          #estáticos como dinámicos
          self.__title_font = tkf.Font(family = "Helvetica",size = 11,weight = "bold")
          self.__name_font = tkf.Font(family = "Helvetica",size = 10,weight = "bold")
          self.__value_font = tkf.Font(family = "Helvetica",size = 10)

          #Estas variables se obtienen para poder crear componentes gráficos para los parámetros
          #(de acuerdo al su tipo), para más información véase Controller/XMLParser.py
          self.__path = features["path"]
          self.__techniques = features["techniques"]
   
          #Se adquiere el nombre de la clase.
          self.__class_name = name.lower()
         
          #self.__widgets son los parámetros de las técnicas a mostrar.
          #self.__techniques_list es la lista de técnicas disponibles para seleccionar. 
          #self.__renamed_techniques_list es una lista de técnicas con su tipo (binary o float).
          #se crea para no "contaminar" la primera.
          self.__widgets = {}
          self.__techniques_list = {}
          self.__renamed_techniques_list = []
          
          #A continuación se crean los elementos gráficos para los parámetros de cada técnica.
          #Dado que estos cambian con la técnica, se les denominará elementos dinámicos.
          self.__create_dynamic_widgets()

          #Las siguientes variables mantienen un control sobre la técnica seleccionada
          #por el usuario.
          self.__current_variable = tk.StringVar(self) 
          self.__current_variable.set(self.__renamed_techniques_list[3])
          self.__old_variable = self.__current_variable.get()     

          #A continuación se crean algunos elementos gráficos para identificar al Frame.
          #tales como un título, la técnica, un separador y una etiqueta que indica cuáles
          #son los parámetros de una técnica (si los tiene).
          self.__title_label = tk.Label(self,text = name + " Settings")
          self.__option_radiobutton_label = tk.Label(self, text = "Technique:")
          self.__separator = ttk.Separator(self,orient = tk.HORIZONTAL)
          self.__parameters_label = tk.Label(self, text = "Parameters for {0}:".format(self.__current_variable.get()))

          #Se le da formato a cada uno de los elementos descritos con anterioridad, excepto
          #al separador.
          self.__title_label["font"] = self.__title_font
          self.__option_radiobutton_label["font"] = self.__name_font
          self.__parameters_label["font"] = self.__title_font    

          #Esta variable sirve para tener un control sobre el renglón en el cual colocar a los
          #elementos gráficos.
          self.__row_position = 0
         
          #A continuación se colocan los elementos ya sean dinámicos o estáticos.
          self.__grid_widgets()

 
      def __create_dynamic_widgets(self):
          """
             .. note:: Este método es privado.

             Inicializa los elementos dinámicos del Frame, esto es, de acuerdo al tipo 
             que lleva cada parámetro se creará un widget diferente.
          """      

          #Se inicializan self.__widgets y self.__chniques_list
          for technique_name in self.__techniques.keys():     
              complete_technique_name = technique_name
              technique_parameters = self.__techniques[technique_name]["parameters"]
              technique_classification = self.__techniques[technique_name]["classification"] 

              #Si la técnica es estrictamente binaria o flotante se agrega esta restricción
              #al nombre de la técnica.                                 
              if technique_classification != "-":
                 complete_technique_name += " (" + technique_classification + ")"

              self.__techniques_list[complete_technique_name] = technique_name
              self.__renamed_techniques_list.append(complete_technique_name)

              #Se crea la infraestructura gráfica de los parámetros usando la información 
              #enviada por el controlador (véase Controller/XMLParser.py).
              provisional_widgets = []
              for element in technique_parameters:
                  element_type = element["type"]
                  element_default = element["default"]

                  #Si el parámetro es de tipo int o float, éste constará gráficamente de 
                  #un Label y un Entry.
                  if element_type == "int" or element_type == "float": 
                     #Se verifican los límites superior e inferior de un parámetro. 
                     #Si alguno no tiene un límite establecido, simplemente se dice que el valor
                     #tenderá a infinito (Inf) o menos infinito (-Inf) (véase Controller/XML/Features.xml)
                     lower_bracket = "["
                     upper_bracket = "]"
                     lower_range = element["lower_range"]
                     upper_range = element["upper_range"]

                     if lower_range == "-":
                        lower_range = "-Inf"
                        lower_bracket = "("  
                  
                     if upper_range == "-":
                        upper_range = "Inf"
                        upper_bracket = ")"
                                              
                     #Aqui se indica el nombre del parámetro y su rango de valores permitido.
                     complete_variable =  u"{0}  ∈  {1} {2} , {3} {4} :".format(element["name"],lower_bracket,lower_range,upper_range,upper_bracket)
                     encoded_variable = complete_variable.encode("utf-8")
                     provisional_label = tk.Label(self,text = encoded_variable)
                     provisional_entry = tk.Entry(self,relief = "sunken")
                     provisional_entry.insert(tk.END,element_default)

                     #Se le da formato a los elementos
                     provisional_label["font"] = self.__name_font
                     provisional_entry["font"] = self.__value_font                                                            
                     provisional_widgets.append([element_type,element_default,provisional_label,provisional_entry])

                  #Si el parámetro es de tipo bool, éste constará de un Label y un Checkbutton para indicar si la opción
                  #será activada o no.
                  elif element_type == "bool":
                       provisional_label = tk.Label(self,text = element["name"])
                       provisional_checkbutton_variable = tk.StringVar(self) 
                       provisional_checkbutton = tk.Checkbutton(self,variable = provisional_checkbutton_variable,onvalue = "True",offvalue = "False")

                       #La opción por defecto es lo que repercutirá si el Checkbutton está activado o no.
                       if element_default == "True":
                          provisional_checkbutton.select()

                       elif element_default == "False":                 
                            provisional_checkbutton.deselect()

                       #Se le da formato a los elementos.
                       provisional_label["font"] = self.__name_font
                       provisional_checkbutton["font"] = self.__value_font                                                            
                       provisional_widgets.append([element_type,element_default,provisional_label,provisional_checkbutton,provisional_checkbutton_variable])

              #Si una técnica no necesita de parámetros, se antepone un elemento Label con la palabra 
              #NONE.     
              if provisional_widgets == []:
                 provisional_label = tk.Label(self,text = " NONE ")
                 #Se le da formado al elemento
                 provisional_label["font"] = self.__title_font
                 provisional_widgets.append(["none",provisional_label])

              #Se agregan los elementos creados a la lista correspondiente.
              self.__widgets[complete_technique_name] = provisional_widgets
      

      def __grid_widgets(self): 
          """
             .. note:: Este método es privado.

             Coloca elementos en el Frame, tanto estáticos como dinámicos.
          """  
  
          #En términos generales, todos los elementos del Frame se colocan en modo grid, esto significa
          #que se le tiene que indicar el renglón y la columna en la que serán puestos.
          #Existen otros parámetros para ajustar mejor la colocación, columnspan permite que el elemento 
          #se traslape tantas columnas como sea necesario, pad da una separación entre el actual y el siguiente
          #elemento gráfico (padx -> horizontal, pady -> vertical); sticky permite alinear los elementos a una orientación
          #determinada.
          #Entonces se empieza por el título del Frame.
          self.__title_label.grid(row = self.__row_position,column = 0,columnspan = 2,pady = (10,1),sticky = tk.N + tk.S)
          #Cada que se inserta un elemento gráfico se actualiza esta variable para tener un apuntador actualizado sobre
          #dónde colocar el siguiente elemento. Así se hará con los restantes.
          self.__row_position += 1

          #A continuación se colocará una etiqueta para identificar los MOEAs.
          self.__option_radiobutton_label.grid(row = self.__row_position,column = 1,padx = (1,1),pady = (9,9),sticky = tk.W)
          self.__row_position += 1

          #Se toman todas las técnicas MOEAs disponibles y se colocan en esta sección.
          for technique_name in self.__techniques_list:
              self.__technique_radiobutton = tk.Radiobutton(self,text = technique_name,variable = self.__current_variable,value = technique_name,command = self.__update_widgets)
              self.__technique_radiobutton["font"] = self.__value_font
              self.__technique_radiobutton.grid(row = self.__row_position,column = 1,padx = (1,1),pady = (4,4),sticky = tk.W)
              self.__row_position += 1
          
          #Se soloca el separador para indicar el término de las técnicas MOEAs.
          self.__separator.grid(row = self.__row_position,column = 0,columnspan = 2,pady = (15,1),sticky = tk.W + tk.E)
          self.__row_position += 1
          
          #Ahora se antepone la etiqueta que indica que los siguientes elementos serán dinámicos, es decir,
          #relativos a la técnica (si los tiene).
          self.__parameters_label.grid(row = self.__row_position,column = 0,columnspan = 2,pady = (10,1),sticky = tk.N + tk.S)
          self.__row_position += 1
          
          #Las siguientes opciones permiten hacer algo muy similar que con la opción columnspan, la diferencia
          #radica en que estas afectan a todos los elementos, dinámicos o estáticos, mientras que columnspan es
          #sólo para un elemento.
          self.grid_columnconfigure(0,weight = 1)
          self.grid_columnconfigure(1,weight = 1)
          
          #Se colocan los elementos dinámicos del Frame.
          self.__update_widgets()        


      def __update_widgets(self,event = None):
          """
             .. note:: Este método es privado.

             | Realiza solamente la actualización y colocación de elementos dinámicos 
              en el Frame.
             | Si el parámetro event es distinto de **None**, significa que se lanzó 
              un evento que provocará que se actualicen los parámetros de acuerdo con
              la técnica seleccionada.
 
             :param event: Contiene el valor del elemento que ejecutó esta función.
             :type event: String      
          """

          #Primero se quitan del Frame los elementos que ya estaban colocados. De acuerdo al tipo de
          #elemento se hará grid_forget sobre partes diferentes de éste.
          for old_widget in self.__widgets[self.__old_variable]:
              old_widget_type = old_widget[0]
              if old_widget_type == "none":
                 old_widget[1].grid_forget()

              elif old_widget_type == "bool" or old_widget_type == "int" or  old_widget_type == "float":
                   old_widget[2].grid_forget()
                   old_widget[3].grid_forget()
             
          #Ahora se colocan los elementos tomando en cuenta la técnica seleccionada.
          #Éstos se colocarán a partir del 4o renglón ya que los renglones 0 al 3 son para 
          #los estáticos.
          counter = self.__row_position
          for current_widget in self.__widgets[self.__current_variable.get()]:
              current_widget_type = current_widget[0]
              #Aqui se colocan los elementos en una posición distinta dependiendo del tipo de valor que 
              #acepte el parámetero:
              if current_widget_type == "none":
                 current_widget[1].grid(row = counter,column = 0, columnspan = 2,sticky = tk.N + tk.S)       

              elif current_widget_type == "bool" or current_widget_type == "int" or current_widget_type == "float":
                   current_widget[2].grid(row = counter,column = 0,padx = (1,9),pady = (1,5),sticky = tk.E)
                   current_widget[3].grid(row = counter,column = 1,pady = (1,5),sticky = tk.W)

              counter += 1   
            
          #Después de haber colocado los elementos, se actualizan las variables pertinentes.
          self.__old_variable = self.__current_variable.get()
          self.__parameters_label.config(text = "Parameters for {0}:".format(self.__current_variable.get()))
      

      def restore_settings(self):
          """
             Asigna los valores por defecto tanto de las técnicas como de sus 
             respectivos parámetros, también limpia aquéllos en donde se hayan 
             insertado valores.
          """

          #Se verifican los parámetros de cada técnica (si los hay) y se limpia el Entry correspondiente.
          for current_technique in self.__renamed_techniques_list: 
              for current_widget in self.__widgets[current_technique]:
                  current_widget_type = current_widget[0]
                  current_widget_default = current_widget[1]

                  #Si el parámetro es bool, se marca la variable como seleccionada.
                  if current_widget_type == "bool":

                     #La opción por defecto es lo que repercutirá si el Checkbutton está activado o no.
                     if current_widget_default == "True":
                        current_widget[3].select()

                     elif current_widget_default == "False":                 
                          current_widget[3].deselect() 
 
                  #Si el parámetro es int o float, se elimina el contenido de su respectivo Entry.
                  elif current_widget_type == "int" or current_widget_type == "float":
                       current_widget[3].delete(0,tk.END)
                       current_widget[3].insert(tk.END,current_widget_default)

          #Se actualiza la selección de técnicas a la que estaba por defecto.
          self.__current_variable.set(self.__renamed_techniques_list[3])          
          self.__update_widgets()


      def get_information(self):
          """
             Recolecta la información que ha seleccionado e introducido el usuario,
             también la organiza para que se pueda utilizar apropiadamente.
 
             :returns: | Un diccionario que contiene:
                       | **Clase**,
                       | **Técnica**,
                       | **Parámetros.**
             :rtype: Dictionary
          """
          selected_parameters = {}
           
          #Se selecciona la técnica que el usuario eligió.
          renamed_selected_technique = self.__current_variable.get()
          actual_selected_technique = self.__techniques_list[renamed_selected_technique]

          #Se seleccionan los elementos asociados a ésta.
          technique_widgets = self.__widgets[renamed_selected_technique]             

          #Se crea la clase que corresponde a la técnica seleccionada para crear su
          #respectiva instancia (véase Controller/Verifier.py).
          selected_class = self.__path + self.__techniques[actual_selected_technique]["class"]

          #Se seleccionan los parámetros asociados a la técnica.
          technique_parameters = self.__techniques[actual_selected_technique]["parameters"]
          
          #Se obtiene el valor de los parámetros (si la técnica a emplear los tiene).
          for x in range (len(technique_parameters)):
              current_parameter_value = ""
              current_parameter_type = technique_widgets[x][0]
              current_parameter_variable = technique_parameters[x]["variable"]

              #De acuerdo al tipo de parámetro se obtiene información de diferentes secciones.
              if current_parameter_type == "bool":
                 current_parameter_value =  technique_widgets[x][4].get()    

              elif current_parameter_type == "int" or current_parameter_type == "float":
                   current_parameter_value =  technique_widgets[x][3].get()
                  
              selected_parameters[current_parameter_variable] = current_parameter_value
        
          #Se regresa un diccionario con estos tres elementos.
          return {
                  self.__class_name + "_class": selected_class,
                  self.__class_name + "_technique": actual_selected_technique, 
                  self.__class_name + "_parameters": selected_parameters 
                 }
