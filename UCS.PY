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

def findStartPos(maze):
    for row  in range(0,len(maze)):
        for col in range(0,len(maze[0])):
            if maze[row][col]  is 0:
                return (row,col)
    
    return (0,0)

def UCS():
    currentValue = 0
    heap = []
    (startrow,startcol) = findStartPos(maze)
    heapq.heappush(heap,(cost,currentValue,(startrow,startcol)))
    while(len(heap) > 0):
        
        currentPosition = heapq.heappop(heap)
        currentCost = currentPosition[0]
        row = currentPosition[2][0]
        col = currentPosition[2][1]

        if(col>0):
            if(maze[row][col-1] == EMPTY):
                currentValue = currentValue + 1
        
                maze[row][col-1] = currentValue
                heapq.heappush(heap,(currentCost + 2,currentValue,(row,col-1)))
                heapq.heapify(heap)
                
                
                #print(maze) 
            
            elif ( maze[row][col-1] == GOAL):
                currentValue = currentValue + 1
                maze[row][col] = currentValue
                return currentValue , currentCost

        if(row >0 ):
            if(maze[row-1][col] == EMPTY):
                currentValue = currentValue + 1
                maze[row-1][col] = currentValue
                heapq.heappush(heap,(currentCost + 1,currentValue,(row-1,col)))
                heapq.heapify(heap)
                #print(maze)
                
            elif ( maze[row-1][col] == GOAL):
                currentValue = currentValue + 1
                maze[row-1][col] = currentValue
                return currentValue , currentCost

        if (col < colLen-1):
            if(maze[row][col+1] == EMPTY):
                currentValue = currentValue + 1
                maze[row][col+1] = currentValue
                heapq.heappush(heap,(currentCost + 2,currentValue,(row,col+1)))
                heapq.heapify(heap)
                #print(maze)
                
            elif ( maze[row][col+1] == GOAL):
                currentValue = currentValue + 1
                maze[row][col+1] = currentValue
                return currentValue , currentCost

        if(row<rowLen-1):
            if(maze[row+1][col] == EMPTY):
                currentValue = currentValue + 1
                maze[row+1][col] = currentValue
                heapq.heappush(heap,(currentCost + 3,currentValue,(row+1,col)))
                heapq.heapify(heap)
                #print(maze)
                
            elif (maze[row+1][col] == GOAL):
                currentValue = currentValue + 1
                maze[row+1][col] = currentValue
                return currentValue , currentCost


def main():
    UCS()
    for items in maze:
                rowString =''
                for item in items:
                      rowString = rowString + str(item).zfill(2) + ' ' 

                print(rowString)
        
        
if __name__ == "__main__":
    main()         

    