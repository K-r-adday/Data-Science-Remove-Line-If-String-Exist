import sys

def remove_lines_with_word(filename, word):
    # Read the contents of the file
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Filter out lines containing the specified word
    lines_to_keep = [line for line in lines if word.lower() not in line.lower()]

    # Write the filtered lines back to the file
    with open(filename, 'w') as file:
        file.writelines(lines_to_keep)

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python remove_stories.py <filename> <word>")
    else:
        filename = sys.argv[1]
        word_to_remove = sys.argv[2]
        remove_lines_with_word(filename, word_to_remove)
