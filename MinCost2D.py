def findMinCost(twoDArray,row,col):
    if row==-1 or col==-1:
        return float('inf')
    elif row==0 and col==0:
        return twoDArray[0][0]
    else:
        op1=findMinCost(twoDArray,row-1,col)
        op2=findMinCost(twoDArray,row,col-1)
        return twoDArray[row][col]+min(op1,op2)

twoDList=[[4,7,8,6,4],
        [6,7,3,9,2],
        [3,8,2,1,4],
        [7,1,7,3,7],
        [2,9,8,9,3]
]
print(findMinCost(twoDList,4,4))