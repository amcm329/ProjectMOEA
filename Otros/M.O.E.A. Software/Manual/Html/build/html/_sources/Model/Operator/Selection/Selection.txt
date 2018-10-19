Selection (módulo)
==================


| En esta sección se encuentran implementadas todas las técnicas relacionadas con 
 la selección de Individuos.
| Como se ha mencionado antes, durante dicha operación la importancia de la elección
 radica en el Fitness de cada Individuo, además un Individuo puede ser seleccionado más de una vez
 si la causa lo amerita.
| Así, se elegirán tantos Individuos como elementos haya en la Población.
| El objetivo radica en mantener el equilibrio entre una "selección justa" y
 la oportunidad de permitir a los Individuos con una calidad media o baja la propagación de su carga genética.
|
| Al final se busca que el usuario desarrolle sus propias técnicas de selección, por lo cual, además
 de añadir el método en el listado localizado en **Controller/XML/Features.xml**, deberá implementar la siguiente
 función:


.. py:function:: execute_selection_technique(population,selection_parameters):
  
   | Lleva a cabo la selección de Individuos de una Población. Es importante recalcar que, la función que 
    más se ocupa es: 
   .. centered:: **get_fitness (Model/Community/Population/Individual.py)**
   | Aunque existen otras que pueden tener relevancia para el usuario **(véase Model/Community/Population.py)**.
   | Como medida adicional, para los eventos de Crossover **(ó Cruza)** y Mutation **(ó Mutación)** se recomienda
    ampliamente que este método regrese únicamente los cromosomas asociados a los Individuos, ya que ésto facilita sobremanera
    las operaciones mencionadas.
  
   :param population: La Población sobre la cual se se seleccionarán los Individuos.
   :param selection_parameters: Un diccionario que puede contener opciones adicionales para la
                                selección de Individuos.

   :type population: Instance
   :type selection_parameters: Dictionary
   :return: Una lista que contiene los cromosomas de los Individuos seleccionados.
   :rtype: List


A continuación se vislumbran los elementos característicos de este módulo:


.. toctree::
    :maxdepth: 3

    Roulette.rst
    ProbabilisticTournament.rst
    StochasticUniversalSampling.rst
