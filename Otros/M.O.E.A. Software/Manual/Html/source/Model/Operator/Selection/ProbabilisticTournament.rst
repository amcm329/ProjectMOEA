ProbabilisticTournament (script)
================================	


| Se desarrolla la técnica conocida como Torneo Probabilístico **(ó Probabilistic Tournament)**.
| Tal como lo sugiere el nombre, la selección será llevada a cabo en forma de competencia
 directa entre los Individuos. 
| Tradicionalmente se comparan sus Fitness y de esta manera el Individuo ganador es aquél con 
 la cantidad mayor de Fitness, pero dado que se maneja un esquema probabilístico la decisión 
 no depende totalmente del factor antes mencionado.
|
| De esta manera se pueden recapitular los siguientes pasos:
* Tomar k :math:`(2 \leqslant k \leqslant tama\tilde{n}o\_poblaci\acute{o}n)` Individuos de la Población.
* Realizar el torneo de manera secuencial entre los elementos seleccionados anteriormente, esto es, tomar el elemento A y enfrentarlo con B, al resultado de la batalla anterior enfrentarlo con C y así sucesivamente.
 Para ello por cada encuentro se crea un número aleatorio entre 0 y 1, si el número es menor a 0.5 
 se toma al elemento con menor Fitness, de lo contrario se elige al de mayor Fitness.
 La operación se lleva a cabo hasta que se tenga un ganador de los k Individuos.
| Los dos pasos anteriores se repiten hasta que se hayan obtenido tantos Individuos 
 como el tamaño de la Población. 


.. automodule:: Model.Operator.Selection.ProbabilisticTournament
    :members:
    :undoc-members:
    :private-members:
    :show-inheritance:
