import heapq
from Graph import Graph


def dijkstra(self, start_vertex):
    v = self.vertices
    graph = self.graph
    distances = {vertex: float('inf') for vertex in range(v)}
    distances[start_vertex] = 0
    previous_nodes = {vertex: None for vertex in range(v)}
    pq = [(0, start_vertex)]


    while pq:
        current_distance, current_vertex = heapq.heappop(pq)


        for neighbor in range(v):
            if graph[current_vertex][neighbor] != 0:  # There is an edge
                distance = current_distance + graph[current_vertex][neighbor]

                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous_nodes[neighbor] = current_vertex
                    heapq.heappush(pq, (distance, neighbor))

    return distances, previous_nodes



def main():
  g = Graph(5)
  g.printGraph()



  d, p = dijkstra (g,0)
  print (d)
  print (p)

if __name__ == "__main__":
  main()
