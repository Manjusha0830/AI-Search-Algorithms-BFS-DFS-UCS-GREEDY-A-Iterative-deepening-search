import heapq


maze = [
        ['[]','[]','[]','[]','[]','[]','[]','[]','[]','[]','*'],
        ['[]','[]','[]','[]','[]','[]','[]','[]','[]','[]','[]'],
        ['[]','[]','[]','[]','##','##','##','##','[]','[]','[]'],
        ['[]','[]','[]','[]','##','[]','[]','##','[]','[]','[]'],
        ['[]','[]','[]','##','##',00,'[]','##','[]','[]','[]'],
        ['[]','[]','[]','[]','[]','[]','##','##','[]','[]','[]'],
        ['[]','[]','[]','[]','[]','[]','[]','[]','[]','[]','[]'],
        ['[]','[]','[]','[]','[]','[]','[]','[]','[]','[]','[]']
    ]

rowLen = len(maze)
colLen= len(maze[0])
EMPTY = '[]'
GOAL = '*'
cost = 0
eastCost =2
westCost = 2
northCost = 1
southCost = 3

def findStartPos(maze):
    for row  in range(0,len(maze)):
        for col in range(0,len(maze[0])):
            if maze[row][col]  is 0:
                return (row,col)
    
    return (0,0) 


def findGoalPos(maze):
    for row  in range(0,len(maze)):
        for col in range(0,len(maze[0])):
            if maze[row][col]  is GOAL:
                return (row,col)
    
    return (0,0)

def GreedySearch():
    currentValue = 0
    heap = []
    (startrow,startcol) = findStartPos(maze)
    (goalrow,goalcol) = findGoalPos(maze)
    heapq.heappush(heap,(cost,currentValue,(startrow,startcol)))
    while(len(heap) > 0):
        
        currentPosition = heapq.heappop(heap)
        estimatedCost = currentPosition[0]
        row = currentPosition[2][0]
        col = currentPosition[2][1]

        if(col>0):
            if(maze[row][col-1] == EMPTY):
                currentValue = currentValue + 1
                maze[row][col-1] = currentValue
                heapq.heappush(heap,(estimateCost((goalrow - row),(goalcol - (col-1))),
                                        currentValue,(row,col-1)))
                heapq.heapify(heap)
                
                
                #print(maze) 
            
            elif ( maze[row][col-1] == GOAL):
                currentValue = currentValue + 1
                maze[row][col] = currentValue
                return currentValue , estimatedCost

        if(row >0 ):
            if(maze[row-1][col] == EMPTY):
                currentValue = currentValue + 1
                maze[row-1][col] = currentValue
                heapq.heappush(heap,(estimateCost((goalrow - (row-1)),(goalcol - col)),
                                        currentValue,(row-1,col)))
        
                heapq.heapify(heap)
                #print(maze)
                
            elif ( maze[row-1][col] == GOAL):
                currentValue = currentValue + 1
                maze[row-1][col] = currentValue
                return currentValue , estimatedCost

        if (col < colLen-1):
            if(maze[row][col+1] == EMPTY):
                currentValue = currentValue + 1
                maze[row][col+1] = currentValue
                heapq.heappush(heap,(estimateCost((goalrow - row),(goalcol - (col+1))),
                                        currentValue,(row,col+1)))
                heapq.heapify(heap)
                #print(maze)
                
            elif ( maze[row][col+1] == GOAL):
                currentValue = currentValue + 1
                maze[row][col+1] = currentValue
                return currentValue , estimatedCost

        if(row<rowLen-1):
            if(maze[row+1][col] == EMPTY):
                currentValue = currentValue + 1
                maze[row+1][col] = currentValue
                heapq.heappush(heap,(estimateCost((goalrow - (row+1)),(goalcol - col)),
                                        currentValue,(row+1,col)))
                heapq.heapify(heap)
                #print(maze)
                
            elif (maze[row+1][col] == GOAL):
                currentValue = currentValue + 1
                maze[row+1][col] = currentValue
                return currentValue , estimatedCost

def estimateCost(row, col):
    if(row <= 0):
        rowCost = (abs(row) * northCost)
    else:
        rowCost = (row * southCost) 
    if(col <= 0):
        colCost = (abs(col) * westCost)
    else:
        colCost = (col * eastCost)
    return (rowCost + colCost)

def main():
    GreedySearch()
    for items in maze:
                rowString =''
                for item in items:
                      rowString = rowString + str(item).zfill(2) + ' ' 

                print(rowString)
        
        
if __name__ == "__main__":
    main()         

    