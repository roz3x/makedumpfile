f = open("out.log", "r").read()

prev = 0
start = 0
mp = {}
for i in f.split("\n"):
    k = int(i)
    if k == prev + 1:
        pass 
    else : 
        start = k
    prev = k
    try: 
        mp[start] = mp[start] + 1
    except : 
        mp[start] = 0

from itertools import islice

pm = dict(sorted(mp.items(), key=lambda item: item[1], reverse=True))

first_10 = dict(islice(pm.items(), 100))
print(first_10)
# print(mp)