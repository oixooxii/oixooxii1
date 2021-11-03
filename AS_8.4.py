fname = input("Enter file name: ")
fh = open(fname)

lst = list()
for x in fh:
    ws = x.split()
    for w in ws:
        if w not in lst:
            lst.append(w)

print(sorted(lst))
