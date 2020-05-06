import argparse
from functions import loadFile, saveFile, sortItemsByPriority, sortItemsByParent, getHeaderRow

#ARGUMENTS
parser = argparse.ArgumentParser(description='Given a CSV file with parent-child relationship column, this task sort the rows. Optional it creates a new column with tree format.')
parser.add_argument('--inputfile', dest='input_file', 
    help='Input file name.', type=str, required=True)
parser.add_argument('--outputfile', dest='output_file', 
    help='Output file name.', type=str, required=False, default='')
parser.add_argument('--childcol', dest='child_column', 
    help='Child column number (default value 0: first column).', type=int, required=True, default=0)
parser.add_argument('--parentcol', dest='parent_column', default=1, 
    help='Parent column number (default value 1: second column).', type=int, required=True)
parser.add_argument('--prioritycol', dest='priority_column', 
    help='Priority column number.', type=int, required=False)
parser.add_argument('--parentrootid', dest='parent_root_id', 
    help='Parent root ID (default value 0).', type=int, required=False, default=0)
parser.add_argument('--ignoreheaderrow', 
    help='Ignore first row (header).', action="store_true")
parser.add_argument('--adddepthcol', 
    help='Add new column with tree depth.', action="store_true")

args = parser.parse_args()
inputFile = args.input_file
outputFile = args.output_file
childColumn = args.child_column
parentColumn = args.parent_column
priorityColumn = args.priority_column
parentRootId = args.parent_root_id
ignoreHeaderRow = args.ignoreheaderrow
addDepthCol = args.adddepthcol

if not outputFile:
    outputFile = inputFile.replace(".csv", "_sorted.csv")

#EXECUTE
items = loadFile(inputFile, ignoreHeaderRow)

if priorityColumn:   
    items = sortItemsByPriority(items, parentColumn, priorityColumn)

itemsSorted = sortItemsByParent(parentRootId, childColumn, 
    parentColumn, addDepthCol, items, -1)

if ignoreHeaderRow:
    #It means that exists first row as Header. Concatenate it.
    header = getHeaderRow(inputFile)
    if addDepthCol:
        header.append("__auto_generated_depth_col__")
    itemsSorted = [header] + itemsSorted

saveFile(outputFile, itemsSorted)

print("Done.")