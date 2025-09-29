
a = input().lower()

chars = {}
bestchars = {}

for ch in a:
    if ch in chars:
        chars[ch] += 1
    else:
        chars[ch] = 1

for ch in chars:
    if len(bestchars) <= 2:
        bestchars[ch] = chars[ch]
    else:
        if int(chars[ch]) > min(bestchars.values()):
            bestchars.pop(min(bestchars, key=bestchars.get))
            bestchars[ch] = chars[ch]

print(bestchars)