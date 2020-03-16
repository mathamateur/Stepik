import os.path
with open('output.txt','w') as w:
    w.write("\n".join(sorted([i[0] for i in list(os.walk('main')) if len([j for j in i[2] if j.endswith('.py')]) > 0])))
