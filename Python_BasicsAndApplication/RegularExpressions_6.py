import sys
import re

for line in sys.stdin:
    print(re.sub(r'((\w)\2+)',r'\2',line.strip()))
