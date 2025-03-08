import csv
f = open("9.csv","r", encoding="utf-8-sig")
reader = csv.reader(f, delimiter=';')
data = [list(map(int, row)) for row in reader if len(row) == 7]


def has_duplicates(numbers):
    return len(numbers) != len(set(numbers))

counter = 0
for i in data:
    if has_duplicates(i):
        unique = [x for x in i if i.count(x) == 1]
        repeated = [x for x in set(i) if i.count(x) > 1]
        product = 1
        for b in repeated:
            product*=b
        if (3 * sum(unique)) <= product:
            counter+=1
print(counter)


