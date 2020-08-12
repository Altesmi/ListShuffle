import sys
import random
from datetime import  date, timedelta


def readInput(filename):
    names = []
    with open(filename) as f:
        lines = f.readlines()
        for line in lines:
            if(len(line) <= 1 or len(line) is None):
                break
            else:
                names.append(line[:-1]) # remove \n
    return names

def nextMonday(d):
    d += timedelta(days = 7 - d.weekday()) # first monday

    return d

if __name__ == '__main__':
    
    names = readInput(sys.argv[1])
    dateNow = date.today()

    # Seed RNG for reproducibility
    # NB! Change this every time to get different results
    
    random.seed(7) # 7 is the best seed

    random.shuffle(names)

    columnLength = max(len(name) for name in names) + 8
    for name in names:
        dateNow = nextMonday(dateNow)
        text = [name, dateNow.strftime('%d.%m')]
        print("".join(t.ljust(columnLength) for t in text))
