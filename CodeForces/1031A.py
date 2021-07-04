inp=input("")
tup=inp.split()
w=int(tup[0])
h=int(tup[1])
k=int(tup[2])
assert w >= 3
assert h <=100
assert k >=1
assert k <= round((min(w,h)+1)/4)
gcells=0
for i in range(k):
    gcells += 2*(w+h)-4
    w=w-4
    h=h-4
print (gcells)