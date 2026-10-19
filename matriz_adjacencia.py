# Atividade Avaliativa 2 - Grafos usando Matriz de Adjacencia
# Integrantes:
# - Carlos Heinrich Ribeiro de Oliveira - RA 2025953
# - Luiz Antonio Marcussi Neto - RA 2035498
# - Marcos Tulio Lopes Junior - RA 2036120
# - Mateus Oliveira Augusto - RA 2037913

# a lista vertices guarda o nome de cada vertice, e a posicao dele
# nessa lista e o indice da linha/coluna dele na matriz
# matriz[i][j] = 1 quer dizer que tem aresta do vertice i pro vertice j
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
    if v in vertices:
        print("O vertice", v, "ja existe")
        return

    vertices.append(v)
    # coloca uma coluna nova em cada linha que ja existe
    for linha in matriz:
        linha.append(0)
    # e cria a linha do vertice novo
    matriz.append([0] * len(vertices))
    print("Vertice", v, "inserido")


def remover_vertice(v):
    i = indice(v)
    if i == -1:
        print("Vertice nao encontrado")
        return

    vertices.pop(i)
    matriz.pop(i)  # tira a linha
    for linha in matriz:
        linha.pop(i)  # tira a coluna
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
            # soma da linha = saida, soma da coluna = entrada
            saida = sum(matriz[i])
            entrada = 0
            for k in range(n):
                entrada += matriz[k][i]
            print(vertices[i], "-> entrada:", entrada, "| saida:", saida, "| total:", entrada + saida)
        else:
            grau = sum(matriz[i])
            # laco conta 2 no grau
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

    print("   ", end="")
    for v in vertices:
        print(v.rjust(3), end="")
    print()
    for i in range(len(vertices)):
        print(vertices[i].rjust(3), end="")
        for valor in matriz[i]:
            print(str(valor).rjust(3), end="")
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
direcionado = resp == "s"

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
        if existe_aresta(x, y):
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
