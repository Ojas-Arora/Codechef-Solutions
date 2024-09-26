#include <stdio.h>

int main() {
    int num_cases;
    scanf("%d", &num_cases);  // Reading the number of test cases
    
    while (num_cases--) {
        long long red, green, blue;
        scanf("%lld %lld %lld", &red, &green, &blue);
        
        // Find the maximum number of butterflies
        long long max_color = red;
        if (green > max_color) max_color = green;
        if (blue > max_color) max_color = blue;
        
        // Check if the max color is less than or equal to the sum of the other two
        if (max_color <= (red + green + blue - max_color)) {
            printf("YES\n");
        } 
        else {
            printf("NO\n");
        }
    }

    return 0;
}

