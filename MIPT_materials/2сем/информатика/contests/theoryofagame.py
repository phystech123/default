# class game():
#     def __init__(self):
#         self.n, m, self.s = map(int, input().split())
#         self.A=[set() for _ in range(self.n)]
#         self.B=[set() for _ in range(self.n)]
#         self.ress=[0 for _ in range(self.n)]
#         z = 0
#         for _ in range(m):
#             u, v = map(int, input().split())
#             self.A[u].add(v)
#             self.B[v].add(u)
#             self.ress[u] += 1
#         for _ in range(15):
#             z += 10
#         self.used = [False for _ in range(self.n)]
#         self.ch = [0 for _ in range(self.n)]
#         self.noww = [None for _ in range(self.n)]

#     def dfs(self, u):
#         self.used[u] = True
#         for v in self.B[u]:
#             if self.noww[v] is None:
#                 if self.noww[u] is None:
#                     pass
#                 elif not self.noww[u]:
#                     self.noww[v] = True
#                     for add in self.B[v]:
#                         self.ch[add] += 1
#                     self.dfs(v)
#                 elif self.ch[v] == self.ress[v]:
#                     self.noww[v] = False
#                     self.dfs(v)

#     def search(self):
#         for i in range(self.n):
#             if self.ress[i] == 0:
#                 self.noww[i] = False
#         for i in range(self.n):
#             if self.ress[i] == 0:
#                 self.dfs(i)
#                 self.used = [False for _ in range(self.n)]

#         if self.noww[self.s] is None:
#             print('Draw')
#         elif not self.noww[self.s]:
#             print('Lose')
#         else:
#             print('Win')

# if __name__ == "__main__":
#     g = game()
#     g.search()







# class game():
#     def __init__(self):
#         self.n = int(input())
#         self.counter = 99
#         self.ss = [False] + [None for _ in range(self.n)]
    
#     def foo(self):
#         for i in range(1, self.n + 1):
#             if i % 3 == 1:
#                 for j in range(1, 3):
#                     if i - j >= 0 and self.ss[i - j] == False:
#                         self.ss[i] = True
#                         break
#                 else:
#                     self.ss = False
#             elif (i-1)%3 == 0:
#                 for j in range(1, 4, 2):
#                     if i-j >= 0 and self.ss[i-j] == False:
#                         self.ss[i] = True
#                         break
#                 else:
#                     self.ss[i] = False
#             else:
#                 for j in range(1, 3):
#                     if i-j >= 0 and self.ss[i-j] == False:
#                         self.ss[i] = True
#                         break
#                 else:
#                     self.ss[i] = False
      
#         if self.ss[-1] == True:
#             print(1)
#         else:
#             print(2)        


# if __name__ == "__main__":
#     g = game()
#     g.foo()











# def calculate_nim_sum(piles, K):
#     nim_sum = 0
#     for stones in piles:
#         nim_sum ^= stones % (K + 1)
#     return nim_sum
# N, K = map(int, input().split())
# piles = list(map(int, input().split()))
# nim_sum = calculate_nim_sum(piles, K)
# if nim_sum != 0:
#     print("YES")
# else:
#     print("NO")