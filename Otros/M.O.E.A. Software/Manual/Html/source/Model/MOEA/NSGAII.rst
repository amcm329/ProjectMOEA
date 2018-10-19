NSGAII (script)
===============


En esta parte se lleva a cabo la implementación del M.O.E.A. denominado
N.S.G.A. II **(Non-dominated Sorting Genetic Algorithm ó Algoritmo Genético 
de Ordenamiento No Dominado)**.

La forma de proceder del método es la siguiente:

1.- Se crea una Población Padre **(de tamaño n)**, a la cual se le evalúan las funciones objetivo de sus Individuos, se les asigna un Ranking **(Goldberg)**
y posteriormente se les otorga un Fitness.

2.- Con base en la Población Padre se aplica el operador de Selección para elegir a los Individuos que serán aptos para reproducirse.

3.- Usando a los elementos del punto 2, se crea una Población Hija **(de tamaño n)**. 
 
4.- Se crea una súper Población **(llamémosle S, de tamaño 2n)** que albergará todos los Individuos tanto de la Población Padre como Hija; a *S* se le evalúan las funciones objetivo de sus Individuos, se les asigna un Ranking **(Goldberg)** y posteriormente se les otorga un Fitness. 

5.- La súper Población *S* se divide en subcategorías de acuerdo a los niveles de dominancia que existan, es decir, existirá la categoría de dominancia 0, la cual almacena Individuos que tengan una dominancia de 0 Individuos **(ningún Individuo los domina)**, existirá la categoría de dominancia 1 con el significado análogo y así sucesivamente hasta haber cubierto todos los niveles de dominancia existentes.

6.- Se construye la nueva Población Padre, pare ello constará de los Individuos de *S* donde la prioridad será el nivel de dominancia, es decir, primero se añaden los elementos del nivel 0,luego los del nivel 1 y así en lo sucesivo hasta haber adquirido n elementos.
Se debe aclarar que la adquisición de Individuos por nivel debe ser total, esto significa que no se pueden dejar Individuos sueltos para el mismo nivel de dominancia. 

Supongamos que a un nivel k existen tantos Individuos que su presunta adquisición supera el tamaño n, en este caso se debe hacer lo siguiente:
    
 6.1.- Se crea una Población provisional **(Prov)** con los Individuos del nivel k, se evalúan las funciones objetivo a cada uno de sus Individuos, se les asigna un Ranking **(Goldberg)** y posteriormente se les asigna el Fitness.

 Con los valores anteriores se calcula el Niche Count **(véase Model/SharingFunction)** de los Individuos; una vez hecho ésto se seleccionan desde Prov los Individuos faltantes con los mayores Niche Count, esto hasta completar el tamaño n de la nueva Población Padre.

7.- Al haber conformado la nueva Población Padre, se evalúan las funciones objetivo de sus Individuos, se les asigna el Ranking correspondiente **(Goldberg)** y se les atribuye su Fitness.

8.- Se repiten los pasos 2 a 7 hasta haber alcanzado el límite de generaciones **(iteraciones)**.

| Como su nombre lo indica, la característica de este algoritmo es la clasificación 
 de los Individuos en niveles para su posterior selección.

| Esto al principio propicia una Presión Selectiva moderada por la ausencia de elementos 
 con dominancia baja que suele existir en las primeras generaciones, sin embargo en iteraciones 
 posteriores se agudiza la Presión Selectiva ya que eventualmente la mayoría de los Individuos 
 serán alojados en las primeras categorías de dominancia, cubriendo casi instantáneamente 
 la demanda de Individuos necesaria en el paso 6, por lo que las categorías posteriores serán 
 cada vez menos necesarias con el paso de los ciclos.

| Por otra parte la fusión de las Poblaciones en *S* garantiza que siempre se conserven a 
 los mejores Individuos independientemente de la generación transcurrida, a eso se le llama Elitismo.
| Por cierto que en el algoritmo original no existe un nombre oficial para *S* sino más bien se señala como
 una estructura genérica, sin embargo se le ha formalizado con un identificador para guiar apropiadamente al 
 usuario en el flujo del algoritmo.
 
| Para finalizar se señala que el uso del ranking de Goldberg **(véase Model/Community/Community.py)** 
 es indispensable.


.. automodule:: Model.MOEA.NSGAII
    :members:
    :undoc-members:
    :private-members:
    :show-inheritance:
