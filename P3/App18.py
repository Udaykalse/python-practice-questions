arr = [1,2,2,3,3,3]

d={}

for num in arr:
    d[num]=d.get(num,0)+1
print(d)