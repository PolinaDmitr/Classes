with open("files/9.22_20488.txt") as file:
    count = 0
    for line in file:
        l = [int(x) for x in line.split()]
        rep = [l.count(x) for x in l]
        if 1 in rep and sum(rep) > 7 \
            and l.count(max(l))  == 1:
            not_rep_sum = sum(l[j] for j in range(7) if rep[j] == 1)
            rep_sum = sum(l) - not_rep_sum
            if not_rep_sum >= rep_sum * 3:
                count += 1
    print(count)

