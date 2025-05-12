#при траектории есть ограничения на испльзование команд содержит 15, 30, не содержит 12, 20

def f(x, y, c):
    if x > y or x in (12, 20):
        return 0
    if x == y:
        return 1
    count = f(x + 1, y, 0)  #всегда придём в нужное число с помощью +1
    if x not in (14, 29):
        count += f(x + 2, y, 0)
    if c != 1 and not (6 <= x <= 14) and not (11 <= x <= 29):
        count += f(x * 3, y, 1)
    return count


print(f(2, 38, 0))