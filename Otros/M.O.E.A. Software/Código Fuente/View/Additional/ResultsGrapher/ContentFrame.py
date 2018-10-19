#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "acmcm329@hotmail.com"
__status__ = "Production"


import tkFont as tkf
import Tkinter as tk


class ContentFrame(tk.Frame):
      """
         Recaba el contenido de todas las funciones objetivo, variables de decisión y demás parámetros que 
         el usuario ingresó para poder ejecutar un Task determinado. Es entonces que plasma toda esta
         información en un Frame para que el usuario pueda cotejar los datos ingresados con los resultados
         obtenidos **(véase View/Additional/ResultsGrapher/GraphFrame.py)**.

         :param parent: Frame padre al que pertenece.
         :param renamed_objective_functions: Diccionario de funciones objetivo renombradas 
                **(véase View/Additional/ResultsGrapher/ResultsGrapherToplevel.py)**.
         :param renamed_decision_variables: Diccionario de variables de decisión renombradas  
                **(véase View/Additional/ResultsGrapher/ResultsGrapherToplevel.py)**.
         :param main_features: Diccionario que contiene, entre otras cosas, los nombres de los
                parámetros asociados a cada técnica.
         :param gathered_information: Diccionario que contiene todas las configuraciones 
                recabadas ingresadas por el usuario **(véase View/Main/MainWindow.py)**.

         :type parent: Tkinter.Frame
         :type renamed_objective_functions: Dictionary
         :type renamed_decision_variables: Dictionary
         :type main_features: Dictionary
         :type gathered_information: Dictionary
         :returns: Tkinter.Frame
         :rtype: Instance
      """


      def __init__(self,parent,renamed_objective_functions,renamed_decision_variables,main_features,gathered_information):
          #El Frame Padre sobre el cual se almacenarán todos los elementos.
          tk.Frame.__init__(self,parent)

          #Se cargan algunas fuentes para darle formato a los elementos en el Frame.
          self.__title_font = tkf.Font(family = "Helvetica",size = 11,weight = "bold")
          self.__name_font = tkf.Font(family = "Helvetica",size = 10,weight = "bold")
          self.__name_font_ii = tkf.Font(family = "Helvetica",size = 11)
          self.__value_font = tkf.Font(family = "Helvetica",size = 10)
          
          #A grandes rasgos en este Frame sólo se acoomodarán contenidos, de modo que por cada sección que
          #se muestra a continuación se declararán dos Frames, uno para mostrar el título y el otro para
          #mostrar el contenido de la sección pertinente.

          #Se declaran los Frames para las funciones objetivo. 
          self.__objective_functions_title_frame = tk.Frame(self)
          self.__objective_functions_content_frame = tk.Frame(self)

          #Se declaran los Frames para las variables de decisión.
          self.__decision_variables_title_frame = tk.Frame(self)
          self.__decision_variables_content_frame = tk.Frame(self)

          #Se crean los Frames para las características relacionadas con la población.
          self.__population_settings_title_frame = tk.Frame(self)
          self.__population_settings_content_frame = tk.Frame(self)

          #Se crean los Frames para los parámetros concernientes al Fitness de la población
          #y si tiene parámetros, también se colocan.
          self.__fitness_settings_title_frame = tk.Frame(self)
          self.__fitness_settings_content_frame = tk.Frame(self)

          #Se crean los Frames relacionados con la técnica de Selección de la población
          #(y sus posibles parámetros).
          self.__selection_settings_title_frame = tk.Frame(self) 
          self.__selection_settings_content_frame = tk.Frame(self) 

          #Se crean los Frames relativos a la técnica de Cruza de la población
          #(y sus plausibles parámetros).
          self.__crossover_settings_title_frame = tk.Frame(self)
          self.__crossover_settings_content_frame = tk.Frame(self)

          #Se inicializan los Frames que almacenan la técnica de Mutación de la población
          #y sus parámetros (de tenerlos).
          self.__mutation_settings_title_frame = tk.Frame(self)
          self.__mutation_settings_content_frame = tk.Frame(self)

          #Se generan los Frames que guardan la técnica del MOEA elegido, así como sus
          #posibles parámetros.
          self.__moea_settings_title_frame = tk.Frame(self)
          self.__moea_settings_content_frame = tk.Frame(self)

          #Se inicializan los Frames que albergan la técnica del Sharing Function, al igual
          #que sus parámetros (de tenerlos).
          self.__sharing_function_settings_title_frame = tk.Frame(self)
          self.__sharing_function_settings_content_frame = tk.Frame(self)
         

          #********OBJECTIVE FUNCTIONS************
          #A continuación se coloca toda la infraestructura de las funciones objetivo.
          #Se coloca el título en el Frame apropiado y se le da formato.
          self.__objective_functions_title_label = tk.Label(self.__objective_functions_title_frame,text = "Objective Functions")
          self.__objective_functions_title_label["font"] = self.__title_font
          self.__objective_functions_title_label.grid(row = 0,column = 0,pady = (15,1),sticky = tk.W)
       
          #Para las funciones objetivo se tomarán las funciones renombradas y se imprimirán las funciones renombradas
          #con su contraparte original.
          current_row = 0
          for renamed_function in renamed_objective_functions.keys():
              #Se crea una etiqueta para la función renombrada.
              current_objective_function_name_label = tk.Label(self.__objective_functions_content_frame,text = renamed_function + ":")
              #Se crea una etiqueta para la función original.
              current_objective_function_value_label = tk.Label(self.__objective_functions_content_frame,text = renamed_objective_functions[renamed_function]) 

              #Se les da el formato apropiado y se colocan en el Frame.
              current_objective_function_name_label["font"] = self.__name_font            
              current_objective_function_value_label["font"] = self.__value_font  
              current_objective_function_name_label.grid(row = current_row,column = 0,padx = (50,9),pady = (1,1),sticky = tk.W)
              current_objective_function_value_label.grid(row = current_row,column = 1,padx = (1,1),pady = (1,1),sticky = tk.W)               
              current_row += 1
          

          #********DECISION VARIABLES************
          #A continuación se coloca toda la infraestructura de las variables de decisión.
          #Primero se crea el título y se coloca en la parte correspondiente.
          self.__decision_variables_title_label = tk.Label(self.__decision_variables_title_frame,text = "Decision Variables")
          self.__decision_variables_title_label["font"] = self.__title_font
          self.__decision_variables_title_label.grid(row = 0,column = 0,pady = (15,1),sticky = tk.W)
          self.__decision_variables_title_frame.grid_columnconfigure(0,weight = 1)

          #Lo siguiente es tomar cada variable renombrada y colocarla junto con su contraparte original, indicando además
          #el rango en el que cada una ocurre.
          current_row = 0
          for renamed_variable in renamed_decision_variables.keys():
              #Se toma la variable renombrada con los rangos.
              current_variable = renamed_decision_variables[renamed_variable][0]
              current_range = renamed_decision_variables[renamed_variable][1]

              #A la variable original se le agrega el rango en el que se llevó a cabo su evaluación.
              complete_variable =  u"{0}  ∈  [ {1} , {2} ]".format(current_variable,current_range[0],current_range[1])
              encoded_variable = complete_variable.encode("utf-8")
          
              #Se crean etiquetas para las variables renombradas y originales.
              current_decision_variable_name_label = tk.Label(self.__decision_variables_content_frame,text = renamed_variable + ":")
              current_decision_variable_value_label = tk.Label(self.__decision_variables_content_frame,text = encoded_variable) 

              #Se les da formato a las variables.
              current_decision_variable_name_label["font"] = self.__name_font            
              current_decision_variable_value_label["font"] = self.__value_font  

              #Finalmente se colocan en el Frame.
              current_decision_variable_name_label.grid(row = current_row,column = 0,padx = (50,9),pady = (1,1),sticky = tk.W)
              current_decision_variable_value_label.grid(row = current_row,column = 1,padx = (1,50),pady = (1,1),sticky = tk.W)               
              current_row += 1
           

          #********POPULATION SETTINGS************
          #A continuación se coloca toda la infraestructura de las características de la población.
          #En primer lugar una variable que mantiene control sobre el renglón actual permitido para
          #agregar elementos.
          population_settings_current_row = 0
          
          #Se obtienen las características de la población (y el Fitness).
          population_settings_information = gathered_information["Population Settings"]

          #Se recaba la técnica usada.
          population_settings_technique = population_settings_information["population_technique"]
 
          #Se obtienen los valores de los parámetros.
          population_settings_technique_parameters_values = population_settings_information["population_parameters"]

          #Se obtienen los parámetros.
          population_settings_technique_parameters = main_features["Population Settings"]["Population"]["techniques"][population_settings_technique]["parameters"]

          #Se crea y coloca el título de la sección no sin antes darle un formato.
          self.__population_settings_title_label = tk.Label(self.__population_settings_title_frame,text = "Population Settings")
          self.__population_settings_title_label["font"] = self.__title_font
          self.__population_settings_title_label.grid(row = 0,column = 0,pady = (15,1),sticky = tk.W)
          self.__population_settings_title_frame.grid_columnconfigure(0,weight = 1)
          
          #Se crean, colocan y decoran etiquetas correspondientes a la técnica usada y al nombre de la técnica. Se actualiza
          #la variable que indica el renglón en el que deben colocarse los elementos.
          self.__population_settings_technique_name_label = tk.Label(self.__population_settings_content_frame,text = "Technique:")
          self.__population_settings_technique_value_label = tk.Label(self.__population_settings_content_frame,text = population_settings_technique)
          self.__population_settings_technique_name_label["font"] = self.__name_font            
          self.__population_settings_technique_value_label["font"] = self.__value_font  
          self.__population_settings_technique_name_label.grid(row = population_settings_current_row,column = 0,padx = (50,9),pady = (1,1),sticky = tk.W)
          self.__population_settings_technique_value_label.grid(row = population_settings_current_row,column = 1,padx = (1,1),pady = (1,1),sticky = tk.W) 
          population_settings_current_row += 1
 
          #Se crean, colocan y decoran etiquetas correspondientes al tamaño de la población y a su valor. Se actualiza
          #la variable que indica el renglón en el que deben colocarse los elementos.          
          self.__population_settings_size_name_label = tk.Label(self.__population_settings_content_frame,text = "Population Size:")
          self.__population_settings_size_value_label = tk.Label(self.__population_settings_content_frame,text = population_settings_information["population_size"])
          self.__population_settings_size_name_label["font"] = self.__name_font            
          self.__population_settings_size_value_label["font"] = self.__value_font  
          self.__population_settings_size_name_label.grid(row = population_settings_current_row,column = 0,padx = (50,9),pady = (1,1),sticky = tk.W)
          self.__population_settings_size_value_label.grid(row = population_settings_current_row,column = 1,padx = (1,50),pady = (1,1),sticky = tk.W)               
          population_settings_current_row += 1
    
          #Se crean, colocan y decoran etiquetas correspondientes al número de decimales y a su valor. Se actualiza
          #la variable que indica el renglón en el que deben colocarse los elementos.          
          self.__population_settings_number_of_decimals_name_label = tk.Label(self.__population_settings_content_frame,text = "Number of Decimals:")
          self.__population_settings_number_of_decimals_value_label = tk.Label(self.__population_settings_content_frame,text = population_settings_information["number_of_decimals"])  
          self.__population_settings_number_of_decimals_name_label["font"] = self.__name_font            
          self.__population_settings_number_of_decimals_value_label["font"] = self.__value_font  
          self.__population_settings_number_of_decimals_name_label.grid(row = population_settings_current_row,column = 0,padx = (50,9),pady = (1,1),sticky = tk.W)
          self.__population_settings_number_of_decimals_value_label.grid(row = population_settings_current_row,column = 1,padx = (1,50),pady = (1,1),sticky = tk.W)               
          population_settings_current_row += 1
     
          #Se crean, colocan y decoran etiquetas correspondientes al número de generaciones y a su valor. Se actualiza
          #la variable que indica el renglón en el que deben colocarse los elementos.          
          self.__population_settings_generations_name_label = tk.Label(self.__population_settings_content_frame,text = "Number of Generations:")
          self.__population_settings_generations_value_label = tk.Label(self.__population_settings_content_frame,text = population_settings_information["number_of_generations"])
          self.__population_settings_generations_name_label["font"] = self.__name_font            
          self.__population_settings_generations_value_label["font"] = self.__value_font  
          self.__population_settings_generations_name_label.grid(row = population_settings_current_row,column = 0,padx = (50,9),pady = (1,1),sticky = tk.W)
          self.__population_settings_generations_value_label.grid(row = population_settings_current_row,column = 1,padx = (1,1),pady = (1,1),sticky = tk.W)               
          population_settings_current_row += 1

          #Si la técnica tiene parámetros asociados, se hace lo siguiente:
          if population_settings_technique_parameters != []:          

             #Se crea, decora y coloca una etiqueta que indica que hay parámetros adicionales; además se actualiza el valor del renglón actual.
             self.__population_settings_additional_parameters_name_label = tk.Label(self.__population_settings_content_frame,text = "Additional Parameters:")
             self.__population_settings_additional_parameters_name_label["font"] = self.__name_font_ii            
             self.__population_settings_additional_parameters_name_label.grid(row = population_settings_current_row,column = 0,padx = (50,9),pady = (10,1),sticky = tk.W)
             population_settings_current_row += 1

             #Se crean, decoran, y alojan etiquetas para el nombre del parámetro y el valor del mismo. Se actualiza la 
             #variable del renglón actual por cada parámetro. 
             for parameter in population_settings_technique_parameters:
                 parameter_name = parameter["name"]
                 parameter_variable = parameter["variable"]
                 parameter_value = population_settings_technique_parameters_values[parameter_variable]
                 population_settings_parameter_name_label = tk.Label(self.__population_settings_content_frame,text = parameter_name + ":")
                 population_settings_parameter_value_label = tk.Label(self.__population_settings_content_frame,text = parameter_value)  
                 population_settings_parameter_name_label["font"] = self.__name_font            
                 population_settings_parameter_value_label["font"] = self.__value_font  
                 population_settings_parameter_name_label.grid(row = population_settings_current_row,column = 0,padx = (75,9),pady = (1,1),sticky = tk.E)
                 population_settings_parameter_value_label.grid(row = population_settings_current_row,column = 1,padx = (1,50),pady = (1,1),sticky = tk.W)               
                 population_settings_current_row += 1
                 

          #********FITNESS SETTINGS************
          #Se crea la infraestructura para colocar los elementos relativos al Fitness.
          #Primero se declara una variable que tenga una referencia actual al renglón disponible
          #en donde se pueda colocar un elemento.
          fitness_settings_current_row = 0

          #Se almacena la técnica seleccionada.
          fitness_settings_technique = population_settings_information["fitness_technique"]

          #Se guardan los valores de los parámetros con los que venía la técnica.
          fitness_settings_technique_parameters_values = population_settings_information["fitness_parameters"]

          #Se almacenan los nombres de los parámetros asociados a la técnica.
          fitness_settings_technique_parameters = main_features["Population Settings"]["Fitness"]["techniques"][fitness_settings_technique]["parameters"]

          #Se crea, decora y coloca una etiqueta alusiva a la sección de Fitness.
          self.__fitness_settings_title_label = tk.Label(self.__fitness_settings_title_frame,text = "Fitness Settings")
          self.__fitness_settings_title_label["font"] = self.__title_font
          self.__fitness_settings_title_label.grid(row = 0,column = 0,pady = (15,1),sticky = tk.W)
          self.__fitness_settings_title_frame.grid_columnconfigure(0,weight = 1)

          #Son creadas, decoradas y colocadas etiquetas para identificar la técnica usada y su valor. Se actualiza
          #también la referencia al renglón actual.
          self.__fitness_settings_technique_name_label = tk.Label(self.__fitness_settings_content_frame,text = "Technique:")
          self.__fitness_settings_technique_value_label = tk.Label(self.__fitness_settings_content_frame,text = fitness_settings_technique) 
          self.__fitness_settings_technique_name_label["font"] = self.__name_font            
          self.__fitness_settings_technique_value_label["font"] = self.__value_font  
          self.__fitness_settings_technique_name_label.grid(row = fitness_settings_current_row,column = 0,padx = (50,9),pady = (1,1),sticky = tk.W)
          self.__fitness_settings_technique_value_label.grid(row = fitness_settings_current_row,column = 1,padx = (1,50),pady = (1,1),sticky = tk.W)  
          fitness_settings_current_row += 1

          #Si la técnica tiene parámetros asociados se hace lo siguiente:
          if fitness_settings_technique_parameters != []:          

             #Se crea, decora y plasma en el Frame una etiqueta que indica que hay parámetros adicionales. También
             #se actualiza la variable del renglón.
             self.__fitness_settings_additional_parameters_name_label = tk.Label(self.__fitness_settings_content_frame,text = "Additional Parameters:")
             self.__fitness_settings_additional_parameters_name_label["font"] = self.__name_font_ii            
             self.__fitness_settings_additional_parameters_name_label.grid(row = fitness_settings_current_row,column = 0,padx = (50,9),pady = (10,1),sticky = tk.W)
             fitness_settings_current_row += 1

             #Por cada parámetro se crean, decoran y acomodan etiquetas referentes al nombre del parámetro y 
             #su valor. También se actualiza la variable que mantiene control sobre el renglón actual.
             for parameter in fitness_settings_technique_parameters:
                 parameter_name = parameter["name"]
                 parameter_variable = parameter["variable"]
                 parameter_value = fitness_settings_technique_parameters_values[parameter_variable]
                 fitness_settings_parameter_name_label = tk.Label(self.__fitness_settings_content_frame,text = parameter_name + ":")
                 fitness_settings_parameter_value_label = tk.Label(self.__fitness_settings_content_frame,text = parameter_value)  
                 fitness_settings_parameter_name_label["font"] = self.__name_font            
                 fitness_settings_parameter_value_label["font"] = self.__value_font  
                 fitness_settings_parameter_name_label.grid(row = fitness_settings_current_row,column = 0,padx = (75,9),pady = (1,1),sticky = tk.E)
                 fitness_settings_parameter_value_label.grid(row = fitness_settings_current_row,column = 1,padx = (1,50),pady = (1,1),sticky = tk.W)               
                 fitness_settings_current_row += 1


          #********SELECTION SETTINGS************
          #Se colocan los elementos gráficos aunados al proceso de Selección.
          #Primero se declara una variable que mantiene control sobre el ranglón
          #actual, esto para evitar problemas de traslape.
          selection_settings_current_row = 0

          #Esta variable nos da las técnicas para la Selección, Cruza y Mutación.
          genetic_operator_settings_information = gathered_information["Genetic Operators Settings"]

          #Se recaba la técnica de selección usada.
          selection_settings_technique = genetic_operator_settings_information["selection_technique"]

          #Se obtienen los valores de los parámetros de la técnica empleada.
          selection_settings_technique_parameters_values = genetic_operator_settings_information["selection_parameters"]

          #Se obtienen los nombres de los parámetros de la técnica usada.
          selection_settings_technique_parameters = main_features["Genetic Operators Settings"]["Selection"]["techniques"][selection_settings_technique]["parameters"]

          #Se crea, decora y coloca una etiqueta alusiva a la sección de selección.
          self.__selection_settings_title_label = tk.Label(self.__selection_settings_title_frame,text = "Selection Settings")
          self.__selection_settings_title_label["font"] = self.__title_font
          self.__selection_settings_title_label.grid(row = 0,column = 0,pady = (15,1),sticky = tk.W)
          self.__selection_settings_title_frame.grid_columnconfigure(0,weight = 1)
          
          #Se crean, decoran y colocan etiquetas concernientes a la técnica empleada y a su valor. Se actualiza
          #la referencia de los renglones.
          self.__selection_settings_technique_name_label = tk.Label(self.__selection_settings_content_frame,text = "Technique:")
          self.__selection_settings_technique_value_label = tk.Label(self.__selection_settings_content_frame,text = selection_settings_technique) 
          self.__selection_settings_technique_name_label["font"] = self.__name_font            
          self.__selection_settings_technique_value_label["font"] = self.__value_font  
          self.__selection_settings_technique_name_label.grid(row = selection_settings_current_row,column = 0,padx = (50,9),pady = (1,1),sticky = tk.W)
          self.__selection_settings_technique_value_label.grid(row = selection_settings_current_row,column = 1,padx = (1,50),pady = (1,1),sticky = tk.W)  
          selection_settings_current_row += 1

          #Si la técnica empleada tiene parámetros aunados, se hace lo siguiente:
          if selection_settings_technique_parameters != []:          

             #Se crea, decora y aloja una etiqueta que permitirá identificar los parámetros, además se actualiza
             #la referencia al renglón actual.
             self.__selection_settings_additional_parameters_name_label = tk.Label(self.__selection_settings_content_frame,text = "Additional Parameters:")
             self.__selection_settings_additional_parameters_name_label["font"] = self.__name_font_ii            
             self.__selection_settings_additional_parameters_name_label.grid(row = selection_settings_current_row,column = 0,padx = (50,9),pady = (10,1),sticky = tk.W)
             selection_settings_current_row += 1

             #Por cada parámetro existente se crean, decoran y colocan etiquetas que contendran el valor de éste,
             #así como su valor. Por cada parámetro se actualiza la variable del control de renglones.
             for parameter in selection_settings_technique_parameters:
                 parameter_name = parameter["name"]
                 parameter_variable = parameter["variable"]
                 parameter_value = selection_settings_technique_parameters_values[parameter_variable]
                 selection_settings_parameter_name_label = tk.Label(self.__selection_settings_content_frame,text = parameter_name + ":")
                 selection_settings_parameter_value_label = tk.Label(self.__selection_settings_content_frame,text = parameter_value)  
                 selection_settings_parameter_name_label["font"] = self.__name_font            
                 selection_settings_parameter_value_label["font"] = self.__value_font  
                 selection_settings_parameter_name_label.grid(row = selection_settings_current_row,column = 0,padx = (75,9),pady = (1,1),sticky = tk.E)
                 selection_settings_parameter_value_label.grid(row = selection_settings_current_row,column = 1,padx = (1,50),pady = (1,1),sticky = tk.W)               
                 selection_settings_current_row += 1


          #********CROSSOVER SETTINGS************
          #Se crean elementos gráficos para soportar la infraestructura relativa a cuestiones de cruza.
          #Primero se tiene una variable que será la referencia entre renglones para que no haya traslapes.
          crossover_settings_current_row = 0

          #Se almacena la técnica usada.
          crossover_settings_technique = genetic_operator_settings_information["crossover_technique"]
     
          #Se obtienen los valores de los parámetros relativos a la técnica usada.
          crossover_settings_technique_parameters_values = genetic_operator_settings_information["crossover_parameters"]

          #Se obtienen los nombres de los parámetros de la técnica empleada.
          crossover_settings_technique_parameters = main_features["Genetic Operators Settings"]["Crossover"]["techniques"][crossover_settings_technique]["parameters"]

          #Se crea, decora y coloca una etiqueta que indicará el inicio de la sección de cruza.
          self.__crossover_settings_title_label = tk.Label(self.__crossover_settings_title_frame,text = "Crossover Settings")
          self.__crossover_settings_title_label["font"] = self.__title_font
          self.__crossover_settings_title_label.grid(row = 0,column = 0,pady = (15,1),sticky = tk.W)
          self.__crossover_settings_title_frame.grid_columnconfigure(0,weight = 1)
          

          #Se crean, decoran y almacenan en el Frame etiquetas que mostrarán la técnica empleada y el valor de ésta.
          #Asímismo se actualiza la variable de referencia de renglones.
          self.__crossover_settings_technique_name_label = tk.Label(self.__crossover_settings_content_frame,text = "Technique:")
          self.__crossover_settings_technique_value_label = tk.Label(self.__crossover_settings_content_frame,text = crossover_settings_technique) 
          self.__crossover_settings_technique_name_label["font"] = self.__name_font            
          self.__crossover_settings_technique_value_label["font"] = self.__value_font  
          self.__crossover_settings_technique_name_label.grid(row = crossover_settings_current_row,column = 0,padx = (50,9),pady = (1,1),sticky = tk.W)
          self.__crossover_settings_technique_value_label.grid(row = crossover_settings_current_row,column = 1,padx = (1,50),pady = (1,1),sticky = tk.W)  
          crossover_settings_current_row += 1

          #Se crean, decoran y almacenan en el Frame etiquetas que mostrarán probabilidad de cruza y el valor de ésta.
          #Asímismo se actualiza la variable de referencia de renglones.        
          self.__crossover_settings_probability_name_label = tk.Label(self.__crossover_settings_content_frame,text = "Probability:")
          self.__crossover_settings_probability_value_label = tk.Label(self.__crossover_settings_content_frame,text = genetic_operator_settings_information["probability_crossover_general"]) 
          self.__crossover_settings_probability_name_label["font"] = self.__name_font            
          self.__crossover_settings_probability_value_label["font"] = self.__value_font  
          self.__crossover_settings_probability_name_label.grid(row = crossover_settings_current_row,column = 0,padx = (50,9),pady = (1,1),sticky = tk.W)
          self.__crossover_settings_probability_value_label.grid(row = crossover_settings_current_row,column = 1,padx = (1,50),pady = (1,1),sticky = tk.W)  
          crossover_settings_current_row += 1

          #Si la técnica trae consigo parámetros adicionales, se hace lo siguiente:
          if crossover_settings_technique_parameters != []: 
          
             #Se crea, decora y acomoda la etiqueta que permitirá discernir la sección de los parámetro adicionales. Se actualiza
             #la variable de la referencia de renglones.         
             self.__crossover_settings_additional_parameters_name_label = tk.Label(self.__crossover_settings_content_frame,text = "Additional Parameters:")
             self.__crossover_settings_additional_parameters_name_label["font"] = self.__name_font_ii            
             self.__crossover_settings_additional_parameters_name_label.grid(row = crossover_settings_current_row,column = 0,padx = (50,9),pady = (10,1),sticky = tk.W)
             crossover_settings_current_row += 1

             #Por cada parámetro, se crea, decora y colocan etiquetas que muestren el nombre del parámetro y 
             #su correspondiente valor. Además se actualiza la  variable de referencia de renglones.
             for parameter in crossover_settings_technique_parameters:
                 parameter_name = parameter["name"]
                 parameter_variable = parameter["variable"]
                 parameter_value = crossover_settings_technique_parameters_values[parameter_variable]
                 crossover_settings_parameter_name_label = tk.Label(self.__crossover_settings_content_frame,text = parameter_name + ":")
                 crossover_settings_parameter_value_label = tk.Label(self.__crossover_settings_content_frame,text = parameter_value)  
                 crossover_settings_parameter_name_label["font"] = self.__name_font            
                 crossover_settings_parameter_value_label["font"] = self.__value_font  
                 crossover_settings_parameter_name_label.grid(row = crossover_settings_current_row,column = 0,padx = (75,9),pady = (1,1),sticky = tk.E)
                 crossover_settings_parameter_value_label.grid(row = crossover_settings_current_row,column = 1,padx = (1,50),pady = (1,1),sticky = tk.W)               
                 crossover_settings_current_row += 1


          #********MUTATION SETTINGS************
          #Las siguientes estructuras gráficas son parte de la infraestructura relacionada con la sección
          #de la mutación.
          #Primero se crea una variable con la que se mantendrá referencia del renglón actual
          #sobre el cual se puede colocar un elemento.
          mutation_settings_current_row = 0

          #Se obtiene la técnica de mutación.
          mutation_settings_technique = genetic_operator_settings_information["mutation_technique"]

          #Ahora se obtienen los valores de los parámetros relativos a la técnica de mutación.
          mutation_settings_technique_parameters_values = genetic_operator_settings_information["mutation_parameters"]

          #A continuación se recaban los nombres de los parámetros asociados a la técnica.
          mutation_settings_technique_parameters = main_features["Genetic Operators Settings"]["Mutation"]["techniques"][mutation_settings_technique]["parameters"]

          #Se crea, decora y coloca una etiqueta alusiva a la sección de los elementos de mutación.
          self.__mutation_settings_title_label = tk.Label(self.__mutation_settings_title_frame,text = "Mutation Settings")
          self.__mutation_settings_title_label["font"] = self.__title_font
          self.__mutation_settings_title_label.grid(row = 0,column = 0,pady = (15,1),sticky = tk.W)
          self.__mutation_settings_title_frame.grid_columnconfigure(0,weight = 1)
          
          #Se crean, decoran y colocan etiquetas que muestran la técnica, así como su valor. Además se actualiza
          #la referencia de los renglones.
          self.__mutation_settings_technique_name_label = tk.Label(self.__mutation_settings_content_frame,text = "Technique:")
          self.__mutation_settings_technique_value_label = tk.Label(self.__mutation_settings_content_frame,text = mutation_settings_technique) 
          self.__mutation_settings_technique_name_label["font"] = self.__name_font            
          self.__mutation_settings_technique_value_label["font"] = self.__value_font  
          self.__mutation_settings_technique_name_label.grid(row = mutation_settings_current_row,column = 0,padx = (50,9),pady = (1,1),sticky = tk.W)
          self.__mutation_settings_technique_value_label.grid(row = mutation_settings_current_row,column = 1,padx = (1,50),pady = (1,1),sticky = tk.W)  
          mutation_settings_current_row += 1
        
          #A continuación las etiquetas para la probabilidad de mutación y su correspondiente valor son creadas,
          #decoradas y colocadas en el Frame. Posteriormente se actualiza la referencia del renglón actual.
          self.__mutation_settings_probability_name_label = tk.Label(self.__mutation_settings_content_frame,text = "Probability:")
          self.__mutation_settings_probability_value_label = tk.Label(self.__mutation_settings_content_frame,text = genetic_operator_settings_information["probability_mutation_general"]) 
          self.__mutation_settings_probability_name_label["font"] = self.__name_font            
          self.__mutation_settings_probability_value_label["font"] = self.__value_font  
          self.__mutation_settings_probability_name_label.grid(row = mutation_settings_current_row,column = 0,padx = (50,9),pady = (1,1),sticky = tk.W)
          self.__mutation_settings_probability_value_label.grid(row = mutation_settings_current_row,column = 1,padx = (1,50),pady = (1,1),sticky = tk.W)  
          mutation_settings_current_row += 1

          #Si la técnica tiene parámetros asociados se hace lo siguiente:
          if mutation_settings_technique_parameters != []:          

             #Se crea, decora y aloja en el Frame una etiqueta que mantenga dividida la sección de los parámetros adicionales.
             #También se actualiza la variable de la referencia de renglones.
             self.__mutation_settings_additional_parameters_name_label = tk.Label(self.__mutation_settings_content_frame,text = "Additional Parameters:")
             self.__mutation_settings_additional_parameters_name_label["font"] = self.__name_font_ii            
             self.__mutation_settings_additional_parameters_name_label.grid(row = mutation_settings_current_row,column = 0,padx = (50,9),pady = (10,1),sticky = tk.W)
             mutation_settings_current_row += 1

             #Por cada parámetro se crean etiquetas que son decoradas y colocadas en el Frame, éstas contendrán
             #el nombre del parámetro, así como su respectivo valor. Además se actualiza la variable de referencia
             #de renglones.
             for parameter in mutation_settings_technique_parameters:
                 parameter_name = parameter["name"]
                 parameter_variable = parameter["variable"]
                 parameter_value = mutation_settings_technique_parameters_values[parameter_variable]
                 mutation_settings_parameter_name_label = tk.Label(self.__mutation_settings_content_frame,text = parameter_name + ":")
                 mutation_settings_parameter_value_label = tk.Label(self.__mutation_settings_content_frame,text = parameter_value)  
                 mutation_settings_parameter_name_label["font"] = self.__name_font            
                 mutation_settings_parameter_value_label["font"] = self.__value_font  
                 mutation_settings_parameter_name_label.grid(row = mutation_settings_current_row,column = 0,padx = (75,9),pady = (1,1),sticky = tk.E)
                 mutation_settings_parameter_value_label.grid(row = mutation_settings_current_row,column = 1,padx = (1,50),pady = (1,1),sticky = tk.W)               
                 mutation_settings_current_row += 1
          
          #********SHARING FUNCTION SETTINGS************
          #A continuación se crean elementos que formarán la infraestructura para atributos relacionados con
          #el Sharing Function.
          #Primero se crea la variable que mantiene control sobre el renglón actual en el que se puede agregar
          #un elemento.
          sharing_function_settings_current_row = 0

          #Con esta variable se obtienen los parámetros de técnicas de MOEAs y Sharing Functions
          moea_settings_information = gathered_information["MOEAs Settings"]

          #Se obtiene la técnica elegida.
          sharing_function_settings_technique = moea_settings_information["sharing_function_technique"]

          #Se obtienen los valores de los parámetros relativos a la técnica.
          sharing_function_settings_technique_parameters_values = moea_settings_information["sharing_function_parameters"]

          #Se obtienen los nombres de los parámetros relacionados con la técnica.
          sharing_function_settings_technique_parameters = main_features["MOEAs Settings"]["Sharing Function"]["techniques"][sharing_function_settings_technique]["parameters"]

          #A continuación se crea, decora y almacena una etiqueta que indica 
          #el inicio de características del Sharing Function.
          self.__sharing_function_settings_title_label = tk.Label(self.__sharing_function_settings_title_frame,text = "Sharing Function Settings")
          self.__sharing_function_settings_title_label["font"] = self.__title_font
          self.__sharing_function_settings_title_label.grid(row = 0,column = 0,pady = (15,1),sticky = tk.W)
          self.__sharing_function_settings_title_frame.grid_columnconfigure(0,weight = 1)
 
          #Ahora se crean, decoran y almacenan etiquetas que contendrán valores relacionados con la técnica y el valor de ésta.
          #Adicionalmente se actualiza la variable de la referencia de renglones.
          self.__sharing_function_settings_technique_name_label = tk.Label(self.__sharing_function_settings_content_frame,text = "Technique:")
          self.__sharing_function_settings_technique_value_label = tk.Label(self.__sharing_function_settings_content_frame,text = sharing_function_settings_technique) 
          self.__sharing_function_settings_technique_name_label["font"] = self.__name_font            
          self.__sharing_function_settings_technique_value_label["font"] = self.__value_font  
          self.__sharing_function_settings_technique_name_label.grid(row = sharing_function_settings_current_row,column = 0,padx = (50,9),pady = (1,1),sticky = tk.W)
          self.__sharing_function_settings_technique_value_label.grid(row = sharing_function_settings_current_row,column = 1,padx = (1,50),pady = (1,1),sticky = tk.W)  
          sharing_function_settings_current_row += 1

          #Luego se crean, decoran y colocan etiquetas concernientes a la variable Alpha y su respectivo valor. También se actualiza
          #la variable de referencia de renglones.
          self.__sharing_function_settings_alpha_name_label = tk.Label(self.__sharing_function_settings_content_frame,text = "Alpha:")
          self.__sharing_function_settings_alpha_value_label = tk.Label(self.__sharing_function_settings_content_frame,text = moea_settings_information["alpha_sharing_function"]) 
          self.__sharing_function_settings_alpha_name_label["font"] = self.__name_font            
          self.__sharing_function_settings_alpha_value_label["font"] = self.__value_font  
          self.__sharing_function_settings_alpha_name_label.grid(row = sharing_function_settings_current_row,column = 0,padx = (50,9),pady = (1,1),sticky = tk.W)
          self.__sharing_function_settings_alpha_value_label.grid(row = sharing_function_settings_current_row,column = 1,padx = (1,50),pady = (1,1),sticky = tk.W)  
          sharing_function_settings_current_row += 1

          #Si la técnica empleada contiene parámetros asociados, se hace lo siguiente:
          if sharing_function_settings_technique_parameters != []:          

             #Se crea, decora y acomoda una etiqueta que indica el inicio de los parámetros adicionales.
             self.__sharing_function_settings_additional_parameters_name_label = tk.Label(self.__sharing_function_settings_content_frame,text = "Additional Parameters:")
             self.__sharing_function_settings_additional_parameters_name_label["font"] = self.__name_font_ii            
             self.__sharing_function_settings_additional_parameters_name_label.grid(row = sharing_function_settings_current_row,column = 0,padx = (50,9),pady = (10,1),sticky = tk.W)
             sharing_function_settings_current_row += 1

             #Por cada parámetro aunado a la técnica se crean, decoran y colocan etiquetas que contendrán el nombre del parámetro y su valor.
             #También se actualiza la variable de referencia de renglones.
             for parameter in sharing_function_settings_technique_parameters:
                 parameter_name = parameter["name"]
                 parameter_variable = parameter["variable"]
                 parameter_value = sharing_function_settings_technique_parameters_values[parameter_variable]
                 sharing_function_settings_parameter_name_label = tk.Label(self.__sharing_function_settings_content_frame,text = parameter_name + ":")
                 sharing_function_settings_parameter_value_label = tk.Label(self.__sharing_function_settings_content_frame,text = parameter_value)  
                 sharing_function_settings_parameter_name_label["font"] = self.__name_font            
                 sharing_function_settings_parameter_value_label["font"] = self.__value_font  
                 sharing_function_settings_parameter_name_label.grid(row = sharing_function_settings_current_row,column = 0,padx = (75,9),pady = (1,1),sticky = tk.E)
                 sharing_function_settings_parameter_value_label.grid(row = sharing_function_settings_current_row,column = 1,padx = (1,50),pady = (1,1),sticky = tk.W)               
                 sharing_function_settings_current_row += 1

          #********MOEA SETTINGS************
          #A continuación se colocan elementos para la base gráfica del MOEA y sus atributos.
          #Primero se declara una variable que mantiene control sobre los renglones en los que se puede
          #agregar elementos, ésto para que no se traslapen.
          moea_settings_current_row = 0

          #Se obtiene la técnica de MOEA.
          moea_settings_technique = moea_settings_information["moea_technique"]

          #Con esta variable los valores de los parámetros aunados a la técnica MOEA son obtenidos.
          moea_settings_technique_parameters_values = moea_settings_information["moea_parameters"]

          #Se asignan los nombres de los parámetros de la técnica MOEA.
          moea_settings_technique_parameters = main_features["MOEAs Settings"]["MOEA"]["techniques"][moea_settings_technique]["parameters"]

          #A continuación se crea, decora y coloca una etiqueta que establece el inicio de los atributos para MOEA.
          self.__moea_settings_title_label = tk.Label(self.__moea_settings_title_frame,text = "M.O.E.A. Settings")
          self.__moea_settings_title_label["font"] = self.__title_font
          self.__moea_settings_title_label.grid(row = 0,column = 0,pady = (15,1),sticky = tk.W)
          self.__moea_settings_title_frame.grid_columnconfigure(0,weight = 1)

          #Ahora se crean, decoran y establecen en el Frame etiquetas que contendrán la técnica y el valor de ésta.
          #También se actualiza la varial de referencia de renglones.
          self.__moea_settings_technique_name_label = tk.Label(self.__moea_settings_content_frame,text = "Technique:")
          self.__moea_settings_technique_value_label = tk.Label(self.__moea_settings_content_frame,text = moea_settings_technique) 
          self.__moea_settings_technique_name_label["font"] = self.__name_font            
          self.__moea_settings_technique_value_label["font"] = self.__value_font  
          self.__moea_settings_technique_name_label.grid(row = moea_settings_current_row,column = 0,padx = (50,9),pady = (1,1),sticky = tk.W)
          self.__moea_settings_technique_value_label.grid(row = moea_settings_current_row,column = 1,padx = (1,50),pady = (1,1),sticky = tk.W)  
          moea_settings_current_row += 1

          #Si la técnica contiene parámetros asociados, se hace lo siguiente:
          if moea_settings_technique_parameters != []:          

             #Se crea, decora y anexa una etiqueta que indique que la sección de parámetros adicionales comienza. También se actualiza
             #la variable de la referencia de renglones.
             self.__moea_settings_additional_parameters_name_label = tk.Label(self.__moea_settings_content_frame,text = "Additional Parameters:")
             self.__moea_settings_additional_parameters_name_label["font"] = self.__name_font_ii            
             self.__moea_settings_additional_parameters_name_label.grid(row = moea_settings_current_row,column = 0,padx = (50,9),pady = (10,1),sticky = tk.W)
             moea_settings_current_row += 1

             #Por cada parámetro de la técnica, se crean, decoran y alojan etiquetas que almacenen el nombre del parámetro
             #y su valor. Además por cada paŕámetro se actualiza la variable de control de la referencia de renglones.
             for parameter in moea_settings_technique_parameters:
                 parameter_name = parameter["name"]
                 parameter_variable = parameter["variable"]
                 parameter_value = moea_settings_technique_parameters_values[parameter_variable]
                 moea_settings_parameter_name_label = tk.Label(self.__moea_settings_content_frame,text = parameter_name + ":")
                 moea_settings_parameter_value_label = tk.Label(self.__moea_settings_content_frame,text = parameter_value)  
                 moea_settings_parameter_name_label["font"] = self.__name_font            
                 moea_settings_parameter_value_label["font"] = self.__value_font  
                 moea_settings_parameter_name_label.grid(row = moea_settings_current_row,column = 0,padx = (75,9),pady = (1,1),sticky = tk.E)
                 moea_settings_parameter_value_label.grid(row = moea_settings_current_row,column = 1,padx = (1,50),pady = (1,1),sticky = tk.W)               
                 moea_settings_current_row += 1

          #A continuacion los Frames relativos a OBJECTIVE FUNCTIONS se colocan en el Frame Padre.
          self.__objective_functions_title_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True)
          self.__objective_functions_content_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True)
          
          #Posteriormente los que son concernientes a DECISION VARIABLES se agrupan en el Frame Padre.
          self.__decision_variables_title_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True) 
          self.__decision_variables_content_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True) 
          
          #Ahora aquellos Frames que tengan que ver con POPULATION SETTINGS son puestos en el Frame Padre.
          self.__population_settings_title_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True) 
          self.__population_settings_content_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True) 
          
          #Así, los Frames que tengan información de FITNESS SETTINGS se colocan en el Frame Padre.
          self.__fitness_settings_title_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True) 
          self.__fitness_settings_content_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True) 
          
          #Luego, los Frames de SELECTION SETTINGS son anidados al Frame Padre.
          self.__selection_settings_title_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True)  
          self.__selection_settings_content_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True)  
          
          #Entonces, los Frames para CROSSOVER SETTINGS son alojados en el Frame Padre.
          self.__crossover_settings_title_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True)  
          self.__crossover_settings_content_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True)  
          
          #Continuando, los Frames que sean relativos a MUTATION SETTINGS se mueven al Frame Padre.
          self.__mutation_settings_title_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True)  
          self.__mutation_settings_content_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True)  
          
          #Posteriormente, aquéllos que tengan que ver con MOEA SETTINGS son movidos al Frame Padre.
          self.__moea_settings_title_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True)  
          self.__moea_settings_content_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True)  
          
          #Para finalizar, los Frames alusivos a SHARING FUNCTION SETTINGS se mezclan en el Frame Padre.
          self.__sharing_function_settings_title_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True)  
          self.__sharing_function_settings_content_frame.pack(side = tk.TOP,fill = tk.BOTH,expand = True)
