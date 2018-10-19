#!/usr/bin/env python
#-*- coding: utf-8 -*-

__author__ = "Aarón Martín Castillo Medina"
__credits__ = ["Aarón Martín Castillo Medina","Dra. Katya Rodríguez Vázquez"]

__version__ = "1.0"
__mantainer__ = "Aarón Martín Castillo Medina"
__email__ = "amcm329@hotmail.com"
__status__ = "Production"


"""
   | Se implementa la asignación de Fitness conocida como Non-Linear Ranking
    **(ó Ranking No Lineal)** que, a diferencia de los demás métodos, la aplica 
    usando como base la posición del Individual **(ó Individuo)** en la Population   
    **(ó Población)** como resultado de las operaciones de ranking
    **(véase Model/Community/Community.py)**.
   | Posteriormente el Fitness se constituye tomando la posición del Individuo y
    una función polinomial **(la cual es una función no lineal, de ahí el nombre)**. 
   | La fórmula es la siguiente:
   .. centered:: :math:`Fitness(Individuo) = \\frac{TP \cdot X^{posici\\acute{o}n(Individuo)}}{\sum_{i=1}^{TP}X^{i - 1}}`
   | Donde:
   |    **TP** es el tamaño de la Población.
   |    **Posición(Individuo)** es la que ocupa éste de acuerdo al ranking previo.
   |    **X** es la solución al polinomio: :math:`(SP - TP) \cdot X^{TP - 1} + SP \cdot X^{TP - 2} + ... + SP \cdot X + SP = 0`
   |    **SP (Selective Pressure ó Presión Selectiva)** varía entre 1 y 2.
   |
   | Haciendo un análisis somero en la fórmula, se puede apreciar que los 
    Individuos con mejor Fitness serán aquéllos que se encuentren en las últimas posiciones, 
    sin embargo los rankings que se manejan en este proyecto son inversamente proporcionales 
    a la calidad de los Individuos **(véase Model/Community/Community.py)**; 
    por ello es importante ordenar a los Individuos de manera descendente para que la operación tenga sentido.
   | La función encargada de esto se llama sort_individuals y está en **Model/Community/Population/Population.py**.
"""


def derivate(polynome):
    """
       Método que calcula la derivada de un polinomio, modificando
       directamente éste sin regresar nada.
       
       :param polynome: El polinomio inicial.

       :type polynome: List
    """

    #Dado que la derivada de un polinomio consiste en derivar
    #cada término, se realiza la derivación de cada uno.
    #Esto implica que se multiplique por el coeficiente el término actual 
    #y se disminuya en una unidad el exponente, o lo que es equivalente 
    #multiplicar todos los coeficientes consigo mismos y eliminar el menos
    #significativo pues sería la derivada del término constante.
    for index in range(len(polynome)):
            polynome[index]*=index
    
    #Se elimina el rérmino constante.
    polynome.pop(0)

    #Sólo como medida preventiva, si la derivada del polinomio es 0, entonces
    #a la lista se le agrega un 0.
    if len(polynome) == 0:
       polynome.append(0.0)
    

def evaluate_polynome(polynome,x):
    """
       Evalúa un polinomio en un cierto valor.

       :param polynome: El polinomio a evaluar.
       :param x: El valor sobre el que se evaluará el polinomio.

       :type polynome: List
       :type x: Float
       :return: La evaluación del polinomio.
       :rtype: Float
    """
    
    #Aquí se almacenará el resultado.
    value = 0.0

    #Se evalúa el polinomio de acuerdo al valor x
    #y se realiza la operación de manera tradicional, esto es,
    #la suma de términos elevados a cierta potencia.
    for index in range(len(polynome)):
        value += polynome[index]*(x**index)
  
    #Se regresa el valor.
    return value


def calculate_root(polynome,x_0,epsilon):
    """
       Calcula la solución de un polinomio usando el método Newton-Raphson.
        A grandes rasgos el funcionamiento es el siguiente:
       | Tomando como base el punto :math:`x_0` se obtiene :math:`x_1` así:
       .. centered:: :math:`x_1 = x_0 - \\frac{f(x_0)}{f'(x_0)}`
       | Una vez obtenido :math:`x_1` se calcula :math:`x_2` de la misma manera:
       .. centered:: :math:`x_2 = x_1 - \\frac{f(x_1)}{f'(x_1)}`
       | El proceso se repite para 'n' iteraciones hasta que el valor alcance la
        precisión de epsilon ó el polinomio ya no tenga más derivadas. Concretando lo anterior:
       .. centered:: :math:`x_{n+1} = x_n - \\frac{f(x_n)}{f'(x_n)}`
       | Cuando :math:`x_{n+1}` se acerque a epsilon ó cuando el
        polinomio no sea más derivable el método se detendrá.

       :param polynome: El polinomio en el que se buscará la solución.
       :param x_0: el punto sobre el que se hará la evaluación del polinomio.
       :param epsilon: La precisión decimal que se necesita para poder devolver
                       el resultado.

       :type polynome: List
       :type x_0: Float
       :type epsilon: Float
       :return: La solución al polinomio.
       :rtype: Float      
    """

    #Se crea un polinomio auxiliar.
    polynome_1 = []

    #Se evalúa el polinomio en el punto x_0 de acuerdo al método.
    value = evaluate_polynome(polynome,x_0)
    
    #Se copian los coeficientes del polinomio original al polinomio auxiliar.
    for number  in polynome:
            polynome_1.append(number)    
    
    #Se deriva el polinomio de acuerdo al método.
    derivate(polynome_1)

    #Mientras el resultado no alcance la precisión deseada o el polinomio 
    #siga siendo derivable, se hace lo siguiente:
    while abs(value) >= epsilon:

          #Se obtiene siguiente derivada del polinomio.
          deriv_value = evaluate_polynome(polynome_1,x_0)

          #Si la derivada es 0, significa que ya no hay más que hacer y el
          #proceso concluye.
          if deriv_value == 0:
             x_0 = 0.0
             break
        
          #En otro caso se actualiza el punto x_0 al obtenido de acuerdo al 
          #método (f(x0)/f'(x0)).
          x_0 = x_0 - (value/deriv_value)

          #Se actualiza también la evaluación del polinomio para el siguiente paso.
          value = evaluate_polynome(polynome,x_0)

    #Se devuelve el último valor obtenido en el ciclo while.
    return x_0


def assign_fitness(population,fitness_parameters):
    """  
       Utilizando la explicación concretada al principio, se realiza
       la implementación de la asignación de Non-Linear Ranking Fitness **(ó Fitness de Ranking No Lineal)**.
    """

    #Esta variable almacenará la suma de la solución elevadas
    #a una cierta potencia (véase la descripción más abajo).
    sum_roots = 0.0

    #Variable usada para almacenar el total del Fitness de la Población.
    total_fitness = 0.0 

    #Se obtienen el tamaño de la población, así como el valor SP.
    population_size = population.get_size()
    sp = fitness_parameters["sp_non_linear_ranking_fitness"] 

    #Tomando en cuenta la explicación del ordenamiento en forma descendente,
    #se efectúa tal operación en esta línea. 
    population.sort_individuals("get_rank",True)
    
    #Se inicializa el polinomio con el que se encontrará el valor de X de acuerdo
    #a la fórmula proporcionada en la descripción; más en específico se creará una lista
    #donde sólo se manejen sus coeficientes.
    #La lista comienza con el coeficiente del término con exponente más alto.
    polynome = [sp - population_size]

    #De acuerdo al polinomio, todos los coeficientes de los términos salvo el del mayor exponente
    #constarán del valor SP, entonces se agrega dicho valor.
    for x in range (population_size - 1,-1,-1):
        polynome.append(sp)

    #Una vez construida la lista de coeficientes se procede a calcular la solución.
    solution = calculate_root(polynome,0.0,0.0000001)         

    #Tomando como referencia la fórmula, se calcula la suma de las soluciones elevadas
    #a la potencia de la posición, esto es: X^0 + X^1 + ... + X^(TP - 1).
    for x in range (population_size):
        sum_roots += solution**x

    #Se inicializa la variable que indicará la posición que ocupa el Individuo.
    posicion = 0

    #Para cada Individuo se hace lo siguiente:
    for individual in population.get_individuals():

        #Se calcula el Fitness tomando en cuenta la posición que ocupa, la solución al polinomio
        #así como la suma de las soluciones (sum_roots).
        current_fitness = (population_size*(solution**posicion))/sum_roots

        #Se actualiza el atributo del Fitness en el Individuo.
        individual.set_fitness(current_fitness)

        #Se agrega el Fitness actual a la variable que llevará el Fitness de la Población.
        total_fitness += current_fitness

        #Se actualiza la posición.
        posicion += 1
  
    #Se actualiza el Fitness total de la Población. 
    population.set_total_fitness(total_fitness) 

    #Se actualizan propiedades concernientes a los Individuos.
    population.calculate_population_properties()
