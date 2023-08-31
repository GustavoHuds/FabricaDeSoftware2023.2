def case1():
    fila = []

    while True:
        opcao = input('digite 1 para adicionar tarefa, 2 para remover tarefa , 3 para mostrar 4 para sair')
        if opcao == 1:
            tarefa = input('adicione uma tarefa\n')
            fila.append(tarefa)
        elif opcao == 2:
            print(f'tarefa {fila[0]} removida')
            fila.pop(0)
        elif opcao == 3:
            print('tarefas:')
            print(fila)
        elif opcao == 4:
            break

def case2():
    fila = []

    while True:
        opcao = input('digite 1 para adicionar tarefa, 2 para remover tarefa , 3 para mostrar 4 para sair')
        if opcao == 1:
            tarefa = input('adicione uma tarefa\n')
            fila.append(tarefa)
        elif opcao == 2:
            print(f'tarefa {fila[0]} removida')
            fila.pop()
        elif opcao == 3:
            print('tarefas:')
            print(fila)
        elif opcao == 4:
            break

#Defina o caso 1 ou 2 (caseX())
case()