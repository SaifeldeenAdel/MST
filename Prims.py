from Graph import Graph
import sys

class Prims:
  def __init__(self) -> None:
    self.mst = {}

  def runPrims(self, graph):
    V = graph.vertices
    edges = graph.graph

    selectedNodes = [0] * V
    selectedNodes[0] = True
    numberOfEdges = 0

    while (numberOfEdges < V -1):
      mini = sys.maxsize
      x = 0
      y = 0
      for i in range(V):
        if selectedNodes[i]:
          for j in range(V):
            if ((not selectedNodes[j]) and edges[i][j]):
              if edges[i][j] < mini:
                mini = edges[i][j]
                x = i
                y = j

      self.mst[(x,y)]  = edges[x][y]
      selectedNodes[y] = True
      numberOfEdges += 1


  def printMST(self):
    print("Edge     :   Weight")
    alphadict = {0: 'a', 1:'b', 2:'c', 3:'d', 4:'e' , 5:'f', 6:'g', 7:'h', 8:'i'}
    for k,v in self.mst.items():
      print(f"{alphadict[k[0]]} - {alphadict[k[1]]}    :    {v}")

def main():
  g = Graph(9)
  g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
              [4, 0, 8, 0, 0, 0, 0, 11, 0],
              [0, 8, 0, 7, 0, 4, 0, 0, 2],
              [0, 0, 7, 0, 9, 14, 0, 0, 0],
              [0, 0, 0, 9, 0, 10, 0, 0, 0],
              [0, 0, 4, 14, 10, 0, 2, 0, 0],
              [0, 0, 0, 0, 0, 2, 0, 1, 6],
              [8, 11, 0, 0, 0, 0, 1, 0, 7],
              [0, 0, 2, 0, 0, 0, 6, 7, 0]]
  g.printGraph()

  p = Prims()
  p.runPrims(g)
  p.printMST()

if __name__ == "__main__":
  main()

