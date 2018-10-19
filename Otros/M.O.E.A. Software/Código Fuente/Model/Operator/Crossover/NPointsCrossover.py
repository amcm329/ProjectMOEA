#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


import random as aleatorio


"""
   | Se implementa el método que lleva por nombre N-Points Crossover **(ó Cruza en N-Puntos)**.
    Para comenzar, esta técnica está elaborada para usarse tanto por Representación Cromosómica
    **(véase Model/ChromosomalRepresentation)** de tipo FloatPoint **(ó de Punto Flotante)** como
    Binary **(ó Binaria)**.
   | Su funcionamiento consiste en construir a los descendientes usando sub-bloques de cromosomas de cada 
    uno de los padres, determinados éstos por una cierta cantidad de puntos de corte, de ahí el nombre.
   | Aterrizando lo anterior de una manera concisa se tiene lo siguiente:
   * Consideremos a los cromosomas de los padres Padre I: :math:`I_1I_2...I_n` 
    y Padre J: :math:`J_1J_2...J_n`
   * Posteriormente se determinan aleatoriamente los puntos de corte, cabe mencionar que si los cromosomas son de tamaño n, pueden existir máximo n - 1 puntos. Supongamos que se crean k puntos :math:`(1 \leqslant k \leqslant n - 1)` y por lo tanto cada cromosoma queda separado en k + 1 bloques. 
    De esta manera obtenemos:
    Padre I en bloques **(BI)**: :math:`BI_1BI_2...BI_{k + 1}`;
    Padre J en bloques **(BJ)**: :math:`BJ_1BJ_2...BJ_{k + 1}`.
   * Finalmente cada hijo constará de la alternancia de bloques de manera secuencial comenzando por el bloque inicial de un padre determinado, dicho de otra forma, los hijos estarán constituidos de la siguiente manera:
    * Para el hijo :math:`H_1`: :math:`BI_1BJ_2...BI_{k + 1}` 
    * Para el hijo :math:`H_2`: :math:`BJ_1BI_2...BJ_{k + 1}`
   | Sólo queda mencionar que hasta el cierre de este proyecto no existe una manera 
    transparente desde el View **(ó Vista)** de conocer, dada una representación Binaria 
    y un conjunto de variables de decisión y funciones objetivo, el número máximo de puntos 
    de corte permitidos para este procedimiento, sin embargo, una manera de mitigar esta situación
    fue contemplar algún posible caso de error en esta sección y mandar un mensaje de error a la Vista
    por si llegase a suceder algún desperfecto durante el proceso.
"""


def execute_crossover_technique(chromosome_a,chromosome_b,crossover_parameters):     
    """
       Usando como base la información proporcionada anteriormente, se implementa
       el método conocido como N-Points Crossover **(ó Cruza en 'N' Puntos)**.
    """
          
    #De la sección de parámetros se obtiene la probabilidad de cruza.
    crossover_probability = crossover_parameters["probability_crossover_general"]    
    
    #Se inicializan los cromosomas hijos, los cuales contendrán la información
    #de la cruza entre los padres.
    chromosome_child_1 = []
    chromosome_child_2 = []
           
    #Se crea el número aleatorio que servirá para verificar la probabilidad
    #de cruza.
    crossover_number = aleatorio.random()

    #Si el número creado anteriormente es menor o igual al parámetro de la
    #probabilidad de cruza, entonces se procede con la etapa de recombinación
    #genética.
    if crossover_number <= crossover_probability:
       #Al entrar en la etapa de recombinación genética, primero se averigua
       #el número de puntos de corte que se solicitarán para la operación.
       how_many_points = crossover_parameters["how_many_points_npoints_crossover"]

       #Se guardan referencias a los cromosomas originales para no modificarlos.
       my_chromosome_a = chromosome_a
       my_chromosome_b = chromosome_b

       #Aquí se almacenarán los bloques alternados de cada hijo.
       mixed_chromosome_1 = [] 
       mixed_chromosome_2 = []

       #Variable que contiene el tamaño del cromosoma (para averiguar los puntos
       #de corte).
       length_chromosome = len(chromosome_a)

       #Aquí serán almacenados los puntos de corte.
       sections_list = []

       #Esta variable permite alternar bloques de una manera rápida.
       flag = 0
           
       #En caso de que no se cumpla la restricción de puntos de corte,
       #se lanza una excepción.
       if how_many_points > length_chromosome - 1:
          raise ValueError("Number of points ({0}) exceeds chromosome's length ({1})".format(how_many_points,length_chromosome)) 

       #Aquí se considera el caso en que el número de puntos de cruza sea
       #'n-1', se utiliza una lista por comprensión para llenar la lista
       #de puntos de corte más rápidamente"""
       if length_chromosome == how_many_points + 1:
          real_sections_list = [x for x in range(length_chromosome + 1)]

       #En caso de tratarse de una menor cantidad de puntos
       #se procede a seleccionar de manera aleatoria los puntos
       #de corte de acuerdo a la variable how_many_points.     
       else: 

          #Se agrega siempre el punto 0 para que tenga coherencia
          #la extracción de bloques.
          sections_list.append(0)
          sections_list.append(length_chromosome)
          how_many_points_auxiliar = how_many_points
        
          #El siguiente ciclo permite seleccionar los puntos de corte,
          #asegurándose de no repetirlos y/o proporcionar valores inválidos.  
          while how_many_points_auxiliar != 0:
                number = 1 + aleatorio.randint(0,length_chromosome - 2)
                
                #Aquí se verifica que los puntos de corte no estén repetidos.
                if not(number in sections_list):
                   sections_list.append(number) 
                   how_many_points_auxiliar -= 1            
                   
          #Se ordenan los puntos de corte para poder extraer 
          #los bloques más fácilmente.
          real_sections_list = sorted(sections_list)
          
       #Una vez creada la lista de puntos de corte, se procede a crear a los hijos.
       #Para ello se toman porciones de acuerdo a los índices de la lista.
       for x in range(1,len(real_sections_list)):
              
           #Esta sección permite la alternancia de los bloques definidos por los puntos
           #de corte.
           if flag == 0:
              mixed_chromosome_1 += my_chromosome_a[real_sections_list[x-1]:real_sections_list[x]]
              mixed_chromosome_2 += my_chromosome_b[real_sections_list[x-1]:real_sections_list[x]]
                                   
           elif flag == 1:
                mixed_chromosome_1 += my_chromosome_b[real_sections_list[x-1]:real_sections_list[x]]
                mixed_chromosome_2 += my_chromosome_a[real_sections_list[x-1]:real_sections_list[x]]
                    
           #Esta variable permite aplicar la alternancia de bloques tantas
           #veces como sea necesario.
           flag = (flag + 1) % 2        
 
       #Se actualizan las variables destinadas a los hijos una vez terminada la concatenación
       #de bloques.
       chromosome_child_1 = mixed_chromosome_1
       chromosome_child_2 = mixed_chromosome_2
      
    #Si el número creado para la probabilidad de cruza es mayor que el parámetro
    #de probabilidad de cruza entonces no se aplica ninguna operación y los hijos
    #resultan en copias idénticas de los padres.
    else:
        chromosome_child_1 = chromosome_a
        chromosome_child_2 = chromosome_b
              
    #Al final se regresa un arreglo conteniendo a los 2 hijos.
    return [chromosome_child_1,chromosome_child_2]
