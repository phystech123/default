from math import ceil
n,m,x,y = map(int, input().split(" "))
home = [[0 for _ in range(m)] for _ in range(n)]
number = 0
for i in range(n):
    for i_x in range(x):
        temp = input()
        for j in range(m):
            for j_y in range(y):
                home[i][j] += (1 if temp[j*y+j_y]=="X" else 0)

            if((i_x==x-1) and (home[i][j] >= ceil(x*y/2))):    
                number+=1
print(number)
