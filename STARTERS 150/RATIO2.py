# cook your dish here
def main():
    test_cases = int(input())
    
    while test_cases > 0:
        test_cases -= 1
        a, b = map(int, input().split())
        
        larger = max(a, b)
        smaller = min(a, b)
        
        option1 = max(0, smaller - (larger // 2))
        option2 = max(0, 2 * smaller - larger)
        
        print(min(option1, option2))

if __name__ == "__main__":
    main()
