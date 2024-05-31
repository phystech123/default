# # КОНТЕСТ ПУТИ НАИМЕНЬШЕГО ВЕСА
# # ЗАДАЧА 1 МОЕ РЕШЕНИЕ
# # import math
# # class graph():
# #     def __init__(self):
# #         self.v, self.e, self.s, self.ss = map(int, input().split(' '))
# #         self.prev={self.s: None}
# #         self.g=[[None for _ in range(self.v)] for _ in range(self.v)]
# #         self.visited = []
# #         self.q = [(self.s, 0)]
# #         self.val={}
# #         for i in range(self.e):
# #             o = list(map(int, input().split(' ')))
# #             self.g[o[0]][o[1]]=o[2]
# #             self.g[o[1]][o[0]]=o[2]

# #             self.val[o[0]] = [float('inf'), 0][o[0] == self.s]
# #             self.val[o[1]] = [float('inf'), 0][o[1] == self.s]
    
# #     def search(self, s):
# #         # print(self.g)
# #         l = {}
# #         for n, i in enumerate(self.g[s]):
# #             if i != None:
# #                 if n not in self.visited:
# #                     if self.val[n]>i:
# #                         self.val[n] = i
# #                         self.prev[n] = s
# #                     l[n] = self.val[n]
# #         self.visited.append(s)
# #         for i in l.items():
# #             self.q.append(i)
# #         if self.q:
# #             self.q = sorted(self.q, key = lambda x: x[1])
# #             self.search(self.q.pop(0)[0])

# #     def way(self):
# #         i = self.ss
# #         lis = []
# #         while i != None:
# #             lis.append(i)
# #             i = self.prev[i]
# #         return(lis[::-1])
# # g=graph()
# # g.search(g.q.pop(0)[0])
# # print(*g.way())







# # ЗАДАЧА 1 НЕ МОЕ НО ВЕРНОЕ РЕШЕНИЕ

# # import heapq

# # def dijkstra(n, graph, start, end):
# #     pq = [(0, start, [])]
# #     visited = set()
    
# #     while pq:
# #         cost, node, path = heapq.heappop(pq)
        
# #         if node in visited:
# #             continue
        
# #         visited.add(node)
# #         path = path + [node]
        
# #         if node == end:
# #             return path
        
# #         for neighbor, weight in graph[node]:
# #             if neighbor not in visited:
# #                 heapq.heappush(pq, (cost + weight, neighbor, path))
    
# #     return None

# # n, m, s, f = map(int, input().split())
# # graph = {i: [] for i in range(n)}

# # for _ in range(m):
# #     a, b, w = map(int, input().split())
# #     graph[a].append((b, w))
# #     graph[b].append((a, w))

# # shortest_path = dijkstra(n, graph, s, f)
# # print(' '.join(map(str, shortest_path)))










# # ЗАДАЧА 2 


# # def bellman_ford(graph, start, n):
# #     dist = [float('inf')] * n
# #     dist[start] = 0
# #     flag = 0
    
# #     for _ in range(n-1):
# #         for u, v, w in graph:
# #             if dist[u] != float('inf') and dist[u] + w < dist[v]:
# #                 dist[v] = dist[u] + w
# #     for _ in range(2):         
# #         for u, v, w in graph:
# #             if dist[u] != float('inf') and dist[u] + w < dist[v]:
# #                 flag = 1
# #     return ['UDF' if d == float('inf') or flag else str(d) for d in dist]

# # # Чтение входных данных
# # n, m, s = map(int, input().split())
# # graph = []
# # for _ in range(m):
# #     u, v, w = map(int, input().split())
# #     graph.append((u, v, w))

# # # Получение результатов и вывод
# # result = bellman_ford(graph, s, n)
# # print(' '.join(result))








# # ЗАДАЧА 3


# # def floyd_warshall(graph, n):
# #     dist = [[float('inf')] * n for _ in range(n)]
# #     for i in range(n):
# #         dist[i][i] = 0
    
# #     for u, v, w in graph:
# #         dist[u][v] = w
# #         dist[v][u] = w
    
# #     for k in range(n):
# #         for i in range(n):
# #             for j in range(n):
# #                 dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
    
# #     capitals = []
# #     min_sum = float('inf')
# #     for i in range(n):
# #         sum_dist = sum(dist[i])
# #         if sum_dist < min_sum:
# #             min_sum = sum_dist
# #             capitals = [i]
# #         elif sum_dist == min_sum:
# #             capitals.append(i)
    
# #     return capitals[0]  # Возвратим одну из вершин, которые могут быть столицей

# # # Чтение входных данных
# # n, m = map(int, input().split())
# # graph = []
# # for _ in range(m):
# #     u, v, w = map(int, input().split())
# #     graph.append((u, v, w))

# # # Получение результата и вывод
# # result = floyd_warshall(graph, n)
# # print(result)








# # ЗАДАЧА 4
# import heapq
# class parity():
#     def __init__(self):
#         self.n, self.m = map(int, input().split(' '))
#         self.graph = {(i, j): [] for i in range(self.n) for j in range(2)}
#         # print(self.graph)
#         self.needs = {}
#         self.nee = []

#         for _ in range(self.m):
#             a, b, w = map(int, input().split(' '))
#             self.graph[(a, 1)].append((b, 0, w))
#             self.graph[(a, 0)].append((b, 1, w))
#             self.graph[(b, 1)].append((a, 0, w))
#             self.graph[(b, 0)].append((a, 1, w))

#         self.k = int(input())
#         for _ in range(self.k):
#             o = tuple(map(int, input().split(' ')))
#             self.needs[o] = -1
#             self.nee += [o]

#         for i in self.needs.keys():
#             self.needs[i] = self.dijkstra((i[0], 0), (i[1], 0))
#         for i in self.nee:
#             if self.needs[i] is None:
#                 print(-1)
#             else:
#                 print(*self.needs[i])



#     def dijkstra(self, start, end):
#         pq = [(0, start, None)]
#         visited = set()
#         prev = {start:None}
        
#         while pq:
#             # print(pq)
#             cost, node, pr = heapq.heappop(pq)
            
#             if node in visited:
#                 continue
            
#             visited.add(node)
            
#             prev[node] = pr

#             if node == end:
#                 out = []
#                 i = end
#                 while i != None:
#                     out.append(i[0])
#                     i = prev[i]
#                 return out[::-1]
            
#             for neighbor in self.graph[node]:
#                 if neighbor not in visited:
#                     heapq.heappush(pq, (cost + neighbor[2], neighbor[:2], node))
        
#         return None
            
# parity()





# # TASK 5 ------ решено до стадии TL (49/50)

# from collections import deque

# class RF():
#     def __init__(self):
#         inp = list(map(int, input().split()))
#         self.n, self.m =inp[0], inp[1]
#         self.data = {i:float('INF') for i in range(self.n)}
#         self.out = {i:None for i in range(self.n)}
#         self.graph = {i: [] for i in range(self.n)}
#         self.major = inp[2:]
#         for _ in range(self.m):
#             a, b, w = map(int, input().split(' '))
#             self.graph[a].append((b, w))
#             self.graph[b].append((a, w))

#         for t in self.major:
#             dist = self.bfs(t)
#             for p in dist.items():
#                 j, i = p[0], p[1]
#                 if i != None:
#                     if i<self.data[j]:
#                         self.data[j] = i
#                         self.out[j] = t
#         for i in self.out.values():
#             if i == None:
#                 print(-1)
#             else:
#                 print(i)
            

#     def bfs(self, start):
#         distances = {i:None for i in range(self.n)}
#         distances[start] = 0
#         queue = deque([start])
#         while queue:
#             node = queue.popleft()
#             for neighbor in self.graph[node]:
#                 if distances[neighbor[0]] is None:
#                     distances[neighbor[0]] = distances[node] + neighbor[1]
#                     queue.append(neighbor[0])
#         return distances

# if __name__ == "__main__":
#     RF()


# # # КОНТЕСТ НА СТЕК ОЧЕРЕДЬ И КУЧУ(1)
# # # TASK 1
# # def foo():
# #     l = []
# #     s = input()
# #     flag=0
# #     for i in s:
# #         if i == '(' or i == '{' or i == '[':
# #             l.append(i)
# #         else:
# #             if not l:
# #                 flag = 1
# #             else:
# #                 j = l.pop()
# #                 if j == '(' and i == ')' or j == '{' and i == '}' or j == '[' and i == ']':
# #                     pass
# #                 else:
# #                     flag = 1

# #     if not flag and not l:
# #         print('YES')
# #     else:
# #         print('NO')

# # foo()


# # TASK 2
# # def foo():
# #     seq = list(map(int, input().split(' ')))
# #     rule = list(map(int, input().split(' ')))
# #     out = []
# #     for i in seq:
# #         for j in rule:
# #             if j != i:
# #                 out.append(j)
# #             else:
# #                 out.append(j)
# #                 break
# #     print(*out)
# # foo()

# # # TASK 3
# # import heapq
# # N = int(input())
# # arr = list(map(int, input().split()))
# # heapq.heapify(arr)
# # while arr:
# #     print(heapq.heappop(arr), end=' ')


# # # TASK 4
# # def heapsort(A):
# #     def sift_down(i, x = 0):
# #         while True:
# #             left = 2 * i + 1
# #             right = 2 * i + 2
# #             max_index = i
# #             if left < len(A)-x and A[left] > A[max_index]:
# #                 max_index = left
# #             if right < len(A)-x and A[right] > A[max_index]:
# #                 max_index = right
# #             if max_index == i:
# #                 break
# #             A[i], A[max_index] = A[max_index], A[i]
# #             i = max_index

# #     # Превращаем массив в кучу
# #     for i in range(len(A) // 2 , -1, -1):
# #        sift_down(i)
# #     print(' '.join(map(str, A)))

# #     # Сортируем кучу
# #     for i in range(len(A) - 1, -1, -1):
# #         A[0], A[i] = A[i], A[0]
# #         sift_down(0, len(A) - i)
# #         print(' '.join(map(str, A)))
# #         if A[0]==min(A):
# #             break

# # # Пример использования
# # heapsort([3,2,5,0,-1])


# TASK 6 ГОБЛИНЫ И ШАМАНЫ
# def goblin():
#     num = int(input())
#     steck = []
#     outp = []
#     for _ in range(num):
#         g = input().split(' ')
#         if g[0] == '-':
#             outp += [steck.pop(0)]
#         elif g[0] == '+':
#             steck += [g[1]]
#         elif g[0] == '*':
#             if len(steck) % 2:
#                 steck.insert(len(steck)//2 + 1, g[1])
#             else:
#                 steck.insert(len(steck)//2, g[1])
#     print(*outp, sep='\n')
# goblin()


# TASK 7 G-STACK
# def foo():
#     steck = []
#     inp = list(map(int, input().split(' ')))
#     for i in inp:
#         if i == 0:
#             break
#         elif i > 0:
#             steck += [i]
#         else:
#             if steck:
#                 if steck[-1] + i >0:
#                     steck[-1] += i
#                 else:
#                     steck.pop()
#     print(len(steck), steck.pop(-1) if steck else -1)
# foo()












# # КОНТЕСТ ОБХОДЫ ГРАФОВ


# # # TASK 1
# # import sys

# # def dfs(graph, node, visited):
# #     visited[node] = True
# #     for neighbor in graph[node]:
# #         if not visited[neighbor]:
# #             dfs(graph, neighbor, visited)

# # n = int(sys.stdin.readline())
# # graph = [[] for _ in range(n)]
# # visited = [False] * n

# # m = int(sys.stdin.readline())
# # for _ in range(m):
# #     u, v = map(int, sys.stdin.readline().split())
# #     graph[u].append(v)
# #     graph[v].append(u)

# # dfs(graph, 0, visited)

# # if all(visited):
# #     print("YES")
# # else:
# #     print("NO")



# # # TASK 2

# # def dfs(i, used, G):
# #     global s
# #     used[i] = 1
# #     for elem in G[i]:
# #         s += elem[1]
# #         if used[elem[0]] == 0:
# #             dfs(elem[0], used, G)
 
# # n, m = map(int, input().split())
# # G = [[] for i in range(n)]
# # answer =[]
# # used = [0 for i in range(n)]

# # for i in range(m):
# #     u, v, c = map(int, input().split())
# #     G[u].append([v, c])
# #     G[v].append([u, c])

# # for i in range(len(used)):
# #     if used[i] == 0:
# #         s = 0
# #         dfs(i, used, G)
# #         answer.append(s // 2)

# # answer.sort()
# # for elem in answer:
# #     print(elem)


# # ДАЛЕЕ ВСЕ ЗАДАНИЯ КАТАЮТСЯ С ДИСКА ФЭФМА 

# # TASK 6

# # from collections import deque

# # def bfs(graph, start, n):
# #     distances = [None] * n
# #     distances[start] = 0
# #     queue = deque([start])
# #     while queue:
# #         node = queue.popleft()
# #         for neighbor in graph[node]:
# #             if distances[neighbor] is None:
# #                 distances[neighbor] = distances[node] + 1
# #                 queue.append(neighbor)
# #     return distances

# # n, m = map(int, input().split())
# # graph = {i: [] for i in range(n)}
# # for _ in range(m):
# #     a, b = map(int, input().split())
# #     graph[a].append(b)
# #     graph[b].append(a)

# # distances = bfs(graph, 0, n)
# # for distance in distances:
# #     print(distance)







# # КОНТЕСТ ДВОИЧНОЕ ДЕРЕВО 
# from random import randint
# from collections import deque
# class Node():
#     def __init__(self, key):
#         self.left = None
#         self.right = None
#         self.val = key
#         self.rep = 1

# def insert(root, key):
#     if root is None:
#         return Node(key)
#     else:
#         if root.val < key:
#             root.right = insert(root.right, key)
#         elif root.val > key:
#             root.left = insert(root.left, key)
#         else:
#             root.rep += 1
#     return root


# def height(root):
#     if root is None:
#         return 0
#     else:
#         left_height = height(root.left)
#         right_height = height(root.right)
#         if left_height > right_height:
#             return left_height + 1
#         else:
#             return right_height + 1

# def bfs(start):
#     outp = [(start.val, start.rep)]
#     queue = deque([start])
#     while queue:
#         node = queue.popleft()
#         if node.left != None:
#             outp.append((node.left.val, node.left.rep))
#             queue.append(node.left)
#         if node.right != None:
#             outp.append((node.right.val, node.right.rep))
#             queue.append(node.right)
#     return outp

# # if __name__ == '__main__':
# while True:
#     # numbers = list(map(int, input().split()))

#     numbers = [randint(-1,1) for _ in range(randint(0, 10000))]
    
#     if not numbers:
#         print('')
#     else:
#         root = None
#         for number in numbers[0:]:
#             root = insert(root, number)
#         o = list()
#         for i in bfs(root):
#             o += [i]
#         o = sorted(o, key = lambda x: x[0])
#         for i in o:
#             print(*i)




# class Node:
#     def __init__(self, key, count=1):
#         self.left = None
#         self.right = None
#         self.val = key
#         self.count = count

# def insert(root, key):
#     if root is None:
#         return Node(key)
#     else:
#         if root.val < key:
#             root.right = insert(root.right, key)
#         elif root.val > key:
#             root.left = insert(root.left, key)
#         else:
#             root.count += 1
#     return root

# def print_tree(root):
#     if root is not None:
#         print_tree(root.left)
#         print(root.val, root.count)
#         print_tree(root.right)

# numbers = list(map(int, input().split()))
# root = None
# for number in numbers:
#     root = insert(root, number)
# print_tree(root)




# # # ШАХМАТНАЯ ДОСКА С ДВУМЯ КОНЯМИ(ВСТРЕЧА)
# # from collections import deque
# # class desk():
# #     def __init__(self):
# #         self.n = 8
# #         self.des = [['x' for _ in range(8)] for _ in range(8)]
# #         st, nd = input().split(' ')
# #         st, nd = (int(st[1]), self.repl(st[0])), (int(nd[1]), self.repl(nd[0]))
# #         self.graph = {(i, j): [] for i in range(self.n) for j in range(self.n)}
# #         for i in self.graph:
# #             self.graph[i].append((i[0] - 2, i[1] + 1)) if 0 <= i[0] - 2 < 8 and 0 <= i[1] + 1 < 8 else 0
# #             self.graph[i].append((i[0] - 2, i[1] - 1)) if 0 <= i[0] - 2 < 8 and 0 <= i[1] - 1 < 8 else 0

# #             self.graph[i].append((i[0] + 2, i[1] + 1)) if 0 <= i[0] + 2 < 8 and 0 <= i[1] + 1 < 8 else 0
# #             self.graph[i].append((i[0] + 2, i[1] - 1)) if 0 <= i[0] + 2 < 8 and 0 <= i[1] - 1 < 8 else 0


# #             self.graph[i].append((i[0] - 1, i[1] + 2)) if 0 <= i[0] - 1 < 8 and 0 <= i[1] + 2 < 8 else 0
# #             self.graph[i].append((i[0] - 1, i[1] - 2)) if 0 <= i[0] - 1 < 8 and 0 <= i[1] - 2 < 8 else 0

# #             self.graph[i].append((i[0] + 1, i[1] + 2)) if 0 <= i[0] + 1 < 8 and 0 <= i[1] + 2 < 8 else 0
# #             self.graph[i].append((i[0] + 1, i[1] - 2)) if 0 <= i[0] + 1 < 8 and 0 <= i[1] - 2 < 8 else 0

# #         # print(self.graph)
# #         self.green = self.bfs(st)
# #         self.red = self.bfs(nd)
# #         self.serch_min()
        

# #     def repl(self, el):
# #         if el == 'a':
# #             return 0
# #         elif el == 'b':
# #             return  1
# #         elif el == 'c':
# #             return  2
# #         elif el == 'd':
# #             return  3
# #         elif el == 'e':
# #             return  4
# #         elif el == 'f':
# #             return  5
# #         elif el == 'g':
# #             return  6
# #         elif el == 'h':
# #             return  7
            
# #     def bfs(self, start):
# #         distances = {(i, j): None for i in range(self.n) for j in range(self.n)}
# #         distances[start] = 0
# #         queue = deque([start])
# #         while queue:
# #             node = queue.popleft()
# #             for neighbor in self.graph[node]:
# #                 if distances[neighbor] is None:
# #                     distances[neighbor] = distances[node] + 1
# #                     queue.append(neighbor)
# #         return distances

# #     def serch_min(self):
# #         self.minn = {}
# #         for i in self.graph:
# #             if self.green[i] == self.red[i]:
# #                 self.minn[i] = self.green[i]
# #         # print(self.minn)
# #         # print(self.red)
# #         # print(self.green)
# #         self.solve = float('INF')
# #         for i in self.minn.items():
# #             self.solve = min(self.solve, i[1])
        
# #         print(self.solve)
# # D = desk()

# МОЕ РЕШЕНИЕ ЗАДАЧИ ПРО ТАБЛИЦЫ И КРАТЧАЙШИЙ ПУТЬ ДО 1
# from random import randint
# from collections import deque
# class desk():
#     def __init__(self):
#         # self.n, self.m, self.tabl = n, m , tabl
#         self.n, self.m = map(int, input().split(' '))
#         self.tabl = []
#         for _ in range(self.n):
#             self.tabl.append(list(map(int, input().split(' '))))
        
#         self.graph = {(i, j): [] for i in range(self.n) for j in range(self.m)}
        
#         for i in self.graph:
#             self.graph[i].append((i[0], i[1] + 1)) if 0 <= i[0] < self.n and 0 <= i[1] + 1 < self.m else 0
#             self.graph[i].append((i[0], i[1] - 1)) if 0 <= i[0] < self.n and 0 <= i[1] - 1 < self.m else 0

#             self.graph[i].append((i[0] + 1, i[1])) if 0 <= i[0] + 1 < self.n and 0 <= i[1] < self.m else 0
#             self.graph[i].append((i[0] - 1, i[1])) if 0 <= i[0] - 1 < self.n and 0 <= i[1] < self.m else 0


#         self.outp = [[0 for _ in range(self.m)] for _ in range(self.n)]
#         for i in range(self.n):
#             for j in range(self.m):
#                 self.outp[i][j] = self.bfs((i, j))
        
#         # print('\n')
#         for i in range(self.n):
#             print(*self.outp[i])


            
#     def bfs(self, start):
#         distances = {(i, j): None for i in range(self.n) for j in range(self.m)}
#         # print('\n\n\n\n\n\n\n', distances, '\n\n\n\n\n\n\n')
#         distances[start] = 0
#         queue = deque([start])
#         while queue:
#             node = queue.popleft()
#             for neighbor in self.graph[node]:
#                 if distances[neighbor] is None:
#                     distances[neighbor] = distances[node] + 1
#                     queue.append(neighbor)
#         lis = []
#         for i in distances.items():
#             if self.tabl[i[0][0]][i[0][1]] == 1:
#                 lis += [i[1]]
#         return min(lis)

# D = desk()

# # while True:
# #     n = randint(0, 300)
# #     m = randint(0, 300)
# #     tabl = [[randint(0, 1) for _ in range(m)] for _ in range(m)]
# #     print(n, m, tabl, sep='\n')
# #     desk(n, m, tabl)


# КОНТЕСТ НА СТРОКИ 
# TASK 1
# print(len(input().split(' ')))

# TASK 2
# import re
# inpp = re.split(r'[.!?]\s', input())
# for i in range(len(inpp)):
#     print(i + 1, len(inpp[i].split(' ')))

# TASK 3
# def kmp():
#     strr = input()
#     n = len(strr)
#     pre = [0 for _ in range(n)]
#     for i in range(1, n):
#         pre[i] = pi(strr, i, pre[i-1])
#     print(*pre)

# def pi(strr, n, l):
#     st = strr[:n+1]
#     if st[l] == st[-1]:
#         return l + 1
#     else:
#         for i in range(l, 0, -1):
#             if st[:i] == st[:-i -1:-1]:
#                 return i
#     return 0
# if __name__ == '__main__':
#     kmp()

# TASK 4 NEYRO
# def compute_prefix_function(s):
#     n = len(s)
#     p = [0] * n
#     j = 0
#     for i in range(1, n):
#         while j > 0 and s[i] != s[j]:
#             j = p[j - 1]
#         if s[i] == s[j]:
#             j += 1
#         p[i] = j
#     return p

# s = input()
# prefix_function = compute_prefix_function(s)
# print(*prefix_function)

# TASK 5
# def zfunction(s):
#     n = len(s)
#     z = [0] * n
#     l, r = 0, 0
#     for i in range(1, n):
#         if i <= r:
#             z[i] = min(r - i + 1, z[i - l])
#         while i + z[i] < n and s[z[i]] == s[i + z[i]]:
#             z[i] += 1
#         if i + z[i] - 1 > r:
#             l, r = i, i + z[i] - 1
#     return z

# s = input().strip()
# result = zfunction(s)
# print(' '.join(map(str, result)))

# TASK 6
# def Afunction(s):
#     n = len(s)
#     result = [0 for _ in range(n)]
#     for i in range(0, n):
#         st = s[:i+1]
#         su = 0
#         j = 0
#         while j <= i and st[j] == st[-j-1]:
#             su += 1
#             j += 1
#         result[i] = su
#     return result

# S = input().strip()
# result = Afunction(S)
# print(' '.join(map(str, result)))

# Task 6 optimization
# def zfunction(s):
#     n = len(s)
#     z = [0] * n
#     l, r = 0, 0
#     for i in range(1, n):
#         if i <= r:
#             z[i] = min(r - i + 1, z[i - l])
#         while i + z[i] < n and s[z[i]] == s[i + z[i]]:
#             z[i] += 1
#         if i + z[i] - 1 > r:
#             l, r = i, i + z[i] - 1
#     return z[n//2:]

# s = input().strip()
# result = zfunction(s+s[::-1])[::-1]
# print(' '.join(map(str, result)))









# КОНТЕСТ НА ОСТОВНЫЕ ДЕРЕВЬЯ
# TASK 1
# from collections import deque
# class tree:
#     def __init__(self):
#         self.n, self.m = map(int, input().split(' '))
#         self.graph = {i:[] for i in range(self.n)}
#         for _ in range(self.m):
#             a, b =map(int, input().split(' '))
#             self.graph[a].append(b)
#             self.graph[b].append(a)
#         self.bfs(0)
#         for i in self.edges:
#             print(*i)
#     def bfs(self, start):
#         self.edges = []
#         distances = [None] * self.n
#         distances[start] = 0
#         queue = deque([start])
#         while queue:
#             node = queue.popleft()
#             for neighbor in self.graph[node]:
#                 if distances[neighbor] is None:
#                     distances[neighbor] = distances[node] + 1
#                     self.edges += [(node, neighbor)]
#                     queue.append(neighbor)
#         return distances
    
# if __name__ == "__main__":
#     Tree = tree()

# TASK 2
# import heapq
# class prima():
#     def __init__(self):
#         self.n, self.m = map(int, input().split(' '))
#         self.graph = {i:[] for i in range(self.n)}
#         for _ in range(self.m):
#             a, b, w =map(int, input().split(' '))
#             self.graph[a].append((b, w))
#             self.graph[b].append((a, w))
#         self.dijkstra(0)
#         print(self.summ)
#         for i in self.edges:
#             print(*i)


#     def dijkstra(self, start):
#         self.edges = []
#         self.summ = 0
#         pq = [(0, start, None)]
#         visited = set()

#         while pq:
#             cost, node, pr = heapq.heappop(pq)
#             if node in visited:
#                 continue
#             visited.add(node)
#             if node != start:
#                 self.edges += [(pr, node)]
#             self.summ += cost
#             for neighbor in self.graph[node]:
#                 if neighbor[0] not in visited:
#                     heapq.heappush(pq, (neighbor[1], neighbor[0], node))
        
#         return None

# if __name__ == "__main__":
#     prima()