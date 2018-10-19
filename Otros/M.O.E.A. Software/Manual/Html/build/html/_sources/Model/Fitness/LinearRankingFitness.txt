LinearRankingFitness (script)
=============================


| Se implementa la asignación de Fitness conocida como Linear Ranking **(ó Ranking Lineal)**.
| Es denominada así porque el Fitness se asigna con una función lineal que tiene como
 fundamento la posición que ocupa el Individuo dentro de la Población.   
| El procedimiento es: tomando en cuenta el ranking asignado a los Individuals 
 **(ó Individuos)** por la clase Community **(véase Model/Community/Community.py)** 
 se ordenan de acuerdo a este valor y entonces el Fitness se basa en la posición 
 que cada uno de los Individuos ocupa. Más en específico, el Fitness está proporcionado 
 por la siguiente fórmula:  
.. centered:: :math:`Fitness(Individuo) = 2 - SP + \frac{2 \cdot (SP - 1) \cdot posici\acute{o}n(Individuo)}{tama\tilde{n}o\_poblaci\acute{o}n - 1}`
| Donde:
|       **SP (Selective Pressure ó Presión Selectiva)** es un valor que oscila entre 1 y 2.
|       **Posición(Individuo)** es la que ocupa el Individuo de acuerdo al rank.  
|
| Haciendo un análisis somero en la fórmula, se puede apreciar que los 
 Individuos con mejor Fitness serán aquéllos que se encuentren en las últimas posiciones, 
 sin embargo los rankings que se manejan en este proyecto son inversamente proporcionales 
 a la calidad de los Individuos **(véase Model/Community/Community.py)**; 
 por ello es importante ordenar a los Individuos de manera descendente para que la operación tenga sentido.
| La función encargada de esto se llama sort_individuals y está en **Model/Community/Population/Population.py**.


.. automodule:: Model.Fitness.LinearRankingFitness
    :members:
    :undoc-members:
    :private-members:
    :show-inheritance:
