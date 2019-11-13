import parse

# token lists
LETTER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
WHITE_SPACE = ' '
DTYPE = ['Byte', 'Short', 'Int', 'Long', 'Float', 'Double', 'Char', 'Boolean', 'Array']

# getting input file
file_name = input("Enter the name of a kotlin file: ")

# creating file object
with open(file_name) as f:
    content = f.readlines()

# this will be real one day
string = parse(content)

if LETTER in string:
    arr.append(string)
