inp=int(input(""))
assert 1 <= inp <= 55
inp2=input("")
tot=0
step=1
string=""
while tot != inp:
    string += inp2[tot]
    tot+=step
    step+=1
print(string)