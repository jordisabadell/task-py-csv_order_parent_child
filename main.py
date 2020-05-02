import argparse
from functions import loadFile, sortItems, saveFile

'''
#Descripcion
parser = argparse.ArgumentParser(description='Process some integers.')

parser.add_argument('integers', metavar='N', type=int, nargs='+',
                   help='an integer for the accumulator')

parser.add_argument('--sum', dest='accumulate', action='store_const',
                   const=sum, default=max,
                   help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args)
print(args.accumulate(args.integers))
exit()
'''

#REQUIRED
inputFileName = "pages.csv"
childColumnName = "layoutId"
parentColumnName = "parentLayoutId"

#OPTIONAL
parentRootId = 0 #default 0
priorityColumnName = "priority" #default empty equals 'not sorted'
newColumnTreeFormat = False
outputFileName = inputFileName.replace(".csv", "_sorted.csv")

#Execute
header, items = loadFile(inputFileName)
itemsSorted = sortItems(parentRootId, childColumnName, parentColumnName, priorityColumnName, items, 0)
saveFile(outputFileName, itemsSorted)