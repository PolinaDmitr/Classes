k = 0 
for i in open('09.txt'): 
    a = [int(x) for x in i.split()] 
    a1 = [x for x in a if a.count(x) == 3] 
    a2 = [x for x in a if a.count(x) == 1] 
    if len(a1) == 3 and len(a2) == 3:
        a.sort()
        print(a1, a2)
        if a[0]**2 + a[5] ** 2 >= (a[1] +a[2] + a[3] + a[4])**2 :
            k += 1 

print(k)