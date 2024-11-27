ans = 0


def check(x):  # 判断是否符合条件
    s1, s2 = sum(int(i) for i in bin(x)[2:]), 0
    while x:
        s2 += x % 4
        x //= 4
        if s1 == s2:
            print(x)
    return s1 == s2


for i in range(1, 2025):
    ans += check(i)


print(ans)  # 63