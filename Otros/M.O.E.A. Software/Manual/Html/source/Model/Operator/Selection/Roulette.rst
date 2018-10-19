Roulette (script)
=================


| Se implementa el método de selección conocido como Roulette **(ó Ruleta)**. También es llamado 
 Proportional Selection **(ó Selección Proporcional)**.
| En la función se distinguen dos etapas principales: construir la ruleta y "ponerla a girar" para que se elija el elemento.
* Para la primera etapa se toma como base el Valor Esperado **(ó Expected Value)** de cada Individuo **(véase Model/Community/Population/Individual.py)**. 
 El Valor Esperado para fines de este proyecto es el número de "hijos" que un Individuo puede ofrecer. Éste se calcula de la siguiente forma:
.. centered:: :math:`Valor\_Esperado(Individuo) = \frac{tama\tilde{n}o\_poblaci\acute{o}n \cdot Fitness(Individuo)}{\sum_{i=1}^{tama\tilde{n}o\_poblaci\acute{o}n}Fitness(Individuo_i)}`
| Al final aquéllos con Valores Esperados altos tendrán lugar a mayores espacios en la ruleta y por ende su probabilidad de elección aumenta.
* Para recorrer la ruleta en realidad se toma un valor aleatorio entre 0 y la suma de los Valores Esperados. Entonces se van sumando los Valores Esperados de los Individuos hasta que se exceda el valor aleatorio mencionado antes. Aquel elemento cuyo Valor Esperado haya excedido la suma se considera el elegido y es seleccionado para la etapa de cruza.
| Para la selección de Individuos se efectúa la segunda operación tantas veces como el tamaño de la Población. 
| Cabe mencionar que el Valor Esperado ya se calcula de manera automática en este proyecto **(véase Model/Community/Population/Population.py)**.


.. automodule:: Model.Operator.Selection.Roulette
    :members:
    :undoc-members:
    :private-members:
    :show-inheritance:
