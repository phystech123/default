class fentree():
    def __init__(self):
        self.arr =[]
        n, m = map(int, input().split())
        self.maxxx = [-10000 for _ in range(n)]
        self.maxx = [-10000 for _ in range(n)]
        for _ in range(n):
            self.arr += [int(input())]
        for i in range(n):
            ma = -1000000
            j = i&(i+1)
            for k in range(j, i+1):
                ma = max(ma, k)
            self.maxx[i] = ma

        for i in range(n):
            ma = -1000000
            j = i|(i+1)
            if j < n:
                for k in range(i, j+1):
                    ma = max(ma, k)
                self.maxxx[i] = ma
        
        for i in range(m):
            l, r =map(int, input().split(' '))
            self.gett(l, r)
    def gett(self, l, r):
        ma = -1000000
        while r&(r+1) >= l:
            ma = max(ma, self.maxx[r])
            r = r&(r+1) - 1
        while l|(l+1) <= r:
            ma = max(ma, self.maxxx[l])
            l = l|(l+1)
        print(ma)
if __name__ == "__main__":
    fentree()