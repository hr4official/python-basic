with open('abc.txt','r+b') as hr :
    hr.write("my test1\n")
    hr.write('test 2')
"""
for print lines 
for line in hr:
    print(line)
"""
#print(hr.tell())
print(open('abc.txt').read())
