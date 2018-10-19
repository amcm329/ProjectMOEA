VEGA (script)
=============


| Se implementa la técnica M.O.E.A conocida como V.E.G.A. **(Vector Evaluated Genetic 
 Algorithm ó Algoritmo Genético de Vectores Evaluados)**.
| La forma de proceder del algoritmo es la siguiente:
|
| 1.- Se crea la Población Padre (de tamaño :math:`n`).

| 2.- Tomando en cuenta las :math:`k` funciones objetivo y la Población Padre, se crean :math:`k` subpoblaciones de tamaño :math:`n/k` cada una, si este número llega a ser irracional se pueden hacer ajustes con respecto de la distribución de los Individuos.

| 3.- Por cada subpoblación, se aplica la técnica de Selección y obtienen los :math:`n/k` Individuos, terminado esto se deben unificar todos los seleccionados de nuevo en una súper Población.

| 4.- Con la súper Población del paso 3, se crea a la población Hija, la cual pasará a convertirse en la la nueva Población Padre.

| 5.- Se repiten los pasos 2 a 4 hasta haber alcanzado el número de generaciones **(iteraciones)** límite.
|
| Como se puede apreciar es una implementación muy sencilla de optimización multiobjetivo,
 sin embargo el inconveniente que tiene es la fácil pérdida de material genético valioso.
| Lo anterior significa que un Individuo que en una generación previa era el mejor para una
 función objetivo :math:`i` al momento de ser separado y seleccionado en una subpoblación :math:`j`
 (y por ende analizado bajo la función objetivo :math:`j`) puede ser muy malo en calidad y por tanto no ser seleccionado; 
 perdiéndose la ganancia genética hasta el momento obtenida para la función objetivo :math:`i;\ i \neq j`.
|
| Por ello es que se puede decir que V.E.G.A. genera soluciones promedio que destacan con una calidad media
 para todas las funciones objetivo.
|
| Finalmente hay que comentar que para este algoritmo no se requiere aplicar un Ranking específico, no obstante,
 se ha decidido utilizar el de Fonseca & Flemming **(véase Model/Community/Community.py)** pues es el más sencillo
 de implementar.


.. automodule:: Model.MOEA.VEGA
    :members:
    :undoc-members:
    :private-members:
    :show-inheritance:
