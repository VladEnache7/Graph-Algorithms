from graph import Graph, EdgeException, VertexException


class User_Interface:
    def __init__(self):
        self.__graph = Graph()

    @staticmethod
    def print_start_menu():
        print("""
          1 - Read graph from a file
          2 - Generate a random graph and save it to random_graph.txt
          x - Exit
          """)

    def start(self):
        while True:
            self.print_start_menu()
            command = input("Enter command: ")

            if command == "1":
                file_name = input("Enter file name: ")
                self.__graph.read_graph_from_file(file_name)

                # and start the main menu
                self.main_menu()

            elif command == "2":
                try:
                    nr_of_vertices = int(input("Enter the number of vertices: "))
                    nr_of_edges = int(input("Enter the number of edges: "))
                    self.__graph.generate_random_graph(nr_of_vertices, nr_of_edges)
                    self.__graph.save_graph_to_file("random_graph.txt")
                except ValueError:
                    print("Invalid input")

            elif command == "x":
                return
            else:
                print("Invalid command")

    def main_menu(self):
        while True:
            self.print_main_menu()
            command = input("Enter command: ")

            if command == "1":
                print("The number of vertices is: " + str(self.__graph.get_nr_of_vertices()))

            elif command == "2":
                print("The set of vertices is:")
                # iterate through the vertices and print them with space between them
                for vertex in self.__graph.vertices_iterator():
                    print(vertex, end=" ")


            elif command == "3":
                try:
                    vertex1 = int(input("Enter the first vertex: "))
                    vertex2 = int(input("Enter the second vertex: "))
                    if self.__graph.is_edge(vertex1, vertex2):
                        print("There is an edge between these two vertices")
                    else:
                        print("There is no edge between these two vertices")
                except ValueError:
                    print("Invalid input")

            elif command == "4":
                try:
                    vertex1 = int(input("Enter the first vertex: "))
                    vertex2 = int(input("Enter the second vertex: "))
                    print("The cost of the edge is: " + str(self.__graph.get_cost(vertex1, vertex2)))
                except ValueError:
                    print("Invalid input")
                except EdgeException:
                    print("There is no edge between these two vertices")

            elif command == "5":
                try:
                    vertex = int(input("Enter the vertex: "))
                    print("The in degree of the vertex is: ")
                    for vertex in self.__graph.inbound_iterator(vertex):
                        print(vertex, end=" ")

                except ValueError:
                    print("Invalid input ")
                except VertexException:
                    print("The vertex is not in the graph")

            elif command == "6":
                try:
                    vertex = int(input("Enter the vertex: "))
                    print("The out degree of the vertex is: " + str(self.__graph.get_out_degree(vertex)))
                except ValueError:
                    print("Invalid input")
                except VertexException:
                    print("The vertex is not in the graph")

            elif command == "7":
                try:
                    vertex = int(input("Enter the vertex: "))
                    print("The set of outbound edges of the vertex is: ")
                    for vertex in self.__graph.outbound_iterator(vertex):
                        print(vertex, end=" ")
                except ValueError:
                    print("Invalid input")

            elif command == "8":
                try:
                    vertex = int(input("Enter the vertex: "))
                    print("The set of inbound edges of the vertex is: ")
                    for vertex in self.__graph.inbound_iterator(vertex):
                        print(vertex, end=" ")
                except ValueError:
                    print("Invalid input")

            elif command == "9":
                try:
                    print(f"The number of edges are {self.__graph.get_nr_of_edges()} and the set of edges is: ")
                    for edge in self.__graph.edges_iterator():
                        print(edge, end=" ")
                except ValueError:
                    print("Invalid input")

            elif command == "10":
                try:
                    vertex = int(input("Enter the vertex: "))
                    self.__graph.add_vertex(vertex)
                except ValueError:
                    print("Invalid input")
                except VertexException:
                    print("The vertex is already in the graph")

            elif command == "11":
                try:
                    vertex1 = int(input("Enter the first vertex: "))
                    vertex2 = int(input("Enter the second vertex: "))
                    cost = int(input("Enter the cost: "))
                    self.__graph.add_edge(vertex1, vertex2, cost)
                except ValueError:
                    print("Invalid input")
                except EdgeException:
                    print("The edge is already in the graph")

            elif command == "12":
                try:
                    vertex = int(input("Enter the vertex: "))
                    self.__graph.remove_vertex(vertex)
                except ValueError:
                    print("Invalid input")
                except VertexException:
                    print("The vertex is not in the graph")

            elif command == "13":
                try:
                    vertex1 = int(input("Enter the first vertex: "))
                    vertex2 = int(input("Enter the second vertex: "))
                    self.__graph.remove_edge(vertex1, vertex2)
                except ValueError:
                    print("Invalid input")
                except EdgeException:
                    print("The edge is not in the graph")

            elif command == "14":
                try:
                    vertex1 = int(input("Enter the first vertex: "))
                    vertex2 = int(input("Enter the second vertex: "))
                    cost = int(input("Enter the cost: "))
                    self.__graph.set_cost(vertex1, vertex2, cost)
                except ValueError:
                    print("Invalid input")
                except EdgeException:
                    print("The edge is not in the graph")

            elif command == "15":
                file_name = input("Enter file name: ")
                self.__graph.save_graph_to_file(file_name)

            elif command == "x":
                return

    @staticmethod
    def print_main_menu():
        print("""
        ---> Main menu <---
        1 - Get the number of vertices
        2 - Parse the set of vertices
        3 - Check if an edge exists
        4 - Get the cost of an edge
        5 - Get the in degree of a vertex
        6 - Get the out degree of a vertex
        7 - Parse the set of outbound edges of a vertex
        8 - Parse the set of inbound edges of a vertex
        9 - Parse the set of edges 
        10 - Add a new vertex
        11 - Add a new edge
        12 - Remove a vertex
        13 - Remove an edge
        14 - Modify the cost of an edge
        15 - Save the graph to a file
        x - Exit
        """)
