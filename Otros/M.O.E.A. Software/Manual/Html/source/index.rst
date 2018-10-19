.. figure:: Icon/unam_shield.png
   :height: 155 px
   :width: 155 px
   :align: left


.. figure:: Icon/sciences_shield.png
   :height: 155 px
   :width: 155 px
   :align: right


==================================
Documentación de M.O.E.A. Software
==================================

| La presente información corresponde a la documentación relacionada con el
 producto de software denominado **M.O.E.A. Software**, la cual, en conjunto con 
 el programa antes mencionado y la obra escrita, constituyen el proyecto que el
 ciudadano **Aarón Martín Castillo Medina** presenta con la finalidad de obtener el
 título de **Licenciado en Ciencias de la Computación**.

| Como se ha mencionado previamente, este escrito recopila las características 
 fundamentales del producto de software tales como las funcionalidades creadas, así 
 como su organización y las relaciones existentes entre éstas.
| No obstante al ser el producto de software mismo una fusión entre la teoría 
 comprendida en el trabajo escrito y sus correspondientes implementaciones técnicas, 
 la documentación por ende también incluye referencias que manifiestan la teoría 
 detrás de cada una de las funcionalidades creadas.

| Con base en lo anterior, es preciso mencionar que en la documentación existe
 terminología meramente técnica que conviene explicar para garantizar
 una comprensión sólida del proyecto.

| Lo primero que se debe hacer notar es la arquitectura de diseño. 
| Este concepto corresponde al tipo de organización que se suele emplear para agrupar 
 y comunicar apropiadamente cada uno de los componentes del producto de software 
 con la finalidad de minimizar los tiempos de corrección y actualización del código, así 
 como proporcionar una presentación digerible para cualquiera que desee familiarizarse con
 las partes codificadas.
| Para este proyecto se ha elegido la arquitectura denominada MVC **(Model-View-Controller ó Modelo-Vista-Controlador)**.
| Siguiendo este tipo de organización, se colocan las funcionalidades en tres 
 categorías principales, que son:

* Model **(ó Modelo)**, se almacenan todos los elementos que realizarán el proceso analítico, en este caso todo lo relacionado con la ejecución de M.O.E.A.'s y la recolección de resultados.

* View **(ó Vista)**, se coloca todo aquéllo asociado a la interfaz gráfica del programa y en el caso del proyecto, la graficación apropiada de resultados.

* Controller **(ó Controlador)**, se guarda toda la parafernalia relativa al control de las comunicaciones entre la Vista y el Modelo.

El proceso usual de interacción entre dichas categorías es el siguiente:

1. El usuario inserta las configuraciones pertinentes en la Vista, las cuales permitirán obtener resultados detallados del M.O.E.A. que se fuera a ejecutar.
2. El Controlador obtiene las configuraciones previamente insertadas por el usuario; durante esta etapa se realiza una verificación y saneamiento de dichas configuraciones. Si el proceso fue exitoso se procede ir al paso **(3)**, en cualquier otro caso se retrocede al paso **(1)** con una notificación de error.
3. El Modelo se encarga de ejecutar el algoritmo precisado por el usuario en **(1)**, para ello se le proporcionan todas las configuraciones adjuntas. Una vez concluido el proceso el Modelo le regresa los resultados al Controlador.
4. El Controlador toma los resultados y a su vez los transfiere a la Vista, quien se encarga de mostrar al usuario los datos finales de manera gráfica. 

En la documentación el usuario notará que las funcionalidades están colocadas siguiendo 
un esquema basado en la arquitectura antes mencionada. Esto permite vislumbrar de manera secundaria
los elementos y sus relaciones.

Con respecto de los tipos de funcionalidades creadas, en la documentación se muestran 
las siguientes clasificaciones **(de menor a mayor jerarquía)**:

* **Script**, el archivo básico de implementación, por lo general en éste se describe infraestructura simple como métodos o variables; su creación se atribuye a concebir el uso de técnicas disponibles para el usuario de una manera más eficiente y menos burocrática. Por lo general, este tipo de archivos se encuentran en el Modelo ya que su uso alude a entornos más dinámicos que requieran de una rápida respuesta.

* **Clase**, similar a los Scripts con la salvedad de que las Clases contienen una estructura más robusta pero también más estática. Su uso se limita en este proyecto a la generación de la interfaz gráfica **(en la Vista)** y en el Controlador ya que, por regla general, éstos deben estar predispuestos a las necesidades del usuario, ante lo cual se tiene la necesidad de destinar mayores recursos.

* **Módulo**, corresponde principalmente a una agrupación de Clases y/o Scripts con características en común. 

* **Sección**, mantiene relación directa con las categorías mencionadas en la arquitectura MVC. Contiene a todos los elementos anteriores.

| Habiendo proporcionado este preámbulo, la finalidad es, a grandes rasgos, 
 otorgar una guía rápida y concisa al usuario en lo concerniente a las funcionalidades 
 pertinentes del producto de software teniendo como apoyo el panorama teórico; la motivación
 detrás de ésto es facilitar la comprensión y posible modificación de componentes.

| Lo anterior deriva del hecho de que, desde el punto de vista del autor, el involucramiento del proyecto
 basándose en una perspectiva pragmática ha tenido un impacto mayor en los conocimientos adquiridos que
 si sólo se abordara un régimen estrictamente teórico.
| De esta manera se comparte dicha filosofía con todos aquéllos que deseen adentrarse en este 
 programa.

| Por consiguiente se refuerzan los puntos esenciales de motivación de la tesis: 
* La divulgación de las técnicas M.O.E.A.'s **(Multi-Objective Evolutionary Algorithms ó Algoritmos Evolutivos Multi-objetivo)** a través del producto de software.
* Comprobar la eficiencia de cada uno de estos M.O.E.A.'s tomando como fundamento el programa elaborado **(lo cual se abordará en la parte escrita)**.


| Ahora se muestra un índice que permite localizar a los componentes del programa
 más rápidamente.

Indices and tables
==================


* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`


| A continuación de muestra el diagrama del contenido del producto de software, donde cada uno de
 los elementos redireccionará al usuario a su respectiva documentación. 

Contenido:
==========


.. toctree::
   
   Begin
   Model/Model.rst
   View/View.rst
   Controller/Controller.rst
   
