n=int(input(""))
inp=input("")
assert 1 <= n <= 100
ls=list(inp.split())
coins=list()
for i in ls:
    assert 1 <= int(i) <= 100
    coins.append(int(i))
tot=0
step=0
while tot <= sum(coins):
    steal=max(coins)
    coins.remove(max(coins))
    tot+=steal
    step+=1
print(step)