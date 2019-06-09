import stack
maze = [
    ["[]","[]","[]","[]","[]","*"],
    ["[]","##","##","##","##","[]"],
    ["[]","[]","[]","[]","##","[]"],
    ["[]","[]",0,"[]","##","[]"],
    ["[]","[]","[]","[]","[]","[]"],
    ["[]","[]","[]","[]","[]","[]"]

]   



"""maze = [
        ['[]','[]','[]','[]','[]','[]','[]','[]','[]','[]',"*"],
        ['[]','[]','[]','[]','[]','[]','[]','[]','[]','[]','[]'],
        ['[]','[]','[]','[]','##','##','##','##','[]','[]','[]'],
        ['[]','[]','[]','[]','##','[]','[]','##','[]','[]','[]'],
        ['[]','[]','[]','##','##',00,'[]','##','[]','[]','[]'],
        ['[]','[]','[]','[]','[]','[]','##','##','[]','[]','[]'],
        ['[]','[]','[]','[]','[]','[]','[]','[]','[]','[]','[]'],
        ['[]','[]','[]','[]','[]','[]','[]','[]','[]','[]','[]']
    ]"""

    
rowLen = len(maze)
colLen= len(maze[0])
EMPTY = '[]'
BLOCKED = '##'
GOAL = "*"
startrow = 3
startcol = 2



class Stack:
     def __init__(self):
         self.items = []

     def isEmpty(self):
         return self.items == []
         
     def size(self):
         return len(self.items)    

     def push(self, item):
         self.items.append(item)
         

     def pop(self):
         return self.items.pop()

def IDFS(limit, currentPosition):
    currentValue = 0
    currentDepth = 0
    frontier = Stack()
    frontier.push([(startrow,startcol),currentDepth])
    while (frontier.size()) is not 0:
      
        currentPosition =   frontier.pop()
        row = currentPosition[0][0]
        col = currentPosition[0][1]
        currentDepth = currentPosition[1]
        if(currentDepth == limit):
            continue

        if(col>0):
            if(maze[row][col-1] == EMPTY):
                currentValue = currentValue + 1
                maze[row][col-1] = currentValue
                frontier.push([(row,col-1),currentDepth+1])
            
            elif ( maze[row][col-1] == GOAL):
                currentValue = currentValue + 1
                maze[row][col] = currentValue
                return (currentValue,True)
            elif ( maze[row][col-1] != BLOCKED):
                frontier.push([(row,col-1),currentDepth+1])

        if(row >0 ):
            if(maze[row-1][col] == EMPTY):
                currentValue = currentValue + 1
                maze[row-1][col] = currentValue
                frontier.push([(row-1,col),currentDepth+1])           
            elif ( maze[row-1][col] == GOAL):
                currentValue = currentValue + 1
                maze[row-1][col] = currentValue
                return (currentValue,True)
            elif ( maze[row-1][col] != BLOCKED):
                    frontier.push([(row-1,col),currentDepth+1])

        if (col < colLen-1):
            if(maze[row][col+1] == EMPTY):
                currentValue = currentValue + 1
                maze[row][col+1] = currentValue
                frontier.push([(row,col+1),currentDepth+1])
            elif ( maze[row][col+1] == GOAL):
                currentValue = currentValue + 1
                maze[row][col+1] = currentValue
                return (currentValue,True)
            elif ( maze[row][col+1] != BLOCKED):
                frontier.push([(row,col+1),currentDepth+1])

        if(row<rowLen-1):
            if(maze[row+1][col] == EMPTY):
                currentValue = currentValue + 1
                maze[row+1][col] = currentValue
                frontier.push([(row+1,col),currentDepth+1])
            elif (maze[row+1][col] == GOAL):
                currentValue = currentValue + 1
                maze[row+1][col] = currentValue
                return (currentValue,True)
            elif ( maze[row+1][col] != BLOCKED):
                frontier.push([(row+1,col),currentDepth+1])
    return (currentPosition,False) 


def main():
    currentPosition =0  
    for limit in range(1,(rowLen*colLen)):
        (currentPosition,ret) = IDFS(limit,currentPosition)
        if(ret):
            for items in maze:
                rowString =''
                for item in items:
                      rowString = rowString + str(item).zfill(2) + ' ' 

                print(rowString)

            return

        
        
if __name__ == "__main__":
    main()    
        


   
        
