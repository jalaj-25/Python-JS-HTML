def total_cost(t, test_cases):
    results = []
    
    for i in range(t):
        x, y = test_cases[i]
        total_amount = x * y
        results.append(total_amount)
    
    return results

# Input reading
t = int(input())
test_cases = []

for _ in range(t):
    test_case = list(map(int, input().split()))
    test_cases.append(test_case)

# Output
results = total_cost(t, test_cases)
for result in results:
    print(result)
