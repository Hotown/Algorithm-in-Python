from networkx import Graph
from heapq import heappush, heappop
import queue
import numpy as np

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

    graph.add_edge(O, Z, weight=71)
    graph.add_edge(O, S, weight=151)
    graph.add_edge(A, Z, weight=75)
    graph.add_edge(A, S, weight=140)
    graph.add_edge(A, T, weight=118)
    graph.add_edge(L, T, weight=111)
    graph.add_edge(L, M, weight=70)
    graph.add_edge(D, M, weight=75)
    graph.add_edge(C, D, weight=120)
    graph.add_edge(C, R, weight=146)
    graph.add_edge(R, S, weight=80)
    graph.add_edge(F, S, weight=99)
    graph.add_edge(B, F, weight=211)
    graph.add_edge(C, P, weight=138)
    graph.add_edge(P, R, weight=97)
    graph.add_edge(B, P, weight=101)
    graph.add_edge(B, G, weight=90)
    graph.add_edge(B, U, weight=85)
    graph.add_edge(H, U, weight=98)
    graph.add_edge(E, H, weight=86)
    graph.add_edge(U, V, weight=142)
    graph.add_edge(I, V, weight=92)
    graph.add_edge(I, N, weight=87)

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
                if g[current] + graph.get_edge_data(current, i)['weight'] < g[i]:
                    g[i] = g[current] + graph.get_edge_data(current, i)['weight']
                    f[i] = g[i] + h[i]
                    parent[i] = current
            else:
                # 即不在open表中也不在close表中，则创建一个新的点加入open
                g[i] = g[current] + graph.get_edge_data(current, i)['weight']
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
    A_star_search(graph, A, B)
    print_path(B)
    print(f[B])