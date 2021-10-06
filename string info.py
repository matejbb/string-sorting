str = """Ahoj"""
l = {}

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
    