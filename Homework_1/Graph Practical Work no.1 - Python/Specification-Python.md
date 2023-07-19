
# Practical work no. 1

## Python Specification

### We shall define a class named Graph representing a directed graph.

### Implementation:
    class Graph:
    def __init__(self, nr_of_vertices=0, nr_of_edges=0):
        self.__vertices = set()  # set of vertices
        self.__outbounds = dict() # dictionary of outbound edges
        self.__inbounds = dict() # dictionary of inbound edges
        self.__cost = dict() # dictionary of costs


### The class Graph will provide the following methods:

__def __init__(self, nr_of_vertices=0, nr_of_edges=0)__

    Creates a graph with the given number of vertices and edges.

__def add_vertex(self, vertex_to_be_added)__

    Adds a vertex to the graph.
    Throws an exception if the vertex already exists.

__def remove_vertex(self, vertex_to_be_removed)__

    Removes a vertex from the graph.
    Throws an exception if the vertex does not exist.

__def add_edge(self, vertex_from, vertex_to, edge_cost)__
    
    Adds an edge to the graph.
    Throws an exception if the edge already exists or if one of the vertices does not exist.

__def remove_edge(self, vertex_from, vertex_to)__

    Removes an edge from the graph.
    Throws an exception if the edge does not exist.

__def get_nr_of_vertices(self)__

    Returns the number of vertices in the graph.

__def get_nr_of_edges(self)__

    Returns the number of edges in the graph.

__def vertices_iterator(self)__

    Returns an iterator for the vertices in the graph.

__def edges_iterator(self)__

    Returns an iterator for the edges in the graph.

__def inbound_iterator(self, vertex_to)__

    Returns an iterator for the inbound edges of a vertex.

__def outbound_iterator(self, vertex_from)__

    Returns an iterator for the outbound edges of a vertex.

__def is_edge(self, vertex_from, vertex_to)__

    Returns True if there is an edge from vertex_from to vertex_to, False otherwise.

__def is_vertex(self, vertex_to_be_checked)__

    Returns True if the vertex_to_be_checked is a vertex in the graph, False otherwise.

__def get_in_degree(self, vertex_to)__

    Returns the in degree of a vertex.

__def get_out_degree(self, vertex_from)__

    Returns the out degree of a vertex.

__def get_cost(self, vertex_from, vertex_to)__

    Returns the cost of an edge.
    Throws an exception if the edge does not exist.

__def set_cost(self, vertex_from, vertex_to, new_cost)__

    Sets the cost of an edge.
    Throws an exception if the edge does not exist.

__def copy(self)__

    Returns a copy of the graph.

__def generate_random_graph(self, nr_of_vertices, nr_of_edges)__

    Generates a random graph with the given number of vertices and edges.

__def read_graph_from_file(self, file_descriptor)__

    Reads a graph from a file.

__def save_graph_to_file(self, file_descriptor)__

    Saves a graph to a file.