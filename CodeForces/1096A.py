T=int(input())
inls=[]
for i in range(T):
    a=input()
    tup=list(a.split())
    inls.append(tup)
    
def divisible(a,b):
    for i in range(a,b+1):
        j=i+i
        k=i
        if j in range(a,b+1):
            return (i,j)
        else:
            j+=k
    
for i in inls:
    out=divisible(int(i[0]),int(i[1]))
    print(out[0],out[1])