text = "X-DSPAM-Confidence:    0.8475"

x = text.find(':')
y = text.find('5')
xy = text[x+1 : y+1]

xxyy = float(xy.lstrip())
print(xxyy)
