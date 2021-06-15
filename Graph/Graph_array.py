class Graph():

    def __init__(self):
        self.n = int(input("Enter the no of node in the graph : ").strip())
        self.a = [[0 for i in range(self.n)] for j in range(self.n)]

    def display(self):
        print(self.a)

    def DFS(self):
        
        visit=[0 for i in range(self.n)]
        pos=int(input("Enter the cell for where searching must start (default = 0) : "))

        j=0
        def dfs(pos,j):
            visit[j]=pos
            j+=1
            for i in range(self.n):
                if self.a[pos][i]==1 and visit[i]==0:
                    dfs(i,j)

        dfs(pos,j)
        print(visit)


    def BFS(self):
        
        visit=[0 for i in range(self.n)]
        pos=int(input("Enter the cell for where searching must start (default = 0) : "))

        queue=[]

        queue.append(pos)
        visit[pos]=1
        
        def bfs(pos):
            if(len(queue)>0):
                i = queue.pop(0)
                visit[i]=1
                for i in range(self.n):
                    if visit[i]==0 and self.a[pos][i]==1:
                        queue.append(i)
                        visit[i]=1

        bfs(pos)
  


def main():
    
    my_graph = Graph()

    print("Before : ",my_graph.a)

    while(True):
        i,j=input("Enter the from,to cell of the graph : ").strip().split(",")
        i,j=int(i),int(j)
        if i == j and i== -1:
            break
        else:
            my_graph.a[i][j]=1
    
    while(True):
        
        ch = int(input("1:Display\n2:DFS\n3:BFS\nEnter your option : "))
        
        if ch == 1:
            my_graph.display()
        
        elif ch ==2:
            my_graph.DFS()
        
        elif ch ==3:
            my_graph.BFS()
        
        else:
            print("Wrong Option ")
            break



if __name__=="__main__":
    main()