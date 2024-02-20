# Function to calculate the minimum total cost
def min_total_cost(N, X):
    # Calculate the number of subscriptions needed
    subscriptions = N // 6
    # If there are remaining friends, add one more subscription
    if N % 6 != 0:
        subscriptions += 1
    # Calculate and return the total cost
    return subscriptions * X

# Input number of test cases
T = int(input())

# Iterate through each test case
for _ in range(T):
    # Input N and X for each test case
    N, X = map(int, input().split())
    # Calculate and print the minimum total cost
    print(min_total_cost(N, X))
