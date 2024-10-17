'''
Usaremos uma matriz assim:
matriz[linha][coluna]
'''
import random


def imprimir_mensagem_inicial():
    print("JOGO DA VELHA")
    print("Você jogará com o X e o computador com o O")
    print("As posições que podem ser escolhidas são:")
    imprimir_tabuleiro()


def gerar_escolha_computador():
    ''' Gera uma escolha aleatória do computador'''
    linha = random.randint(1, 3)
    coluna = random.randint(1, 3)
    return (linha, coluna)


def imprimir_tabuleiro():
    print(f"| {tabuleiro[0][0]} | {tabuleiro[0][1]} | {tabuleiro[0][2]} |")
    print(f"| {tabuleiro[1][0]} | {tabuleiro[1][1]} | {tabuleiro[1][2]} |")
    print(f"| {tabuleiro[2][0]} | {tabuleiro[2][1]} | {tabuleiro[2][2]} |")


def avaliar_vencedor():
    # Implementar depois
    return False


tabuleiro = [["1", "2", "3"], ["4", "5", "6"], ["7", "8", "9"]]
imprimir_mensagem_inicial()


def obter_linha_no_tabuleiro_indexado_por_zero(posicao):
    return (posicao - 1) // 3


def obter_coluna_no_tabuleiro_indexado_por_zero(posicao):
    return (posicao - 1) % 3


def celula_esta_preenchida(linha, coluna):
    return tabuleiro[linha][coluna] == "X" or tabuleiro[linha][coluna] =="O"


while True:
    try:
        posicao = int(input("Escolha uma posição conforme você viu no tabuleiro: "))
                       
        if posicao < 1 or posicao > 9:
            raise ValueError("")
    except ValueError:
        print("Tente novamente, o número não é válido no intervalo de 1 a 9: ")
        continue
   
    linha = obter_linha_no_tabuleiro_indexado_por_zero(posicao)
    coluna = obter_coluna_no_tabuleiro_indexado_por_zero(posicao)


    if celula_esta_preenchida(linha, coluna):
        print("Tente novamente, esta célula já está preenchida")
    else:
        tabuleiro[linha][coluna] = "X"


    imprimir_tabuleiro()
