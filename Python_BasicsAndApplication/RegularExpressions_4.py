import sys
import re

for line in sys.stdin:
    print(re.sub(r'a+\b', 'argh', line.strip(), 1, re.IGNORECASE))