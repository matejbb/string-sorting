str = """Ahoj ako sa ako Ahoj"""
l = {}
slovo = ""
l2 = {}

for i in str:
    if i in l:
        l[i] = (l[i])+1
    else:
        l[i] = 1

s = list(sorted(set(l.values()),reverse=True))

print(l)

for c in s:
    for x in l:
        if l[x] == c:
            print(x, c)
    
for o in str:
    if o == " ":
        if slovo in l2:
            l2[slovo] = (l2[slovo])+1
        else:
            l2[slovo] = 0
        slovo = ""
    else:
        slovo = slovo + o
if slovo in l2:
    l2[slovo] = (l2[slovo])+1
else:
    l2[slovo] = 0

for cd in l2:
    if i in l:
        l2[cd] = (l2[cd])+1
    else:
        l2[cd] = 1

print(l2)

