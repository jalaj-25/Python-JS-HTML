
def split_and_join(line):
    words = line.split()
    result_string = "-".join(words)
    return result_string

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
