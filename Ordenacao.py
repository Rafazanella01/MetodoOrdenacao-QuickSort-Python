class Ordenacao:
    def quickSort(self, lista, primeiraPosicao, ultimaPosicao):
        pivo = lista[primeiraPosicao]
        ponteiroEsquerda = primeiraPosicao
        ponteiroDireita = ultimaPosicao

        while ponteiroEsquerda <= ponteiroDireita:
            while lista[ponteiroEsquerda] < pivo:
                ponteiroEsquerda += 1

            while lista[ponteiroDireita] > pivo:
                ponteiroDireita -= 1

            if ponteiroEsquerda <= ponteiroDireita:
                lista[ponteiroEsquerda], lista[ponteiroDireita] = lista[ponteiroDireita], lista[ponteiroEsquerda]
                ponteiroEsquerda += 1
                ponteiroDireita -= 1

        if primeiraPosicao < ponteiroDireita:
            self.quickSort(lista, primeiraPosicao, ponteiroDireita)
        if ponteiroEsquerda < ultimaPosicao:
            self.quickSort(lista, ponteiroEsquerda, ultimaPosicao)
    
        return lista
