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
            if maze[row][col]  is 00:
                return (row,col)
    
    return (0,0) 


def findGoalPos(maze):
    for row  in range(0,len(maze)):
        for col in range(0,len(maze[0])):
            if maze[row][col]  is GOAL:
                return (row,col)
    
    return (0,0)     

def AstarSearch():
    currentValue = 0
    heap = []
    (startrow,startcol) = findStartPos(maze)
    (goalrow,goalcol) = findGoalPos(maze)
    costtoNode = 0
    costtoGoal = 0
    totalCost = 0
    
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
                costtoNode = calculateCost((row - startrow),((col-1) - startcol))
                costtoGoal = calculateCost((goalrow - row),(goalcol - (col-1)))
                totalCost = costtoNode + costtoGoal
                heapq.heappush(heap,(totalCost,
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
                costtoNode = calculateCost(((row-1) - startrow),(col - startcol))
                costtoGoal = calculateCost((goalrow - (row-1)),(goalcol - col))
                totalCost = costtoNode + costtoGoal
                heapq.heappush(heap,(totalCost,
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
                costtoNode = calculateCost((row - startrow),((col+1) - startcol))
                costtoGoal = calculateCost((goalrow - row),(goalcol - (col+1)))
                totalCost = costtoNode + costtoGoal
                heapq.heappush(heap,(totalCost,
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
                costtoNode = calculateCost(((row+1) - startrow),(col - startcol))
                costtoGoal = calculateCost((goalrow - (row+1)),(goalcol - col))
                totalCost = costtoNode + costtoGoal
                heapq.heappush(heap,(totalCost,
                                        currentValue,(row+1,col)))
                heapq.heapify(heap)
                #print(maze)
                
            elif (maze[row+1][col] == GOAL):
                currentValue = currentValue + 1
                maze[row+1][col] = currentValue
                return currentValue , estimatedCost

def calculateCost(row, col):
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
    AstarSearch()
    for items in maze:
                rowString =''
                for item in items:
                      rowString = rowString + str(item).zfill(2) + ' ' 

                print(rowString)
        
        
if __name__ == "__main__":
    main()         

    