'''import os
print (os.getcwd() + "hi")

f = open("crestor_data.txt")

x - 0
while x < 10:

    for line in f:
        print line
        x = x + 1
'''
import os


with open(os.path.join(os.getcwd(), 'sample_data.txt'), 'r') as text_file:
    count = 1
    for line in text_file:
        x = str(line)
        #print x[:2]
        if x[0:2] == 'rs':
            print x
        
        #try:
        #    c = float(line)
        #    if c < 1:
        #        print c

        #except:
        #    print "-"
        '''if count == 1 or count == 2 or count == 6:
            print line

        if count == 13:
            count = 1
        count = count + 1
        '''
        #print str (line)

#print os.path.join(os.getcwd(), 'hello.txt') - prints C:\Users\ronoy\AppData\Local\atom\Atom Files\hello.txt
#print os.getcwd()
