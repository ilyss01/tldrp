import argparse


# TODO: print multiline args
def parse_multiline_args(line):
    pass


# TODO: add module parse
def parse_modules(file,
                  hi_mom,
                  thing):
    pass


def get_lang_keywords(extension):
    """Returns tuple of keywords by extension"""
    # python lang
    if extension in ('py', 'pyi', 'pyc', 'pyd',
                     'pyw', 'pyz', 'pyo'):
        return ('def', 'class')
    # rust lang
    elif extension in ('rs', 'rlib'):
        return ('fn', 'pub', 'trait', 'impl')
    # go lang
    elif extension in ('go'):
        return ('package', 'func', 'type')
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
        # catch for files w/o extension
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
                # FIXME infinite loop
                if '(' in line and ')' not in line:
                    while ')' not in line:
                        print(line, end='')
                else:
                    # end='' bc strings have \n byte
                    print(line, end='')
