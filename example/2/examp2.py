print("x y z w")
for x in (0, 1):
    for y in (0, 1):
        for z in (0, 1):
            for w in (0, 1):
                res = (not (x <= w)) or (y <= z) or (not y)
                if not res:
                    print(x, y, z, w, res)
