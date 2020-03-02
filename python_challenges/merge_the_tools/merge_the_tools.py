def merge_the_tools(string, k):
    # your code goes here
    splitStrings = split_str(string, k)
    # for each string set loop and find the ones that don't match

def split_str(sequence, chunk, skip_tail = False):
    lst = []
    if chunk <= len(sequence):
        lst.extend([sequence[:chunk]])
        lst.extend(split_str(sequence[chunk:], chunk, skip_tail))
    elif not skip_tail and sequence:
        lst.extend([sequence])

    return lst


if __name__ == '__main__':
    string = input("Enter the string")
    k = input("Enter your divisor")

    merge_the_tools(string, k)