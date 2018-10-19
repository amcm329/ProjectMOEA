Operator (módulo)
=================


| En éste se encuentran implementadas todas aquellas funcionalidades que intervengan 
 en el proceso de la creación de una nueva Population **(ó Población)** hija.
| La finalidad de ésto es propagar y realizar combinaciones de la carga genética de 
 los Individuals **(ó Individuos)** más aptos mediante el cromosoma **(véase Model/ChromosomalRepresentation)** para obtener soluciones con una mejor calidad 
 que sus predecesoras.
| Para este punto es importante mencionar que la calidad de un Individuo es directamente proporcional a su Fitness
 **(véase Model/Fitness)**
| En términos generales, la manera de construir una Población hija es la siguiente:
* De la Población actual y tomando como base el Fitness de cada Individuo se seleccionan aquéllos que serán los elegidos para reproducirse. Nótese que un Individuo puede ser tomado en cuenta más de una vez si se da el caso.
* Con base en los elegidos, se toman sus respectivos cromosomas y se realiza la operación de Crossover **(ó Cruza)**. Ésta es una simulación de una reproducción de tipo sexual donde se toman dos padres para "procrear" dos hijos. Las características de los hijos dependerán de las técnicas usadas **(véase Model/Operator/Crossover)**.
* Se toman los hijos y uno a uno se les aplica la operación de mutación.
Al final Población hija constará de los hijos "mutados".

A continuación se muestran las siguientes subcategorías correspondientes a los pasos descritos anteriormente, cada una con sus respectivas técnicas desarrolladas:


.. toctree::
    :maxdepth: 3

    Selection/Selection.rst
    Crossover/Crossover.rst
    Mutation/Mutation.rst
