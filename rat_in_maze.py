res =[]
def solve(maze,x,y,m_x,m_y,path,visited):
    if x == m_x-1 and y== m_y -1:
        res.append(path[:])
        return
    direc = [('U', -1, 0), ('D', 1, 0), ('L', 0, -1), ('R', 0, 1)]
    for di,dx,dy in direc:
        nx = x+dx
        ny = y+dy
        if  nx>=0 and nx<m_x and ny>=0 and ny<m_y and maze[nx][ny] ==1 and (nx,ny) not in visited:
            visited.add((nx,ny))
            solve(maze,nx,ny,m_x,m_y,path+di,visited)
            visited.remove((nx,ny))
            
if __name__ == "__main__":
    maze = [[1, 0, 0, 0],
        [1, 1, 0, 1],
        [0, 1, 0, 0],
        [1, 1, 1, 1]]
    visited = set()
    m_x = len(maze)
    m_y = len(maze[0])
    path =""
    if maze[0][0] == 1:
        visited.add((0,0))
        solve(maze,0,0,m_x,m_y,path,visited)
    print(res)
