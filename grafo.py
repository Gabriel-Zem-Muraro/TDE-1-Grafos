#Gabriel Zem Muraro
#Gustavo Jansen
#Joao Pedro Bezerra

class Grafo:

    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.adjacencias = [[] for _ in range(num_vertices)]
        self.rotulos = ["" for _ in range(num_vertices)]

    def cria_adjacencia(self, i, j, peso):
        if i < 0 or i >= self.num_vertices or j < 0 or j >= self.num_vertices:
            print(f"Erro: vertices invalidos (i={i}, j={j}).")
            return

        for (destino, _) in self.adjacencias[i]:
            if destino == j:
                print(f"Adjacencia {i} -> {j} ja existe.")
                return

        self.adjacencias[i].append((j, peso))

    def remove_adjacencia(self, i, j):
        if i < 0 or i >= self.num_vertices or j < 0 or j >= self.num_vertices:
            print(f"Erro: vertices invalidos (i={i}, j={j}).")
            return

        for idx, (destino, _) in enumerate(self.adjacencias[i]):
            if destino == j:
                self.adjacencias[i].pop(idx)
                return

        print(f"Adjacencia {i} -> {j} nao encontrada.")

    def imprime_adjacencias(self):
        #print("\n")
        print("LISTA DE ADJACENCIAS DO GRAFO")
        #print("\n")

        for i in range(self.num_vertices):
            rotulo = f' ("{self.rotulos[i]}")' if self.rotulos[i] else ""
            print(f"Vertice {i}{rotulo} -> ", end="")

            if not self.adjacencias[i]:
                print("(sem adjacentes)")
            else:
                vizinhos = []
                for (destino, peso) in self.adjacencias[i]:
                    vizinhos.append(f"{destino} (peso {peso})")
                print(" | ".join(vizinhos))

        print("\n")

    def seta_informacao(self, i, valor):
        if i < 0 or i >= self.num_vertices:
            print(f"Erro: vertice {i} invalido.")
            return

        self.rotulos[i] = valor

    def adjacentes(self, i):
        if i < 0 or i >= self.num_vertices:
            print(f"Erro: vertice {i} invalido.")
            return 0, []

        adj = []
        for (destino, _) in self.adjacencias[i]:
            adj.append(destino)

        return len(adj), adj


if __name__ == "__main__":
    g = Grafo(5)

    g.seta_informacao(0, "Flamengo")
    g.seta_informacao(1, "Corinthians")
    g.seta_informacao(2, "Palmeiras")
    g.seta_informacao(3, "Athletico-PR")
    g.seta_informacao(4, "Gremio")

    g.cria_adjacencia(0, 1, 3)
    g.cria_adjacencia(0, 2, 2)
    g.cria_adjacencia(1, 0, 1)
    g.cria_adjacencia(1, 3, 2)
    g.cria_adjacencia(2, 4, 4)
    g.cria_adjacencia(3, 2, 1)
    g.cria_adjacencia(4, 0, 2)

    print("GRAFO INICIAL")
    g.imprime_adjacencias()

    print("\nADJACENTES DO FLAMENGO (vertice 0)")
    qtd, adj = g.adjacentes(0)
    print(f"Flamengo jogou contra {qtd} time(s): vertices {adj}")

    print("\nTESTE DE DUPLICACAO ")
    g.cria_adjacencia(0, 1, 3)

    print("\nREMOVENDO ADJACENCIA: Flamengo -> Palmeiras")
    g.remove_adjacencia(0, 2)

    print("\nGRAFO APOS REMOCAO ")
    g.imprime_adjacencias()

    print("\nATUALIZANDO ROTULO DO VERTICE 0 ")
    g.seta_informacao(0, "Flamengo-RJ")
    g.imprime_adjacencias()
