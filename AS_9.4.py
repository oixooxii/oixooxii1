fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
handle = open(fname)

di = dict()
for li in handle:
    li = li.rstrip()
    if not li.startswith("From "): continue
    wds = li.split()
    di[wds[1]] = di.get(wds[1],0) + 1

Hcount = None
Hcountwriter = None

for k in di:
    if Hcount is None: Hcount = di[k]
    if Hcount < di[k]:
        Hcount = di[k]
        Hcountwriter = k

print(Hcountwriter,Hcount)


fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
handle = open(fname)

di = dict()
for li in handle:
    li = li.rstrip()
    if not li.startswith("From "): continue
    wds = li.split()
    di[wds[1]] = di.get(wds[1],0) + 1

Hcount = -1
Hcountwriter = None
for k,v in di.items():
    if v > Hcount:
        Hcount = v
        Hcountwriter = k

print(Hcountwriter,Hcount)
