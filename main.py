import os
    # 1
with open('one.txt', 'r') as input_file:
    with open('two.txt', 'w') as output_file:
        for line in input_file:
            words = line.split()
            for word in words:
                if len(word) >= 7:
                    output_file.write(word + '\n')

    # 2
with open('one2.txt', 'r') as input_file:
    with open('two2.txt', 'w') as output_file:
        for line in input_file:
            output_file.write(line)

    # 3
with open('one3.txt', 'r') as input_file:
    with open('two3.txt', 'w') as output_file:
        line = input_file.readlines()
        for line in reversed(line):
            output_file.write(line)