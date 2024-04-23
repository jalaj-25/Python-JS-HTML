import textwrap
def wrap(string, max_width):
    # Use textwrap.wrap to wrap the string into lines of the specified width
    wrapped_lines = textwrap.wrap(string, width=max_width)
    
    # Join the wrapped lines with newline characters to form the final output string
    wrapped_string = '\n'.join(wrapped_lines)
    
    return wrapped_string
if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
