//
// Created by Admin on 05-Apr-23.
//

#include "graph.h"

#include <random>
#include <utility>
#include <algorithm>
#include <fstream>
#include <sstream>


Graph::Graph(int n) {
    for (int i = 0; i < n; i++) {
        this->add_vertex(i);
    }
}

void Graph::add_vertex(int vertex_to_be_added) {
    if (this->is_vertex(vertex_to_be_added)) {
        throw VertexException("The vertex is already in the Graph!");
    }
    this->vertices.insert(vertex_to_be_added);
    this->outbounds[vertex_to_be_added] = std::set<int>();
    this->inbounds[vertex_to_be_added] = std::set<int>();
}

void Graph::remove_vertex(int vertex_to_be_removed) {
    if (!this->is_vertex(vertex_to_be_removed)) {
        throw VertexException("The vertex is not in the Graph!");
    }
    this->vertices.erase(vertex_to_be_removed);
    for (auto vertex : this->outbounds[vertex_to_be_removed]) {
        this->inbounds[vertex].erase(vertex_to_be_removed);
        this->cost.erase(std::make_pair(vertex_to_be_removed, vertex));
    }
    for (auto vertex : this->inbounds[vertex_to_be_removed]) {
        this->outbounds[vertex].erase(vertex_to_be_removed);
        this->cost.erase(std::make_pair(vertex, vertex_to_be_removed));
    }
    this->outbounds.erase(vertex_to_be_removed);
    this->inbounds.erase(vertex_to_be_removed);

}

void Graph::add_edge(int vertex_from, int vertex_to, int cost) {
    if (!this->is_vertex(vertex_from)) {
        throw VertexException("The vertex_from is not in the Graph!");
    }
    if (!this->is_vertex(vertex_to)) {
        throw VertexException("The vertex_to is not in the Graph!");
    }
    if (this->is_edge(vertex_from, vertex_to)) {
        throw EdgeException("The edge is already in the Graph!");
    }
    this->outbounds[vertex_from].insert(vertex_to);
    this->inbounds[vertex_to].insert(vertex_from);
    this->cost[std::make_pair(vertex_from, vertex_to)] = cost;
}


void Graph::remove_edge(int vertex_from, int vertex_to) {
    if (!this->is_vertex(vertex_from)) {
        throw VertexException("The vertex_from is not in the Graph!");
    }
    if (!this->is_vertex(vertex_to)) {
        throw VertexException("The vertex_to is not in the Graph!");
    }
    if (!this->is_edge(vertex_from, vertex_to)) {
        throw EdgeException("The edge is not in the Graph!");
    }
    this->outbounds[vertex_from].erase(vertex_to);
    this->inbounds[vertex_to].erase(vertex_from);
    this->cost.erase(std::make_pair(vertex_from, vertex_to));
}

unsigned long Graph::get_nr_of_vertices() const {
    return this->vertices.size();
}

unsigned long Graph::get_nr_of_edges() const {
    return this->cost.size();
}

std::vector<int> Graph::get_vertices() const {
    std::vector<int> verticesToBeReturned;
    for (auto vertex : this->vertices) {
        verticesToBeReturned.push_back(vertex);
    }
    return verticesToBeReturned;
}

std::vector<std::pair<int, int>> Graph::get_edges() const {
    std::vector<std::pair<int, int>> edgesToBeReturned;
    for (auto edge : this->cost) {
        edgesToBeReturned.push_back(edge.first);
    }
    return edgesToBeReturned;
}

std::vector<int> Graph::get_inbound_vertices(int vertex_to) const {
    if (!this->is_vertex(vertex_to)) {
        throw VertexException("The vertex_to is not in the Graph!");
    }
    std::vector<int> inboundVerticesToBeReturned;
    for (auto vertex : this->inbounds.at(vertex_to)) {
        inboundVerticesToBeReturned.push_back(vertex);
    }
    return inboundVerticesToBeReturned;
}

std::vector<int> Graph::get_outbound_vertices(int vertex_from) const {
    if (!this->is_vertex(vertex_from)) {
        throw VertexException("The vertex_from is not in the Graph!");
    }
    std::vector<int> outboundVerticesToBeReturned;
    for (auto vertex : this->outbounds.at(vertex_from)) {
        outboundVerticesToBeReturned.push_back(vertex);
    }
    return outboundVerticesToBeReturned;
}

bool Graph::is_edge(int vertex_from, int vertex_to) const {
    if (!this->is_vertex(vertex_from)) {
        throw VertexException("The vertex_from is not in the Graph!");
    }
    if (!this->is_vertex(vertex_to)) {
        throw VertexException("The vertex_to is not in the Graph!");
    }
    return this->cost.find(std::make_pair(vertex_from, vertex_to)) != this->cost.end();
}

bool Graph::is_vertex(int vertex) const {
    return this->vertices.find(vertex) != this->vertices.end();
}

unsigned long Graph::get_in_degree(int vertex_to) const {
    if (!this->is_vertex(vertex_to)) {
        throw VertexException("The vertex_to is not in the Graph!");
    }
    return this->inbounds.at(vertex_to).size();
}

unsigned long Graph::get_out_degree(int vertex_from) const {
    if (!this->is_vertex(vertex_from)) {
        throw VertexException("The vertex_from is not in the Graph!");
    }
    return this->outbounds.at(vertex_from).size();
}

void Graph::set_cost(int vertex_from, int vertex_to, int new_cost) {
    if (!this->is_vertex(vertex_from)) {
        throw VertexException("The vertex_from is not in the Graph!");
    }
    if (!this->is_vertex(vertex_to)) {
        throw VertexException("The vertex_to is not in the Graph!");
    }
    if (!this->is_edge(vertex_from, vertex_to)) {
        throw EdgeException("The edge is not in the Graph!");
    }
    this->cost[std::make_pair(vertex_from, vertex_to)] = new_cost;
}

long long Graph::get_cost(int vertex_from, int vertex_to) const {
    if (!this->is_vertex(vertex_from)) {
        throw VertexException("The vertex_from is not in the Graph!");
    }
    if (!this->is_vertex(vertex_to)) {
        throw VertexException("The vertex_to is not in the Graph!");
    }
    if (!this->is_edge(vertex_from, vertex_to)) {
        throw EdgeException("The edge is not in the Graph!");
    }
    return this->cost.at(std::make_pair(vertex_from, vertex_to));
}

void Graph::generate_random_graph(int nr_of_vertices, int nr_of_edges) {
    if (nr_of_vertices < 0) {
        throw VertexException("The number of vertices must be positive!");
    }
    if (nr_of_edges < 0) {
        throw EdgeException("The number of edges must be positive!");
    }
    if (nr_of_edges > nr_of_vertices * (nr_of_vertices)) {
        throw EdgeException("The number of edges must be less than the number of vertices * (number of vertices)!");
    }
    for (int i = 0; i < nr_of_vertices; i++) {
        this->add_vertex(i);
    }
    std::vector<std::pair<int, int>> edges;
    for (int i = 0; i < nr_of_vertices; i++) {
        for (int j = 0; j < nr_of_vertices; j++) {
                edges.emplace_back(i, j);
        }
    }
    std::shuffle(edges.begin(), edges.end(), std::mt19937(std::random_device()()));
    for (int i = 0; i < nr_of_edges; i++) {
        // random newCost
        int newCost = rand() % 1000000;
        this->add_edge(edges[i].first, edges[i].second, newCost);
    }

}

void Graph::clear() {
    if (this->vertices.empty()) {
        return;
    }
    this->vertices.clear();
    this->inbounds.clear();
    this->outbounds.clear();
    this->cost.clear();
}


void Graph::read_graph_from_file(const std::string &file_descriptor) {
    std::ifstream file(file_descriptor);
    if (!file.is_open()) {
        throw FileException("The file could not be opened!");
    }
//    this->clear();
    std::string line;
    while (std::getline(file, line)) {
        if (line.empty() || line.find('#') != std::string::npos) {
            continue;
        }
        // splitting the line
        std::vector<std::string> line_split;
        std::istringstream iss(line);
        std::string word;
        while (iss >> word) {
            line_split.push_back(word);
        }

        if (line_split.size() == 1) {
            this->add_vertex(std::stoi(line_split[0]));
        }
        if (line_split.size() == 3) {
            int vertex_from = std::stoi(line_split[0]);
            int vertex_to = std::stoi(line_split[1]);
            int cost = std::stoi(line_split[2]);
            try {
                this->add_vertex(vertex_from);
            } catch (VertexException &e) {
                // if the vertex is already in the Graph
            }
            try {
                this->add_vertex(vertex_to);
            } catch (VertexException &e) {
                // if the vertex is already in the Graph
            }
            try {
                this->add_edge(vertex_from, vertex_to, cost);
            } catch (EdgeException &e) {
                // if the edge is already in the Graph
                this->set_cost(vertex_from, vertex_to, cost);
            }
        }
    }
    file.close();
}


void Graph::save_graph_to_file(const std::string &file_descriptor) const {
    std::ofstream file(file_descriptor);
    if (!file.is_open()) {
        throw FileException("The file could not be opened!");
    }
    for (auto vertex : this->vertices) {
        if (this->get_out_degree(vertex) == 0 && this->get_in_degree(vertex) == 0) {
            file << vertex << "\n";
        }
        for (auto vertex_to : this->outbounds.at(vertex)) {
            file << vertex << " " << vertex_to << " " << this->get_cost(vertex, vertex_to) << "\n";
        }
    }
    file.close();
}

















