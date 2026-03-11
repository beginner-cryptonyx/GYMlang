import sys
import os
import tokenize
import io

TYPE_IGNORE = 56
TYPE_COMMENT = 57
FSTRING_START = 59
FSTRING_MIDDLE = 60
FSTRING_END = 61
TSTRING_START = 62
TSTRING_MIDDLE = 63
TSTRING_END = 64
COMMENT = 65
STRING = 3

ignore_list = [TYPE_IGNORE, TYPE_COMMENT, FSTRING_START, FSTRING_MIDDLE, FSTRING_END, TSTRING_START, TSTRING_MIDDLE, TSTRING_END, COMMENT, STRING]

keywords = {
    'natty':'def',
    'failure': 'return',
    'jacked':'if',
    'rookie': 'else',
    'juiced': 'elif',
    'skip_legs': 'pass',
    'circuit':'while',
    'rack': '=',
    'ego_lift': 'try',
    'injury': 'except',
    'burnout': 'finally',
    'rep': 'for',
    'workout': 'class',
    'superset' : 'with',
    'flex': 'print'
}
# check if there is **a** file that is passed into the gl.py
number_of_argments = len(sys.argv)
if number_of_argments != 2:
    print("incorrect argument passed to transcriber")
    sys.exit(1)

# check if path is valud
if not os.path.isfile(sys.argv[1]):
    print("File not found")
    sys.exit(1)

# check file extention
if sys.argv[1].split('.')[-1] != 'gympy':
    print("Incorrect File Type Provided")
    sys.exit(1)

# print the content of the file
with open(sys.argv[1], 'r') as f:
    source = f.read()
    tokens = list(tokenize.generate_tokens(io.StringIO(source).readline))

    # for token in tokens:
    #     print(token)

    new_tokens = []
    for token in tokens:
        if token.type not in ignore_list:

            # now sub out all the keywords
            string = token.string
            for old, new in keywords.items():
                string = string.replace(old,new)
            
            line = token.line
            for old, new in keywords.items():
                line = line.replace(old,new)
                
            new_token = tokenize.TokenInfo(
                type = token.type,
                string = string,
                start = token.start,
                end = token.end,
                line = line
            )
            new_tokens.append(new_token)
        else:
            new_tokens.append(token)

    # for token in new_tokens:
    #     print(token)
    
    new_code = tokenize.untokenize(new_tokens)
    # print(new_code)
    exec(new_code)
