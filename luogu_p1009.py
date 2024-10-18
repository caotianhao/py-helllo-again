def jc1009(k) -> int:
    if k == 1:
        return 1
    return k * jc1009(k - 1)


n = int(input())
s = 0
for i in range(n, 0, -1):
    s += jc1009(i)
print(s)
