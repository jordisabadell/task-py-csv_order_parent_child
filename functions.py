import os
import codecs

def loadFile(fileName):

    #read file
    file = open(fileName, "r", encoding="utf8")

    #get header from first line
    header = file.readline().replace("\n", "").split("\t")

    #iterate lines
    items = []
    for i, line in enumerate(file):
        if i>0:
            if line:
                #convert line to dictionary
                item = {}
                values = line.replace("\n", "").split("\t")
                for j, value in enumerate(values):
                    item[header[j].strip()] = value.strip()
                
                items.append(item)
    
    return header, items

def sortItems(id, fieldNameId, fieldNameParentId, priorityColumnName, items, depth):

    result = []

    print("Analysing "+ fieldNameId +" = "+ str(id) +" / depth="+ str(depth) +"...")
    for item in items:
        if int(item[fieldNameParentId]) == int(id):
            
            print(fieldNameParentId +" = "+ str(item[fieldNameId]) +"...")            
            
            #append parent to result
            result.append(item)

            #explore childs
            childs = sortItems(item[fieldNameId], fieldNameId, fieldNameParentId, priorityColumnName, items, depth+1)
            if childs:
                for child in childs:
                    result.append(child)

    return result

def saveFile(fileName, items):

    #remove file if exists
    if os.path.exists(fileName):
        os.remove(fileName)

    #wirte output file
    f = codecs.open(fileName, "a", "utf-8")
    f.write('\n'.join(map(str, items)))
    f.close()

    return True
