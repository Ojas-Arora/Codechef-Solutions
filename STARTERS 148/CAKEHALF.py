# cook your dish here
x = int(input())
for j in range(0, x):
    C, D = map(int, input().split())
    steps = 0
        
    if C == D:
        print("0")
    else:
        while C != D:
            if C > D:
                steps += (C + 1) // 2
                C -= (C + 1) // 2
            else:
                steps += (D + 1) // 2
                D -= (D + 1) // 2
        print(steps)
