import sys
import os
import tokenize
import io

keywords = {
    'natty':'def',
    'failure': 'return',
    'jacked':'if',
    'rookie': 'else',
    'jucied': 'elif',
    'skip_legs': 'pass'
}
# check if there is **a** file that is passed into the gl.py
number_of_argments = len(sys.argv)
if number_of_argments != 2:
    print("incorrect argument passed to transcriber")

# check if path is valud
if not os.path.isfile(sys.argv[1]):
    print("File not found")

# print the content of the file
with open(sys.argv[1], 'r') as f:
    source = f.read()
    tokens = list(tokenize.generate_tokens(io.StringIO(source).readline))

    for token in tokens:
        print(token)

    new_tokens = []
    for token in tokens:
        if token.type not in [59,60,61,62,63,64,65,3]:
            # now sub out all the keywords
            string = token.string
            for old, new in keywords.items():
                string.replace(old,new)
            new_token = tokenize.TokenInfo(
                type = token.type,
                string = string,
                start = token.start,
                end = token.end,
                line = token.line.replace('natty', 'def').replace('rack', '=')
            )
            new_tokens.append(new_token)
        else:
            new_tokens.append(token)
    print('/-------/')
    print('/-------/')
    print('/-------/')
    print('/-------/')
    print('/-------/')
    
    for token in new_tokens:
        print(token)
    
    new_code = tokenize.untokenize(new_tokens)
    print(new_code)
