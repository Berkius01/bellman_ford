class Graph:
 
    def __init__(self, vertices):
        self.V = vertices 
        self.graph = []
 
    # graph içine edge eklem
    def addEdge(self, u, v, w):
        self.graph.append([u, v, w])
         
    # uzaklığı bastırma
    def printArr(self, dist):
        print("Vertex Distance from Source")
        for i in range(self.V):
            print("{0}\t\t{1}".format(i, dist[i]))
     
  
    def BellmanFord(self, src):
 
        # bütün uzaklıkları sonsuz yap
        dist = [float("Inf")] * self.V
        dist[src] = 0
 
 
       #bir vertex en fazla v- 1 tane bağlantıya sahpi olabilir
        for _ in range(self.V - 1):
            #vertexlerin value değerini güncelle
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        dist[v] = dist[u] + w
 
        # negatif cycle kısmı
        for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                        print("negatif cycle var")
                        return
                         
        
        self.printArr(dist)
 
g = Graph(7)
g.addEdge(0, 1, -1)
g.addEdge(1,2,3)
g.addEdge(1,5,2)
g.addEdge(2,0,-1)
g.addEdge(2,3,1)
g.addEdge(3,4,5)
g.addEdge(4,0,-2)
g.addEdge(5,6,1)
 
g.BellmanFord(1)