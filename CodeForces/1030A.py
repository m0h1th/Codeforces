inp1=int(input(""))
assert inp1>=1
assert inp1<=100
inp2=input("")
easy=True
for i in range(0,2*inp1-1,2):
    if inp2[i] == "1":
        easy=False
        break
    else:
        continue
if easy:
    print("EASY")
else:
    print("HARD")