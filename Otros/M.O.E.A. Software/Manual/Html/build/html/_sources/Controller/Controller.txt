Controller (Sección)
====================


Su función principal es la de establecer medidas de comunicación entre la Vista **(ó View)**
y el Modelo **(ó Model)** de tal manera que el Controller **(ó Controlador)** recibe los datos 
recabados en la Vista y los transfiere al Modelo para que se puedan llevar a cabo las operaciones 
pertinentes y una vez concluidas dichas labores los resultados pasan por éste para llegar a la Vista y 
desde ahí graficarse apropiadamente.

De manera secundaria el Controlador ofrece métodos de saneamiento de los datos recabados en la Vista,
con la finalidad de evitar al máximo disturbios indeseables en la sección Modelo y que éste opere con total
eficiencia, además de alimentar la Vista con las técnicas **(y sus respectivos parámetros)** disponibles
en la sección Modelo para así permitirle al usuario operar con éstas de manera expedita.

Dicho almacén se encuentra en la sección **Controller/XML**, donde se deduce que las técnicas y características
secundarias se encuentran plasmadas en archivos .xml

El proyecto contempla métodos para operar con dichos archivos y el usuario entonces sólo tendrá que preocuparse
por dar de alta la técnica pertinente en el archivo .xml adecuado **(además de implementarla en Modelo)** para que 
ésta sea reconocida en la sección Vista y se pueda hacer uso de ella.

A continuación se muestran los componentes principales de la sección Controller:


.. toctree::

    ControllerClass.rst
    XMLParser.rst
    Verifier.rst
