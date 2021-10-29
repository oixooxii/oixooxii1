fname = input("Enter file:")
if len(fname) < 1:
    fname = "mbox-short.txt"
handle = open(fname)

di = dict()
for li in handle:
    if not li.startswith("From "): continue
    wds = li.split()
    h = wds[5].split(':')
    di[h[0]] = di.get(h[0],0)+1

tmp = list()
for k,v in di.items():
    tmp.append((k,v))

tmp = sorted(tmp)
for k,v in tmp:
    print(k,v)
