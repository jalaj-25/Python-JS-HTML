def print_formatted(number):
    width = len(bin(number)[2:])  # [2:] to exclude '0b' prefix
    for i in range(1, number + 1):
        dec_str = f"{i:{width}d}"
        oct_str = f"{i:{width}o}"
        hex_str = f"{i:{width}X}"
        bin_str = f"{i:{width}b}"
        print(f"{dec_str} {oct_str} {hex_str} {bin_str}")
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
