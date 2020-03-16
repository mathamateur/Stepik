import sys
import re

for line in sys.stdin:
    line = line.strip()
    if re.fullmatch(r'(1(01*0)*1|0)*', line):
        print(line)
