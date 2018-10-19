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


class IntroductionFrame(tk.Frame):
      """
         | Contiene información básica y concisa sobre el producto de software,
          la cual es organizada y mostrada de acuerdo al número de secciones existentes
          en éste.
         | De manera secundaria proporciona la infraestructura para poder darle al usuario
          un desplazamiento más rápido entre dichas secciones.

         :param parent: Frame padre al que pertenece.
         :param canvas_function: Una función alusiva al funcionamiento del Canvas.
         :param features: Conjunto de técnicas con sus respectivos parámetros para que
                          se puedan cargar automáticamente en este Frame.

         :type parent: Tkinter.Frame
         :type canvas_function: Instance
         :type features: Dictionary
         :returns: Tkinter.Frame
         :rtype: Instance
      """
      
      
      def __init__(self,parent,canvas_function,features):
          #Se crea el Frame Padre sobre el que descansará toda la infraestructura
          #gráfica.
          tk.Frame.__init__(self,parent,relief = "groove")

          #En esta sección se brindarán algunos vínculos para poder saltar a la
          #información pertinente más rápidamente sin necesidad de pasar por todas
          #las secciones; para ello es necesario capturar la función que se pasa como
          #parámetro que permite moverse de una región a otra basándose en un par de
          #coordenadas. 
          self.__canvas_function = canvas_function

          #Se obtiene el color de fondo del Frame principal.
          self.__parent_bg = features["parent_bg"]

          #A continuación se crean dos subframes, uno contendrá las imágenes de los 
          #escudos de la U.N.A.M y la Facultad de Ciencias mientras que el otro tendrá
          #la introducción al tema.         
          self.__image_frame = tk.Frame(self)
          self.__text_frame = tk.Frame(self)

          #A continuación se crean las tipografías que serán empleadas para mostrar
          #la información pertinente.
          self.__title_font = tkf.Font(family = "Helvetica",size = 19,weight = "bold")
          self.__name_font = tkf.Font(family = "Helvetica",size = 10,weight = "bold")
          self.__value_font = tkf.Font(family = "Helvetica",size = 12)

          #Esta Frame usará íconos, en específico los escudos de la U.N.A.M. y
          #la Facultad de Ciencias, entonces se cargan automáticamente todas
          #las imágenes disponibles y aquí se decide cuál usar (véase View/Image y View/MainWindow.py)
          self.__images = features["images"]

          #Se obtiene el ícono del escudo de la U.N.A.M.
          self.__unam_shield_image = self.__images["unam_shield"]
          self.__unam_shield_label = tk.Label(self.__image_frame,image = self.__unam_shield_image)

          #Se obtiene el ícono del escudo de la Facultad de Ciencias.
          self.__sciences_shield_image = self.__images["sciences_shield"] 
          self.__sciences_shield_label = tk.Label(self.__image_frame,image = self.__sciences_shield_image)

          #Se crea el Label del mensaje de bienvenida al usuario y se le da el 
          #formato apropiado.
          self.__welcome_label = tk.Label(self.__image_frame,text = "Welcome to M.O.E.A. Software")
          self.__welcome_label["font"] = self.__title_font
          
          #Se colocan los Labels a manera de grid (malla).
          self.__unam_shield_label.grid(row = 0,column = 0,padx = (1,260),pady = (8,10),sticky = tk.W)
          self.__sciences_shield_label.grid(row = 0,column = 1,pady = (8,10),sticky = tk.E)
          self.__welcome_label.grid(row = 1,column = 0,columnspan = 2,pady = (1,10),sticky = tk.N + tk.S)

          #Ahora se crean los Labels con el título para identificar la información de cada una de
          #las secciones gráficas creadas en el proyecto.
          self.__decision_variables_title_label = tk.Label(self.__text_frame,text = "Decision Variables")
          self.__objective_functions_title_label = tk.Label(self.__text_frame,text = "Objective Functions")
          self.__population_settings_title_label = tk.Label(self.__text_frame,text = "Population Settings")
          self.__genetic_operators_settings_title_label = tk.Label(self.__text_frame,text = "Genetic Operators Settings")
          self.__moeas_settings_title_label = tk.Label(self.__text_frame,text = "MOEAs Settings") 

          #A las Labels antes mencionadas se les da el formato apropiado.
          self.__decision_variables_title_label["font"] = self.__title_font         
          self.__objective_functions_title_label["font"] = self.__title_font
          self.__population_settings_title_label["font"] = self.__title_font
          self.__genetic_operators_settings_title_label["font"] = self.__title_font
          self.__moeas_settings_title_label["font"] = self.__title_font

          #Se crean los elementos gráficos conocidos como Text, los cuales almacenarán 
          #la información correspondiente a la sección que representan.
          self.__introduction_text = tk.Text(self.__text_frame,height = 28,width = 62,background = self.__parent_bg,relief = "flat")
          self.__decision_variables_text = tk.Text(self.__text_frame,height = 26,width = 62,background = self.__parent_bg,relief = "flat")
          self.__objective_functions_text = tk.Text(self.__text_frame,height = 35,width = 62,background = self.__parent_bg,relief = "flat")
          self.__population_settings_text = tk.Text(self.__text_frame,height = 26,width = 62,background = self.__parent_bg,relief = "flat")
          self.__genetic_operators_settings_text = tk.Text(self.__text_frame,height = 27,width = 62,background = self.__parent_bg,relief = "flat")
          self.__moeas_settings_text = tk.Text(self.__text_frame,height = 25,width = 62,background = self.__parent_bg,relief = "flat")

          #A cada uno de los Text se le da el formato apropiado para ser mostrado en la pantalla.
          self.__introduction_text["font"] = self.__value_font
          self.__decision_variables_text["font"] = self.__value_font
          self.__objective_functions_text["font"] = self.__value_font
          self.__population_settings_text["font"] = self.__value_font
          self.__genetic_operators_settings_text["font"] = self.__value_font
          self.__moeas_settings_text["font"] = self.__value_font

          #Las siguientes son coordenadas (en Y) que se usarán para redirigir al usuario
          #hacia posiciones específicas.
          self.__destination_coordinates = {
                                            '0': 0.20176767676767676,
                                            '1': 0.3522727272727273,
                                            '2': 0.5484848484848485,
                                            '3': 0.6989898989898989,
                                            '4': 1
                                           }

          #Aquí irán los nombres de las ligas que redireccionarán al usuario hacia 
          #posiciones específicas del Frame.
          link_quotes = [
                         """                                           Decision Variables\n""",
                         """                                           Objective Functions\n""",
                         """                                           Population Settings\n""",
                         """                                           Genetic Operators Settings\n""",
                         """                                           MOEAs Settings\n"""
                        ]

          #A continuación se muestran las líneas que conformarán la introducción.
          introduction_quotes = [
                                 """The following software product solves Multi-Objective problems using 
evolutionary algorithms as a basis and altogether with the software 
documentation and the written work they define the project that the 
citizen Aarón Martín Castillo Medina presents in order to obtain his 
Bachelor Science degree in Computer Science.\n""",
                                 """\n""",
                                 """The main goal is to facilitate the comprehension of M.O.E.A.'s 
(Multi-Objective Evolutionary Algorithms) through a simple, dynamic and 
modifiable program in order to divulge these kind of techniques and
therefore, inviting those people interested (if possible) to considerate and
acquire these topics in their academic or working activities.\n""",
                                 """\n""",
                                 """Each one of the sections of this program will be briefly described, whereby
it is highly recommended to check both the software documentation and
the written work in case of a misunderstanding, because they serve as a
complement trying to not repeating the same information in the whole
project.\n""",
                                 """The created sections are listed below (if you want to skip to a specific one
just click on it; if you want to return to the beginning click on the button
"Restore Settings"):\n""",
                                 """\n"""
                                ]
          
          #Ahora se implementan las línas que conformarán la sección Decision Variables
          #(ó Variables de Decisión).
          decision_variables_quotes = [
                                       """According to the Multi-Objective environment, a decision variable means at first sight the restriction binded to the objective functions in order to get
the optimal solution, it is important to mention that if there are two or more
decision variables it is called a Multi-Criteria problem, therefore the user
must not confuse both the Multi-Objective and the Multi-Criteria terms
because they are independent from each other.\n""",
                                       """\n""",
                                       """At second sight the best values for every decision variable
(considering their restrictions) will shape the optimal solution, this means
that the optimal solution will be the best choice for each one of the
objective functions inserted by the user, there can be more than one 
optimal solution. The set of optimal solutions is called the Pareto Optimal.\n""",
                                       """\n""",
                                       """In the respective section there is already implemented the necessary
infrastructure so the user can add as many decision variables as desired. 
All of them must have an identifier (name) and both the lower and upper
ranges (restrictions).\n""",
                                       """\n""",
                                       """Finally at the menu "Edit -> Options" there is a feature called
"M.O.P. Examples". It is basically a set of benchmarks (each one is a mixture of objective functions and decision variables) whose behavior is already
studied. These M.O.P.s can be loaded into both the Decision Variables and the Objective Functions sections so the user can get an easy way of
testing and learning from the software product.\n"""
                                      ]

          #Luego se implementan las líneas que construirán la sección Objective Functions (ó
          #Funciones Objetivo).
          objective_functions_quotes = [
                                        """Continuing with the Multi-Objective development, the objective functions
are precisely the "goals" used to get the optimal solution.\nUsually the perspective is to obtain the desired solution which minimizes all the functions, but in case when the user needs to get the ideal solution
which maximizes at least one of them (functions), the software product has already considered this case, this means that a special feature has been
created in the section to allow the user the selection of either maximizing or minimizing one single function.\nBy the way, the set of optimal solutions evaluated in the objective functions is called the Pareto Front.\n""",
                                        """\n""",
                                        """Moreover, the respective section is developed so the user can insert as
much objective functions as desired, however, they must be inserted using Python syntax.\nFor basic purposes it only means that the operator ^ (exponential) changes to ** and when a fraction appears, at least one of the factors must include a decimal point even if the result is integer (example: 4/2 -> 4.0/2.0); the other
operators remain the same.\nNevertheless, when the user tries to insert advanced operators such as
trigonometric functions, there is a special menu at "Edit -> Options" called
"Python Expressions"; this contains nothing but renamed functions
(officially called syntactic sugar) so the Python interpreter can "understand" them.\nWith this feature the user will be able to add as many advanced operators
as possible. There are some preloaded examples to understand better
these options.\n""",
                                        """\n""",
                                        """Finally at the same menu "Edit -> Options" there is another feature called
"M.O.P. Examples". It is basically a set of benchmarks (each one is a mixture of objective functions and decision variables) whose behavior is already
studied. These M.O.P.s can be loaded into both the Decision Variables and the Objective Functions sections so the user can get an easy way of
testing and learning from the software product.\n"""
                                       ]
                           
          #Ahora se construyen las líneas que darán forma a la 
          #sección Population Settings (ó Características de la Población).
          population_settings_quotes = [
                                        """This section starts with the evolutionary environment related to the
Multi-Objective development.\nIn order to get the optimal solution, the computer suggests initial random
solutions so they can "evolve" into more adaptable ones, that is, upgrading
the solutions using techniques based on natural selection theories in order
to obtain those that minimize the most the objective functions provided by
the user.\nThe set of the suggested solutions and their eventual upgrades is called a
Population, and each one of them (for the project's purposes) is called an
Individual.\n""",
                                        """\n"""
                                        """By using this section the user will define the Population's characteristics
such as the chromosomal representation which leads into the mathematical
representation to upgrade one solution, the number of Individuals, the
number of decimals in each solution (see the Decision Variables section),
the number of generations (iterations) needed to upgrade the Population
and the selection of Fitness.\nFitness is basically a measure which indicates the level of superiority of an
Individual, usually the amount of Fitness is proportional to that superiority,
this factor is essential when the evolving operations are being executed.\n""",
                                       """\n""",
                                       """It is important to mention that the chromosomal representation selected
must coincide with both Crossover and Mutation operators used at
"Genetic Operators Settings".\n"""  
                                       ]

          #Luego se crean las líneas que formarán parte de la sección
          #Genetic Operators Settings (ó Características de los Operadores Genéticos).
          genetic_operators_settings_quotes = [
                                               """When a Population is about being upgraded, actually it means that a new
Population is created based on the "old one", such operation is called the
generation of an offspring.\nJust like in the biological ecosystems, this method allows to obtain more
adaptable Individuals by selecting and combining their genetic payload
(provided in this case by the chromosomal representation).\n""",
                                               """\n""",
                                               """In this section there are three operators involved in the generation of an
offspring:\n  *The Selection operator which, based on the Fitness, selects the optimal
Individuals in order to define the new Population.\n  *The Crossover operator, which consists on a sexual reproduction in
order to create new Individuals.\n  *The Mutation operator which changes the genetic payload in the recently
created Individuals so the Population do not stay stuck in the same genetic features.\n"""
                                               """\n""",
                                               """There are many implementations for each one of these operators but
generally speaking, all of them are considered in this section, therefore the user can select and modify the techniques or values regarding this
evolutionary process.\n""",
                                               """\n""",
                                               """It is important to mention that the techniques related to both Crossover and Mutation operators must coincide with the chromosomal representation
selected at "Population Settings.\n"""
                                              ]

          #Finalmente se crean las líneas que constituirán la sección
          #MOEAS Settings (ó Características de los MOEAs).
          moeas_settings_quotes = [
                                   """In this section the user can choose one technique (M.O.E.A) from a concise variety of M.O.E.A.s.\nThe M.O.E.A. provides the set of optimal solutions according to the
objective functions given; to reach this goal the M.O.E.A. uses all the
information gathered in this and the other sections as well.\nThe main difference between one M.O.E.A and another is the applied
restriction (also called selective pressure) when it is choosing the optimal
Individuals.\nThis project contains the most representative algorithms so the user can
test them and see the results.\nThis sections also contains a feature called Sharing Function, it is used
when the algorithm tries to make an even more restrictive selection of
Individuals.\nNot all M.O.E.A.s use this option but it was considered to put this feature
because of its importance in the evolutionary process.\n""",
                                   """\n""",
                                   """As usual, the user has options to his disposal in order to modify the
correspondent values related to the selection of M.O.E.A. and the Sharing Function as well.\n""",
                                   """\n""",
                                   """Speaking of which, the configurations established in this program are 
related to the use of the NSGA-II algorithm, that is because in all the
scientific sources the authors consider this algorithm as a benchmark, so
the same is done here."""
                                  ]

          #A continuación se coloca la información correspondiente a la introducción
          #en su Text correspondiente.
          for quote in introduction_quotes:
              self.__introduction_text.insert(tk.END,quote)

          #Para poder acceder a la información más rápidamente, se colocan ligas (links) para cada
          #una de las secciones gráficas. Cuando el usuario dé click en alguna de éstas será redireccionado
          #al inicio de la información de la sección en cuestión.
          for x in range (len(link_quotes)):
              current_quote = link_quotes[x]
              self.__introduction_text.insert(tk.END,current_quote,("link",str(x)))
          
          #Las ligas se colocan de color azul.
          self.__introduction_text.tag_config("link",foreground = "blue")

          #Se agrega el evento de cada una de las ligas.
          self.__introduction_text.tag_bind("link","<Button-1>",self.__go_to_selected_section)

          #Ahora se coloca la información relativa a las variables de decisión (Decision Variables).
          for quote in decision_variables_quotes:
              self.__decision_variables_text.insert(tk.END,quote)

          #A continuación la información relativa a las funciones objetivo (Objective Functions)
          #es colocada.
          for quote in objective_functions_quotes:
              self.__objective_functions_text.insert(tk.END,quote)

          #Luego la información relacionada con las características de la Población (Population Settings)
          #es mostrada.
          for quote in population_settings_quotes:
              self.__population_settings_text.insert(tk.END,quote)

          #La información concerniente a las características para la descendencia de una Población
          #(Genetic Operators Settings) es mostrada.
          for quote in genetic_operators_settings_quotes:
              self.__genetic_operators_settings_text.insert(tk.END,quote)

          #Ahora la información aunada a las características para el uso de MOEAs y Sharing Functions ó
          #Funciones de Compartición (MOEAs Settings) es colocada.
          for quote in moeas_settings_quotes:
              self.__moeas_settings_text.insert(tk.END,quote)

          #Dado que la introducción será colocada en Text, éstos por defecto pueden
          #modificar su contenido, por ello es que una vez que se les insertó la información,
          #se desactivan para no permitir que el usuario cambie la información.
          self.__introduction_text.configure(state = tk.DISABLED)
          self.__decision_variables_text.configure(state = tk.DISABLED)
          self.__objective_functions_text.configure(state = tk.DISABLED)
          self.__population_settings_text.configure(state = tk.DISABLED)
          self.__genetic_operators_settings_text.configure(state = tk.DISABLED)
          self.__moeas_settings_text.configure(state = tk.DISABLED)
          
          #A continuación se colocan los Text que identifican a cada sección del texto
          #y los Text que indican la información de cada sección. Esto sucede en el Text Frame. El método
          #de colocación es en forma de malla (grid).
          self.__introduction_text.grid(row = 0,column = 0,padx = (1,1),pady = (1,1),sticky = tk.W)
          self.__decision_variables_title_label.grid(row = 1,column = 0,padx = (1,1),pady = (1,7),sticky = tk.N + tk.S)
          self.__decision_variables_text.grid(row = 2,column = 0,padx = (1,1),pady = (1,1),sticky = tk.W)
          self.__objective_functions_title_label.grid(row = 3,column = 0,padx = (1,1),pady = (1,7),sticky = tk.N + tk.S)
          self.__objective_functions_text.grid(row = 4,column = 0,padx = (1,1),pady = (1,1),sticky = tk.W)
          self.__population_settings_title_label.grid(row = 5,column = 0,padx = (1,1),pady = (1,7),sticky = tk.N + tk.S)
          self.__population_settings_text.grid(row = 6,column = 0,padx = (1,1),pady = (1,1),sticky = tk.W)
          self.__genetic_operators_settings_title_label.grid(row = 7,column = 0,padx = (1,1),pady = (1,7),sticky = tk.N + tk.S)
          self.__genetic_operators_settings_text.grid(row = 8,column = 0,padx = (1,1),pady = (1,1),sticky = tk.W)
          self.__moeas_settings_title_label.grid(row = 9,column = 0,padx = (1,1),pady = (1,7),sticky = tk.N + tk.S)
          self.__moeas_settings_text.grid(row = 10,column = 0,padx = (1,1),pady = (1,1),sticky = tk.W)

          #Finalmente se colocan los Subframes en el Frame principal.
          self.__image_frame.pack()
          self.__text_frame.pack()  


      def __go_to_selected_section(self,event):
          """
             .. note:: Este método es privado.  

             Con base en la liga elegida por el usuario, realiza el
             desplazamiento hacia la sección correspondiente.

             :param event: Elemento que ejecutó esta función.
             :type event: String
          """

          #Dentro de los Links se obtiene la posición de aquél que fue seleccionado
          #por el usuario.
          index_length = len(event.widget.tag_names(tk.CURRENT))
          index = event.widget.tag_names(tk.CURRENT)[index_length - 1]         

          #A continuación dentro de la estructura pertinente se obtiene la coordenada
          #en Y a la que se moverá el Scrollbar (barra de desplazamiento). 
          y_coordinate = self.__destination_coordinates[index]

          #Finalmente se manda llamar a la función que realiza este movimiento.
          self.__canvas_function(y_coordinate) 
