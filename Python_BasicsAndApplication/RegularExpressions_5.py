import sys
import re

for line in sys.stdin:
    line = line.strip()
    a = re.findall(r'\b\w{2,}\b', line)
    for i in a:
        line = re.sub(r'\b'+i, re.sub(r''+i[0:2], i[1]+i[0], i), line, 1)
    print(line)

# еще один вариант решения
# for line in sys.stdin:
#     line = line.strip()
#     pattern = r'\b(\w)(\w)(\w*)\b'
#     print(re.sub(pattern, r'\2\1\3', line))
