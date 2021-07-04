import math
inp=input("")
tup=inp.split()
k=int(tup[0])   #Number of people
n=int(tup[1])   #Number of planes per person
s=int(tup[2])   #Number of planes per sheet
p=int(tup[3])   #Number of sheets per pack
assert 1 <= k <= 10000
assert 1 <= n <= 10000
assert 1 <= s <= 10000
assert 1 <= p <= 10000
a=s
b=p
step=math.ceil(n/s)
totsheets=step*k
packs=math.ceil(totsheets/p)
print(packs)