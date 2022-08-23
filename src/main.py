import argparse

# TODO: print multiline args
def multiline_args(line):

# TODO: add module parse
def parse_modules(file):

# kind of modularity, to add new programming language you just need to add new if statement
def match_file_type(extension):
    # 6 variables 
    """Returns tuple of func_lengh, func_decl, pub_func, priv_func, class_decl, another_class_decl"""
    if extension == 'py':
        # python language
        return (3, 'def', 'def', 'def', 'class', 'class')
    elif extension == 'rs':
        # rust language
        return (2, 'fn', 'pub', 'fn', 'trait', 'impl')
    else:
        # break for not supported filetypes 
        print('File type is not supported')
        exit()

def main():
    # parse arguments
    parser = argparse.ArgumentParser(description='Prints out functions and classes of the source code')
    parser.add_argument('-parsed_file', help='Source code of the program', default=None)
    args = parser.parse_args()
    
    # check for any args
    if args.parsed_file == None:
        exit()

    # filetype variables
    try:
        func_length, func_decl, pub_func, private_func, class_decl, \
        another_class_decl = match_file_type(args.parsed_file.split('.')[1])
    except IndexError:
        # catch for files with no dot in their name
        print('File type is not supported')
        exit()

    # parsing file and printing functions and classes
    with open(args.parsed_file, 'r') as file:
        for line in file:
            # skipping empty lines
            if line == '\n' or line.isspace(): file.read(1)
            # functions declaration
            elif line[:func_length] == func_decl:
                print('\n', line)
            # clases declaration
            elif line.split()[0] == class_decl or \
                 line.split()[0] == another_class_decl:
                print(line, end='')
            # class methods (public and private ones)
            elif line.split()[0] == func_decl or \
                 line.split()[0] == pub_func or \
                 line.split()[0] == private_func:
                print(line, end='')
