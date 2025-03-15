from importlib.metadata import files

with open("files/17_2_1.txt") as file:
    numbers = [int(x) for x in file]
    num_m = max(x for x in numbers if x % 10 == 5)
    k = []
    for i in range(len(numbers) - 2):
        l = []
        for x in (numbers[i], numbers[i + 1], numbers[i + 2]):
            l.append(len(str(x)))
        sum_three = numbers[i] + numbers[i + 1] + numbers[i + 2]
        if l.count(5) == 2 and (sum_three > num_m):
            k.append(sum_three)

    print(len(k), max(k))




