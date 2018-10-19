ChromosomalRepresentation (módulo)
==================================


Ofrece elementos para elaborar una codificación adecuada. 

Entiéndase por codificación a la forma de determinar el cromosoma y sus propiedades; 
cabe mencionar que el cromosoma será portado por los Individuals **(ó Individuos)**.

Es importante mencionar que cualquier codificación implementada debe ser sustentada
en los métodos correspondientes al Crossover **(ó Cruza)** y Mutation **(ó Mutación)**,
ésto porque dichas operaciones funcionan con cromosomas.

De esta manera, la idea es que el usuario pueda crear sus propias codificaciones, 
por lo que, además de agregar la descripción de la codificación a Controller/XML/Features.xml
**(véase el archivo mencionado en la sección de código)**, deberá implementar por 
lo menos las siguientes funciones:


.. py:function:: calculate_length_subchromosomes(vector_variables,number_of_decimals,representation_parameters):
          
   Por cada variable de decisión se crea una porción del cromosoma, entonces en esta función se calcula
   el tamaño de cada porción **(ó subcromosoma)**, ya que al final las operaciones de cruza y mutación se realizarán
   sobre el súper crosomoma, el cual es la concatenacion de todos los subcromosomas. Por eso es importante identificar
   el tamaño de cada subcromosoma, así como sus límites dentro del súper cromosoma.   

   :param vector_variables: El vector de variables de decisión, donde cada variable trae consigo sus límites inferior
                            y superior.
   :param number_of_decimals: El número de decimales que deberá traer cada variable de decisión.
   :param representation_parameters: Un diccionario que contiene todas las opciones adicionales para cada tipo de
                                    codificación.

   :type vector_variables: List
   :type number_of_decimals: Integer
   :type representation_parameters: Dictionary
   :return: Una lista que contiene el tamaño del cromosoma por cada variable de decisión. Dado que el orden de las
            variables de decisión es inmutable, se preserva el mismo y por ello la lista contiene sólo los tamaños.
   :rtype: List


.. py:function:: create_chromosome(length_subchromosomes,vector_variables,number_of_decimals,representation_parameters):
 
   Función que crea el cromosoma. Se usa la como apoyo el método **calculate_length_subchromosomes** descrito con
   anterioridad. 

   :param length_subchromosomes: La lista que contiene los tamaños de cada variable de decisión.
   :param vector_variables: La lista que contiene las variables de decisión, así como sus rangos.
   :param number_of_decimals: El número de decimales que traerá cada variable de decisión.
   :param representation_parameters: Un diccionario que contiene todas las opciones adicionales para cada tipo de
                                     codificación.

   :type length_subchromosomes: List
   :type vector_variables: List
   :type number_of_decimals: Integer
   :type representation_parameters: Dictionary
   :return: El cromosoma devuelto en forma de lista.
   :rtype: List


.. py:function:: evaluate_subchromosomes(complete_chromosome,length_subchromosomes,vector_variables,number_of_decimals,representation_parameters): 

   Tomando en cuenta que el cromosoma ya ha sido creado usando los tamaños de los subcromosomas,
   en esta función se procede a evaluar el súper cromosoma partiéndolo en los subcromosomas pertinentes y evaluando
   individualmente cada uno de éstos.

   :param complete_chromosome: El súper cromosoma a ser evaluado.
   :param length_subchromosomes: La lista que contiene los tamaños de cada variable de decisión.
   :param vector_variables: La lista que contiene las variables de decisión, así como sus rangos.
   :param number_of_decimals: El número de decimales que traerá cada variable de decisión.
   :param representation_parameters: Un diccionario que contiene todas las opciones adicionales para cada tipo de
                                     codificación.

   :type complete_chromosome: List
   :type length_subchromosomes: List
   :type vector_variables: List
   :type number_of_decimals: Integer
   :type representation_parameters: Dictionary
   :return: Un diccionario que contiene como llave la variable de decisión y como valor la evaluación del
            subcromosoma correspondiente.
   :rtype: Dictionary


A continuación se develan los elementos que constituyen a este módulo:


.. toctree::
    :maxdepth: 2

    BinaryRepresentation.rst
    FloatPointRepresentation.rst
