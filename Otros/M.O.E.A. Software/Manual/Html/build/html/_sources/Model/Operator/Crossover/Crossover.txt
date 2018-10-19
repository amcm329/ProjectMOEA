Crossover (módulo)
==================


| Aquí se desarrollan las técnicas de Crossover **(ó Cruza)**.
| Prosiguiendo con el ciclo de creación de una nueva Población, es en este apartado donde
 se lleva a cabo la concepción de nuevos Individuos.
|
| Debido a esto se busca crear "hijos" más aptos que respondan mejor ante la problemática
 fundamentada, es decir, concebir soluciones que se adapten mejor a los criterios establecidos 
 por el usuario desde un inicio basándose en las soluciones predecesoras.
|
| Es menester mencionar que esta función es meramente binaria, lo cual significa que siempre 
 deben haber dos padres, además se debe hacer hincapié en que la Cruza se ejecuta a nivel
 cromosómico **(véase Model/ChromosomalRepresentation)**,por lo que se debe tener mesura 
 con el tratamiento de los métodos, dicho de otra manera, cada Representación Cromosómica debe ir 
 acompañada de al menos una función de Cruza.
|
| Como dato para posteriores referencias, un gen hace referencia a una casilla del cromosoma,
 mientras que un alelo es el valor que puede existir en un gen.
|
| Entonces se persigue que el usuario construya sus propias funciones de Cruza, para lo cual,
 además de añadir el método en el listado localizado en **Controller/XML/Features.xml**, deberá 
 implementar la siguiente función:


.. py:function:: execute_crossover_technique(chromosome_a,chromosome_b,crossover_parameters):
  
   | Lleva a cabo la cruza de dos Individuos a nivel cromosómico. 
   | Además esta función debe retornar siempre dos hijos los cuales serán la cruza de A con B y
    la cruza de B con A, esto nos indica que, con el objetivo de incrementar la calidad de los Individuos
    sin perder la carga genética ganada o introducir elementos riesgosos, la cruza consiste en generar un
    nuevo Individuo y su recíproco; así se garantiza una adecuada y controlada descendencia.
   | Finalmente, esta función debe contar con la probabilidad de Cruza, la cual indica si se debe o
    no hacer la operación cromosómica; en caso de ser la respuesta negativa los hijos resultan en copias
    idénticas de los padres.

   :param chromosome_a: El cromosoma del Individuo A.
   :param chromosome_b: El cromosoma del Individuo B.
   :param crossover_parameters: Un diccionario que puede contener opciones adicionales para la
                                cruza de Individuos.

   :type chromosome_a: List
   :type chromosome_b: List
   :type crossover_parameters: Dictionary
   :return: Un arreglo con dos cromososomas, el primero es la cruza de A con B, mientras que el segundo 
            es la cruza de B con A.
   :rtype: Array


Se colocan los elementos alusivos a este módulo:


.. toctree::
    :maxdepth: 2

    NPointsCrossover.rst
    UniformCrossover.rst
