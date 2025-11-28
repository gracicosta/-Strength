import fileHandler as fh
from random import choice
import desenhos as d


def jogar():
    lista_palavras = list()
    arquivo = fh.abrirArquivoLeitura('palavras.txt')
    for linha in arquivo:
        palavra = linha.strip() #remove caracteres iniciais e finais de uma string
        lista_palavras.append(palavra)
    palavra_sorteada = choice(lista_palavras)

    for x in range(50):
        print()

    digitadas = []
    acertos = []
    erros = 0

    nome = input('Quem está jogando? ')

    while True:
        adivinha = d.imprimir_palavra_secreta(palavra_sorteada, acertos)
        #CONDIÇÃO DE VITORIA
        if adivinha == palavra_sorteada:
            print('Você acertou!')
            break

        #TENTATIVAS
        tentativa = input('\nDigite uma letra: ').lower().strip()

        if tentativa in digitadas:
            print('Você já usou essa letra! ')
            continue

        else:
            digitadas += tentativa #ou append
            if tentativa in palavra_sorteada:
                acertos += tentativa
            else:
                erros += 1
                print('Você errou!')


        score = d.desenha_forca(erros)


        #CONDIÇÂO DE FIM DE JOGO
        if erros == 6:
            print('Enforcado!')
            print(f'A palavra correta era {palavra_sorteada.upper()}\n')
            break
        
    fh.inserir_score('score.txt', nome, score)

