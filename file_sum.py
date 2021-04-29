"""
Author: Masud Hussain
Course: CS162
Assignment: 5A
"""


def file_sum(text_file_name):
    total = 0

    # Reads numbers line by line from a file and converts them to int/float to add
    try:
        with open(text_file_name, 'r') as infile:
            for line in infile:
                total += int(float(line))
    # Except throws an error if the file is not found
    except FileNotFoundError:
        print("The file was not found")

    # Creates a file named sum.txt and writes the total sum to the file
    with open('sum.txt', 'w') as outfile:
        outfile.write(str(total) + '\n')
