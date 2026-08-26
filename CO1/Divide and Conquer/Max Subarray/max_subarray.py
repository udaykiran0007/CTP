def max_crossing_sum(arr, low, mid, high):
    # Find maximum sum on the left side
    left_sum = float("-inf")
    total = 0

    for i in range(mid, low - 1, -1):
        total += arr[i]

        if total > left_sum:
            left_sum = total

    # Find maximum sum on the right side
    right_sum = float("-inf")
    total = 0

    for i in range(mid + 1, high + 1):
        total += arr[i]

        if total > right_sum:
            right_sum = total

    return left_sum + right_sum


def max_subarray(arr, low, high):
    # Base case
    if low == high:
        return arr[low]

    # Find middle
    mid = (low + high) // 2

    # Maximum subarray in the left half
    left_sum = max_subarray(arr, low, mid)

    # Maximum subarray in the right half
    right_sum = max_subarray(arr, mid + 1, high)

    # Maximum subarray crossing the middle
    crossing_sum = max_crossing_sum(arr, low, mid, high)

    # Return the maximum of the three
    return max(left_sum, right_sum, crossing_sum)


# Daily profit/loss in thousands of rupees
profits = [-2, 3, 4, -1, 2, 1, -5, 4]

maximum_profit = max_subarray(
    profits,
    0,
    len(profits) - 1
)

print("Daily Profit/Loss:")
print(profits)

print("\nMaximum Continuous Profit:", maximum_profit)

print("Maximum Profit in Rupees: ₹", maximum_profit * 1000)