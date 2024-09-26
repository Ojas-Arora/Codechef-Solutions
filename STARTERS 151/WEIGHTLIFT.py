# cook your dish here
def main():
    # Read six integers from input
    try:
        X1, X2, Y1, Y2, Z1, Z2 = map(int, input().split())
    except ValueError:
        # Handle invalid input
        return
    
    # Calculate the maximum for each round
    round_a = max(X1, X2)
    round_b = max(Y1, Y2)
    round_c = max(Z1, Z2)
    
    # Calculate the total score
    final_score = round_a + round_b + round_c
    
    # Output the total score
    print(final_score)

if __name__ == "__main__":
    main()
