# cook your dish here
def main():
    test_cases = int(input())
    
    while test_cases > 0:
        test_cases -= 1
        length = int(input())
        
        sug = list(map(int, input().split()))
        
        frequency = [0] * 101
        for num in sug:
            frequency[num] += 1
        
        zero_freq = frequency[0]
        max_freq = 0
        max_index = -1
        
        for i in range(1, 101):
            if frequency[i] > max_freq:
                max_freq = frequency[i]
                max_index = i
        
        max_freq += zero_freq
        
        max_freq -= 1  # decrement max_freq to get the correct count after removing the most frequent element
        oja = max_freq * (max_freq + 1) // 2
        
        for i in range(1, 101):
            if i != max_index:
                oja += (frequency[i] - 1) * frequency[i] // 2
        
        print(oja)

if __name__ == "__main__":
    main()
