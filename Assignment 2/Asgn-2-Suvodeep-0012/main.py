s = ['a', 'a', 'a', 'b', 'c', 'a', 'd', 'c', 'b']
res = []
i = 0
while i < len(s) - 1:
    if s[i] != s[i + 1]:
        res.append(s[i]) 
    else:
        while i < len(s) - 1 and s[i] == s[i + 1]:
            i = i + 1

    i = i + 1

res.append(s[-1])
print(f"Orginal String: {s}")
print(f"Result String: {res} ") 
