#...======================[ Vetores ]==========================...

lista_de_tarefas = []

dia_semanal = ["Domingo","Segunda","Terça","Quarta","Quinta","Sexta","Sabado"]

matriz = [lista_de_tarefas, dia_semanal]


#...======================[ Funções ]==========================...

def adicionar_tarefa(dia, tarefa):
    
    lista_de_tarefas.append(tarefa)
    print("Adicionando com sucesso\n")
    return lista_de_tarefas

def remover_tarefa(dia, tarefa):
    print("Removendo")

def vizu_tarefas(dia):

    print(lista_de_tarefas)
    print("Vizualizando")

#...======================[ Inputs e Execução ]==========================...

print("Dias da semana começam de 0 e vai até o 6")

while True:

    try:
        decidir = int(input(" O que vc gostaria de fazer? \n [1] Adicionar\n [2] remover\n [3] Vizualizar tarefas\n"))
    except: print("Digite Números")
    
    if decidir == 1: #--------------- Adicionar ---------------
        
        try:
            dia = int(input("Digite o numero da semana de 0 a 6: "))
        except: print("Nem digo mais nada")

        tarefa = input("Digite a tarefa que deseja adicionar: ").strip()

        adicionar_tarefa(dia,tarefa)

    elif decidir == 2:#--------------- Remover ---------------
        
        try:
            dia = int(input("Digite o numero da semana de 0 a 6: "))
        except: print("Nem digo mais nada")
        tarefa = input("Digite a tarefa que deseja remover: ").strip

        remover_tarefa(dia,tarefa)
    
    elif decidir == 3: #--------------- Vizualizar ---------------
        vizu_tarefas(dia)
    
    else:
        saida = input("Deseja sair?\n [1] Sim\n [2] Não").strip()

        if saida == "1":
            continue
        elif saida == "2":
            break
        else: print("\nInvalidação...")