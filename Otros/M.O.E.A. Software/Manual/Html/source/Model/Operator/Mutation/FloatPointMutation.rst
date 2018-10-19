FloatPointMutation (script)
===========================


| Se concreta el método conocido como Float Point Mutation **(ó Mutación de Punto Flotante)**.
| El procedimiento es el siguiente:
* Se trata cada gen individualmente y se modifica de acuerdo a una probabilidad de Mutación asignada, si ésta es suficiente se procede a hacer el cambio, en otro caso se deja el alelo asociado al gen intacto.
* Retomando el caso en que se puede modificar el alelo del gen se verifica los límites de la variable de decisión que está ligada a éste, así como la precisión decimal. Entonces se crea el nuevo número con la precisión decimal requerida y se sustituye por el anterior.


.. automodule:: Model.Operator.Mutation.FloatPointMutation
    :members:
    :undoc-members:
    :private-members:
    :show-inheritance:
