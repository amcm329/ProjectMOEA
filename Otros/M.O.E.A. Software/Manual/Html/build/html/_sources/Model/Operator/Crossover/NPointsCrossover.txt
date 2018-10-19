NPointsCrossover (script)
=========================


| Se implementa el método que lleva por nombre N-Points Crossover **(ó Cruza en N-Puntos)**.
 Para comenzar, esta técnica está elaborada para usarse tanto por Representación Cromosómica
 **(véase Model/ChromosomalRepresentation)** de tipo FloatPoint **(ó de Punto Flotante)** como
 Binary **(ó Binaria)**.
| Su funcionamiento consiste en construir a los descendientes usando sub-bloques de cromosomas de cada 
 uno de los padres, determinados éstos por una cierta cantidad de puntos de corte, de ahí el nombre.
| Aterrizando lo anterior de una manera concisa se tiene lo siguiente:
* Consideremos a los cromosomas de los padres Padre I: :math:`I_1I_2...I_n` 
 y Padre J: :math:`J_1J_2...J_n`
* Posteriormente se determinan aleatoriamente los puntos de corte, cabe mencionar que si los cromosomas son de tamaño n, pueden existir máximo n - 1 puntos. Supongamos que se crean k puntos :math:`(1 \leqslant k \leqslant n - 1)` y por lo tanto cada cromosoma queda separado en k + 1 bloques. 
 De esta manera obtenemos:
 Padre I en bloques **(BI)**: :math:`BI_1BI_2...BI_{k + 1}`;
 Padre J en bloques **(BJ)**: :math:`BJ_1BJ_2...BJ_{k + 1}`.
* Finalmente cada hijo constará de la alternancia de bloques de manera secuencial comenzando por el bloque inicial de un padre determinado, dicho de otra forma, los hijos estarán constituidos de la siguiente manera:
 * Para el hijo :math:`H_1`: :math:`BI_1BJ_2...BI_{k + 1}` 
 * Para el hijo :math:`H_2`: :math:`BJ_1BI_2...BJ_{k + 1}`
| Sólo queda mencionar que hasta el cierre de este proyecto no existe una manera 
 transparente desde el View **(ó Vista)** de conocer, dada una representación Binaria 
 y un conjunto de variables de decisión y funciones objetivo, el número máximo de puntos 
 de corte permitidos para este procedimiento, sin embargo, una manera de mitigar esta situación
 fue contemplar algún posible caso de error en esta sección y mandar un mensaje de error a la Vista
 por si llegase a suceder algún desperfecto durante el proceso.


.. automodule:: Model.Operator.Crossover.NPointsCrossover
    :members:
    :undoc-members:
    :private-members:
    :show-inheritance:
