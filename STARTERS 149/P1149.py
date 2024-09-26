# cook your dish here
# Read the input values
X, Y, K = map(int, input().split())

# Calculate the absolute difference
difference = abs(X - Y)

# Check if the difference is within the allowed range K
if difference <= K:
    print("Yes")
else:
    print("No")
