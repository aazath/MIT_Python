def uniqueValues(aDict):
    '''
    aDict: a dictionary
    '''
    sortedList=[]
    outList=[]
    # Place values into a list
    #If there is only one of the values, then add to list. Otherwise, don't
    sortedList = list(aDict.values())
    #need a loop to remove all instances of a duplicate
    #the length of the list will go down every time I remove an element
    #for i in range(len(sortList)):
    #    while sortList[i] in sortList[i+1:len(sortList)]:
    #        sortList.remove(sortList[i])
    #for i in range(len(sortList)):
    for i in sortedList:
        if sortedList.count(i) > 1: #if the item i appears in the list  > 1
            while i in sortedList: #while that item is in the list
                sortedList.remove(i) #remove that item!
   
    for k, v in aDict.items():
        if v in sortedList:
            outList.append(k)
           
    outList.sort()
    return outList
   
testDict = {8: 3, 1: 3, 2: 2, 5:9}
print(str(uniqueValues(testDict)))