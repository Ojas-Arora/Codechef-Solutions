# cook your dish here
def main():
    test_cases = int(input())
    while test_cases > 0:
        test_cases -= 1
        x, y = map(int, input().split())
        array = list(map(int, input().split()))
        sum_value = sum(array[:y])
        array[-1] += sum_value
        print(" ".join(map(str, array[y:])))

if __name__ == "__main__":
    main()
