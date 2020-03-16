import sys
import re

for line in sys.stdin:
    line = line.strip()
    for i in re.split(r" ", line):
        if re.fullmatch(r'('+i[0:len(i) // 2]+')'+'{2}'+'\\b', i):
            print(line)
            break

# еще один вариант решения
#     for line in sys.stdin:
#         line = line.strip()
#         if re.search(r"\b(\w+)\1\b", line):
#             print(line)
