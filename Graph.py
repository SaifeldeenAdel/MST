import random

class Graph:
  def __init__(self, v):
    # Creates a random weighted connected graph. 
    # Adjacency matrix representation, each value in the matrix is the weight of the edge.
    self.vertices = v
    self.graph = self.generateMatrix(v)

  def generateMatrix(self,v):
    # Initialize an empty adjacency matrix
    mat = [[0 for _ in range(v)] for _ in range(v)]
    
    vertices = list(range(v))
    random.shuffle(vertices)
    
    # Connect each vertex to the next vertex to ensure connectivity
    for i in range(v - 1):
        weight = random.randint(1, 10)  # Random weight for the edge
        mat[vertices[i]][vertices[i + 1]] = weight
        mat[vertices[i + 1]][vertices[i]] = weight

    # Connect the last vertex to the first vertex to close the cycle
    weight = random.randint(1, 10) 
    mat[vertices[-1]][vertices[0]] = weight
    mat[vertices[0]][vertices[-1]] = weight
    
    return mat
  
  def printGraph(self):
    print(self.graph)


def main():
  g = Graph(4)
  g.printGraph()

if __name__ == "__main__":
  main()
