import random
import time


def miller_rabin(n):
    k = 0
    q = n - 1
    while 1:
        q //= 2
        k += 1
        if q % 2:
            break

    # 经典算法思想
    a = random.randint(2, n - 2)
    if a**q % n == 1:
        return "不确定"
    else:
        for j in range(0, k):
            if a ** (2**j * q) % n == n - 1:
                return "不确定"
            # return '合数'


num = int(input())
time_begin = time.time()
print(miller_rabin(num))
time_end = time.time()
print(time_end - time_begin, "seconds")
