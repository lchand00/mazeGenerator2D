class Graph:
    def _init_(self,num_nodes):
        self.num_node=num_nodes
        self.graph={}

class Maze:
    def _init_(self,size):
        self.size=size
        self.nodes=[]
        self.graph=Graph(size*size)

maze=Maze(5)
print("Welcome to 2D maze")