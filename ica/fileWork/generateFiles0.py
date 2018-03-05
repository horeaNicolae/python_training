import re
import random

regList = ['AT', 'AU', 'BE', 'BG', 'CA', 'FR', 'IT', 'ES', 'DK', 'LU', 'MX', 'NZ', 'PT', 'RU']

def initializeFile():
    with open('newProducts.txt', 'w+') as f:
        f.write('UNA+14A00223:+\r\n')
        f.write('UNB+14A00223:+\r\n')

def firstWrite():
    with open('newProducts.txt', 'a+') as f:
            f.write('LIN+1+3+3SB19012AE\r\n')
            f.write('PIA+?+1+{}\r\n'.format(random.randint(1,9)))
            f.write('FTX+AAA+Description Long {} DE\r\n'.format(random.randint(1,100)))
            f.write('FTX+AAA+Description Short {} DE\r\n'.format(random.randint(1,100)))
            f.write('FTX+AAB+Successor text {} DE\r\n'.format(random.randint(1,100)))
            f.write('FTX+AFQ+ATBECAFRIT\r\n')
            f.write('NAD+TT+{}\r\n'.format(regList[random.randint(0, 13)]))
            f.write('NAD+TT+{}\r\n'.format(regList[random.randint(0, 13)]))
            f.write('NAD+TT+{}\r\n'.format(regList[random.randint(0, 13)]))
            f.write('NAD+TT+{}\r\n'.format(regList[random.randint(0, 13)]))
            f.write('NAD+TT+{}\r\n'.format(regList[random.randint(0, 13)]))
            f.write('NAD+TT+{}\r\n'.format(regList[random.randint(0, 13)]))
            f.write('NAD+TT+{}\r\n'.format(regList[random.randint(0, 13)]))
            f.write('NAD+TT+{}\r\n'.format(regList[random.randint(0, 13)]))


with open('newProducts.txt') as f:
    for line in f:
        if re.search('^UNB.+', line):
            print(line)

initializeFile()
firstWrite()
