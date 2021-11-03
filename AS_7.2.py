fname = input("Enter file name: ")


try:
    fh = open(fname)
except:
    print ("File can not found", fh)


count = 0
total = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue

    else:
        line = line[20:]
        value = float(line)

        count = count+1
        total = total + value
        avr = total / count


print("Average spam confidence:" ,avr )
