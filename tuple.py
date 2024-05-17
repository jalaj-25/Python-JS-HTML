from collections import namedtuple
n = int(input())
columns = input().split()
Student = namedtuple('Student', columns)
print(f"{sum([int(Student(*input().split()).MARKS) for _ in range(n)]) / n:.2f}")
