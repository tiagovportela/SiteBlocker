f = open('example.txt', 'r+')
f.seek(0)
lines = f.readlines()
count = 0
tam = len(lines) -1
for line in lines:
    count = count + len(line)

print str(tam) + '\n'
f.seek(tam*count)
f.write('[0]---------------------[0]')

f.close()
