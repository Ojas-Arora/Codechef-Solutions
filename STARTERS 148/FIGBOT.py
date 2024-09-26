# cook your dish here
def check():
    a, b, c = map(int, input().split())
    moves = input().strip()

    dx, dy = 0, 0  

    for j in range(1, a + 1):
        if moves[j - 1] == 'U':
            dy += 1  
        elif moves[j - 1] == 'D':
            dy -= 1  
        elif moves[j - 1] == 'L':
            dx -= 1  
        elif moves[j - 1] == 'R':
            dx += 1  
            
        dist = abs(b - dx) + abs(c - dy)  
        if dist <= j and dist % 2 == j % 2:
            print("Yes")
            return

    print("No")

if __name__ == "__main__":
    test_cases = int(input())
    for _ in range(test_cases):
        check()
