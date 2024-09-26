# cook your dish here
def main():
    t = int(input())  # number of test cases

    for _ in range(t):
        n = int(input())  # size of the array

        vec = list(map(int, input().split()))  # input the list of integers

        vec.sort()  # sort the array

        # Compute the three possible differences
        ans1 = vec[n-3] - vec[0]
        ans2 = vec[n-1] - vec[2]
        ans3 = vec[n-2] - vec[1]

        # Print the minimum difference
        print(min(ans1, min(ans2, ans3)))

if __name__ == "__main__":
    main()

