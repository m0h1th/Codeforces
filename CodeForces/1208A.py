T=int(input())
inls=[]
for i in range(T):
    inp=input()
    tup=list(inp.split())
    inls.append(tup)
    
for i in inls:
    a=int(i[0])
    b=int(i[1])
    n=int(i[2])
    if n%3==0:
        print(a)
    elif n%3==1:
        print(b)
    elif n%3==2:
        print(a^b)