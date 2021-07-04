def checktriangle(a,b,c):
    if a+b > c and b+c > a and a+c > b:
        return True
    else:
        return False

inp=input("")
splt=inp.split()
a=int(splt[0])
b=int(splt[1])
c=int(splt[2])
assert 1 <= a <= 100
assert 1 <= b <= 100
assert 1 <= c <= 100
step=0
while not checktriangle(a,b,c):
    step +=1
    if min(a,b,c)==a:
        a+=1
    elif min(a,b,c)==b:
        b+=1
    elif min(a,b,c)==c:
        c+=1
print(step)