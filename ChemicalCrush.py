import os
import random
import time


def Line_art():
    art = [
        "  ***   *  *   |***  ***   ***  *   ***    ***    *             ***   *  *   *  *  ****   *   *",
        " *      ****   |***  *  * *  *  *  *      * * *   *            *      ****   *  *    \    **** ",
        "  ***   *  *   |***  *   *   *  *   ***  *     *  ****          ***   *  *   ****  ****   *   *",
    ]
    for i in art:
        print(i)


def Clear():
    if os.name == "nt":
        os.system("cls")  # Comando para Windows
    else:
        os.system("clear")  # Comando para Unix


def Menu(inicio):  # Funcao de exibição do menu do jogo
    Line_art()
    print(" " * 43, "Menu")
    print(" " * 38, "1: Iniciar;")
    print(" " * 38, "2: Sair;")
    pontuacao = 0
    opcao = int(input("Digite sua escolha: "))
    if (opcao == 1):
        Clear()
        print(" " * 14, "\nForme 3 molecuals de água!")
        InGame(inicio, pontuacao)


def Efeito_Point(pontuacao):
    Clear()
    print("*********** Parabéns Você Fez Mais um Ponto! ***********")
    print(" " * 20, "Pontuacão:", pontuacao)
    time.sleep(3)


def InGame(elementos, pontuacao):
    Clear()
    print("********** Forme 3 molecuals de água! **********\n")
    print(" " * 8, "A", " " * 5, "B", " " * 5, "C", " " * 15, "Pontuação atual:", pontuacao)
    print(" " * 3, "-" * 26)
    guiaLinha = 1
    for i in elementos:
        print(guiaLinha, "|", end="")
        for j in i:
            print(" " * 5, j, end=" ")
        if (guiaLinha == 1):
            print(" " * 7, "Se oriente pelas coordenadadas que separam linhas e colunas. ", end="")
        elif (guiaLinha == 2):
            print(" " * 7,
                  "Selecione primerio a coluna, depois a linha e por ultimo o movimento (cima, baixo, direita, esquerda)",
                  end="")
        else:
            print(" " * 7, "Exemplo: Escolha uma linha: 2;\n", " " * 42, "Escolha uma coluna: B;\n", " " * 42,
                  "Escolha um movimento: cima;\n", " " * 33, "Apenas digitando o comando e pressionando 'Enter'.\n",
                  " " * 33, "Para sair digite 0.", end="")
        guiaLinha += 1
        print("\n")
    time.sleep(3)
    while (Point(elementos) == 1 and pontuacao < 3):
        pontuacao += 1
        Efeito_Point(pontuacao)
        return InGame(elementos, pontuacao)
    if (pontuacao >= 3):
        Clear()
        print("*********** Parabéns Você Ganhou! ***********\n")
        print(" " * 13, "Jogo Encerrado.")
        os._exit(0)
        time.sleep(5)
    else:
        print("Faça sua jogada!")
        elementos = Movimenta(elementos, Jogada_Linha(), Jogada_Coluna(), Jogada_Mov())
        return InGame(elementos, pontuacao)


def Movimenta(elementos, linha, coluna, movimento):  # Função para realizar a alteração aplicada pelo jogador na matriz
    if (movimento == "cima" and linha > 0):
        elementos[linha][coluna], elementos[linha - 1][coluna] = elementos[linha - 1][coluna], elementos[linha][coluna]
    elif (movimento == "direita" and coluna < 2):
        elementos[linha][coluna], elementos[linha][coluna + 1] = elementos[linha][coluna + 1], elementos[linha][coluna]
    elif (movimento == "baixo" and linha < 2):
        elementos[linha][coluna], elementos[linha + 1][coluna] = elementos[linha + 1][coluna], elementos[linha][coluna]
    elif (movimento == "esquerda" and coluna > 0):
        elementos[linha][coluna], elementos[linha][coluna - 1] = elementos[linha][coluna - 1], elementos[linha][coluna]
    else:
        print("Escolha um movimento válido dentro ")
        time.sleep(3)
    return elementos


def Jogada_Linha():  # Funcao para receber a entrada do jogador, referente a linha e evitar erros
    linha = input("Escolha uma linha: ")
    while (linha not in ['1', '2', '3', '0']):
        print("Digite um valor para linha entre 1 e 3!")
        linha = input("Escolha uma linha: ")
    if (linha == '0'):
        Clear()
        print("Jogo Encerrado.")
        os._exit(0)
    linha = int(linha) - 1
    return linha


def Jogada_Coluna():  # Funcao para receber a entrada do jogador, referente a coluna e evitar erros
    coluna = input("Escolha uma coluna: ")
    while (coluna.upper() not in ['A', 'B', 'C', '0']):
        print("Escolha uma coluna entre A, B e C!")
        coluna = input("Escolha uma coluna: ")
    if (coluna == '0'):
        Clear()
        print("Jogo Encerrado.")
        os._exit(0)
    elif (coluna == "A"):
        coluna = 0
    elif (coluna == "B"):
        coluna = 1
    else:
        coluna = 2
    return coluna


def Jogada_Mov():  # Funcao para receber a entrada do jogador, referente ao movimento e evitar erros
    mov = input("Escolha um movimento: ")
    while (mov.lower() not in ['cima', 'baixo', 'direita', 'esquerda', '0']):
        print("Escolha um movimento entre cima, baixo, direita e esquerda. Escreva em letra minuscula!")
        mov = input("Escolha um movimento: ")
    if (mov == '0'):
        Clear()
        print("Jogo Encerrado.")
        os._exit(0)
    return mov


def GeraElementos():  # Funcao para criar uma nova lista com elementos de maneira aleatória
    ch = 0  # Conta H
    co = 0  # Conta O
    elementos = ["H", "O"]
    novoselementos = []
    for i in range(0, 3):
        novoselementos.append(elementos[(random.randint(0, 1))])
        if (novoselementos[i] == "H"):
            ch += 1
        else:
            co += 1
    if (co != 1 and ch != 2):
        return novoselementos
    else:
        return GeraElementos()


def SubNovoElem(elementos, cord, num):  # Função para substituir os elementos após fazer um ponto
    aux = GeraElementos()
    if (cord == 'h'):  # Inserir na Horizontal
        for i in range(0, 3):
            elementos[num][i] = aux[i]
    else:  # Inserir na Vertical
        for i in range(0, 3):
            elementos[i][num] = aux[i]

    return elementos


def Point(elementos):  # Função para verificar se houve a formação de H2O
    chv = 0  # Conta H na Vertical
    chh = 0  # Conta H na Horizontal
    cov = 0  # Conta O na Vertical
    coh = 0  # Conta O na Horizontal

    for i in range(0, 3):  # Verificação se foi pontuado na horizontal
        for j in range(0, 3):
            if (elementos[i][j] == 'H'):
                chh += 1
            else:
                coh += 1
        if (chh == 2 and coh == 1):
            SubNovoElem(elementos, 'h', i)  # Formou H2O, então substituir linha
            return 1
        else:  # Caso não tenha forma H20, zerar os contadores para a proxima linha
            chh = 0
            coh = 0

    for i in range(0, 3):  # Verificação se foi pontuado na vertical
        for j in range(0, 3):
            if (elementos[j][i] == "H"):
                chv += 1
            else:
                cov += 1
        if (chv == 2 and cov == 1):
            SubNovoElem(elementos, 'v', i)  # Formou H2O, então substituir coluna
            return 1
        else:  # Caso não tenha forma H2O, zerar os contadores para a proxima coluna
            chv = 0
            cov = 0
    return 0


def main():
    Clear()
    inicio = [['H', "H", "H"], ["O", "Fe", "H"], ["C", "O", "H"]]
    Menu(inicio)
    return 0


main()