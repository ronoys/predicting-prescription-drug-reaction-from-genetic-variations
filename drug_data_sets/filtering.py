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


with open(os.path.join(os.getcwd(), 'synthroid_data.txt'), 'r') as text_file:
    for line in text_file:
        print line
