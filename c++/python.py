arr = [3, 9, 12, 16, 20]
k = 3
n =5

l = []
for x in arr:
    if x<k:
        l.append(x+k)
    else:
        l.append(x-k)
print(l)

height = l[-1]-l[0]
print(height)