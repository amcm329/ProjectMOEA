MOGA (script)
=============


| Se desarrolla la técnica M.O.E.A. que lleva por nombre M.O.G.A. 
 **(Multi Objective Genetic Algorithm ó Algoritmo Genético Multi Objetivo)**.
| Su funcionamiento es el siguiente:
|
| 1.- Se crea la Población Padre, se evalúan las funciones objetivo de sus correspondientes Individuos.

| 2.- Se asigna a los Individuos un Ranking **(Fonseca & Flemming)** y posteriormente se calcula el Niche Count de la Población Padre.

| 3.- Tomando en cuenta los valores del punto 2 se obtiene el Fitness para cada Individuo y posteriormente su Shared Fitness.

| 4.- Se aplica el operador de selección sobre la Población Padre para determinar los elegidos para dejar descendencia.

| 5.- Se crea la Población Hija, se evalúan las funciones objetivo de sus correspondientes Individuos.

| 6.- Se asigna a los Individuos un Ranking **(Fonseca & Flemming)** y posteriormente se calcula el Niche Count de la Población Hija.

| 7.- Tomando en cuenta los valores del punto 6 se obtiene el Fitness para cada Individuo y posteriormente su Shared Fitness.

| 8.- La Población Hija pasará a ser la nueva Población Padre.

| 9.- Se repiten los pasos 4 a 8 hasta que se haya alcanzado el número límite de generaciones **(iteraciones)**.
|
| Como se puede apreciar, la implementación de este algoritmo es muy sencilla, además 
 se rige casi en su totalidad por el Shared Fitness **(ó Fitness Compartido)**, por lo 
 que la Presión Selectiva **(ó Selective Pressure)** incluida dependerá en gran medida
 de la función de Distancia que se utilice, así como de la magnitud indicada por
 el usuario.
|
| Finalmente es menester mencionar que para esta implementación el Ranking utilizado debe ser
 estrictamente el de Fonseca & Flemming **(véase Model/Community/Community.py)**.


.. automodule:: Model.MOEA.MOGA
    :members:
    :undoc-members:
    :private-members:
    :show-inheritance:
