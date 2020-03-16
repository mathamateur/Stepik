import sys
import re

for line in sys.stdin:
    line = line.strip()
    if re.match(r'.*\bcat\b', line):
        print(line)
