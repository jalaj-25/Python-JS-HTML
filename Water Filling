def can_fill_bottles(b1, b2, b3):
    empty_count = 0
    if b1 == 0:
        empty_count += 1
    if b2 == 0:
        empty_count += 1
    if b3 == 0:
        empty_count += 1
    if empty_count >= 2:
        return "Water filling time"
    else:
        return "Not now"
def main():
    T = int(input())
    for _ in range(T):
        b1, b2, b3 = map(int, input().split())
        print(can_fill_bottles(b1, b2, b3))
if __name__ == "__main__":
    main()
