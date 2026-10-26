grafo = {}
direcionado = False


def inserir_vertice(v):
    if v == "":
        print("Nome invalido")
        return
    if " " in v:
        print("O nome do vertice nao pode ter espaco")
        return
    if v in grafo:
        print("O vertice", v, "ja existe")
        return
    grafo[v] = []
    print("Vertice", v, "inserido")


def remover_vertice(v):
    if v not in grafo:
        print("Vertice nao encontrado")
        return
    del grafo[v]

    
    for u in grafo:
        while v in grafo[u]:
            grafo[u].remove(v)
    print("Vertice", v, "removido")


def existe_aresta(x, y):
    if x not in grafo:
        return False
    return y in grafo[x]


def inserir_aresta(x, y):
    if x not in grafo or y not in grafo:
        print("Um dos vertices nao existe, insere ele primeiro")
        return
    if existe_aresta(x, y):
        print("Essa aresta ja existe")
        return

    grafo[x].append(y)
    if not direcionado and x != y:
        grafo[y].append(x)
    print("Aresta", x, "-", y, "inserida")


def remover_aresta(x, y):
    if not existe_aresta(x, y):
        print("Essa aresta nao existe")
        return
    grafo[x].remove(y)
    if not direcionado and x != y:
        grafo[y].remove(x)
    print("Aresta removida")


def mostrar_graus():
    if len(grafo) == 0:
        print("Grafo vazio")
        return

    for v in grafo:
        if direcionado:
            saida = len(grafo[v])
            entrada = 0
            for u in grafo:
                if v in grafo[u]:
                    entrada += 1
            print(v, "-> entrada:", entrada, "| saida:", saida, "| total:", entrada + saida)
        else:
            grau = len(grafo[v])
            # laco conta 2 no grau
            if v in grafo[v]:
                grau += 1
            print(v, "-> grau", grau)


def verificar_percurso(caminho):
    if len(caminho) < 2:
        print("Digita pelo menos 2 vertices")
        return

    for v in caminho:
        if v not in grafo:
            print("O vertice", v, "nao existe no grafo")
            return

    for i in range(len(caminho) - 1):
        if not existe_aresta(caminho[i], caminho[i + 1]):
            print("Percurso NAO e possivel, nao tem aresta de", caminho[i], "para", caminho[i + 1])
            return

    print("Percurso possivel!")


def mostrar_grafo():
    if len(grafo) == 0:
        print("Grafo vazio")
        return
    for v in grafo:
        print(v, "->", ", ".join(grafo[v]))


def menu():
    print()
    print("------ GRAFO (Lista de Adjacencia) ------")
    print("1 - Inserir vertice")
    print("2 - Remover vertice")
    print("3 - Inserir aresta")
    print("4 - Remover aresta")
    print("5 - Mostrar grau dos vertices")
    print("6 - Verificar se existe aresta")
    print("7 - Listar vizinhos de um vertice")
    print("8 - Verificar percurso")
    print("9 - Mostrar grafo")
    print("0 - Sair")


resp = input("O grafo e direcionado? (s/n): ").strip().lower()
while resp not in ("s", "sim", "n", "nao", "não"):
    print("Responde so com s ou n")
    resp = input("O grafo e direcionado? (s/n): ").strip().lower()
direcionado = resp in ("s", "sim")

while True:
    menu()
    op = input("Opcao: ").strip()

    if op == "1":
        v = input("Nome do vertice: ").strip().upper()
        inserir_vertice(v)

    elif op == "2":
        v = input("Vertice que vai remover: ").strip().upper()
        remover_vertice(v)

    elif op == "3":
        x = input("Vertice de origem: ").strip().upper()
        y = input("Vertice de destino: ").strip().upper()
        inserir_aresta(x, y)

    elif op == "4":
        x = input("Vertice de origem: ").strip().upper()
        y = input("Vertice de destino: ").strip().upper()
        remover_aresta(x, y)

    elif op == "5":
        mostrar_graus()

    elif op == "6":
        x = input("De qual vertice: ").strip().upper()
        y = input("Para qual vertice: ").strip().upper()
        if x not in grafo or y not in grafo:
            print("Um dos vertices nao existe no grafo")
        elif existe_aresta(x, y):
            print("Existe aresta de", x, "para", y)
        else:
            print("Nao existe aresta de", x, "para", y)

    elif op == "7":
        v = input("Vertice: ").strip().upper()
        if v not in grafo:
            print("Vertice nao encontrado")
        elif len(grafo[v]) == 0:
            print(v, "nao tem vizinhos")
        else:
            print("Vizinhos de", v + ":", ", ".join(grafo[v]))

    elif op == "8":
        caminho = input("Digita o percurso separado por espaco (ex: A B C): ").upper().split()
        verificar_percurso(caminho)

    elif op == "9":
        mostrar_grafo()

    elif op == "0":
        print("Saindo...")
        break

    else:
        print("Opcao invalida")
