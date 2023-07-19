from copy import deepcopy
from random import randint


class VertexException(Exception):
    pass


class EdgeException(Exception):
    pass

class NegativeCycleException(Exception):
    pass

class PathDoesNotExistException(Exception):
    pass

class Graph:
    def __init__(self, nr_of_vertices=0, nr_of_edges=0):
        self.__vertices = set()  # because we cannot have multiple occurrences of the same element
        self.__outbounds = dict()
        self.__inbounds = dict()
        self.__cost = dict()

    def add_vertex(self, vertex_to_be_added):
        """
        Adds a vertex to the graph
        :param vertex_to_be_added: the vertex to be added
        :return: nothing
        """
        if vertex_to_be_added in self.__vertices:
            raise VertexException("The vertex is already in the graph!")
        self.__vertices.add(vertex_to_be_added)
        self.__outbounds[vertex_to_be_added] = set()
        self.__inbounds[vertex_to_be_added] = set()

    def remove_vertex(self, vertex_to_be_removed):
        """
        Removes a vertex from the graph
        :param vertex_to_be_removed: the vertex to be removed
        :return: nothing
        """
        if vertex_to_be_removed not in self.__vertices:
            raise VertexException("The vertex is not in the graph!")
        for vertex in self.__vertices:
            if (vertex, vertex_to_be_removed) in self.__cost:
                del self.__cost[(vertex, vertex_to_be_removed)]
                # deleting the vertex from the inbounds and outbounds of the other vertices
                self.__outbounds[vertex].remove(vertex_to_be_removed)
            if (vertex_to_be_removed, vertex) in self.__cost:
                del self.__cost[(vertex_to_be_removed, vertex)]
                self.__inbounds[vertex].remove(vertex_to_be_removed)

        del self.__outbounds[vertex_to_be_removed]
        del self.__inbounds[vertex_to_be_removed]
        self.__vertices.remove(vertex_to_be_removed)

    def add_edge(self, vertex_from, vertex_to, edge_cost):
        """
        Adds an edge to the graph
        :param vertex_from: the starting vertex of the edge
        :param vertex_to: the ending vertex of the edge
        :param edge_cost: the cost of the edge
        :return: nothing
        """
        if vertex_from not in self.__vertices or vertex_to not in self.__vertices:
            raise VertexException("The vertices are not in the graph!")
        if (vertex_from, vertex_to) in self.__cost:
            # print((vertex_from, vertex_to))
            raise EdgeException("The edge is already in the graph!")

        self.__outbounds[vertex_from].add(vertex_to)
        self.__inbounds[vertex_to].add(vertex_from)
        self.__cost[(vertex_from, vertex_to)] = edge_cost

    def remove_edge(self, vertex_from, vertex_to):
        """
        Removes an edge from the graph
        :param vertex_from: the starting vertex of the edge
        :param vertex_to: the ending vertex of the edge
        :return: nothing
        """
        if (vertex_from, vertex_to) not in self.__cost:
            raise EdgeException("The edge is not in the graph!")

        self.__outbounds[vertex_from].remove(vertex_to)
        self.__inbounds[vertex_to].remove(vertex_from)
        del self.__cost[(vertex_from, vertex_to)]

    def get_nr_of_vertices(self):
        """
        Returns the number of vertices in the graph
        """
        return len(self.__vertices)

    def get_nr_of_edges(self):
        """
        Returns the number of edges in the graph
        """
        return len(self.__cost)

    def vertices_iterator(self):
        """
        Returns an iterator for the vertices in the graph
        """
        for vertex in self.__vertices:
            yield vertex

    def edges_iterator(self):
        """
        Returns an iterator for the edges in the graph
        """
        for edge in self.__cost:
            yield edge  # TODO - change it if is needed

    def inbound_iterator(self, vertex_to):
        """
        Returns an iterator for the vertices that have an edge that ends in vertex_to
        """
        for vertex_from in self.__inbounds[vertex_to]:
            yield vertex_from

    def outbound_iterator(self, vertex_from):
        """
        Returns an iterator for the vertices that have an edge that starts from vertex_from
        """
        for vertex_to in self.__outbounds[vertex_from]:
            yield vertex_to

    def is_edge(self, vertex_from, vertex_to):
        """
        Returns True if the edge (vertex_from, vertex_to) is in the graph, False otherwise
        """
        return (vertex_from, vertex_to) in self.__cost

    def is_vertex(self, vertex_to_be_checked):
        return vertex_to_be_checked in self.__vertices

    def get_in_degree(self, vertex_to):
        """
        Returns the number of edges that end in vertex_to
        """
        return len(self.__inbounds[vertex_to])

    def get_out_degree(self, vertex_from):
        """
        Returns the number of edges that start from vertex_from
        """
        return len(self.__outbounds[vertex_from])

    def set_cost(self, vertex_from, vertex_to, new_cost):
        if (vertex_from, vertex_to) not in self.__cost:
            raise EdgeException("The edge is not in the graph!")
        self.__cost[(vertex_from, vertex_to)] = new_cost

    def get_cost(self, vertex_from, vertex_to):
        if (vertex_from, vertex_to) not in self.__cost:
            print((vertex_from, vertex_to))
            raise EdgeException("The edge is not in the graph!")
        return self.__cost[(vertex_from, vertex_to)]

    def copy_graph(self, graph_to_be_copied):
        """
        Returns a copy of the graph
        :return:
        """
        for vertex in graph_to_be_copied.vertices_iterator():
            self.add_vertex(vertex)

        for edge in graph_to_be_copied.edges_iterator():
            self.add_edge(edge[0], edge[1], graph_to_be_copied.get_cost(edge[0], edge[1]))


    def read_graph_from_file(self, file_descriptor):
        # graph_read_from_file = Graph()
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
                if len(line) == 3:
                    # adding the vertices to the graph
                    try:
                        self.add_vertex(int(line[0]))
                    except VertexException:  # if the vertex is already in the graph
                        pass
                    try:
                        self.add_vertex(int(line[1]))
                    except VertexException:  # if the vertex is already in the graph
                        pass

                    # adding the edge to the graph with the given cost
                    try:
                        self.add_edge(int(line[0]), int(line[1]), int(line[2]))
                    except EdgeException:  # if the edge is already in the graph
                        self.set_cost(int(line[0]), int(line[1]), int(line[2]))

    def save_graph_to_file(self, file_descriptor):
        with open(file_descriptor, "w") as fout:
            for vertex in self.vertices_iterator():
                if self.get_out_degree(vertex) == 0 and self.get_in_degree(vertex) == 0:
                    fout.write(str(vertex) + "\n"   )
                for neighbour in self.outbound_iterator(vertex):
                    fout.write(str(vertex) + " " + str(neighbour) + " " + str(
                        self.get_cost(vertex, neighbour)) + "\n")

    def kruskal_algorithm(self):
        """
        Returns the minimum spanning tree of the graph
        :return:
        """
        # creating an empty graph
        minimum_spanning_tree = Graph()

        # creating the list of edges sorted by cost
        sorted_edges = []
        for edge in self.edges_iterator():
            sorted_edges.append((self.get_cost(edge[0], edge[1]), edge[0], edge[1]))
        sorted_edges.sort()

        # creating the list of sets
        components = []
        for vertex in self.vertices_iterator():
            components.append({vertex}) # each vertex is in a component by itself

        # creating the minimum spanning tree
        for edge in sorted_edges:
            component1 = None
            component2 = None
            for component in components:
                if edge[1] in component:
                    component1 = component
                if edge[2] in component:
                    component2 = component
            if component1 != component2:
                # adding the nodes if they do not already exist
                if edge[1] not in minimum_spanning_tree.vertices_iterator():
                    minimum_spanning_tree.add_vertex(edge[1])
                if edge[2] not in minimum_spanning_tree.vertices_iterator():
                    minimum_spanning_tree.add_vertex(edge[2])

                # adding the edge to the minimum spanning tree
                minimum_spanning_tree.add_edge(edge[1], edge[2], edge[0])

                # updating the components
                component1.update(component2)
                components.remove(component2)
                # it the size of component1 si equal to the number of vertices, then the minimum spanning tree is complete
                if len(component1) == len(self.vertices_iterator()):
                    break

        return minimum_spanning_tree


def generate_random_graph(nr_of_vertices, nr_of_edges):
    generated_graph = Graph()
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
        cost = randint(-1000000, 1000000)
        generated_graph.add_edge(vertex1, vertex2, cost)

    return generated_graph

# def lowest_cost_walk(graph, start_vertex, end_vertex):
#     """
#     Returns the lowest cost walk in the graph from start_vertex to end_vertex using Bellman-Ford algorithm
#     :return: the lowest cost walk in the graph from start_vertex to end_vertex
#     """
#     # initialising the distances with infinity
#     infinity = 9999999999
#     distance = {}
#     for vertex in graph.vertices_iterator():
#         distance[vertex] = infinity
#
#     # initialising the distances of the start_vertex with 0
#     distance[start_vertex] = 0
#
#     # initialising the predecessors with None
#     predecessor = {}
#     for vertex in graph.vertices_iterator():
#         predecessor[vertex] = None
#
#
#     # Bellman-Ford algorithm
#     for i in range(graph.get_nr_of_vertices() - 1):
#         nothing_changed = True
#         for edge in graph.edges_iterator():
#             if distance[edge[0]] + graph.get_cost(edge[0], edge[1]) < distance[edge[1]]:
#                 distance[edge[1]] = distance[edge[0]] + graph.get_cost(edge[0], edge[1])
#                 predecessor[edge[1]] = edge[0]
#                 nothing_changed = False
#
#         if nothing_changed:
#             break # if nothing changed in the last iteration, the algorithm stops, making it more efficient
#
#     # checking for negative cost cycles
#     for edge in graph.edges_iterator():
#         if distance[edge[0]] + graph.get_cost(edge[0], edge[1]) < distance[edge[1]]:
#             raise NegativeCycleException("The graph contains a negative cost cycle!")
#
#     if distance[end_vertex] == infinity:
#         raise PathDoesNotExistException("There is no path between the given vertices!")
#
#     # reconstructing the path
#     path = []
#     current_vertex = end_vertex
#     while current_vertex is not None:
#         path.append(current_vertex)
#         current_vertex = predecessor[current_vertex]
#
#     # reversing the path
#     path.reverse()
#
#     return (distance[end_vertex], path)

def lowest_cost_walk(graph, start_vertex, end_vertex):
    """
    Returns the lowest cost walk in the graph from start_vertex to end_vertex using Bellman-Ford algorithm
    The program will use a matrix defined as d[x,k]=the cost of the lowest cost walk from s to x and of length at most k, where s is the starting vertex.
    :param graph: the graph
    :param start_vertex: the start vertex
    :param end_vertex: the end vertex
    :return: the lowest cost walk in the graph from start_vertex to end_vertex
    """
    # The program will use a matrix defined as d[x,k]=the cost of the lowest cost walk from s to x and of length at most k, where s is the starting vertex.
    # The program will also use a matrix defined as p[x,k]=the predecessor of x in the lowest cost walk from s to x and of length at most k, where s is the starting vertex.

    # initialising the distances with infinity
    infinity = 9999999999
    n = graph.get_nr_of_vertices()
    d = [[infinity for i in graph.vertices_iterator()] for j in graph.vertices_iterator()]
    p = [[None for i in graph.vertices_iterator()] for j in graph.vertices_iterator()]

    # initialising the distances of the start_vertex with 0
    d[start_vertex][0] = 0

    # Bellman-Ford algorithm
    for k in range(1, n):
        for x in graph.vertices_iterator():
            d[x][k] = d[x][k-1]
            p[x][k] = p[x][k-1]
            for y in graph.inbound_iterator(x):
                if d[y][k-1] + graph.get_cost(y, x) < d[x][k]:
                    d[x][k] = d[y][k-1] + graph.get_cost(y, x)
                    p[x][k] = y
    # checking for negative cost cycles
    for x in range(n):
        if d[x][n - 1] != d[x][n - 2]:
            raise NegativeCycleException("The graph contains anegative cost cycle!")
    if d[end_vertex][n - 1] == infinity:
        raise PathDoesNotExistException("There is no path between the given vertices!")

    # reconstructing the path
    path = []
    current_vertex = end_vertex
    k = n - 1
    while current_vertex is not None:
        path.append(current_vertex)
        current_vertex = p[current_vertex][k]
        k -= 1
    # reversing the path
    path.reverse()
    return d[end_vertex][n - 1], path