import sys
import os
import re

# check if there is **a** file that is passed into the gl.py
number_of_argments = len(sys.argv)
if number_of_argments != 2:
    print("incorrect argument passed to transcriber")

# check if path is valud
if not os.path.isfile(sys.argv[1]):
    print("File not found")

# print the content of the file
with open(sys.argv[1], 'r') as f:
    target_lines = []
    for i, line in enumerate(f.readlines()):
        if re.search(f"\\bnatty\\b", line) and not re.search("(\'|\").*natty.*(\"|\')", line) and not re.search("#.*natty", line):
            target_lines.append(i)
    print(target_lines)


