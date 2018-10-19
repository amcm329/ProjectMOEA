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


class TemplateGeneticOperatorFrame(tk.Frame):
      """ 
         | Proporciona la infraestructura gráfica para que el usuario pueda 
          elegir técnicas y configurar atributos concernientes a la Selección, Cruza y 
          Mutación de Individuos de una Población.
         | A grandes rasgos se trata de una plantilla que deberán implementar las clases
          SelectionFrame, CrossoverFrame y MutationFrame.
         | La clase permite la selección de cada posible técnica disponible y automáticamente 
          se muestran los parámetros necesarios **(si los hay)** para cada una de éstas.

         :param parent: Frame padre al que pertenece.
         :param name: Identificador **(único)** que tendrá el Frame.
         :param features: Conjunto de técnicas con sus respectivos parámetros para que
                          se puedan cargar automáticamente en este Frame **(véase
                          Controller/XMLParser.py)**.
         :param sort_techniques: Indica si las técnicas disponibles se ordenan alfabéticamente
                                 o no.
                               
         :type parent: Tkinter.Frame
         :type name: String
         :type features: Dictionary
         :type sort_techniques: Boolean
         :returns: Tkinter.Frame
         :rtype: Instance
      """


      def __init__(self,parent,name,features,sort_techniques = False):
          #Se declara el Frame correspondiente a esta clase.
          tk.Frame.__init__(self,parent,bd = 4,relief = "groove")

          #Se declaran tipografías que servirán para identificar tanto a los elementos 
          #estáticos como dinámicos
          self.title_font = tkf.Font(family = "Helvetica",size = 11,weight = "bold")
          self.name_font = tkf.Font(family = "Helvetica",size = 10,weight = "bold")
          self.value_font = tkf.Font(family = "Helvetica",size = 10)

          #Se obtiene la información de las técnicas que se mostrarán en este frame
          #(véase Controller/XMLParser.py) 
          self.__path = features["path"]
          self.__techniques = features["techniques"]

          #El identificador será el nombre de la clase.
          self.__class_name = name.lower()
          
          #self.__widgets son los parámetros de las técnicas a mostrar.
          #self.__techniques_list es la lista de técnicas disponibles para seleccionar. 
          self.__widgets = {}
          self.__techniques_list = {}
          self.__renamed_techniques_list = []
          
          #Se crean los componentes gráficos para cada uno de los parámetros de los métodos
          #disponibles.
          self.__create_dynamic_widgets()
                 
          #En caso de que se deseen ordenar las técnicas por orden alfabético, se realiza
          #dicha operación.
          if sort_techniques == True:
             self.__renamed_techniques_list.sort()

          #La siguientes variables mantienen un control de la elección previa y actual
          #del usuario, esto para poder actualizar u obtener información de las técnicas 
          #y sus parámetros.
          self.__current_variable = tk.StringVar(self) 
          self.__current_variable.set(self.__renamed_techniques_list[0])          
          self.__old_variable = self.__current_variable.get()     

          #Se declaran los elementos estáticos del Frame. Básicamente éstas son etiquetas
          #creadas para identificar los elementos del Frame, así como un OptionMenu que
          #contendrá todas las técnicas disponibles para la asignación de Fitness.
          self.title_label = tk.Label(self,text = name + " Settings")
          self.__option_menu_label = tk.Label(self,text = "Technique:")
          self.__option_menu = tk.OptionMenu(self,self.__current_variable,*self.__renamed_techniques_list,command = self.__update_widgets)
          self.__parameters_label = tk.Label(self,text = "Parameters for {0}:".format(self.__current_variable.get()))
          self.__separator = ttk.Separator(self)

          #Dándole formato a cada uno de los elementos estáticos del Frame.
          self.title_label["font"] = self.title_font
          self.__option_menu_label["font"] = self.name_font
          self.__option_menu["font"] = self.value_font
          self.__parameters_label["font"] = self.title_font          
         
          #Se colocan los elementos en el Frame.
          self.row_position = 0
    

      def __create_dynamic_widgets(self):
          """
             .. note:: Este método es privado.

             Inicializa los elementos dinámicos del Frame, esto es, de acuerdo al tipo 
             que lleva cada parámetro se creará un widget diferente.
          """      

          #Se inicializan self.__widgets y self.__techniques_list
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
                     provisional_label["font"] = self.name_font
                     provisional_entry["font"] = self.value_font                                                            
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
                       provisional_label["font"] = self.name_font
                       provisional_checkbutton["font"] = self.value_font                                                            
                       provisional_widgets.append([element_type,element_default,provisional_label,provisional_checkbutton,provisional_checkbutton_variable])
                  

              #Si una técnica no necesita de parámetros, se antepone un elemento Label con la palabra 
              #NONE.     
              if provisional_widgets == []:
                 provisional_label = tk.Label(self,text = " NONE ")
                 #Se le da formado al elemento
                 provisional_label["font"] = self.title_font
                 provisional_widgets.append(["none",provisional_label])

              #Se agregan los elementos creados a la lista correspondiente.
              self.__widgets[complete_technique_name] = provisional_widgets


      def grid_widgets(self):
          """
             Permite la colocación adecuada de elementos estáticos y dinámicos, considerando
             además el espacio o características necesarias de redimensionamiento para éstos últimos.
          """      

          #La colocación de elementos se hace en forma de grid, es decir, indicándole al Frame en qué
          #columna y renglón (row) se van a agregar. 
          #La opción columnspan permite traslapar columnas entre sí, esto es muy útil al momento de 
          #la colocación de elementos y que ésta no se veaa afectada al manipular el tamaño de la ventana. 
          #La opción pad indica el espacio que se deja entre un elemento y el siguiente 
          #(padx -> horizontal, pady -> vertical).
          #La opción sticky es para  alinear los elementos hacia un lado determinado.
          self.__option_menu_label.grid(row = self.row_position,column = 0,padx = (1,8),pady = (9,9),sticky = tk.E)
          self.__option_menu.grid(row = self.row_position,column = 1,padx = (1,1),pady = (9,9),sticky = tk.W)
          self.row_position += 1
          self.__separator.grid(row = self.row_position,column = 0,columnspan = 2,pady = (5,1),sticky = tk.W + tk.E)
          self.row_position += 1
          self.__parameters_label.grid(row = self.row_position,column = 0,columnspan = 2,pady = (6,9),sticky = tk.N + tk.S)
          self.row_position += 1
          
          #Las siguientes opciones permiten hacer algo muy similar que con la opción columnspan, la diferencia
          #radica en que estas afectan a todos los elementos, dinámicos o estáticos, mientras que columnspan es
          #sólo para un elemento.
          self.grid_columnconfigure(0,weight = 1)
          self.grid_columnconfigure(1,weight = 1)
          
          #A continuación se colocan los elementos dinámicos.
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
          counter = self.row_position
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
          self.__current_variable.set(self.__renamed_techniques_list[0])          
          self.__update_widgets()


      def get_information(self):
          """
             Recolecta la información que ha seleccionado e introducido el usuario,
             también la organiza para que se pueda utilizar apropiadamente.
 
             :returns: | Un diccionario que contiene:
                       | **Clase**,
                       | **Técnica**,
                       | **Parámetros**
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
