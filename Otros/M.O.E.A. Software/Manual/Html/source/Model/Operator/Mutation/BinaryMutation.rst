BinaryMutation (script)
=======================


| Se implementa el método conocido como Binary Mutation **(ó Mutación Binaria)**.
| El procedimiento es el siguiente:
* Se trata cada gen individualmente y se modifica de acuerdo a una probabilidad de Mutación asignada, si ésta es suficiente se procede a hacer el cambio, en otro caso se deja el alelo asociado al gen intacto.
* Retomando el caso en que se puede modificar el alelo del gen se verifica su valor actual y ya que se maneja una representación Binaria su transformación es muy simple: si se encuentra un 0, el alelo toma el valor 1 y viceversa.


.. automodule:: Model.Operator.Mutation.BinaryMutation
    :members:
    :undoc-members:
    :private-members:
    :show-inheritance:
