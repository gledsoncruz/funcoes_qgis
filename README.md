# funcoes_qgis
Aqui estão contidas as funções que tenho criado para o QGIS.

Função verifica_valor:
  Recebe uma lista, ou um campo que contenha uma lista, os valores deve possui um separador (virgula, dois pontos, ponto e vírgula, etc),
  e retorna Verdadeiro ou Falso.
  Dependencias: 
  Lita de funções: "Lista"
  Sintaxe: verifica_valor(lista, divisor, dado)
  Argumentos:
  lista: É a lista, ou campo que conhenha uma lista.
  divisor: é o simbolo utilizado como separador (vírgula, ponto, dois pontos, ponto e vígula...) entre aspas simples ''.
  dado: é o dado que deseja procurar dentro da lista.
  Exemplo verifica_valor('1, 2, 3, 4', ',', 1) >> True
  OBS: É importante não utilizar letras como separador, bem como espaço e o simbolo _ (underline).
  
