import re

def getParameter():
    parameter = input(str("Baga aci:"))
    return parameter

def getProduct():

    product = getParameter()

    with open('fisier.txt', 'r') as f:
        open('resultFile.txt', 'w').close()
        for i, line in enumerate(f):
            if re.search(".*" + product + "$", line):
                print("Line {}: {}".format(i,line))
                with open('resultFile.txt', 'a+') as rf:
                    rf.write(line)

                for j, linie in enumerate(f):
                    if re.search('.*lin', linie):
                        break
                    else:
                        with open('resultFile.txt', 'a+') as rf:
                            rf.write(linie)

getProduct()
