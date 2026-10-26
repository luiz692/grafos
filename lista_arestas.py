vertices = []
arestas = [] 
direcionado = False


def existe_vertice(v):
    return v in vertices


def inserir_vertice(v):
    if v == "":
        print("Nome invalido")
        return
    if " " in v:
        print("O nome do vertice nao pode ter espaco")
        return
    if existe_vertice(v):
        print("O vertice", v, "ja existe")
        return
    vertices.append(v)
    print("Vertice", v, "inserido")


def remover_vertice(v):
    global arestas
    if not existe_vertice(v):
        print("Vertice nao encontrado")
        return
    vertices.remove(v)

   
    nova = []
    for a in arestas:
        if a[0] != v and a[1] != v:
            nova.append(a)
    arestas = nova
    print("Vertice", v, "removido (e as arestas dele tambem)")


def existe_aresta(x, y):
    for a in arestas:
        if a[0] == x and a[1] == y:
            return True
        if not direcionado and a[0] == y and a[1] == x:
            return True
    return False


def inserir_aresta(x, y):
    if not existe_vertice(x) or not existe_vertice(y):
        print("Um dos vertices nao existe, insere ele primeiro")
        return
    if existe_aresta(x, y):
        print("Essa aresta ja existe")
        return
    arestas.append((x, y))
    print("Aresta", x, "-", y, "inserida")


def remover_aresta(x, y):
    for a in arestas:
        if a == (x, y) or (not direcionado and a == (y, x)):
            arestas.remove(a)
            print("Aresta removida")
            return
    print("Essa aresta nao existe")


def mostrar_graus():
    if len(vertices) == 0:
        print("Grafo vazio")
        return

    for v in vertices:
        if direcionado:
            entrada = 0
            saida = 0
            for a in arestas:
                if a[0] == v:
                    saida += 1
                if a[1] == v:
                    entrada += 1
            print(v, "-> entrada:", entrada, "| saida:", saida, "| total:", entrada + saida)
        else:
            grau = 0
            for a in arestas:
                if a[0] == v:
                    grau += 1
                if a[1] == v:
                    grau += 1
            print(v, "-> grau", grau)


def vizinhos(v):
    lista = []
    for a in arestas:
        if a[0] == v:
            lista.append(a[1])
        elif not direcionado and a[1] == v:
            lista.append(a[0])
    return lista


def verificar_percurso(caminho):
    if len(caminho) < 2:
        print("Digita pelo menos 2 vertices")
        return

    for v in caminho:
        if not existe_vertice(v):
            print("O vertice", v, "nao existe no grafo")
            return

    for i in range(len(caminho) - 1):
        if not existe_aresta(caminho[i], caminho[i + 1]):
            print("Percurso NAO e possivel, nao tem aresta de", caminho[i], "para", caminho[i + 1])
            return

    print("Percurso possivel!")


def mostrar_grafo():
    print("V = {" + ", ".join(vertices) + "}")

    lista = []
    for a in arestas:
        if direcionado:
            lista.append("(" + a[0] + "," + a[1] + ")")
        else:
            lista.append("{" + a[0] + "," + a[1] + "}")
    print("E = {" + ", ".join(lista) + "}")

    print("Lista de arestas:")
    if len(arestas) == 0:
        print("  (nenhuma)")
    for a in arestas:
        print("  ", a[0], "|", a[1])


def menu():
    print()
    print("------ GRAFO (Lista de Arestas) ------")
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
        if not existe_vertice(x) or not existe_vertice(y):
            print("Um dos vertices nao existe no grafo")
        elif existe_aresta(x, y):
            print("Existe aresta de", x, "para", y)
        else:
            print("Nao existe aresta de", x, "para", y)

    elif op == "7":
        v = input("Vertice: ").strip().upper()
        if not existe_vertice(v):
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
        mostrar_grafo()

    elif op == "0":
        print("Saindo...")
        break

    else:
        print("Opcao invalida")
