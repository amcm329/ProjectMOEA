NonLinearRankingFitness (script)
================================


| Se implementa la asignación de Fitness conocida como Non-Linear Ranking
 **(ó Ranking No Lineal)** que, a diferencia de los demás métodos, la aplica 
 usando como base la posición del Individual **(ó Individuo)** en la Population 
 **(ó Población)** como resultado de las operaciones de ranking
 **(véase Model/Community/Community.py)**.
| Posteriormente el Fitness se constituye tomando la posición del Individuo y
 una función polinomial **(la cual es una función no lineal, de ahí el nombre)**. 
| La fórmula es la siguiente:
.. centered:: :math:`Fitness(Individuo) = \frac{TP \cdot X^{posici\acute{o}n(Individuo)}}{\sum_{i=1}^{TP}X^{i - 1}}`
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


.. automodule:: Model.Fitness.NonLinearRankingFitness
    :members:
    :undoc-members:
    :private-members:
    :show-inheritance:
