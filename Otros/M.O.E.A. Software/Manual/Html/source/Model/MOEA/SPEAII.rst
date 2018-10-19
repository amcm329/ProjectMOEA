SPEAII (script)
===============


Se desarrolla la implementación de la técnica M.O.E.A. conocida como S.P.E.A. II
**(Strength Pareto Evolutionary Algorithm ó Algoritmo Evolutivo de Fuerza de Pareto)**.

El funcionamiento del algoritmo es el siguiente:

| 1.- Se inicializa una población llamada *P* y un conjunto inicialmente vacío llamado *E* **(E albergará Individuos también)**; ambos son de tamaño n.

| 2.- Se asigna el Fitness a los Individuos de *P* y *E* **(para ello se evalúan las funciones objetivo de los Individuos de ambos conjuntos y se asigna el Ranking Zitzler & Thiele)**.

| 3.- A continuación se funden *P* y *E* en una súper Población **(llamémosle S también señalado en el algoritmo como Mating Pool, de tamaño n)**.Para ello primero se añaden los Individuos *NO DOMINADOS* de *P* en *S* y posteriormente los *NO DOMINADOS* de *E* en *S*.
| Aquí se distinguen dos casos:
*   Si llegasen a faltar Individuos se añaden al azar Individuos *DOMINADOS* de *P* en *S* hasta completar la demanda.
*   Si después de la fusión el número de Individuos supera a n, entonces se hace un truncamiento en *S* hasta ajustar su tamaño a n.

| 4.- *S* será la nueva *E*, además se crea la población Hija de la recién creada *E* **(E-Child)**.

| 5.- E-Child será la nueva P.

| 6.- Se repiten los pasos 2 a 5 hasta que se haya alcanzado el límite de generaciones **(iteraciones)**.

| Finalmente lo que se regresa es *E*, ya que ahí es donde se han 
 almacenado los mejores Individuos de todas las generaciones.
|
| La característica de este algoritmo es que tiene una Presión Selectiva alta ya que 
 se da prioridad a los Individuos no dominados **(de ahí el nombre de 
 Fuerza de Pareto ó los más fuertes con respecto al principio de Pareto)**, 
 y el hecho de mezclar a *E* y *P* en una súper Población garantiza la conservación 
 de los mejores Individuos sin importar el transcurso de las generaciones 
 **(a eso se le conoce como Elitismo)**, pero también da una tolerancia, aunque mínima, a los
 Individuos de menor calidad como en el punto 3.
| Además al momento de actualizar *S* a *E* y E-Child a *P* se tiene una especie de 
 seguro de vida, es decir, si en algún momento la población E-Child llegara a 
 tener una calidad baja se tiene el respaldo de *E* para una generación posterior
 para formar *S*.
|
| Se debe tener en cuenta que el algoritmo originalmente no contempla ni una súper 
 Población *S* ni E-Child sino que en los pasos 3 y 4 se utiliza solamente *E* para referirse tanto a E-child como a *S*,
 sin embargo para no confundir al usuario en la funcionalidad del método se decidió colocar contenedores 
 extra para poder diferenciar más precisamente a los elementos involucrados.
|
| Algo muy importante a mencionar es que en el paso 1 y al momento de crear la población E-Child
 es necesario evaluar las funciones objetivo, asignar un Ranking y posteriormente un Fitness 
 para que se puedan aplicar los operadores geneticos **(véase Model/GeneticOperator)**, para este caso 
 el Ranking es estrictamente el de Zitzler & Thiele; la descripción completa de éste se 
 encuentra en **Model/Community/Community.py**.


.. automodule:: Model.MOEA.SPEAII
    :members:
    :undoc-members:
    :private-members:
    :show-inheritance:
