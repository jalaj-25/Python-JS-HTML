def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        substr = string[i:i+k]  # Extract the current substring
        unique_chars = []  # List to store unique characters
        for char in substr:
            if char not in unique_chars:
                unique_chars.append(char)
        print(''.join(unique_chars))  # Print the unique characters as a string

if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)
