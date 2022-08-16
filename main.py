import argparse

# parse arguments and make --help page
parser = argparse.ArgumentParser()
parser.add_argument('parsed_file',help='Name of the file', type=str)
args = parser.parse_args()

with open(args.parsed_file, 'r') as file:
    for line in file:
        # skipping empty lines
        if line == '\n' or line.isspace(): file.read(1)
        # functions not in classes
        elif line[:3] == 'def':
            print()
            print(line)
        elif line.split()[0] == 'class':
            print(line, end='')
        elif line.split()[0] == 'def':
            print(line, end='')



