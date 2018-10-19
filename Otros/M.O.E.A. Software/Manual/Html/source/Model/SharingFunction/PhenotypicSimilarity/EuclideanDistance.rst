EuclideanDistance (script)
==========================


| La Distancia Euclidiana **(ó Euclidean Distance)** es una implementación 
 de cálculo de distancia entre dos Individuos que pertenece a la subcategoría 
 Phenotypic Similarity **(ó Similaridad Fenotípica)**.
| Esta versión está dirigida para las Funciones Objetivo **(ó Objective Functions)**
 que poseen cada uno de los Individuos **(ó Individuals)** de una Población **(ó Population)**.
|
| Primero que nada para obtener el cálculo de :math:`\sigma_{share}` la operación está regida por la siguiente
 fórmula:
.. centered:: :math:`\sigma_{share} = \frac{\sum_{j=1}^{n\acute{u}m\_funciones\_objetivo}(max(F_j) - min(F_j))}{tama\tilde{n}o\_poblaci\acute{o}n - 1}`
| Lo anterior significa que se van a obtener los valores máximo y mínimo de cada función objetivo, 
 se restan entre sí y al resultado anterior se le divide entre el tamaño de la población menos uno; esto por cada generación.
|
| La forma de hacer el cálculo de la distancia es la siguiente:
| Supongamos que tenemos los vectores :math:`U = (u_1,u_2,...,u_n)` y :math:`V = (v_1,v_2,...,v_n)`. Entonces la Distancia Euclidiana se define como:
.. centered:: :math:`d_E(U,V) = \sqrt{(v_1 - u_1)^2 + (v_2 - u_2)^2 + ... + (v_n - u_n)^2}`
| Para los fines que nos conciernen, los vectores :math:`U\ y\ V` serán las evaluaciones en las funciones objetivos 
 de cada Individuo participante.
|
| Finalmente es menester mencionar que, aunque tradicionalmente esta técnica se usa para Representaciones Cromosómicas
 **(véase Model/ChromosomalRepresentation)** de tipo FloatPoint **(ó Punto Flotante)**, en sentido estricto no se encuentra
 limitada sólo a este tipo de codificación.


.. automodule:: Model.SharingFunction.PhenotypicSimilarity.EuclideanDistance
    :members:
    :undoc-members:
    :private-members:
    :show-inheritance:
