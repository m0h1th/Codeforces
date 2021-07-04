inp=input("")
tup=inp.split()
n=int(tup[0])
S=int(tup[1])
assert 1 <= n <= 100000
assert 1 <=S <= 10**9
tot=0
step=1
step+=S//n
if S%n==0:
    step=step-1
print(step)