import argparse
from functions import loadFile, saveFile, sortItemsByParent, sortItemsByPriority

#ARGUMENTS
#--inputfile pages.csv --childcol layoutId --parentcol parentLayoutId --prioritycol priority --newcoltreeformat True
parser = argparse.ArgumentParser(description='Given a CSV file with parent-child relationship column, this task sort the rows. Optional it creates a new column with tree format.')
parser.add_argument('--inputfile', dest='inputFileName', help='Input file name.', type=str, required=True)
parser.add_argument('--childcol', dest='childColumnName', help='Child column name.', type=str, required=True)
parser.add_argument('--parentcol', dest='parentColumnName', help='Parent column name.', type=str, required=True)
parser.add_argument('--parentrootid', dest='parentRootId', help='Parent root ID.', type=int, required=False, default=0)
parser.add_argument('--prioritycol', dest='priorityColumnName', help='Priority column name.', type=str, required=False, default='')
parser.add_argument('--newcoltreeformat', dest='newColumnTreeFormat', help='New column with tree format.', type=bool, required=False, default=False)
parser.add_argument('--outputfile', dest='outputFileName', help='Output file name.', type=str, required=False, default='')

# PARAMS
args = parser.parse_args()
inputFileName = args.inputFileName
childColumnName = args.childColumnName
parentColumnName = args.parentColumnName
parentRootId = args.parentRootId
priorityColumnName = args.priorityColumnName
newColumnTreeFormat = args.newColumnTreeFormat
outputFileName = args.outputFileName

if not outputFileName:
    outputFileName = inputFileName.replace(".csv", "_sorted.csv")

print("inputFileName=" + inputFileName + ", childColumnName=" + childColumnName + 
    ", parentColumnName=" + parentColumnName + ", parentRootId=" + str(parentRootId) + 
    ", priorityColumnName=" + priorityColumnName + ", newColumnTreeFormat=" + str(newColumnTreeFormat) + 
    ", outputFileName=" + outputFileName)

#EXECUTE
header, items = loadFile(inputFileName)
itemsSorted = sortItemsByParent(parentRootId, childColumnName, parentColumnName, items, 0)
if priorityColumnName:
    itemsSorted = sortItemsByPriority(priorityColumnName, itemsSorted)

saveFile(outputFileName, itemsSorted)