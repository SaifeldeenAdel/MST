from Graph import Graph
import sys
class Prims:
  def __init__(self) -> None:
    self.mst = {}

  def runPrims(self, graph):
    V = graph.vertices
    edges = graph.graph

    selectedNodes = [False] * V
    selectedNodes[0] = True
    numberOfEdges = 0

    while numberOfEdges < V -1:
      mini = sys.maxsize
      selected = 0
      for i in range(V):
        if selectedNodes[i]:
          for j in range(V):
            if ((not selectedNodes[j]) and edges[i][j]):
              if edges[i][j] < mini:
                mini = edges[i][j]
                self.mst[(i,j)]  = edges[i][j]
                selected = j

      selectedNodes[selected] = True
      numberOfEdges += 1


  def printMST(self):
    print("Edge     :   Weight")
    for k,v in self.mst.items():
      print(f"{k[0]} - {k[1]}    :    {v}")

def main():
  g = Graph(5)
  g.printGraph()

  p = Prims()
  p.runPrims(g)
  p.printMST()

if __name__ == "__main__":
  main()

