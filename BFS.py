import queue

maze = [
        ['[]','[]','[]','[]','[]','[]','[]','[]','[]','[]','[]'],
        ['[]','[]','[]','[]','[]','[]','[]','[]','[]','[]','[]'],
        ['[]','[]','[]','[]','##','##','##','##','[]','[]','[]'],
        ['[]','[]','*','[]','##','[]','[]','##','[]','[]','[]'],
        ['[]','[]','[]','##','##',00,'[]','##','[]','[]','[]'],
        ['[]','[]','[]','[]','[]','[]','##','##','[]','[]','[]'],
        ['[]','[]','[]','[]','[]','[]','[]','[]','[]','[]','[]'],
        ['[]','[]','[]','[]','[]','[]','[]','[]','[]','[]','[]']
    ]

    
rowLen = len(maze)
colLen= len(maze[0])
EMPTY = '[]'
GOAL = '*'
frontier = queue.Queue()

def findStartPos(maze):
    for row  in range(0,len(maze)):
        for col in range(0,len(maze[0])):
            if maze[row][col]  is 0:
                return (row,col)
    
    return (0,0) 

def BFS():
    currentValue = 0
    (startrow,startcol) = findStartPos(maze)
    frontier.put([startrow,startcol])
    while frontier.not_empty:
        
        currentPosition =   frontier.get()
        row = currentPosition[0]
        col = currentPosition[1]
        
        if(col>0):
            if(maze[row][col-1] == EMPTY):
                currentValue = currentValue + 1
                maze[row][col-1] = currentValue
                frontier.put([row,col-1])
            
            elif ( maze[row][col-1] == GOAL):
                currentValue = currentValue + 1
                maze[row][col] = currentValue
                return currentValue

        if(row >0 ):
            if(maze[row-1][col] == EMPTY):
                currentValue = currentValue + 1
                maze[row-1][col] = currentValue
                frontier.put([row-1,col])
                
            elif ( maze[row-1][col] == GOAL):
                currentValue = currentValue + 1
                maze[row-1][col] = currentValue
                return currentValue

        if (col < colLen-1):
            if(maze[row][col+1] == EMPTY):
                currentValue = currentValue + 1
                maze[row][col+1] = currentValue
                frontier.put([row,col+1])
                
            elif ( maze[row][col+1] == GOAL):
                currentValue = currentValue + 1
                maze[row][col+1] = currentValue
                return currentValue

        if(row<rowLen-1):
            if(maze[row+1][col] == EMPTY):
                currentValue = currentValue + 1
                maze[row+1][col] = currentValue
                frontier.put([row+1,col])
                
            elif (maze[row+1][col] == GOAL):
                currentValue = currentValue + 1
                maze[row+1][col] = currentValue
                return currentValue


def main():
    BFS()
    for items in maze:
                rowString =''
                for item in items:
                      rowString = rowString + str(item).zfill(2) + ' ' 

                print(rowString)
        
if __name__ == "__main__":
    main()    
        
