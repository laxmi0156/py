'''60)Sample string:
 'w3resource' Expected output:
• {'3': 1,’s’: 1, 'r': 2, 'u': 1, 'w': 1, 'c': 1, 'e': 2, 'o': 1}'''

s='w3resource'
d={}
d[s[1]]='l'
d[s[4]]='l'
d[s[2]]='l'
d[s[-4]]='l'
d[s[0]]='l'
d[s[-2]]='l'
d[s[-1]]='l'
d[s[-5]]='l'
print(d)