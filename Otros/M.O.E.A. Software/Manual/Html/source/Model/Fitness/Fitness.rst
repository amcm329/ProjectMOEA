Fitness (módulo)
================


Este módulo provee técnicas que calculan el Fitness **(ó Aptitud)** de los 
Individuals **(ó Individuos)** de una Population **(ó Población)**.

Se entiende por Fitness a un número que indica la calidad del 
Individuo **(en particular de sus variables de decisión)** frente a 
las funciones objetivo al momento de ser evaluadas, esto es, a mayor Fitness, mayor 
es la probalidad de que las variables de decisión del Individuo sean la solución óptima
para las funciones objetivo.

La asignación del Fitness depende en gran medida del ranking que se les haya
otorgado a los Individuos previamente **(véase Model/Community/Community.py)**. 

Indirectamente, esto nos indica que un Individuo con un Fitness alto
tiene más probabilidades de ser elegido en los métodos de Selection **(ó Selección)**
y propagar su carga genética; así en las funciones de dicha sección **(Model/Operator/Selection)**
el criterio para escoger a un Individuo está basado comúnmente en su Fitness.

Al final la meta es que el usuario cree sus propias versiones de asignación
de Fitness, para lo cual es imperativo que, además de agregar la descripción de 
la codificación a Controller/XML/Features.xml **(véase el archivo mencionado en la sección de código)**, 
se implemente la siguiente función:


.. py:function:: assign_fitness(population,fitness_parameters):

   | Realiza la asignación de Fitness de los Individuos.
   | Dentro de esta se suelen usar métodos de la clase Population **(véase Model/Community/Population/Population.py)**
    y de la clase Individual **(véase Model/Community/Population/Individual/Individual.py)**, por lo que es 
    muy recomendable que el usuario verifique las funciones disponibles. Algunas de las que se ocupan 
    más frecuentemente son:
   |    **get_rank (Individual)**
   |    **set_fitness (Individual).**
   |    **set_total_fitness (Population)**
   |    **calculate_population_properties (Population)**
    
   :param population: La Población sobre la cual se hará el cálculo de Fitness por cada Individuo.
   :param fitness_parameters: Un diccionario que puede contener opciones adicionales para el cálculo
                           de Fitness.

   :type population: Instance
   :type fitness_parameters: Dictionary
  

Ahora se muestran los elementos que conforman el módulo actual:


.. toctree::
    :maxdepth: 3

    LinearRankingFitness.rst
    NonLinearRankingFitness.rst
    ProportionalFitness.rst
