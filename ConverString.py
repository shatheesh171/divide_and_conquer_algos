def findMinOperation(s1,s2,index1,index2):
    if index1==len(s1):
        return len(s2)-index2
    if index2==len(s2):
        return len(s1)-index1
    if s1[index1]==s2[index2]:
        return findMinOperation(s1,s2,index1+1,index2+1)

    else:
        insertOp=1+findMinOperation(s1,s2,index1+1,index2)
        deleteOp=1+findMinOperation(s1,s2,index1,index2+1)
        replaceOp=1+findMinOperation(s1,s2,index1+1,index2+1)
        return min(insertOp,deleteOp,replaceOp)

print(findMinOperation("table","tbrles",0,0))
