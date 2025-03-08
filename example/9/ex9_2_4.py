with open("files/9_4.txt") as file:
    k = 0
    for l in file:
        numbers = [int(x) for x in l.split()]
        numbers.sort()
        c_numbers = [numbers.count(x) for x in numbers]
        if c_numbers.count(2) == 4 and c_numbers.count(1) == 3 \
            and numbers[0] * numbers[1] > sum(numbers) - numbers[0] - numbers[1]:
            k += 1
    print(k)