num=int(input())
if num < 4:
    num+=4
if num%2!=0:
    if num%4==1:
        print(1)
    else:
        print(0)
if num%2==0:
    num=num-1
    if num%4==1:
        print(1)
    else:
        print(0)