vertices = []
matriz = []
direcionado = False


def indice(v):
    if v in vertices:
        return vertices.index(v)
    return -1


def inserir_vertice(v):
    if v == "":
        print("Nome invalido")
        return
    if " " in v:
        print("O nome do vertice nao pode ter espaco")
        return
    if v in vertices:
        print("O vertice", v, "ja existe")
        return

    vertices.append(v)
    for linha in matriz:
        linha.append(0)
    matriz.append([0] * len(vertices))
    print("Vertice", v, "inserido")


def remover_vertice(v):
    i = indice(v)
    if i == -1:
        print("Vertice nao encontrado")
        return

    vertices.pop(i)
    matriz.pop(i) 
    for linha in matriz:
        linha.pop(i)  
    print("Vertice", v, "removido")


def existe_aresta(x, y):
    i = indice(x)
    j = indice(y)
    if i == -1 or j == -1:
        return False
    return matriz[i][j] == 1


def inserir_aresta(x, y):
    i = indice(x)
    j = indice(y)
    if i == -1 or j == -1:
        print("Um dos vertices nao existe, insere ele primeiro")
        return
    if matriz[i][j] == 1:
        print("Essa aresta ja existe")
        return

    matriz[i][j] = 1
    if not direcionado:
        matriz[j][i] = 1
    print("Aresta", x, "-", y, "inserida")


def remover_aresta(x, y):
    i = indice(x)
    j = indice(y)
    if i == -1 or j == -1 or matriz[i][j] == 0:
        print("Essa aresta nao existe")
        return

    matriz[i][j] = 0
    if not direcionado:
        matriz[j][i] = 0
    print("Aresta removida")


def mostrar_graus():
    if len(vertices) == 0:
        print("Grafo vazio")
        return

    n = len(vertices)
    for i in range(n):
        if direcionado:
            
            saida = sum(matriz[i])
            entrada = 0
            for k in range(n):
                entrada += matriz[k][i]
            print(vertices[i], "-> entrada:", entrada, "| saida:", saida, "| total:", entrada + saida)
        else:
            grau = sum(matriz[i])
           
            if matriz[i][i] == 1:
                grau += 1
            print(vertices[i], "-> grau", grau)


def vizinhos(v):
    i = indice(v)
    lista = []
    for j in range(len(vertices)):
        if matriz[i][j] == 1:
            lista.append(vertices[j])
    return lista


def verificar_percurso(caminho):
    if len(caminho) < 2:
        print("Digita pelo menos 2 vertices")
        return

    for v in caminho:
        if v not in vertices:
            print("O vertice", v, "nao existe no grafo")
            return

    for i in range(len(caminho) - 1):
        if not existe_aresta(caminho[i], caminho[i + 1]):
            print("Percurso NAO e possivel, nao tem aresta de", caminho[i], "para", caminho[i + 1])
            return

    print("Percurso possivel!")


def mostrar_matriz():
    if len(vertices) == 0:
        print("Grafo vazio")
        return

    # largura da coluna depende do maior nome
    larg = 1
    for v in vertices:
        if len(v) > larg:
            larg = len(v)
    larg += 2

    print(" " * larg, end="")
    for v in vertices:
        print(v.rjust(larg), end="")
    print()
    for i in range(len(vertices)):
        print(vertices[i].rjust(larg), end="")
        for valor in matriz[i]:
            print(str(valor).rjust(larg), end="")
        print()


def menu():
    print()
    print("------ GRAFO (Matriz de Adjacencia) ------")
    print("1 - Inserir vertice")
    print("2 - Remover vertice")
    print("3 - Inserir aresta")
    print("4 - Remover aresta")
    print("5 - Mostrar grau dos vertices")
    print("6 - Verificar se existe aresta")
    print("7 - Listar vizinhos de um vertice")
    print("8 - Verificar percurso")
    print("9 - Mostrar matriz")
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
        if x not in vertices or y not in vertices:
            print("Um dos vertices nao existe no grafo")
        elif existe_aresta(x, y):
            print("Existe aresta de", x, "para", y)
        else:
            print("Nao existe aresta de", x, "para", y)

    elif op == "7":
        v = input("Vertice: ").strip().upper()
        if v not in vertices:
            print("Vertice nao encontrado")
        else:
            viz = vizinhos(v)
            if len(viz) == 0:
                print(v, "nao tem vizinhos")
            else:
                print("Vizinhos de", v + ":", ", ".join(viz))

    elif op == "8":
        caminho = input("Digita o percurso separado por espaco (ex: A B C): ").upper().split()
        verificar_percurso(caminho)

    elif op == "9":
        mostrar_matriz()

    elif op == "0":
        print("Saindo...")
        break

    else:
        print("Opcao invalida")
