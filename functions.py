import os
import codecs

def loadFile(fileName, ignoreHeaderRow):
    '''
    '''

    #read file
    file = open(fileName, "r", encoding="utf8")

    #iterate lines
    items = []
    for i, line in enumerate(file):
        if (ignoreHeaderRow and i>0) or (not ignoreHeaderRow):
            if line:
                #convert line to array of elements
                item = []
                values = line.replace("\n", "").split("\t")
                for value in values:
                    item.append(value.strip())

                items.append(item)
    
    return items


def saveFile(fileName, items):
    '''
    '''

    #remove file if exists
    if os.path.exists(fileName):
        os.remove(fileName)

    #wirte output file
    f = codecs.open(fileName, "a", "utf-8")
    for item in items:
        f.write('\t'.join(map(str, item))+"\n")
    f.close()

    return True


def sortItemsByPriority(items, parentColumn, priorityColumn):
    '''
    '''
    
    #add temporal column with id+priority, order by this and remove this
    for item in items:
        item.append(int(item[parentColumn]) + int(item[priorityColumn]))

    tmpCol = len(items[0])-1

    #sort by temporal col
    for i, item in enumerate(items):
        x = int(item[tmpCol])
        j = i 
        while j>0 and int(items[j-1][tmpCol]) > x:
            items[j] = items[j-1]
            j = j - 1
        items[j] = item
    
    #remove temporal col
    for i, item in enumerate(items):
        items[i] = item[0:tmpCol]

    return items


def sortItemsByParent(parentRootId, childColumn, parentColumn, 
    addDepthCol, items, depth):
    '''
    '''

    depth = depth + 1
    result = []

    for item in items:
        if int(item[parentColumn]) == int(parentRootId):

            #append parent to result
            if addDepthCol:
                item.append(depth)
            result.append(item)

            #explore childs
            childs = sortItemsByParent(item[childColumn], childColumn, parentColumn,
                addDepthCol, items, depth)
            
            if childs:
                for child in childs:
                    result.append(child)
    
    return result


def getHeaderRow(fileName):
    '''
    '''
    
    file = open(fileName, "r", encoding="utf8")
    return file.readline().replace("\n", "").split("\t")