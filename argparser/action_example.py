import argparse

my_parser = argparse.ArgumentParser()
my_parser.version = '1.0'
my_parser.add_argument('-a', action='store')
my_parser.add_argument('-b', action='store_const', const=42)
my_parser.add_argument('-c', action='store_true')
my_parser.add_argument('-d', action='store_false')
my_parser.add_argument('-e', action='append')
my_parser.add_argument('-f', action='append_const', const=42)
my_parser.add_argument('-g', action='count')
my_parser.add_argument('-i', action='help')
my_parser.add_argument('-j', action='version')

args = my_parser.parse_args()

print(vars(args))

#RUN commands::
#python actions_example.py
#python actions_example.py -a 42
#python actions_example.py -a "test"
#python actions_example.py -b
#python actions_example.py -c
#python actions_example.py -d
#python actions_example.py -e me -e you -e us
#python actions_example.py -f -f
#python actions_example.py -ggggg
#python actions_example.py -j