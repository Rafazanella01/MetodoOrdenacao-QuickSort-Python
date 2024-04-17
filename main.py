from Ordenacao import Ordenacao

ordenacao = Ordenacao()

lista = [9, 8, 7, 6, 5, 4, 3, 2, 1]

ultimaPos = len(lista) - 1

listaOrdenada = ordenacao.quickSort(lista, 0, ultimaPos)
print(listaOrdenada)