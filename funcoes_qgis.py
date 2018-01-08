# -*- coding: utf-8 -*-

from qgis.core import *
from qgis.gui import *
from re import sub

@qgsfunction(args="auto", group='Lista')
def verifica_valor(lista, divisor, dado, feature, parent):
    """ Essa funcao verifica se o se um determinado valor encontra-se dentro de uma determinada lista. 
	LISTA = coluna onde encontra-se o dado.
	DIVISOR = simbolo utilizado para separar o dado, deve estar entre ''. Exemplo: ',' ou ':'.
	DADO = Valor procurado dentro da coluna. """
    remove = "[{} ]".format(divisor)
    val = list(sub(remove, '', lista))
    for i in val:
        if i == str(dado):
            return dado