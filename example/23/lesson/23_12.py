# + 2 sum(dig)  1 -> 70

def sum_d(a):
    return sum(int(x) for x in str(a))



def f(x, y, op: str):
    if x > y:
        return 0
    if x == y and op.count('1111111') == 1 and op.count('2222222') == 1 and '11111111' not in op and '22222222' not in op:
        print(op)
        return 1
    return f(x + 2, y, op + '1') + f(x + sum_d(x), y, op + '2')


print(f(1, 70, ''))