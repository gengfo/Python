
f = open('test1.txt', 'rt')
line = f.readline()
while line:
    print line
    line = f.readline()
