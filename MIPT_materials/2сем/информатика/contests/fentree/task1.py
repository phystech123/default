# from array import array
# class rvq():
#     def __init__(self):
#         self.lenn = 100000
#         self.sequence = [((n ** 2) % 12345) + ((n ** 3) % 23456) for n in range(100001)]
#         # print(self.sequence)
#         self.maxx = [self.smax(i) for i in range(self.lenn)]
#         self.minn = [self.smin(i) for i in range(self.lenn)]
#         self.rminn = [self.srmin(i) for i in range(self.lenn)]
#         self.rmaxx = [self.srmax(i) for i in range(self.lenn)]

#         self.k = int(input())
#         for _ in range(self.k):
#             x, y = map(int, input().split(' '))
#             if x > 0:
#                 self.difference(x, y)
#             elif x < 0:
#                 self.replacement(x, y)





    
#     def difference(self, xx, yy):
#         ma = float('-INF')
#         mi = float('INF')
#         y = yy
#         x = xx
#         while self.f(y) >= x:
#             ma = max(ma, self.maxx[y])
#             mi = min(mi, self.minn[y])
#             y = self.f(y) - 1
#         while x < y:
#             ma = max(ma, self.rmaxx[x])
#             mi = min(mi, self.rminn[x])
#             x = self.g(x) + 1
#         print(ma - mi)
#         # print(ma, mi)

#     def replacement(self, x, val):
#         x *= -1
#         self.sequence[x] = val
#         self.maxx = [self.smax(i) for i in range(len(self.sequence))]
#         self.minn = [self.smin(i) for i in range(len(self.sequence))]
#         self.rminn = [self.srmin(i) for i in range(len(self.sequence))]
#         self.rmaxx = [self.srmax(i) for i in range(len(self.sequence))]

#     def f(self, i):
#         return i & (i + 1)
    
#     def g(self, i):
#         return i | (i + 1)
    
#     def smax(self, i):
#         return max(self.sequence[self.f(i):i + 1])
    
#     def smin(self, i):
#         return min(self.sequence[self.f(i):i + 1])
    
#     def srmax(self, i):
#         if self.g(i) + 1 < len(self.sequence):
#             return max(self.sequence[i:self.g(i) + 1])
#         else:
#             return max(self.sequence[i:])
        
#     def srmin(self, i):
#         if self.g(i) + 1 < len(self.sequence):
#             return min(self.sequence[i:self.g(i) + 1])
#         else:
#             return min(self.sequence[i:])
    
    


# if __name__ == '__main__':
#     obj = rvq()
#     # import psutil
#     # print(f"Память: {psutil.Process().memory_info().rss / 1024 ** 2:.2f} МБ")




















class fentree():
    def __init__(self):
        self.a = [0] * ((2**17) - 1) 
        for i in range(len(self.a)): 
            self.a[i] = [10**6, - 10**6] 
        for i in range (1, 10**5 + 1): 
            self.a.append([(i**2) % 12345 + (i**3) % 23456, (i**2) % 12345 + (i**3) % 23456]) 
        for i in range(2**17 - 1, 0, -1): 
            if(i * 2 < len(self.a)): 
                self.a[i - 1] = [min(self.a[i * 2 - 1][0], self.a[i * 2][0]), max(self.a[i * 2 - 1][1], self.a[i * 2][1])] 

        s=int(input()) 
        for i in range(s): 
            i,j=map(int, input().split()) 
            if(i < 0): 
                self.a=self.update(abs(i),j) 
            if(i > 0): 
                print(self.gett(i,j))

    def update(self, i, p): 
        self.a[2**17 - 2 + i] = [p, p] 
        k = 2**17 - 1 + i 
        while(k != 0): 
            if(k % 2 == 1): 
                k -= 1 
            self.a[k // 2 - 1] = [min(self.a[k - 1][0], self.a[k][0]), max(self.a[k - 1][1], self.a[k][1])] 
            k //= 2 
        return self.a 
    
    def gett(self, i, j): 
        _min = 999999 
        _max = -999999 
        i+=2**17-1 
        j+=2**17-1 
        while(i <= j): 
            if(i & 1): 
                _min = min(_min, self.a[i - 1][0]) 
                _max = max(_max, self.a[i - 1][1]) 
            if(not(j & 1)): 
                _min = min(_min, self.a[j - 1][0]) 
                _max = max(_max, self.a[j- 1][1]) 
            i=(i+1)//2 
            j=(j-1)//2 
        return _max-_min 
    
if __name__ == "__main__":
    fentree()