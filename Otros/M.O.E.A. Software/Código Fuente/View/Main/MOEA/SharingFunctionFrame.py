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


class SharingFunctionFrame(tk.Frame):
      """
         | Esta clase proporciona una base gráfica para que el usuario pueda
          seleccionar métodos con sus respectivos parámetros **(si es que tienen)**
          referentes a Sharing Function.          
         | Una técnica de Sharing Function sirve para aplicar una selección más intensiva
          de Individuos en caso de haber un "empate" entre éstos.

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
          #Se crea el Frame que contendrá todos los elementos gráficos.
          tk.Frame.__init__(self,parent,bd = 4,relief = "groove")

          #Para esta clase se agregarán dos elementos estáticos: 
          #Alpha Sharing Function
          #En esta parte se agregan sus respectivos valores por defecto.
          self.__default_alpha_sharing_function = "4"
          
          #Se declaran tipografías que servirán para identificar tanto a los elementos 
          #estáticos como dinámicos
          self.__title_font = tkf.Font(family = "Helvetica",size = 11,weight = "bold")
          self.__name_font = tkf.Font(family = "Helvetica",size = 10,weight = "bold")
          self.__value_font = tkf.Font(family = "Helvetica",size = 10)

          #Se obtiene la información necesaria para poder llenar con elementos
          #gráficos este Frame (véase Controller/XMLParser.py)
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
       
          #Se crean elementos gráficos para las técnicas y sus parámetros (si los tienen).
          self.__create_dynamic_widgets()

          #Se ordenan las técnicas disponibles.
          self.__renamed_techniques_list.sort()

          #Las siguientes variables almacenan la técnica escogida por el usuario.
          self.__current_variable = tk.StringVar(self) 
          self.__current_variable.set(self.__renamed_techniques_list[0])
          self.__old_variable = self.__current_variable.get()     

          #Se crea un elemento gráfico para el título del Frame.
          self.__title_label = tk.Label(self,text = name + " Settings")

          #Se crea el elemento gráfico para el alpha_sharing_function. Éste constará
          #de un Label y un Entry.
          self.__alpha_sharing_function_label = tk.Label(self,text = "Alpha value:")
          self.__alpha_sharing_function_entry = tk.Entry(self,relief = "sunken")
          self.__alpha_sharing_function_entry.insert(tk.END,self.__default_alpha_sharing_function)

          #Los siguientes elementos sirven para mostrar las técnicas disponibles
          #para el usuario
          self.__option_menu_label = tk.Label(self,text = "Technique: ")
          self.__option_menu = tk.OptionMenu(self,self.__current_variable,*self.__techniques_list,command = self.__update_widgets)

          #Se crea un separador.
          self.__separator = ttk.Separator(self,orient = tk.HORIZONTAL)

          #Se crea una etiqueta para comenzar a enumerar los parámetros disponibles para
          #una técnica dada.
          self.__parameters_label = tk.Label(self,text = "Parameters for {0}:".format(self.__current_variable.get()))
                    
          #A todos los parámetros descritos con anterioridad se les asigna un formato.
          self.__title_label["font"] = self.__title_font
          self.__alpha_sharing_function_label["font"] = self.__name_font
          self.__alpha_sharing_function_entry["font"] = self.__value_font
          self.__option_menu_label["font"] = self.__name_font
          self.__option_menu["font"] = self.__value_font
          self.__parameters_label["font"] = self.__title_font

          #Esta variable mantiene un control sobre el renglón en el que se colocan los elementos para evitar
          #su traslape.
          self.__row_position = 0

          #A continuación se colocan los elementos tanto estáticos como dinámicos.
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
          self.__row_position += 1

          #A continuación se colocan los elementos relativos al alpha_sharing_function.
          self.__alpha_sharing_function_label.grid(row = self.__row_position,column = 0,padx = (1,8),pady = (9,2),sticky = tk.E) 
          self.__alpha_sharing_function_entry.grid(row = self.__row_position,column = 1,padx = (1,1),pady = (9,2),sticky = tk.W)
          self.__row_position += 1

          #Ahora se colocan los elementos concernientes a las técnicas disponibles.
          self.__option_menu_label.grid(row = self.__row_position,column = 0,padx = (1,8),pady = (9,5),sticky = tk.E)
          self.__option_menu.grid(row = self.__row_position,column = 1,padx = (1,1),pady = (9,5),sticky = tk.W)
          self.__row_position += 1

          #A continuación se coloca el separador.        
          self.__separator.grid(row = self.__row_position,column = 0,columnspan = 2,pady = (15,1),sticky = tk.W + tk.E)
          self.__row_position += 1

          #Finalmente se coloca la etiqueta que identificará los elementos dinámicos para cada técnica.
          self.__parameters_label.grid(row = self.__row_position,column = 0,columnspan = 2,pady = (10,1),sticky = tk.N + tk.S)
          self.__row_position += 1

          #Las siguientes opciones permiten hacer algo muy similar que con la opción columnspan, la diferencia
          #radica en que estas afectan a todos los elementos, dinámicos o estáticos, mientras que columnspan es
          #sólo para un elemento.
          self.grid_columnconfigure(0,weight = 1)
          self.grid_columnconfigure(1,weight = 1)
          
          #Ahora se colocan los elementos dinámicos.
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
                   current_widget[2].grid(row = counter,column = 0,padx = (1,9),pady = (1,8),sticky = tk.E)
                   current_widget[3].grid(row = counter,column = 1,pady = (1,8),sticky = tk.W)

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
       
          #Se selecciona la técnica que estaba por defecto.
          self.__current_variable.set(self.__renamed_techniques_list[0])    

          #Se elimina el contenido actual de los Entrys de los elementos estáticos y 
          #Posteriormente se les añade su respectivo valor por defecto.
          self.__alpha_sharing_function_entry.delete(0,tk.END)
          self.__alpha_sharing_function_entry.insert(tk.END,self.__default_alpha_sharing_function)     
         
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
          self.__current_variable.set(self.__renamed_techniques_list[0])          
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
       
          return {
                  "sharing_function_class": selected_class,
                  "sharing_function_technique": actual_selected_technique,
                  "sharing_function_parameters": selected_parameters,
                  "alpha_sharing_function": self.__alpha_sharing_function_entry.get()
                 }
