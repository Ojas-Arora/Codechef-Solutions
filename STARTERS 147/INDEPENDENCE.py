# cook your dish here
t = int(input())
for i in range(t):
    a, b, c = map(int, input().split())
    d = max(a, b, c)
    re = (a + b + c) - d
    if d <= re + 1:
        print("YES")
    else:
        print("NO")