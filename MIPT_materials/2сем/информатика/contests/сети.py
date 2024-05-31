# # from collections import defaultdict

# # def dfs(graph, visited, u, t, f):
# #     if u == t:
# #         return f
# #     visited[u] = True
# #     for v, cap in graph[u]:
# #         if not visited[v] and cap > 0:
# #             df = dfs(graph, visited, v, t, min(f, cap))
# #             if df > 0:
# #                 graph[u][graph[u].index((v, cap))] = (v, cap - df)
# #                 graph[v][graph[v].index((u, graph[v][u]))] = (u, graph[v][u] + df)
# #                 return df
# #     return 0

# # def max_flow(graph, s, t):
# #     flow = 0
# #     while True:
# #         visited = [False] * len(graph)
# #         df = dfs(graph, visited, s, t, float('inf'))
# #         if df == 0:
# #             break
# #         flow += df
# #     return flow

# # N, M, K = map(int, input().split())

# # graph = defaultdict(list)
# # for _ in range(M):
# #     u, v = map(int, input().split())
# #     graph[u].append((v, 1))
# #     graph[v].append((u, 0))

# # if max_flow(graph, 0, N - 1) >= K:
# #     print("YES")
# # else:
# #     print("NO")




# class capacity():
#     def __init__(self):
#         self.n, self.m = map(int, input().split())
#         self.graph = [[] for _ in range(self.n)]
#         self.g1 = [{} for _ in range(self.n)]
#         self.g2 = [{} for _ in range(self.n)]
#         self.cap = 0
#         self.div = [float('INF')] + [0 for _ in range(self.n - 1)]
#         for _ in range(self.m):
#             a, b, w = map(int, input().split())
#             self.graph[a].append((b, w))
#             self.g1[a][b] = w
#             self.g2[b][a] = 0

    
#     def dfs(self, vertex, visited, tags, way):
#         if vertex == self.n - 1:
#             tag = min(tags)
#             for i in range(len(way)):
#                 if i < len(way) - 1:
#                     self.g1[way[i]][way[i + 1]] -= tag
#                 if i > 0:
#                     self.g2[way[i]][way[i - 1]] += tag
#             self.dfs(0, [], [float('INF')], [0])
#             return 0
        

#         else:
#             for child in self.g1[vertex]:
#                 valuue = self.g1[vertex][child]
#                 if child in visited:
#                     continue
#                 elif valuue == 0:
#                     visited += [child]
#                     continue
#                 elif valuue > 0:
#                     tags += [valuue]
#                     visited += [vertex]
#                     way += [child]
#                     self.dfs(child, visited, tags, way)
#                     break
#             else:
#                 for child in self.g2[vertex]:
#                     valuue = self.g2[vertex][child]
#                     if child in visited:
#                         continue
#                     elif valuue == 0:
#                         visited += [child]
#                         continue
#                     elif valuue > 0:
#                         tags += [valuue]
#                         visited += [vertex]
#                         way += [child]
#                         self.dfs(child, visited, tags, way)
#                         break
#                 else:
#                     if way:
#                         way.pop()
#                         tags.pop()
#                         print(way)
#                         self.dfs(way[-1], visited, tags, way)
#                     else:
#                         return 1
#             return 0
    
                


# if __name__ == "__main__":
#     obj = capacity()
#     obj.dfs(0, [], [float('INF')], [0])





def bfs(graph, start, end, parent):
    visited = [False] * len(graph)
    queue = []
    queue.append(start)
    visited[start] = True
    
    while queue:
        u = queue.pop(0)
        for ind, val in enumerate(graph[u]):
            if visited[ind] == False and val > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
    return True if visited[end] else False

def ford_fulkerson(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0
    
    while bfs(graph, source, sink, parent):
        path_flow = float('Inf')
        s = sink
        while(s != source):
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while(v != source):
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow

N, M = map(int, input().split())
graph = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    u, v, w = map(int, input().split())
    graph[u][v] += w 

print(ford_fulkerson(graph, 0, N-1))
























def bfs(graph, start, end, parent):
    visited = [False] * len(graph)
    queue = []
    queue.append(start)
    visited[start] = True
    
    while queue:
        u = queue.pop(0)
        for v in range(len(graph)):
            if visited[v] == False and graph[u][v] > 0:
                queue.append(v)
                visited[v] = True
                parent[v] = u
    return True if visited[end] else False

def edmonds_karp(graph, source, sink):
    parent = [-1] * len(graph)
    max_flow = 0
    
    while bfs(graph, source, sink, parent):
        path_flow = float('Inf')
        s = sink
        while(s != source):
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while(v != source):
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow

# Чтение входных данных
N, M, K = map(int, input().split())
graph = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1  # Ребра графа с пропускной способностью 1

# Вызов функции и вывод результата
max_flow = edmonds_karp(graph, 0, N-1)
if max_flow >= K:
    print("YES")
else:
    print("NO")