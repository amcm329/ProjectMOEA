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


class MOPFrame(tk.Frame):
      """
         Muestra la información relativa a los M.O.P.'s y
         provee de métodos que facilitan la carga de éstos en la
         Ventana Principal.
         Un M.O.P. **(Multi Objective Problem)** es un conjunto de funciones
         y variables bien definidas que ya han sido previamente estudiadas,
         así como su comportamiento en conjunto; la idea es proporcionarle al
         usuario un ambiente de carga fácil de datos para que pueda probar los
         ejemplos ya tratados por muchos autores en los libros que se citarán
         en el trabajo escrito.

         :param parent: El elemento Padre al que pertenece el actual
                        Frame.
         :param grandparent: El elemento Padre del Padre al que pertenece el actual
                             Frame.
         :param features: Un diccionario que contiene las características necesarias
                          que serán mostradas en este Frame. 
 
         :type parent: Tkinter.Frame
         :type grandparent: Tkinter.Toplevel
         :type features: Dictionary
         :returns: El Frame que contiene la información señalada.
         :rtype: Tkinter.Frame
      """

      
      def __init__(self,parent,grandparent,features): 

          #Se crea el Frame principal sobre el que descansará
          #toda la información gráfica.
          tk.Frame.__init__(self,parent)

          #Se guarda una referencia al elemento "abuelo" (el Padre del Padre)
          #de este Frame.
          self.__parent = grandparent

          #Se obtiene la información completa de todos los M.O.P.'s y sus
          #características.
          self.__features = features[0]

          #Se obtiene una referencia a la función que permitirá
          #la carga de elementos en la Ventana Principal.
          self.__parent_load_mop_example = features[1]
          
          #Este es un listado de todos los nombres de los M.O.P.'s 
          #disponibles.
          self.__available_mops = self.__features.keys()	

          #Aquí se almacenarán los elementos gráficos relacionados
          #con la información que se mostrará cada vez que el usuario
          #seleccione un M.O.P.          
          self.__current_mop_displayed = []

          #A continuación se crean las tipografías que serán empleadas para mostrar
          #la información pertinente.
          self.__title_font = tkf.Font(family = "Helvetica",size = 11,weight = "bold")
          self.__name_font = tkf.Font(family = "Helvetica",size = 10,weight = "bold")
          self.__value_font = tkf.Font(family = "Helvetica",size = 10)

          #El primer Frame tendrá un esbozo de información rápida para orientar al usuario,
          #el segundo Frame contendrá los elementos relatvos a los posibles M.O.P. y el Button que
          #garantiza su elección mientras que el tercero mostrará el contenido de los M.O.P.
          #seleccionados en el primer Frame.
          self.__information_frame = tk.Frame(self)
          self.__options_frame = tk.Frame(self)
          self.__features_frame = tk.Frame(self)

          #Se crean Labels de información que dan una descripción
          #breve de un M.O.P. y sus aditamentos, así como una breve guía para
          #agregar más.
          self.__information_1_label = tk.Label(self.__information_frame,text = "The M.O.P. (Multi Objective Problem) is a set of well-defined variables, functions and their ")
          self.__information_2_label = tk.Label(self.__information_frame,text = "behavior; they are widely used because of their known results. If you want a new M.O.P. you ")
          self.__information_3_label = tk.Label(self.__information_frame,text = "must add it manually using the XML file located at Controller/XML/MOPExamples.xml ")
          self.__information_4_label = tk.Label(self.__information_frame,text = "and rerun the program. Check out the current examples in the file for a better orientation.") 
          self.__information_1_label["font"] = self.__name_font
          self.__information_2_label["font"] = self.__name_font
          self.__information_3_label["font"] = self.__name_font
          self.__information_4_label["font"] = self.__name_font
  
          #Se colocan los Labels de información en forma de grid (malla) en el contenedor Padre
          #correspondiente (Options Frame).
          self.__information_1_label.grid(row = 0,column = 0,columnspan = 4,padx = (5,1),pady = (10,1),sticky = tk.W)
          self.__information_2_label.grid(row = 1,column = 0,columnspan = 4,padx = (5,1),pady = (1,1),sticky = tk.W)
          self.__information_3_label.grid(row = 2,column = 0,columnspan = 4,padx = (5,1),pady = (1,1),sticky = tk.W)
          self.__information_4_label.grid(row = 3,column = 0,columnspan = 4,padx = (5,1),pady = (1,1),sticky = tk.W)

          #Si los features no incluyen una llave que se llame "recent", significa que
          #se colocan en el Frame junto con los Buttons y el OptionMenu, en otro caso 
          #se omite esta operación debido a un fallo en la lectura del archivo .xml
          #en el que se basa esta sección.
          if not(self.__features.has_key("recent")):

             #Esta variable permite identificar la selección de M.O.P.
             #hecha por el usuario.
             self.__current_mop = tk.StringVar()
             self.__current_mop.set(self.__available_mops[0])          

             #Se crea el Button para cargar en la Ventana Principal el M.O.P. seleccionado
             #por el usuario, también se le da el formato apropiado y la función que se
             #activa al presionar el botón es ligada a éste.
             self.__load_mop_button = tk.Button(self.__options_frame,text = "Load Current M.O.P.")
             self.__load_mop_button["font"] = self.__title_font
             self.__load_mop_button.bind("<ButtonRelease-1>",self.__get_mop_example)

             #Se crea la Label para identificar la sección del menú de opciones.
             #Además se le da el formato correspondiente.
             self.__mop_option_menu_label = tk.Label(self.__options_frame,text = "Current M.O.P.:")
             self.__mop_option_menu_label["font"] = self.__title_font

             #Se crea el menú de opciones que incluirá todos los M.O.P.'s disponibles
             #para que el usuario pueda seleccionar uno de ellos.
             #También se le da el formato pertinente. 
             self.__mop_option_menu = tk.OptionMenu(self.__options_frame,self.__current_mop,*self.__available_mops,command = self.__update_current_mop)
             self.__mop_option_menu["font"] = self.__title_font  

             #Se coloca el Button en forma de grid (malla) en el contenedor Padre
             #correspondiente (Options Frame).
             self.__load_mop_button.grid(row = 0,column = 0,columnspan = 4,pady = (11,1),sticky = tk.N + tk.S)
          
             #Se colocan la Label del menú de opciones y el menú de opciones 
             #en forma de grid (malla) en el contenedor Padre correspondiente (Options Frame).
             self.__mop_option_menu_label.grid(row = 1,column = 0,padx = (13,10),pady = (15,10),sticky = tk.N + tk.S)
             self.__mop_option_menu.grid(row = 1,column = 1,padx = (1,1),pady = (13,10),sticky = tk.N + tk.S)
          
             #Se manda llamar a la función que actualiza la información
             #desplegada acorde al M.O.P. seleccionado.
             self.__update_current_mop()

          #Se colocan los Frames principales en su contenedor Padre,
          #el cual es el Frame principal.
          self.__information_frame.pack()
          self.__options_frame.pack()
          self.__features_frame.pack()
          

      def __update_current_mop(self,event = None):
          """
             .. note:: Este método es privado.

             Despliega la información relacionada con el
             M.O.P. seleccionado.

             :param event: El evento del elemento gráfico que
                           activa esta función.

             :type event: String
          """

          #Primero se eliminan de la pantalla los
          #elementos gráficos de una selección anterior.
          for element in self.__current_mop_displayed:
              element.destroy()

          #Se mantiene una referencia acerca del renglón sobre
          #el que se pueden insertar elementos gráficos.
          my_current_row = 0

          #Se obtiene toda la información relacionada con el M.O.P.
          #que el usuario ha seleccionado.
          current_mop = self.__features[self.__current_mop.get()]

          #Estos contadores permiten llevar un orden entre funciones
          #y variables.
          function_count = 1
          variable_count = 1

          #Se obtienen las funciones y variables asociadas con el M.O.P.
          #elegido.
          functions = current_mop[0]
          variables = current_mop[1]
          
          #Se crea la Label que indicará el comienzo de la sección de
          #funciones asociadas al M.O.P. También se le da el formato a dicha 
          #Label.
          function_label = tk.Label(self.__features_frame,text = "Functions:")
          function_label["font"] = self.__title_font

          #Se agrega este elemento gráfico en el contenedor de elementos
          #gráficos actualmente en la pantalla.
          self.__current_mop_displayed.append(function_label) 

          #Se coloca dicha Label en la pantalla y se actualiza 
          #la referencia de renglones.
          function_label.grid(row = my_current_row,column = 0,padx = (5,1),pady = (5,5),sticky = tk.W)
          my_current_row += 1

          #Por cada función se hará lo siguiente:
          for function in functions:
              #Se crea la Label que llevará la nomenclatura de la función.
              #También se le da el formato apropiado.
              current_function_id = tk.Label(self.__features_frame,text = "F{0}:".format(function_count))
              current_function_id["font"] = self.__name_font

              #Se crea la Label que contendrá la función, además se le da el
              #formato pertinente.
              current_function_label = tk.Label(self.__features_frame,text = function)
              current_function_label["font"] = self.__value_font

              #Ambos Labels son agregados a la lista de elementos gráficos actualmente
              #mostrados.
              self.__current_mop_displayed.append(current_function_id)
              self.__current_mop_displayed.append(current_function_label)

              #Ambos Labels se colocan en la pantalla.
              current_function_id.grid(row = my_current_row,column = 0,padx = (30,1),pady = (5,5),sticky = tk.E)
              current_function_label.grid(row = my_current_row,column = 1,padx = (5,1),pady = (5,5),sticky = tk.W)

              #Se actualizan las referencias tanto del renglón actual
              #como de la función siguiente.
              my_current_row += 1
              function_count += 1
          
          #Se crea la Label que indicará el comienzo de la sección de
          #variables asociadas al M.O.P. También se le da el formato a dicha 
          #Label.    
          variable_label = tk.Label(self.__features_frame,text = "Variables:")
          variable_label["font"] = self.__title_font

          #Se agrega este elemento gráfico en el contenedor de elementos
          #gráficos actualmente en la pantalla.
          self.__current_mop_displayed.append(variable_label)

          #Se coloca dicha Label en la pantalla y se actualiza 
          #la referencia de renglones.
          variable_label.grid(row = my_current_row,column = 0,padx = (5,1),pady = (5,5),sticky = tk.W)
          my_current_row += 1
           
          #Por cada variable se hace lo siguiente:
          for variable in variables:
              #Se obtienen el nombre de la variable así como sus rangos mínimo y máximo.
              name = variable[0]
              lower_range = variable[1]
              upper_range = variable[2]

              #Se crea la Label que llevará la nomenclatura de la variable.
              #También se le da el formato apropiado.
              current_variable_id = tk.Label(self.__features_frame,text = "V{0}:".format(variable_count))
              current_variable_id["font"] = self.__name_font
             
              #Se crea la Label que contendrá la variable, además se le da el
              #formato pertinente.
              encoded_string = u"{0}  ∈  [ {1} , {2} ]".format(name,lower_range,upper_range)
              current_variable_label = tk.Label(self.__features_frame,text = encoded_string.encode("utf8"))
              current_variable_label["font"] = self.__value_font

              #Ambos Labels son agregados a la lista de elementos gráficos actualmente
              #mostrados.
              self.__current_mop_displayed.append(current_variable_id)
              self.__current_mop_displayed.append(current_variable_label)

              #Ambos Labels se colocan en la pantalla.              
              current_variable_id.grid(row = my_current_row,column = 0,padx = (30,1),pady = (5,5),sticky = tk.E)
              current_variable_label.grid(row = my_current_row,column = 1,padx = (5,1),pady = (5,5),sticky = tk.W)

              #Se actualizan las referencias tanto del renglón actual
              #como de la variable siguiente.
              my_current_row += 1
              variable_count += 1


      def __get_mop_example(self,event):
          """
             .. note:: Este método es privado.

             Con base en la selección de M.O.P.
             hecha por el usuario, se carga éste
             en la Ventana Principal.

             :param event: El evento del elemento gráfico que
                           activa esta función.
 
             :type event: String
          """
 
          #Se obtiene el M.O.P. que seleccionó el usuario.
          selected_mop = self.__current_mop.get()

          #Se obtiene la información asociada al
          #M.O.P. seleccionado por el usuario.
          selected_mop_example = self.__features[selected_mop]

          #Se carga en la Ventana Principal dicho M.O.P.
          self.__parent_load_mop_example(selected_mop_example)

          #Se cierra la ventana independiente que contiene
          #este Frame para que el usuario pueda ver los cambios.
          self.__parent.close()
