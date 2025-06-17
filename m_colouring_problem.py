
def isSafe(graph,col,m,n,node,colour):
     for i in range(n):
          if (graph[node][i] ==1):
               if col[i] == colour:
                   return False
     return True
             
             
     

def solve(graph,col,m,n,node):
     if  node == n:
          return True
     for colour in range(1,m+1):
          if isSafe(graph,col,m,n,node,colour):
               col[node] =colour
               if (solve(graph,col,m,n,node+1)):
                   return True
               col[node]=0
     return False


if __name__ == "__main__": 
     graph = [[0, 1, 1, 1],
         [1, 0, 1, 0],
         [1, 1, 0, 1],
         [1, 0, 1, 0]]
     m = 3
     n = 4
     col =[0]*n
     print(solve(graph,col,m,n,0))

    
