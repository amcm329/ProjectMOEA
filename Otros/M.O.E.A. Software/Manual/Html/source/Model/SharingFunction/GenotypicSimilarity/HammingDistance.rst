HammingDistance (script)
========================


| La Distancia de Hamming **(ó Hamming Distance)** es una implementación
 perteneciente a la subcategoría Genotypic Similarity **(ó Similaridad Genotípica)**.
| Esta consiste en comparar los alelos entre los cromosomas de los Individuos y devolver un valor numérico
 que indica en cuántos alelos los cromosomas de los Individuos resultaron tener valores diferentes.
| Como consecuencia lógica, la magnitud de la Distancia de Hamming es inversamente proporcional a la calidad
 de los Individuos.
|
| Es ampliamente usada para la Representación Cromosómica **(véase Model/ChromosomalRepresentation)**
 de tipo Binario **(ó Binary)**, aunque su uso no se limita sólo a esta codificación.
|
| Con respecto del cálculo del :math:`\sigma_{share}`, éste se hace tomando en cuenta el número máximo 
 permitido de genes diferentes entre dos cromosomas cualesquiera.
| Dicha cantidad es deducida solicitándole al usuario únicamente el porcentaje máximo permitido, con base
 en éste se determina entonces el número en concreto.


.. automodule:: Model.SharingFunction.GenotypicSimilarity.HammingDistance
    :members:
    :undoc-members:
    :private-members:
    :show-inheritance:

