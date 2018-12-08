import math
class Node:
    def __init__(self, coordinates):
        self.x = coordinates[0]
        self.y = coordinates[1]
        
class Edge:
    def __init__(self, start, stop):
        self.start = start
        self.stop  = stop

class Wireframe:
    def __init__(self, length):
        self.nodes = []
        self.edges = []
        self.length = length
        
    def addNodes(self, nodeList):
        for node in nodeList:
            self.nodes.append(Node(node))
            
    def addEdges(self, edgeList):
        for (start, stop) in edgeList:
            print(start,stop)
            self.edges.append(Edge(self.nodes[start], self.nodes[stop]))
            
    def outputNodes(self):
        print "\n --- Nodes --- "
        for i, node in enumerate(self.nodes):
            print " %d: (%.2f, %.2f)" % (i, node.x, node.y)
            
    def outputEdges(self):
        print "\n --- Edges --- "
        for i, edge in enumerate(self.edges):
            print " %d: (%.2f, %.2f)" % (i, edge.start.x, edge.start.y),
            print "to (%.2f, %.2f)" % (edge.stop.x,  edge.stop.y)
            
        
if __name__ == "__main__":
    cube_nodes = [(x,y) for x in (0,1) for y in (0,1)]
    print(cube_nodes)
    
    cube = Wireframe(100)
    cube.addNodes(cube_nodes)
    
    print([(n,n+1) for n in range(0,3,2)])
    print([(n,n+1) for n in range(0,3,2)])
    

    cube.addEdges([(n,n+1) for n in range(0,3,2)])
    cube.addEdges([(n,n+1) for n in range(0,3,2)])
    cube.horizontal_translate(0.5,100,(1,1))

    #cube.addEdges([(n,n+1) for n in range(0,8,2)])
    #cube.addEdges([(n,n+2) for n in (0,1,4,5)])

    #cube.outputNodes()
    #cube.outputEdges()