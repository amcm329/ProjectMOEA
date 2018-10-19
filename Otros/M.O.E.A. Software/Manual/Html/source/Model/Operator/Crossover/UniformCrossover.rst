UniformCrossover (script)
=========================


| Se lleva a cabo la implementación de la técnica conocida como Uniform Crossover
 **(ó Cruza Uniforme)**.
| Primero que nada esta operación está fabricada para usarse tanto con la Representación
 Cromosómica **(véase Model/ChromosomalRepresentation)**
 de tipo FloatPoint **(ó Punto Flotante)** como Binary **(ó Binaria)**.
|
| La característica de este procedimiento es crear nuevos Individuos intercambiando 
 secuencialmente los genes de sus padres; visto de una manera más estructurada consiste en lo siguiente:
* Tenemos a los cromosomas de los padres Padre A: :math:`A_1A_2...A_n` 
 y Padre B: :math:`B_1B_2...B_n`
* Ahora, cada hijo será construido con genes de uno y sólo uno de los padres a menos que se indique lo contrario; este movimiento será posible con una variable denominada Pmask **(Pm)** que toma valores de 0 a 1 y una probabilidad de Pmask **(Pp)** que también toma valores de 0 a 1. Entonces lo anterior se puede declarar así:   
 * Para el hijo :math:`(H_1)` que tomará sus genes del padre A **(PA)**: 
  Si :math:`Pm \leqslant Pp\ entonces\ H_1(i) = A_i,\ en\ otro\ caso\ H_1(i) = B_i; 1 \leqslant i \leqslant n`
 * Para el hijo :math:`(H_2)` que tomará sus genes del padre B **(PB)**: 
  Si :math:`Pm \leqslant Pp\ entonces\ H_2(i) = B_i,\ en\ otro\ caso\ H_1(i) = A_i; 1 \leqslant i \leqslant n`


.. automodule:: Model.Operator.Crossover.UniformCrossover
    :members:
    :undoc-members:
    :private-members:
    :show-inheritance:
