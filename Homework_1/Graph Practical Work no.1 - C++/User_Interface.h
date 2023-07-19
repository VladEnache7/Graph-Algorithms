#pragma once


#include "graph.h"
#include <iostream>
using namespace std;

class VertexException;

class EdgeException;



class User_Interface {
private:
    Graph *graph;
public:
    User_Interface() = default;
    explicit User_Interface(Graph *graph) {
        this->graph = graph;
    }

    static void print_main_menu() {
        cout << " ---> Main menu <--- " << endl;
        cout << "1 - Get the number of vertices" << endl;
        cout << "2 - Parse the set of vertices" << endl;
        cout << "3 - Check if an edge exists" << endl;
        cout << "4 - Get the cost of an edge" << endl;
        cout << "5 - Get the in degree of a vertex" << endl;
        cout << "6 - Get the out degree of a vertex" << endl;
        cout << "7 - Parse the set of outbound edges of a vertex" << endl;
        cout << "8 - Parse the set of inbound edges of a vertex" << endl;
        cout << "9 - Parse the set of edges" << endl;
        cout << "10 - Add a new vertex" << endl;
        cout << "11 - Add a new edge" << endl;
        cout << "12 - Remove a vertex" << endl;
        cout << "13 - Remove an edge" << endl;
        cout << "14 - Modify the cost of an edge" << endl;
        cout << "15 - Save the Graph to a file" << endl;
        cout << "16 - Copy the graph and save it to copy_graph.txt" << endl;
        cout << "x - Exit" << endl;
    }

    void main_menu() {
        string command;
        while (true) {
            print_main_menu();
            cout << "Enter command: ";
            cin >> command;
            // get nr of vertices
            if (command == "1") {
                cout << "The number of vertices is: " << graph->get_nr_of_vertices() << endl;
            }
                // print vertices
            else if (command == "2") {
                cout << "The set of vertices is: ";
                for (auto vertex: graph->get_vertices()) {
                    cout << vertex << " ";
                }
                cout << endl;
            }
                // is edge
            else if (command == "3") {
                int vertex1, vertex2;
                cout << "Enter the first vertex: ";
                cin >> vertex1;
                cout << "Enter the second vertex: ";
                cin >> vertex2;
                if (graph->is_edge(vertex1, vertex2)) {
                    cout << "There is an edge between these two vertices" << endl;
                } else {
                    cout << "There is no edge between these two vertices " << endl;

                }
            }
                // get cost
            else if (command == "4") {
                int vertex1, vertex2;
                cout << "Enter the first vertex: ";
                cin >> vertex1;
                cout << "Enter the second vertex: ";
                cin >> vertex2;
                cout << "The cost is: " << graph->get_cost(vertex1, vertex2) << endl;
            }
                // get in degree
            else if (command == "5") {
                int vertex;
                cout << "Enter the vertex: ";
                cin >> vertex;
                cout << "The in degree is: " << graph->get_in_degree(vertex) << endl;
            }
                // get out degree
            else if (command == "6") {
                int vertex;
                cout << "Enter the vertex: ";
                cin >> vertex;
                cout << "The out degree is: " << graph->get_out_degree(vertex) << endl;
            }
                // print outbound edges
            else if (command == "7") {
                int vertex;
                cout << "Enter the vertex: ";
                cin >> vertex;
                cout << "The set of outbound edges is: ";
                for (auto edge: graph->get_outbound_vertices(vertex)) {
                    cout << edge << " ";
                }
                cout << endl;
            }
                // print inbound edges
            else if (command == "8") {
                int vertex;
                cout << "Enter the vertex: ";
                cin >> vertex;
                cout << "The set of inbound edges is: ";
                for (auto edge: graph->get_inbound_vertices(vertex)) {
                    cout << edge << " ";
                }
                cout << endl;
            }
                // print edges
            else if (command == "9") {
                cout << "The number of edges are " << graph->get_nr_of_edges() << " and the set of edges is: ";
                for (auto edge: graph->get_edges()) {
                    cout << "(" << edge.first << ", " << edge.second << ") ";
                }
                cout << endl;
            }
                // add vertex
            else if (command == "10") {
                int vertex;
                cout << "Enter the vertex to be added: ";
                cin >> vertex;
                try {
                    graph->add_vertex(vertex);
                    cout << "The vertex was added successfully" << endl;
                } catch (VertexException & e) {
                    cout << e.what() << endl;
                }
            }
                // add edge
            else if (command == "11") {
                int vertex1, vertex2, cost;
                cout << "Enter the first vertex: ";
                cin >> vertex1;
                cout << "Enter the second vertex: ";
                cin >> vertex2;
                cout << "Enter the cost: ";
                cin >> cost;
                try {
                    graph->add_edge(vertex1, vertex2, cost);
                    cout << "The edge was added successfully" << endl;
                } catch (VertexException &e) {
                    cout << e.what() << endl;
                } catch (EdgeException &e) {
                    cout << e.what() << endl;
                }
            }
                // remove vertex
            else if (command == "12") {
                int vertex;
                cout << "Enter the vertex to be removed: ";
                cin >> vertex;
                try {
                    graph->remove_vertex(vertex);
                    cout << "The vertex was removed successfully" << endl;
                } catch (VertexException &e) {
                    cout << e.what() << endl;
                }
            }
                // remove edge
            else if (command == "13") {
                int vertex1, vertex2;
                cout << "Enter the first vertex: ";
                cin >> vertex1;
                cout << "Enter the second vertex: ";
                cin >> vertex2;
                try {
                    graph->remove_edge(vertex1, vertex2);
                    cout << "The edge was removed successfully" << endl;
                } catch (VertexException &e) {
                    cout << e.what() << endl;
                } catch (EdgeException &e) {
                    cout << e.what() << endl;
                }
            }
                // set cost
            else if (command == "14") {
                int vertex1, vertex2, cost;
                cout << "Enter the first vertex: ";
                cin >> vertex1;
                cout << "Enter the second vertex: ";
                cin >> vertex2;
                cout << "Enter the cost to be set: ";
                cin >> cost;
                try {
                    graph->set_cost(vertex1, vertex2, cost);
                    cout << "The cost was set successfully" << endl;
                } catch (VertexException &e) {
                    cout << e.what() << endl;
                } catch (EdgeException &e) {
                    cout << e.what() << endl;
                }
            }
                // save to file
            else if (command == "15") {
                string filename;
                cout << "Enter the filename: ";
                cin >> filename;
                try {
                    graph->save_graph_to_file(filename);
                    cout << "The graph was saved successfully" << endl;
                } catch (FileException &e) {
                    cout << e.what() << endl;
                }
            }
            // Copy the graph and save it to copy_graph.txt
            else if (command == "16") {
                try {
                    Graph *copy = new Graph(*graph);
                    copy->save_graph_to_file("copy_graph.txt");
                    cout << "The graph was copied successfully" << endl;
                } catch (FileException &e) {
                    cout << e.what() << endl;
                }
            }
                // exit
            else if (command == "x")
                break;
            else
                cout << "Invalid command" << endl;
        }
    }

    static void print_start_menu(){
        cout << "1 - Read Graph from a file" << endl;
        cout << "2 - Generate a random Graph and save it to random_graph.txt" << endl;
        cout << "x - Exit" << endl;
    }

    void start(){
        while (true){
            print_start_menu();
            string command;
            cout << "Enter command: ";
            cin >> command;

            if (command == "1"){
                string file_name;
                cout << "Enter file name: ";
                cin >> file_name;
                try{
                    graph = new Graph();
                    graph->read_graph_from_file(file_name);
                    cout << "Graph read successfully from file" << endl;
                } catch (FileException &e){
                    cout << e.what() << endl;
                }

                // and start the main menu
                main_menu();

            } else if (command == "2"){
                try{
                    int nr_of_vertices;
                    cout << "Enter the number of vertices: ";
                    cin >> nr_of_vertices;
                    int nr_of_edges;
                    cout << "Enter the number of edges: ";
                    cin >> nr_of_edges;
                    graph = new Graph(nr_of_vertices);
                    graph->generate_random_graph(nr_of_vertices, nr_of_edges);
                    graph->save_graph_to_file("random_graph.txt");
                } catch (exception &e){
                    cout << "Probably you have not entered numbers\n" << endl;
                }
            } else if (command == "x"){
                return;
            } else {
                cout << "Invalid command" << endl;
            }
        }
    }
};





