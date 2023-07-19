
from copy import deepcopy
from random import randint


class VertexException(Exception):
    pass


class EdgeException(Exception):
    pass

#
# class Graph:
#     def __init__(self, nr_of_vertices=0, nr_of_edges=0):
#         self.__vertices = set()  # because we cannot have multiple occurrences of the same element
#         self.__outbounds = dict()
#         self.__inbounds = dict()
#         self.__cost = dict()
#
#     def add_vertex(self, vertex_to_be_added):
#         """
#         Adds a vertex to the graph
#         :param vertex_to_be_added: the vertex to be added
#         :return: nothing
#         """
#         if vertex_to_be_added in self.__vertices:
#             raise VertexException("The vertex is already in the graph!")
#         self.__vertices.add(vertex_to_be_added)
#         self.__outbounds[vertex_to_be_added] = set()
#         self.__inbounds[vertex_to_be_added] = set()
#
#     def remove_vertex(self, vertex_to_be_removed):
#         """
#         Removes a vertex from the graph
#         :param vertex_to_be_removed: the vertex to be removed
#         :return: nothing
#         """
#         if vertex_to_be_removed not in self.__vertices:
#             raise VertexException("The vertex is not in the graph!")
#         for vertex in self.__vertices:
#             if (vertex, vertex_to_be_removed) in self.__cost:
#                 del self.__cost[(vertex, vertex_to_be_removed)]
#                 # deleting the vertex from the inbounds and outbounds of the other vertices
#                 self.__outbounds[vertex].remove(vertex_to_be_removed)
#             if (vertex_to_be_removed, vertex) in self.__cost:
#                 del self.__cost[(vertex_to_be_removed, vertex)]
#                 self.__inbounds[vertex].remove(vertex_to_be_removed)
#
#         del self.__outbounds[vertex_to_be_removed]
#         del self.__inbounds[vertex_to_be_removed]
#         self.__vertices.remove(vertex_to_be_removed)
#
#     def add_edge(self, vertex_from, vertex_to, edge_cost):
#         """
#         Adds an edge to the graph
#         :param vertex_from: the starting vertex of the edge
#         :param vertex_to: the ending vertex of the edge
#         :param edge_cost: the cost of the edge
#         :return: nothing
#         """
#         if vertex_from not in self.__vertices or vertex_to not in self.__vertices:
#             raise VertexException("The vertices are not in the graph!")
#         if (vertex_from, vertex_to) in self.__cost:
#             # print((vertex_from, vertex_to))
#             raise EdgeException("The edge is already in the graph!")
#
#         self.__outbounds[vertex_from].add(vertex_to)
#         self.__inbounds[vertex_to].add(vertex_from)
#         self.__cost[(vertex_from, vertex_to)] = edge_cost
#
#     def remove_edge(self, vertex_from, vertex_to):
#         """
#         Removes an edge from the graph
#         :param vertex_from: the starting vertex of the edge
#         :param vertex_to: the ending vertex of the edge
#         :return: nothing
#         """
#         if (vertex_from, vertex_to) not in self.__cost:
#             raise EdgeException("The edge is not in the graph!")
#
#         self.__outbounds[vertex_from].remove(vertex_to)
#         self.__inbounds[vertex_to].remove(vertex_from)
#         del self.__cost[(vertex_from, vertex_to)]
#
#     def get_nr_of_vertices(self):
#         """
#         Returns the number of vertices in the graph
#         """
#         return len(self.__vertices)
#
#     def get_nr_of_edges(self):
#         """
#         Returns the number of edges in the graph
#         """
#         return len(self.__cost)
#
#     def vertices_iterator(self):
#         """
#         Returns an iterator for the vertices in the graph
#         """
#         for vertex in self.__vertices:
#             yield vertex
#
#     def edges_iterator(self):
#         """
#         Returns an iterator for the edges in the graph
#         """
#         for edge in self.__cost:
#             yield edge  # TODO - change it if is needed
#
#     def inbound_iterator(self, vertex_to):
#         """
#         Returns an iterator for the vertices that have an edge that ends in vertex_to
#         """
#         for vertex_from in self.__inbounds[vertex_to]:
#             yield vertex_from
#
#     def outbound_iterator(self, vertex_from):
#         """
#         Returns an iterator for the vertices that have an edge that starts from vertex_from
#         """
#         for vertex_to in self.__outbounds[vertex_from]:
#             yield vertex_to
#
#     def is_edge(self, vertex_from, vertex_to):
#         """
#         Returns True if the edge (vertex_from, vertex_to) is in the graph, False otherwise
#         """
#         return (vertex_from, vertex_to) in self.__cost
#
#     def is_vertex(self, vertex_to_be_checked):
#         return vertex_to_be_checked in self.__vertices
#
#     def get_in_degree(self, vertex_to):
#         """
#         Returns the number of edges that end in vertex_to
#         """
#         return len(self.__inbounds[vertex_to])
#
#     def get_out_degree(self, vertex_from):
#         """
#         Returns the number of edges that start from vertex_from
#         """
#         return len(self.__outbounds[vertex_from])
#
#     def set_cost(self, vertex_from, vertex_to, new_cost):
#         if (vertex_from, vertex_to) not in self.__cost:
#             raise EdgeException("The edge is not in the graph!")
#         self.__cost[(vertex_from, vertex_to)] = new_cost
#
#     def get_cost(self, vertex_from, vertex_to):
#         if (vertex_from, vertex_to) not in self.__cost:
#             print((vertex_from, vertex_to))
#             raise EdgeException("The edge is not in the graph!")
#         return self.__cost[(vertex_from, vertex_to)]
#
#     def copy_graph(self, graph_to_be_copied):
#         """
#         Returns a copy of the graph
#         :return:
#         """
#         for vertex in graph_to_be_copied.vertices_iterator():
#             self.add_vertex(vertex)
#
#         for edge in graph_to_be_copied.edges_iterator():
#             self.add_edge(edge[0], edge[1], graph_to_be_copied.get_cost(edge[0], edge[1]))
#
#
#     # def generate_random_graph(self, nr_of_vertices, nr_of_edges):
#     #     """
#     #     Generates a random graph
#     #     :param nr_of_vertices: the number of vertices
#     #     :param nr_of_edges: the number of edges
#     #     :return: nothing
#     #     """
#     #     # adding the vertices to the graph
#     #     for vertex in range(nr_of_vertices):
#     #         self.add_vertex(vertex)
#     #
#     #     # adding the edges randomly to the graph
#     #     for edge in range(nr_of_edges):
#     #         vertex1 = randint(0, nr_of_vertices-1)
#     #         vertex2 = randint(0, nr_of_vertices-1)
#     #         while (vertex1, vertex2) in self.__cost:
#     #             vertex1 = randint(0, nr_of_vertices-1)
#     #             vertex2 = randint(0, nr_of_vertices-1)
#     #         cost = randint(-1000000, 1000000)
#     #         self.add_edge(vertex1, vertex2, cost)
#
#     def read_graph_from_file(self, file_descriptor):
#         # graph_read_from_file = Graph()
#         with open(file_descriptor, "r") as fin:
#             for line in fin:
#                 line = line.strip()
#                 if line == "" or line[0] == "#":  # empty line or comment
#                     continue
#
#                 line = line.split()
#
#                 # if the line has only one element, it is a vertex that has no edges
#                 if len(line) == 1:
#                     self.add_vertex(int(line[0]))
#
#                 # if the line has three elements, it is an edge between two vertices with a given cost
#                 if len(line) == 3:
#                     # adding the vertices to the graph
#                     try:
#                         self.add_vertex(int(line[0]))
#                     except VertexException:  # if the vertex is already in the graph
#                         pass
#                     try:
#                         self.add_vertex(int(line[1]))
#                     except VertexException:  # if the vertex is already in the graph
#                         pass
#
#                     # adding the edge to the graph with the given cost
#                     try:
#                         self.add_edge(int(line[0]), int(line[1]), int(line[2]))
#                     except EdgeException:  # if the edge is already in the graph
#                         self.set_cost(int(line[0]), int(line[1]), int(line[2]))
#
#     def save_graph_to_file(self, file_descriptor):
#         with open(file_descriptor, "w") as fout:
#             for vertex in self.vertices_iterator():
#                 if self.get_out_degree(vertex) == 0 and self.get_in_degree(vertex) == 0:
#                     fout.write(str(vertex) + "\n"   )
#                 for neighbour in self.outbound_iterator(vertex):
#                     fout.write(str(vertex) + " " + str(neighbour) + " " + str(
#                         self.get_cost(vertex, neighbour)) + "\n")
#
# def generate_random_graph(nr_of_vertices, nr_of_edges):
#     generated_graph = Graph()
#     """
#     Generates a random graph
#     :param nr_of_vertices: the number of vertices
#     :param nr_of_edges: the number of edges
#     :return: nothing
#     """
#     # adding the vertices to the graph
#     for vertex in range(nr_of_vertices):
#         generated_graph.add_vertex(vertex)
#
#     # adding the edges randomly to the graph
#     for edge in range(nr_of_edges):
#         vertex1 = randint(0, nr_of_vertices-1)
#         vertex2 = randint(0, nr_of_vertices-1)
#         while generated_graph.is_edge(vertex1, vertex2):
#             vertex1 = randint(0, nr_of_vertices-1)
#             vertex2 = randint(0, nr_of_vertices-1)
#         cost = randint(-1000000, 1000000)
#         generated_graph.add_edge(vertex1, vertex2, cost)
#
#     return generated_graph
#

# having the model from above directed graph, now implement a class for an undirected graph

def generate_random_graph(nr_of_vertices, nr_of_edges):
    generated_graph = UndirectedGraph()
    """
    Generates a random graph
    :param nr_of_vertices: the number of vertices
    :param nr_of_edges: the number of edges
    :return: nothing
    """
    # adding the vertices to the graph
    for vertex in range(nr_of_vertices):
        generated_graph.add_vertex(vertex)

    # adding the edges randomly to the graph
    for edge in range(nr_of_edges):
        vertex1 = randint(0, nr_of_vertices-1)
        vertex2 = randint(0, nr_of_vertices-1)
        while generated_graph.is_edge(vertex1, vertex2):
            vertex1 = randint(0, nr_of_vertices-1)
            vertex2 = randint(0, nr_of_vertices-1)
        generated_graph.add_edge(vertex1, vertex2)
    return generated_graph


class UndirectedGraph:
    def __init__(self):
        """
        Creates an empty undirected graph
        """
        self.__vertices = []
        self.__adj = dict()
        self.__nr_of_edges = 0

        self.__visited = []

    def add_vertex(self, vertex):
        """
        Adds a new vertex to the graph
        :param vertex: the vertex to be added
        :return: nothing
        """
        if vertex in self.__vertices:
            raise VertexException("The vertex already exists!")
        self.__vertices.append(vertex)
        self.__adj[vertex] = []

    def remove_vertex(self, vertex):
        """
        Removes a vertex from the graph
        :param vertex: the vertex to be removed
        :return: nothing
        """
        if vertex not in self.__vertices:
            raise VertexException("The vertex does not exist!")
        self.__vertices.remove(vertex)
        for neighbour in self.__adj[vertex]:
            self.__adj[neighbour].remove(vertex)
        del self.__adj[vertex]

    def add_edge(self, vertex1, vertex2):
        """
        Adds a new edge to the graph
        :param vertex1: the first vertex
        :param vertex2: the second vertex
        :return: nothing
        """
        if vertex1 not in self.__vertices or vertex2 not in self.__vertices:
            raise VertexException("The vertex does not exist!")
        if vertex2 in self.__adj[vertex1]:
            raise EdgeException("The edge already exists!")
        self.__adj[vertex1].append(vertex2)
        self.__adj[vertex2].append(vertex1)
        self.__nr_of_edges += 1

    def remove_edge(self, vertex1, vertex2):
        """
        Removes an edge from the graph
        :param vertex1: the first vertex
        :param vertex2: the second vertex
        :return: nothing
        """
        if vertex1 not in self.__vertices or vertex2 not in self.__vertices:
            raise VertexException("The vertex does not exist!")
        if vertex2 not in self.__adj[vertex1]:
            raise EdgeException("The edge does not exist!")
        self.__adj[vertex1].remove(vertex2)
        self.__adj[vertex2].remove(vertex1)
        self.__nr_of_edges -= 1

    def get_number_of_vertices(self):
        """
        Returns the number of vertices in the graph
        :return: the number of vertices
        """
        return len(self.__vertices)

    def get_number_of_edges(self):
        """
        Returns the number of edges in the graph
        :return: the number of edges
        """
        return self.__nr_of_edges

    def is_edge(self, vertex1, vertex2):
        """
        Checks if there is an edge between two vertices
        :param vertex1: the first vertex
        :param vertex2: the second vertex
        :return: True if there is an edge between the two vertices, False otherwise
        """
        if vertex1 not in self.__vertices or vertex2 not in self.__vertices:
            raise VertexException("The vertex does not exist!")
        return vertex2 in self.__adj[vertex1]

    def vertices_iterator(self):
        """
        Returns an iterator for the vertices in the graph
        """
        for vertex in self.__vertices:
            yield vertex

    def get_degree(self, vertex):
        """
        Returns the degree of a vertex
        :param vertex: the vertex
        :return: the degree of the vertex
        """
        if vertex not in self.__vertices:
            raise VertexException("The vertex does not exist!")
        return len(self.__adj[vertex])

    def neighbours_iterator(self, vertex):
        """
        Returns an iterator for the outbound neighbours of a vertex
        :param vertex: the vertex
        :return: the iterator
        """
        if vertex not in self.__vertices:
            raise VertexException("The vertex does not exist!")
        for neighbour in self.__adj[vertex]:
            yield neighbour

    def edges_iterator(self):
        """
        Returns an iterator for the edges in the graph
        """
        for vertex in self.__vertices:
            for neighbour in self.__adj[vertex]:
                if vertex < neighbour:
                    yield (vertex, neighbour)

    def connected_components(self):
        """
        Returns a list of all the connected components of the graph
        :return: the list of connected components
        """
        connectedComponents = []
        self.__visited = []

        for vertex in self.__vertices:
            if vertex not in self.__visited:
                connectedComponent = self.DepthFirstSearch(vertex)
                connectedComponents.append(connectedComponent)

        return connectedComponents

    def DepthFirstSearch(self, startVertex):
        """
        Depth First Search algorithm
        :param startVertex: the starting vertex
        :return:  a graph object containing the connected component of startVertex
        """
        if startVertex not in self.__vertices:
            raise VertexException("The vertex does not exist!")

        self.__visited.append(startVertex)

        # create a graph object for the connected component
        connectedComponent = UndirectedGraph()
        connectedComponent.add_vertex(startVertex)

        # stack for DFS
        stack = [startVertex]

        while len(stack) > 0:
            # pop the top element from the stack
            currentVertex = stack.pop()

            # iterate through the neighbours of the currentVertex
            for neighbour in self.__adj[currentVertex]:
                if neighbour not in self.__visited:
                    # add the neighbour to the stack
                    stack.append(neighbour)
                    self.__visited.append(neighbour)
                    try:
                        connectedComponent.add_vertex(neighbour)
                    except Exception:
                        pass
                    for neighbourNeighbour in self.__adj[neighbour]:
                        if neighbourNeighbour not in connectedComponent.__adj[neighbour]:
                            try:
                                connectedComponent.add_edge(neighbour, neighbourNeighbour)
                            except Exception:
                                pass


        return connectedComponent

    def read_graph_from_file(self, file_descriptor):
        with open(file_descriptor, "r") as fin:
            for line in fin:
                line = line.strip()
                if line == "" or line[0] == "#":  # empty line or comment
                    continue

                line = line.split()

                # if the line has only one element, it is a vertex that has no edges
                if len(line) == 1:
                    self.add_vertex(int(line[0]))

                # if the line has three elements, it is an edge between two vertices with a given cost
                if len(line) == 2:
                    # adding the vertices to the graph
                    try:
                        self.add_vertex(int(line[0]))
                    except Exception:  # if the vertex is already in the graph
                        pass
                    try:
                        self.add_vertex(int(line[1]))
                    except Exception:  # if the vertex is already in the graph
                        pass

                    # adding the edge to the graph with the given cost
                    try:
                        self.add_edge(int(line[0]), int(line[1]))
                    except EdgeException:  # if the edge is already in the graph
                        pass

    def save_graph_to_file(self, file_descriptor):
        with open(file_descriptor, "w") as fout:
            edges = []
            for vertex in self.vertices_iterator():
                if self.get_degree(vertex) == 0:
                    fout.write(str(vertex) + "\n")
                else:
                    for neighbour in self.vertex_iterator(vertex):
                        edge = (min(neighbour, vertex), max(neighbour, vertex))
                        if edge not in edges:
                            fout.write(str(edge[0]) + " " + str(edge[1]) + "\n")
                            edges.append(edge)




