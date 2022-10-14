alpha = 'abcdefghijklmnopqrstuvwxyz 1234567890'

n = int(input('Step: ')) # STEP
s = input('Line: ').strip() #LINE

res = ''
for c in s:
    res += alpha[(alpha.index(c) + n) % len(alpha)]
print('Result: "' + res + '"')