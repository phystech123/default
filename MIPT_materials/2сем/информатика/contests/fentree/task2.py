class cum():
    def __init__(self):
        int(input()) #this string for c++
        self.arr=list(map(int,input().split())) 

    def update(self, inp):
        self.arr[inp[1]-1]=inp[2] 

    def gett(self, inp):
        sum=0 
        l=inp[1] 
        r=inp[2] 
        for j in range(l-1,r): 
            if (j-(l-1))%2==0: 
                sum+=self.arr[j] 
            else: 
                sum-=self.arr[j] 
        print(sum)

if __name__ == "__main__":  
    tr = cum()
    m=int(input()) 
    for i in range(m): 
        inp=list(map(int,input().split())) 
        if inp[0]==0: 
            tr.update(inp) 
        else: 
            tr.gett(inp)