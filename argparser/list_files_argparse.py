# Import the argparse library
import argparse

import os
import sys

# Create the parser
#description: for the text that is shown before the help text
#epilog: for the text shown after the help text
#prefix chars: default it is -h but you can use your specified one
my_parser = argparse.ArgumentParser(prog='list_files',
                                    usage='%(prog)s [options /h ] path',
                                    description='List the content of a folder',
                                    epilog='Enjoy the program! :)',
                                    prefix_chars='/')

# Add the arguments
my_parser.add_argument('Path',
                       metavar='path',
                       type=str,
                       help='the path to list')

# Execute the parse_args() method
args = my_parser.parse_args()

input_path = args.Path

if not os.path.isdir(input_path):
    print('The path specified does not exist')
    sys.exit()

print('\n'.join(os.listdir(input_path)))