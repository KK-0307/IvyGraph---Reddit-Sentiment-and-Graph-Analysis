import heapq


class ivyGraph:
    
    def __init__(self):
        self.matrix = []
        self.vertex_names = []

    # add a vertex to the graph, the default edge weight is 0
    def add_vertex(self, vertex_name):
        self.vertex_names.append(vertex_name)
        for row in self.matrix:
            row.append(0)
        self.matrix.append([0] * len(self.matrix))

    # add an adge between two vertices with a given weight
    def add_positive_edge(self, from_vertex, to_vertex, weight):
        from_index = self.vertex_names.index(from_vertex)
        to_index = self.vertex_names.index(to_vertex)
        if from_index >= len(self.matrix) or to_index >= len(self.matrix):
            print("Vertex index out of range.")
            return
        self.matrix[from_index][to_index] = weight
        self.matrix[to_index][from_index] = weight



    # given two classes, if people like class A also like class B, their relevance is marked 1;
    # given two classes, calculate the shortest distance as the relevance
    def get_relevance(graph, start_vertex, end_vertex):
        if start_vertex not in graph.vertex_names or end_vertex not in graph.vertex_names:
            print("Start or end vertex not found.")
            return None

        # Initialize distances to infinity for all vertices except the start vertex
        distances = {vertex: float('inf') for vertex in graph.vertex_names}
        distances[start_vertex] = 0

        # Priority queue to store vertices with their current distances from the start vertex
        priority_queue = [(0, start_vertex)]  # (distance, vertex)

        while priority_queue:
            current_distance, current_vertex = heapq.heappop(priority_queue)

            # If the current vertex is the end vertex, return its distance
            if current_vertex == end_vertex:
                return current_distance

            # Otherwise, explore neighbors of the current vertex
            current_index = graph.vertex_names.index(current_vertex)
            for i, weight in enumerate(graph.matrix[current_index]):
                if weight == 0:  # Skip edges with weight 0 
                    continue
                neighbor_vertex = graph.vertex_names[i]
                new_distance = current_distance + weight
                if new_distance < distances[neighbor_vertex]:
                    distances[neighbor_vertex] = new_distance
                    heapq.heappush(priority_queue, (new_distance, neighbor_vertex))

        # If no path is found
        print("No path found between the vertices.")
        return None


    
    # display the graph
    def display(self):
        print("   ", end="")
        for name in self.vertex_names:
            print(name, end=" ")
        print()
        for i, row in enumerate(self.matrix):
            print(self.vertex_names[i], end=": ")
            for val in row:
                print(val, end=" ")
            print()
