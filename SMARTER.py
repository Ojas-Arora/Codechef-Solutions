# cook your dish here
import math

t = int(input())
for _ in range(t):
    x,y,z = map(int, input().split())
    c1 = math.ceil(x/ y)
    c2 = math.ceil(x/ z)
    if c1 == c2:
        print("-1")
    else:
        print(abs(c1 - c2) - 1)