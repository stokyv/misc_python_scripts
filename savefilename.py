import sys


droppedFile = sys.argv[1]

with open('savedFilename.txt', 'w') as f:
    #f.write(sys.argv[1] + '\n')
    f.write(droppedFile + '\n')
