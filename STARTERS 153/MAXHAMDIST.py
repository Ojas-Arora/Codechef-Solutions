# cook your dish here
def process_test_cases():
    test_cases = int(input())
    
    for _ in range(test_cases):
        num_rows, num_strings = map(int, input().split())
        
        data = [[0, [0, 0]] for _ in range(num_rows)]
        result = 0
        
        for _ in range(num_strings):
            line = input()
            
            for idx in range(len(line)):
                if line[idx] == '0':
                    data[idx][0] += 1
                elif line[idx] == '1':
                    data[idx][1][0] += 1
                else:
                    data[idx][1][1] += 1
        
        for idx in range(num_rows):
            zeros = data[idx][0]
            ones = data[idx][1][0]
            questions = data[idx][1][1]
            
            while questions > 0:
                if zeros <= ones:
                    zeros += 1
                else:
                    ones += 1
                questions -= 1
            
            result += zeros * ones
        
        print(result)

process_test_cases()
