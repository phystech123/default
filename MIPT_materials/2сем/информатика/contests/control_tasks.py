# # first task heap
# class heap():
#     def __init__(self):
#         self.c=int(input())
#         self.numbers=list(map(int, input().split()))
#         self.flag=0
#     def pro(self, n=0):
#         if 2*n+1<len(self.numbers)-1:
#             if self.numbers[2*n+1]<=self.numbers[n]:
#                 self.pro(2*n+1)
#             else:
#                 self.flag+=1
#         if 2*n+2<len(self.numbers)-1:
#             if self.numbers[2*n+2]<=self.numbers[n]:
#                 self.pro(2*n+2)
#             else:
#                 self.flag+=1
#     def pr(self):
#         if not self.flag:
#             print('YES')
#         else:
#             print('NO')
# h=heap()
# h.pro()
# h.pr()

# # second task linked_list
# def list_to_array(linked_list, head, lis=[]):
#     lis.append(head[0])
#     if head[1]!=-1:
#         a = list_to_array(linked_list, linked_list[head[1]], lis)
#         return a
#     else:
#         return lis

# # third task calc
# import re
# class calc():
#     def __init__(self):
#         self.s=input().split(' ')
#         self.x=[]
#         self.xx={}
#         self.flag=0
#         for i in self.s:
#             if re.fullmatch(r'\d+\D+(\d\D)*', i):
#                 self.flag=1
#                 if i not in self.x:
#                     self.x.append(i)
#             else:
#                 if not re.fullmatch(r'[-+*/0-9=]+', i):
#                     if i not in self.x:
#                         self.x.append(i)
            
#         for _ in range(len(self.x)):
#             i=input().split(' ')
#             i.pop()
#             self.xx[i[0]]=i[1]
        
#         for i in self.x:
#             if i in self.xx.keys():
#                 pass
#             else:
#                 self.flag=2
#                 print('incorrect')

#         # print(self.s, self.xx, sep='\n')
        
#     def cal(self):
#         if not self.flag:
#             qu=[]
#             for i in self.s:
#                 if i!='*' and i!='-' and i!='+' and i!='=' and i!='/':
#                     try:
#                         i=int(i)
#                     except:
#                         qu.append(int(self.xx[i]))
#                     else:
#                         i=int(i)
#                         qu.append(i)
#                 elif i!='=':
#                     if i=='+':
#                         if len(qu)>1:
#                             b, a = qu.pop(), qu.pop()
#                             qu.append(a+b)
#                         else:
#                             self.flag=1
#                     elif i=='-':
#                         if len(qu)>1:
#                             b, a = qu.pop(), qu.pop()
#                             qu.append(a-b)
#                         else:
#                             self.flag=1
#                     elif i=='*':
#                         if len(qu)>1:
#                             b, a = qu.pop(), qu.pop()
#                             qu.append(a*b)
#                         else:
#                             self.flag=1
#                     elif i=='/':
#                         if len(qu)>1:
#                             b, a = qu.pop(), qu.pop()
#                             qu.append(a//b)
#                         else:
#                             self.flag=1
#             if len(qu)==1 and not self.flag:
#                 print(qu[0])
#             else:
#                 self.flag=1
            
#             if self.flag:
#                 print('incorrect')
# z=calc()
# z.cal()


# # sixth task degree_of_string 
# def foo():
#     s=input()
#     n=int(input())
#     flag=0
#     if n>0:
#         return s*n
#     else:
#         n=abs(n)
#         if not len(s)%n:
#             a=int(len(s)//n)
#             l=[]
#             for i in range(n):
#                 l.append(s[i*a:i*a+a])
#             u=l[0]
#             for i in range(1,n):
#                 if u!=l[i]:
#                     flag+=1
#             if not flag:
#                 return s[:a]
#             else:
#                 return 'NO SOLUTION'
#         return 'NO SOLUTION'

# print(foo())


# # fourth task the island of knights and liars
# class island():
#     def __init__(self):
#         self.n, self.val = map(int, input().split())
#         self.s = []
#         for _ in range(self.n):
#             name, fl = input().split()
#             self.s.append([name, int(fl)])
#         self.m = int(input())


#         self.foo(0, self.val, 0)

#         for person in self.s:
#             if person == None:
#                 continue
#             else:
#                 print(*person)


#     def foo(self, h, flag, day):
#         cs = 0
#         for j in self.s:
#             if j != None:
#                 cs += 1
#         if cs == 1:
#             return [self.s]
        
#         if self.s[h][1] == 1:
#             if flag == 1:
#                 pass
#             else:
#                 self.s[h] = None

#         else:
#             if flag == 0:
#                 self.s[h][1] = 1
#                 flag = (flag + 1) % 2 
#             else:
#                 flag = (flag + 1) % 2  
#         # print(self.s, day)

#         day += 1
#         p = (h + 1) % self.n

#         while self.s[p] == None:
#             p = (p + 1) % self.n

#         if day == self.m:
#             return self.s
#         else:
#             return self.foo(p, flag, day)


# if __name__ == "__main__":
#     obj = island()



# fifth task fenvik (mean) -- unfinished
class fenvik():
    def __init__(self):
        self.n = int(input())
        self.s = list(map(int, input().split()))
        self.k = int(input())
        self.requests = []
        for _ in range(self.k):
            request = input().split()
            if request[0] == 'mean':
                self.mean(request[1:])
            elif request[0] == 'add':
                self.update(request[1:])
        self.call()


    def mean(self, req):
        l, r = int(req[0]), int(req[1])
        _sum = 0
        for i in self.s[l:r + 1]:
            _sum += i
        self.requests += [f'{_sum/(r+1-l):.3}']

    def update(self, req):
        l, r, v = int(req[0]), int(req[1]), int(req[2])
        for i in range(l, r + 1):
            self.s[i] += v

    def call(self):
        print(*self.requests)

if __name__ == '__main__':
    obj = fenvik()




