
# Practical work no. 1

## C++ Specification

### We shall define a class named Graph representing a directed graph.

### Implementation:

    class Graph {
    private:
        std::set<int> vertices {}; // set of vertices
        std::map<int, std::set<int>> outbounds {}; // map of outbounds
        std::map<int, std::set<int>> inbounds {}; // map of inbounds
        std::map<std::pair<int, int>, int> cost {}; // map of costs
    }

###  The class Graph will provide the following methods:

__Graph()__ : constructor

    Creates a empty graph

__explicit Graph(int n)__ : constructor

    Creates a graph with n vertices

__Graph(const Graph& g)__ : copy constructor

    Creates a graph with the same vertices and edges as g

__~Graph()__ : destructor

    Destroys the graph

__void clear()__ : method

    Removes all vertices and edges from the graph

__void add_vertex(int vertex_to_be_added)__ : method

    Adds a vertex to the graph
    Throws an exception if the vertex already exists

__void remove_vertex(int vertex_to_be_removed)__ : method

    Removes a vertex from the graph
    Throws an exception if the vertex does not exist

__void add_edge(int vertex_from, int vertex_to, int edge_cost)__ : method

    Adds an edge to the graph
    Throws an exception if the edge already exists

__void remove_edge(int vertex_from, int vertex_to)__ : method

    Removes an edge from the graph
    Throws an exception if the edge does not exist

__unsigned long get_nr_of_vertices() const__ : method

    Returns the number of vertices in the graph

__unsigned long get_nr_of_edges() const__ : method

    Returns the number of edges in the graph

__std::vector<int> get_vertices() const__ : method

    Returns a vector containing all vertices in the graph

__std::vector<std::pair<int, int>> get_edges() const__ : method

    Returns a vector containing all edges in the graph

__std::vector<int> get_inbound_vertices(int vertex_to) const__ : method

    Returns a vector containing all inbound vertices of vertex_to
    Throws an exception if the vertex does not exist

__std::vector<int> get_outbound_vertices(int vertex_from) const__ : method

    Returns a vector containing all outbound vertices of vertex_from
    Throws an exception if the vertex does not exist

__bool is_edge(int vertex_from, int vertex_to) const__ : method

    Returns true if the edge (vertex_from, vertex_to) exists in the graph
    Throws an exception if the vertex does not exist

__bool is_vertex(int vertex_to_be_checked) const__ : method

    Returns true if the vertex vertex_to_be_checked exists in the graph

__unsigned long get_in_degree(int vertex_to) const__ : method

    Returns the in degree of the vertex vertex_to
    Throws an exception if the vertex does not exist

__unsigned long get_out_degree(int vertex_from) const__ : method

    Returns the out degree of the vertex vertex_from
    Throws an exception if the vertex does not exist

__void set_cost(int vertex_from, int vertex_to, int new_cost)__ : method

    Sets the cost of the edge (vertex_from, vertex_to) to new_cost
    Throws an exception if the edge does not exist

__long long get_cost(int vertex_from, int vertex_to) const__ : method
    
    Returns the cost of the edge (vertex_from, vertex_to)
    Throws an exception if the edge does not exist

__void generate_random_graph(int nr_of_vertices, int nr_of_edges)__ : method

    Generates a random graph with nr_of_vertices vertices and nr_of_edges edges

__void read_graph_from_file(const std::string& file_descriptor)__ : method

    Reads a graph from a file
    Throws an exception if the file does not exist

__void save_graph_to_file(const std::string& file_descriptor) const__ : method

    Saves the graph to a file


