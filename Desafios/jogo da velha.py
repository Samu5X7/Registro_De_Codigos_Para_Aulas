#Criar jogo da velha, para desafio escolar 
#Usar o conceito de matriz 
#Usar o conceito de List Compression 

jogoDaVelha = [0, 1, 2, 3, 4, 5, 6, 7, 8]

def mostrar_tabuleiro():
    print(f"""
        {jogoDaVelha[0]} | {jogoDaVelha[1]} | {jogoDaVelha[2]}
        --+---+--
        {jogoDaVelha[3]} | {jogoDaVelha[4]} | {jogoDaVelha[5]}
        --+---+--
        {jogoDaVelha[6]} | {jogoDaVelha[7]} | {jogoDaVelha[8]}
    """)

def verificar_vencedor():
    combinacoes = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]
    for a, b, c in combinacoes:
        if jogoDaVelha[a] == jogoDaVelha[b] == jogoDaVelha[c]:
            return jogoDaVelha[a]
    return None

def jogar():
    jogador = "X"
    jogadas = 0

    while True:
        mostrar_tabuleiro()
        posicao = input(f"Jogador {jogador}, escolha uma posição (0-8): ")

        if not posicao.isdigit():
            print("Digite um número válido!")
            continue

        posicao = int(posicao)

        if posicao < 0 or posicao > 8:
            print("Posição inválida!")
            continue

        if jogoDaVelha[posicao] in ["X", "O"]:
            print("Posição já ocupada!")
            continue

        jogoDaVelha[posicao] = jogador
        jogadas += 1

        vencedor = verificar_vencedor()
        if vencedor:
            mostrar_tabuleiro()
            print(f"Jogador {vencedor} venceu!")
            break

        if jogadas == 9:
            mostrar_tabuleiro()
            print("Empate!")
            break

        # Alternar jogador
        jogador = "O" if jogador == "X" else "X"

# Iniciar o jogo
jogar()
