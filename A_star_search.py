# from networkx import Graph
from heapq import heappush, heappop

class Graph:
    def __init__(self):
        self.node_edge_list = []

    def neighbors(self, n):
        list = []
        for (src, target, weight) in self.node_edge_list:
            if src == n:
                list.append(target)
        return iter(list)

    def add_edge(self, a, b, weight):
        tup1 = (a, b, weight)
        tup2 = (b, a, weight)
        self.node_edge_list.append(tup1)
        self.node_edge_list.append(tup1)
        self.node_edge_list.append(tup2)
        return self.node_edge_list

    def get_edge_data(self, a ,b):
        for (src, target, weight) in self.node_edge_list:
            if src == a and target == b:
                return weight


A, B, C, D, E, F, G, H, I, L, M, N, O, P, R, S, T, U, V, Z = 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19
h = (366, 0, 160, 242, 161,
     178, 77, 151, 226, 244,
     241, 234, 380, 98, 193,
     253, 329, 80, 199, 374)
f = [-1 for i in range(20)]
g = [0 for i in range(20)]
open = []
close = []
parent = [-1 for i in range(20)]

def init_graph():
    graph = Graph()

    graph.add_edge(O, Z, 71)
    graph.add_edge(O, S, 151)
    graph.add_edge(A, Z, 75)
    graph.add_edge(A, S, 140)
    graph.add_edge(A, T, 118)
    graph.add_edge(L, T, 111)
    graph.add_edge(L, M, 70)
    graph.add_edge(D, M, 75)
    graph.add_edge(C, D, 120)
    graph.add_edge(C, R, 146)
    graph.add_edge(R, S, 80)
    graph.add_edge(F, S, 99)
    graph.add_edge(B, F, 211)
    graph.add_edge(C, P, 138)
    graph.add_edge(P, R, 97)
    graph.add_edge(B, P, 101)
    graph.add_edge(B, G, 90)
    graph.add_edge(B, U, 85)
    graph.add_edge(H, U, 98)
    graph.add_edge(E, H, 86)
    graph.add_edge(U, V, 142)
    graph.add_edge(I, V, 92)
    graph.add_edge(I, N, 87)

    return graph


def A_star_search(graph, start, goal):
    heappush(open, (h[start], start))
    while open:
        current = heappop(open)[1]
        if current == goal:
            break
        close.append(current)
        # 遍历当前节点的相邻节点
        for i in graph.neighbors(current):
            # 如果已经在close中，则检查下一个节点
            if close.count(i) > 0:
                continue
            elif open.count((f[i], i)) > 0:
                # 如果在open中
                # 如果经过current到达i更好的话，就更新
                if g[current] + graph.get_edge_data(current, i) < g[i]:
                    g[i] = g[current] + graph.get_edge_data(current, i)
                    f[i] = g[i] + h[i]
                    parent[i] = current
            else:
                # 即不在open表中也不在close表中，则创建一个新的点加入open
                g[i] = g[current] + graph.get_edge_data(current, i)
                f[i] = g[i] + h[i]
                parent[i] = current
                heappush(open, (f[i], i))

def print_path(goal):
    p = goal
    road = []
    road.append(p)
    while parent[p] != -1:
        road.append(parent[p])
        p = parent[p]
    print('start: ',end='')
    while road:
        print('{:d}->'.format(road.pop()), end='')

    print('end')


if __name__ == '__main__':
    graph = init_graph()
    [src, target] = input().split()
    A_star_search(graph, eval(src), eval(target))
    print_path(B)
    print(f[eval(target)])
