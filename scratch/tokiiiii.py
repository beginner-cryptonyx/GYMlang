import sys
import os
import tokenize
import io

with open('samples/binary search.gym', 'r') as f:
    source = f.read()
    tokens = list(tokenize.generate_tokens(io.StringIO(source).readline))

    # for token in tokens:
    #     print(token.type)
    # print('/-------/')
    for token in tokens:
        print(token)

    new_tokens = []
    for token in tokens:
        if token.type not in [59,60,61,62,63,64,65,3]:
            new_token = tokenize.TokenInfo(
                type = token.type,
                string = token.string.replace('natty', 'def').replace('rack', '='),
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