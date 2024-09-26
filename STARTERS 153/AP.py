def main():
    t = int(input())  
    while t > 0:
        t -= 1
        a, b, c = map(int, input().split())
        if (b - a) == (c - b):
            print(0)
        else:
            print(1)
if __name__ == "__main__":
    main()
