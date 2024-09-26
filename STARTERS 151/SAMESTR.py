def count_valid_k(john_length, emma_string):
    alice_zeros = 0
    bob_ones = 0

    for michael in range(john_length):
        if emma_string[michael] == '0':
            alice_zeros += 1
        else:
            bob_ones += 1

    david_result = 0

    for lisa_k in range(1, john_length + 1):
        if lisa_k >= alice_zeros and (lisa_k - alice_zeros) % 2 == 0:
            david_result += 1
        elif lisa_k >= bob_ones and (lisa_k - bob_ones) % 2 == 0:
            david_result += 1

    return david_result

def main():
    test_cases = int(input())

    while test_cases > 0:
        test_cases -= 1
        john_length = int(input())
        emma_string = input()

        print(count_valid_k(john_length, emma_string))

if __name__ == "__main__":
    main()
