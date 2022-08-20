import argparse

# TODO: print multiline args
def multiline_args(line):
    openinig_brackets = 0
    closing_brackets = 0
    while (openinig_brackets != closing_brackets):
        line = file.readline()
        if '(' in line:
            openinig_brackets += 1
        if ')' in line:
            closing_brackets += 1

# made main function for stopping the program if filetype is not supported
def main():
    # parse arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('parsed_file', help='Name of the file', type=str)
    args = parser.parse_args()

    # file extension defenition
    if args.parsed_file.split('.')[1] == 'py':
        function_length = 3
        class_declaration = 'class'
        function_declaration = 'def'
        pub_function = 'def'
    elif args.parsed_file.split('.')[1] == 'rs':
        function_lengh = 2
        class_declaration = 'impl'
        function_declaration = 'fn'
        pub_function = 'pub'
    else:
        print('Not supported file extension')
        return 0

    # parsing file and printing functions and classes
    with open(args.parsed_file, 'r') as file:
        for line in file:
            # skipping empty lines
            if line == '\n' or line.isspace(): file.read(1)
            # functions that are not in classes
            elif line[:function_length] == function_declaration:
                print('\n', line)
            # clases themselves
            elif line.split()[0] == class_declaration:
                print(line, end='')
            # class methods
            elif line.split()[0] == function_declaration or line.split()[0] ==pub_function:
                print(line, end='')
