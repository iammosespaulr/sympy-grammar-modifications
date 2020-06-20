import re
from sys import argv
f = open('LaTeX.g4','r')
data = f.read()
f.close()
start = argv[1]
resp = re.findall('{}:.*?;'.format(start),data,re.DOTALL)
if resp:
    resp = resp[0]
    resp = re.split('\s+\|\s+|\n',resp)
    sorted_lst = sorted(resp,key=lambda x: -len(x))
    for token in sorted_lst:
        if ':' not in token:
            print('\t','|','\t',token.strip())

