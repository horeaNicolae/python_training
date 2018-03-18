import re
from itertools import islice

def getProduct():
    global indexProdus
    global indexNextMlfb
    indexProdus = []
    indexNextMlfb = []
    nextMlfb = []
    productCount = -1
    mlfbFound = False


    with open('fisier.txt', 'r') as f:
        for i, line in enumerate(f):
            print("Line {}: {}".format(i,line))

            if re.search('.*produs2', line):
                indexProdus.append(i)
                productCount +=1

                mlfbFound = True

                if nextMlfb != []:
                    nextMlfb.pop()
                    print(nextMlfb)

            if mlfbFound == True and nextMlfb == []:
                if re.search('.*lin', line) and i > indexProdus[productCount]:
                    nextMlfb.append(i)
                    print(nextMlfb)
                    indexNextMlfb.append(i)




    print(indexProdus)
    print(indexNextMlfb)

getProduct()

def copyProduct():
    with open('fisier.txt', 'w+') as f:
        lines = list(islice(f, indexProdus[0], indexNextMlfb[0]))
        print(lines)


copyProduct()
