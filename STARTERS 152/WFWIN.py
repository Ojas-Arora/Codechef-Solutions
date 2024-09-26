# cook your dish here
def main():
    test_cases = int(input())  

    for _ in range(test_cases):
        value_m, value_p = map(int, input().split())  
        counter = 0

        
        while value_m < 299 and value_m + value_p + 20 * counter < 1000:
            value_m += 1
            counter += 1

       
        if value_m + value_p + 20 * counter <= 1000:
            print(counter)
        else:
            print(counter - 1)

if __name__ == "__main__":
    main()
