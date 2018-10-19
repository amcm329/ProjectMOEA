Mutation (módulo)
=================


| En esta parte se encuentran detalladas las técnicas relacionadas con
 Mutation **(ó Mutación)**.
| Retomando el proceso de creación de una nueva Población, es aquí donde 
 una vez obtenidos los hijos, se modifican pequeñas porciones **(genes)** de sus cromosomas
 de manera individual.
| Con ésto se persigue principalmente que estas ínfimas alteraciones permitan
 incrementar la exploración del material genético y por ende otorgar Individuos
 aún más aptos sin caer en el peligro de perder características valiosas en la
 Población.
|
| Considerando lo anterior, lo primero que hay que tomar en cuenta es que
 la operación de Mutación es unaria, esto significa que sólo se puede mutar
 el cromosoma de un Individuo a la vez.
| También y reiterando la información pasada, la Mutación es una operación
 que se lleva a cabo a nivel cromosómico **(véase Model/ChromosomalRepresentation)**,
 por lo que se debe tener mesura  con el tratamiento de los métodos, dicho de otra manera, 
 cada Representación Cromosómica debe ir acompañada de al menos una función de Mutación.
|
| Como dato para posteriores referencias, un gen hace referencia a una casilla del cromosoma,
 mientras que un alelo es el valor que puede existir en un gen.
|
| Así, se invita a que el usuario construya sus propias versiones 
 de Mutación, por lo cual, además de añadir el método en el listado localizado en
 **Controller/XML/Features.xml**, deberá implementar la siguiente función:


.. py:function:: execute_mutation_technique(chromosome,mutation_parameters):
  
   | Lleva a cabo mutación del Individuo a nivel cromosómico. 
   | A grandes rasgos, modifica los alelos de los genes tomando en cuenta 
    la gama de valores a los que se pueden transformar **(por ejemplo, una mutación de representación
    Binaria puede transformarse sólo en valores 0 ó 1)**.
   | El método debe retornar siempre el cromosoma mutado.
   | Finalmente, esta función debe contar con la probabilidad de Mutación, 
    la cual indica si se debe o no hacer la operación cromosómica por cada gen; en caso 
    de ser la respuesta negativa el Individuo no experimenta modificación alguna en el gen y
    se pasa al siguiente y así sucesivamente.

   :param chromosome: El cromosoma para ser mutado.
   :param mutation_parameters: Un diccionario que puede contener opciones adicionales para la
                               mutación del cromosoma del Individuo.

   :type chromosome: List
   :type mutation_parameters: Dictionary
   :return: El cromosoma modificado.
   :rtype: List


A continuación se muestran los elementos concernientes a este módulo:


.. toctree::
    :maxdepth: 2

    BinaryMutation.rst
    FloatPointMutation.rst
