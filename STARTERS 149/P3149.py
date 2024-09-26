def process_test_cases():
    num_tests = int(input())
    
    for _ in range(num_tests):
        array_size = int(input())
        numbers = list(map(int, input().split()))
        
        left_index = 0
        while left_index < array_size and numbers[left_index] <= 0:
            left_index += 1
        
        right_index = array_size - 1
        while right_index >= 0 and numbers[right_index] <= 0:
            right_index -= 1
        
        if right_index <= left_index:
            print(0)
        else:
            negative_count = 0
            for current_index in range(left_index, right_index + 1):
                if numbers[current_index] < 0:
                    negative_count += 1
            print(negative_count)

if __name__ == "__main__":
    process_test_cases()
