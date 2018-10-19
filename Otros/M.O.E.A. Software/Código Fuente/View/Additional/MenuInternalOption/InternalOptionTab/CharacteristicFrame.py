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


class CharacteristicFrame(tk.Frame):
      """
         | Despliega información concerniente a todas las técnicas 
          **(con sus respectivos parámetros)** disponibles para el usuario.
         | Se agrupan éstas en las mismas categorías que presenta el programa,
          más en concreto, las secciones que conforman a la Ventana Principal 
          **(véase View/MainWindow.py)**.
         |
         | También señala someramente las instrucciones necesarias para que el
          programa pueda reconocer cualquier técnica que desarrolle el usuario.
    
         :param parent: El elemento Padre al que pertenece el actual
                        Frame.
         :param features: Un diccionario que contiene las características necesarias
                          que serán mostradas en este Frame. 
 
         :type parent: Tkinter.Toplevel
         :type features: Dictionary
         :returns: El Frame que contiene la información señalada.
         :rtype: Tkinter.Frame
      """


      def __init__(self,parent,features):
          #Se crea el Frame sobre el cual descansará toda la infraestructura gráfica. 
          tk.Frame.__init__(self,parent)

          #Se crearán dos Frames secundarios con la finalidad de poder acomodar mejor
          #la información que se presenta en este Frame.
          #__information_frame mantiene los elementos necesarios para dar instrucciones
          #someras pero concisas al usuario.
          #__techniques_frame muestra todo el listado de tecnicas disponibles para 
          #el usuario.
          self.__information_frame = tk.Frame(self)
          self.__techniques_frame = tk.Frame(self)

          #Esta variable es creada para poder tener una referencia rápida del renglón actual
          #sobre el cual se puede hacer una inserción o eliminación de elementos.
          self.__current_row = 0

          #A continuación se crean las tipografías que serán empleadas para mostrar
          #la información pertinente.
          self.__name_font = tkf.Font(family = "Helvetica",size = 10,weight = "bold")

          #Estas fuentes indican el tipo de contenido que se coloca.
          self.__category_title_font = tkf.Font(family = "Helvetica",size = 11,weight = "bold")
          self.__division_title_font = tkf.Font(family = "Helvetica",size = 10,weight = "bold")
          self.__technique_title_font = tkf.Font(family = "Helvetica",size = 9,weight = "bold")
          
          #Las siguientes fuentes resaltan el contenido que se muestra. 
          self.__category_content_font = tkf.Font(family = "Helvetica",size = 11)
          self.__division_content_font = tkf.Font(family = "Helvetica",size = 10)
          self.__technique_content_font = tkf.Font(family = "Helvetica",size = 9)
          
          #A continuación se desarrollan Labels (Labels) que contendrán la información
          #básica del comportamiento de esta sección.
          self.__information_1_label = tk.Label(self.__information_frame,text = "The following section shows all the techniques with their respective parameters, currently")
          self.__information_2_label = tk.Label(self.__information_frame,text = "stored at the tier Model and therefore available for the user.")
          self.__information_3_label = tk.Label(self.__information_frame,text = "The main goal is, once implemented a certain technique, track it down so the user have ")
          self.__information_4_label = tk.Label(self.__information_frame,text = "the updated references of the current technique. ")
          self.__information_5_label = tk.Label(self.__information_frame,text = "It also allows to execute those techniques faster and without much burocracy because at ")
          self.__information_6_label = tk.Label(self.__information_frame,text = "a given technique the user implements only what it is needed.")                  
          self.__information_7_label = tk.Label(self.__information_frame,text = "Besides developing the technique at Model, the user has to insert its name (among other ")                  
          self.__information_8_label = tk.Label(self.__information_frame,text = "data) at Controller/XML/Features.xml in order to establish its usage.")                  

          #A las Labels antes mencionadas se les da el formato adecuado.
          self.__information_1_label["font"] = self.__name_font         
          self.__information_2_label["font"] = self.__name_font
          self.__information_3_label["font"] = self.__name_font
          self.__information_4_label["font"] = self.__name_font
          self.__information_5_label["font"] = self.__name_font
          self.__information_6_label["font"] = self.__name_font
          self.__information_7_label["font"] = self.__name_font
          self.__information_8_label["font"] = self.__name_font

          #Se colocan los Labels en cuestión en su Frame padre (__information_frame).
          self.__information_1_label.grid(row = 0,column = 0,padx = (5,1),pady = (10,1),sticky = tk.W)
          self.__information_2_label.grid(row = 1,column = 0,padx = (5,1),pady = (1,1),sticky = tk.W)
          self.__information_3_label.grid(row = 2,column = 0,padx = (5,1),pady = (1,1),sticky = tk.W)
          self.__information_4_label.grid(row = 3,column = 0,padx = (5,1),pady = (1,1),sticky = tk.W)
          self.__information_5_label.grid(row = 4,column = 0,padx = (5,1),pady = (1,1),sticky = tk.W)
          self.__information_6_label.grid(row = 5,column = 0,padx = (5,1),pady = (1,1),sticky = tk.W)
          self.__information_7_label.grid(row = 6,column = 0,padx = (5,1),pady = (1,1),sticky = tk.W)
          self.__information_8_label.grid(row = 7,column = 0,padx = (5,1),pady = (1,1),sticky = tk.W)

          #Si la estructura que almacena los features NO contiene la llave "recent"
          #significa que los datos se recolectaron apropiadamente por lo que se puede
          #proseguir con la operación, por el contrario si tal llave existe entonces hubo
          #un problema con la lectura de los datos y se interrumpe el proceso.
          if not(features.has_key("recent")):

             #Los elementos principales a colocar son las categorías, éstas
             #distinguen a grandes rasgos la ubicación de las técnicas, de modo que
             #son los primeros elementos para mostrar.
             for category in features.keys():
              
                 #Se crean las Labels que indican que se trata de una categoría y el contenido
                 #de ésta respectivamente.
                 category_title_label = tk.Label(self.__techniques_frame,text = "Category:")
                 category_content_label = tk.Label(self.__techniques_frame,text = category)

                 #A continuación se le da el formato apropiado a las Labels anteriores.
                 category_title_label["font"] = self.__category_title_font
                 category_content_label["font"] = self.__category_content_font

                 #Ahora se colocan ambas Labels en forma de grid (o malla).
                 category_title_label.grid(row = self.__current_row,column = 0,padx = (75,1),pady = (17,1),sticky = tk.W)
                 category_content_label.grid(row = self.__current_row,column = 1,padx = (1,1),pady = (17,1),sticky = tk.W)
              
                 #Se actualiza el renglón actual sobre el cual se pueden seguir insertando
                 #elementos.
                 self.__current_row += 1 
              
                 #Cada categoría tiene un número de divisiones asociado, entonces se obtienen
                 #las divisiones de la categoría actual.
                 divisions = features[category]

                 #Ahora los elementos a colocarse son las divisiones.
                 for division in divisions.keys():

                     #Se crean las Labels que indicarán que el elemento es una división, además
                     #del contenido en sí, respectivamente.
                     division_title_label = tk.Label(self.__techniques_frame,text = "Division:")
                     division_content_label = tk.Label(self.__techniques_frame,text = division)

                     #A las Labels descritas anteriormente se les asigna el formato adecuado.
                     division_title_label["font"] = self.__division_title_font
                     division_content_label["font"] = self.__division_content_font

                     #Se agregan ambos elementos en forma de malla (grid).
                     division_title_label.grid(row = self.__current_row,column = 0,padx = (90,1),pady = (12,1),sticky = tk.W)
                     division_content_label.grid(row = self.__current_row,column = 1,padx = (1,1),pady = (12,1),sticky = tk.W)

                     #Se incrementa el contador de renglones para indicar el espacio
                     #en el que se pueden agregar nuevos elementos.
                     self.__current_row += 1 

                     #Cada división consta de técnicas, entonces aquí se obtienen aquéllas
                     #asociadas a una división dada.
                     division_techniques = features[category][division]["techniques"]

                     #Entonces la búsqueda prosigue por cada técnica.          
                     for technique in division_techniques.keys():

                         #A continuación se crean Labels para almacenar el tipo de elemento (en este caso
                         #una técnica) y su contenido respectivamente.
                         technique_title_label = tk.Label(self.__techniques_frame,text = "Technique:")
                         technique_content_label = tk.Label(self.__techniques_frame,text = technique)

                         #A los Labels anteriores se les asigna el formato adecuado.
                         technique_title_label["font"] = self.__technique_title_font
                         technique_content_label["font"] = self.__technique_content_font

                         #Se colocan los elementos en el Frame correspondiente.
                         technique_title_label.grid(row = self.__current_row,column = 0,padx = (115,1),pady = (7,1),sticky = tk.W)
                         technique_content_label.grid(row = self.__current_row,column = 1,padx = (1,1),pady = (7,1),sticky = tk.W)

                         #Se actualiza el renglón inmediatamente disponible en el que se pueden seguir
                         #agregando elementos.
                         self.__current_row += 1 

                         #Cada técnica puede tener asociada parámetros, los cuales son valores 
                         #adicionales necesarios para poder alimentar la técnica correctamente.
                         #En esta línea se obtienen dichos parámetros.
                         technique_parameters = features[category][division]["techniques"][technique]["parameters"]
                      
                         #Por cada parámetro se hace lo siguiente:
                         for parameter in technique_parameters:
                          
                             #Se obtienen tanto el nombre como el tipo del parámetro.
                             parameter_name = parameter["name"]
                             parameter_type = parameter["type"]

                             #Aquí se colocará la información completa sobre el parámetro.
                             parameter_complete_name = ""
                 
                             #Si el parámetro es de tipo "float" o "int" se hace lo siguiente:
                             if parameter_type != "bool":
                             
                                #Primero se construyen los límites del rango del parámetro.
                                parameter_lower_range_bracket = "["
                                parameter_upper_range_bracket = "]"

                                #A continuación se obtienen los límites del parámetro.
                                parameter_lower_range = parameter["lower_range"]
                                parameter_upper_range = parameter["upper_range"]
                             
                                #Si el límite inferior del parámetro es "-" significa que está
                                #indeterminado, por lo que se considera como infinito (inf).
                                if parameter_lower_range == "-":
                                   parameter_lower_range = "-Inf"          
                                   parameter_lower_range_bracket = "("
   
                                #Si el límite superior del parámetro es "-" significa que está
                                #indeterminado, por lo que se considera como infinito (inf).                             
                                if parameter_upper_range == "-":
                                   parameter_upper_range = "Inf"          
                                   parameter_upper_range_bracket = ")"

                                #A la variable original se le agrega su tipo y rango transformado 
                                #en el que se llevó a cabo su evaluación.
                                complete_variable =  u"{0} ({1}) ∈  {2} {3} , {4} {5}".format(parameter_name,parameter_type,parameter_lower_range_bracket,parameter_lower_range,parameter_upper_range,parameter_upper_range_bracket)
                                parameter_complete_name = complete_variable.encode("utf-8")

                             #Si el parámetro es de tipo bool significa que no tiene rango y sólo se añade su nombre
                             #con el tipo.
                             else:
                                parameter_complete_name = parameter_name + " (" + parameter_type + ")"

                             #A continuación se crean dos Labels, una para indicar que el elemento actual es un parámetro
                             #mientras que el otro es el contenido del mismo.
                             parameter_title_label = tk.Label(self.__techniques_frame,text = "Parameter:")
                             parameter_content_label = tk.Label(self.__techniques_frame,text = parameter_complete_name)
   
                             #A los Labels se les otorga el formato adecuado.
                             parameter_title_label["font"] = self.__technique_title_font
                             parameter_content_label["font"] = self.__technique_content_font

                             #Los Labels se colocan en el Frame indicado.
                             parameter_title_label.grid(row = self.__current_row,column = 0,padx = (130,1),pady = (1,1),sticky = tk.W)
                             parameter_content_label.grid(row = self.__current_row,column = 1,padx = (1,1),pady = (1,1),sticky = tk.W)
                       
                             #Se actualiza la referencia al renglón actual en el que se pueden
                             #agregar elementos al Frame.
                             self.__current_row += 1 

          #Finalmente se añaden los Frames secundarios al Frame principal.
          self.__information_frame.grid(row = 0,column = 0,sticky = tk.N + tk.S + tk.E + tk.W)
          self.__techniques_frame.grid(row = 1,column = 0,sticky = tk.N + tk.S + tk.E + tk.W)
