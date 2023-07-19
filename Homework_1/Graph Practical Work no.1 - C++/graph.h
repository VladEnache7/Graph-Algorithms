#pragma once

#include <map>
#include <vector>
#include <set>
#include <string>


/// Exception classes
class VertexException: public std::exception {
    std::string message;
public:
    explicit VertexException(std::string message) {
        this->message = std::move(message);
    }

    const char *what() const noexcept override {
        return this->message.c_str();
    }
};

class EdgeException: public std::exception {
    std::string message;
public:
    explicit EdgeException(std::string message) {
        this->message = std::move(message);
    }

    const char *what() const noexcept override {
        return this->message.c_str();
    }
};

class FileException: public std::exception {
    std::string message;
public:
    explicit FileException(std::string message) {
        this->message = std::move(message);
    }

    const char *what() const noexcept override {
        return this->message.c_str();
    }
};


class Graph {
private:
    std::set<int> vertices {};
    std::map<int, std::set<int>> outbounds {};
    std::map<int, std::set<int>> inbounds {};
    std::map<std::pair<int, int>, int> cost {};

public:
    //implicit constructor
    Graph() = default;

    //explicit constructor
    explicit Graph(int n);

    //copy constructor
    Graph(const Graph&) = default;

    // assignment operator
    Graph& operator=(const Graph&) = default;

    //destructor
    ~Graph() = default;

    void clear();

    void add_vertex(int vertex_to_be_added);

    void remove_vertex(int vertex_to_be_removed);

    void add_edge(int vertex_from, int vertex_to, int edge_cost);

    void remove_edge(int vertex_from, int vertex_to);

    unsigned long get_nr_of_vertices() const;

    unsigned long get_nr_of_edges() const;

    std::vector<int> get_vertices() const;

    std::vector<std::pair<int, int>> get_edges() const;

    std::vector<int> get_inbound_vertices(int vertex_to) const;

    std::vector<int> get_outbound_vertices(int vertex_from) const;

    bool is_edge(int vertex_from, int vertex_to) const;

    bool is_vertex(int vertex_to_be_checked) const;

    unsigned long get_in_degree(int vertex_to) const;

    unsigned long get_out_degree(int vertex_from) const;

    void set_cost(int vertex_from, int vertex_to, int new_cost);

    long long get_cost(int vertex_from, int vertex_to) const;

    void generate_random_graph(int nr_of_vertices, int nr_of_edges);

    void read_graph_from_file(const std::string& file_descriptor);

    void save_graph_to_file(const std::string& file_descriptor) const;

};
