import argparse


# TODO: print multiline args
def multiline_args(line):
    pass


# TODO: add module parse
def parse_modules(file):
    pass


def get_lang_keywords(extension):
    #
    # define filetype by extension, should return tuple of keywords,
    # not something abstract
    #
    """Returns tuple of keywords"""
    # python lang
    if extension in ('py', 'pyi', 'pyc', 'pyd', 'pyw', 'pyz', 'pyo'):
        return ('def', 'class')
    # rust lang
    elif extension in ('rs', 'rlib'):
        return ('fn', 'pub', 'trait', 'impl')
    # go lang
    elif extension in ('go'):
        return ()
    # TODO: c lang
    else:
        # break for not supported filetypes
        print('File type is not supported')
        exit()


def main():
    # parse arguments
    parser = argparse.ArgumentParser(
            description='Prints out functions and classes of the source code'
    )
    parser.add_argument('parsed_file',
                        help='Source code of the program',
                        default=None)
    args = parser.parse_args()

    # check for any args
    if args.parsed_file is None:
        exit()

    # filetype variables
    try:
        lang_keywords = get_lang_keywords(args.parsed_file.split('.')[1])
    except IndexError:
        # catch for files w/o dot in their name
        print('File type is not supported')
        exit()

    # parsing file and printing functions and classes
    with open(args.parsed_file, 'r') as file:
        for line in file:
            # skipping empty lines
            if line == '\n' or line.isspace():
                file.read(1)
            # found keyword
            elif line.split()[0] in lang_keywords:
                print(line, end='')
