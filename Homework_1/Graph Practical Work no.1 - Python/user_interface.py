from graph import Graph, EdgeException, VertexException, generate_random_graph, lowest_cost_walk, \
    PathDoesNotExistException, NegativeCycleException


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
                try:
                    self.__graph.read_graph_from_file(file_name)
                    print("Graph read successfully from file")
                except FileNotFoundError:
                    print("File not found")


                # and start the main menu
                self.main_menu()

            elif command == "2":
                try:
                    nr_of_vertices = int(input("Enter the number of vertices: "))
                    nr_of_edges = int(input("Enter the number of edges: "))
                    if nr_of_edges > nr_of_vertices * (nr_of_vertices):
                        print ("The number of edges is too big")
                        continue
                    self.__graph = generate_random_graph(nr_of_vertices, nr_of_edges)
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
            # print number of vertices
            if command == "1":
                print("The number of vertices is: " + str(self.__graph.get_nr_of_vertices()))
            # print vertices
            elif command == "2":
                print("The set of vertices is:")
                # iterate through the vertices and print them with space between them
                for vertex in self.__graph.vertices_iterator():
                    print(vertex, end=" ")
            # is edge
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
            # get cost
            elif command == "4":
                try:
                    vertex1 = int(input("Enter the first vertex: "))
                    vertex2 = int(input("Enter the second vertex: "))
                    print("The cost of the edge is: " + str(self.__graph.get_cost(vertex1, vertex2)))
                except ValueError:
                    print("Invalid input")
                except EdgeException:
                    print("There is no edge between these two vertices")
            # get in degree
            elif command == "5":
                try:
                    vertex = int(input("Enter the vertex: "))
                    print("The in degree of the vertex is: " + str(self.__graph.get_in_degree(vertex)))

                except ValueError:
                    print("Invalid input ")
                except VertexException:
                    print("The vertex is not in the graph")
            # get out degree
            elif command == "6":
                try:
                    vertex = int(input("Enter the vertex: "))
                    print("The out degree of the vertex is: " + str(self.__graph.get_out_degree(vertex)))
                except ValueError:
                    print("Invalid input")
                except VertexException:
                    print("The vertex is not in the graph")
            # get outbound edges
            elif command == "7":
                try:
                    vertex = int(input("Enter the vertex: "))
                    print("The set of outbound edges of the vertex is: ")
                    for vertex in self.__graph.outbound_iterator(vertex):
                        print(vertex, end=" ")
                except ValueError:
                    print("Invalid input")
            # get inbound edges
            elif command == "8":
                try:
                    vertex = int(input("Enter the vertex: "))
                    print("The set of inbound edges of the vertex is: ")
                    for vertex in self.__graph.inbound_iterator(vertex):
                        print(vertex, end=" ")
                except ValueError:
                    print("Invalid input")
            # get nr of edges
            elif command == "9":
                try:
                    print(f"The number of edges are {self.__graph.get_nr_of_edges()} and the set of edges is: ")
                    for edge in self.__graph.edges_iterator():
                        print(edge, end=" ")
                except ValueError:
                    print("Invalid input")
            # add vertex
            elif command == "10":
                try:
                    vertex = int(input("Enter the vertex to be added: "))
                    self.__graph.add_vertex(vertex)
                    print("The vertex was added successfully")
                except ValueError:
                    print("Invalid input")
                except VertexException:
                    print("The vertex is already in the graph")
            # add edge
            elif command == "11":
                try:
                    vertex1 = int(input("Enter the first vertex of the edge to be added: "))
                    vertex2 = int(input("Enter the second vertex of the edge to be added: "))
                    cost = int(input("Enter the cost: "))
                    self.__graph.add_edge(vertex1, vertex2, cost)
                    print("The edge was added successfully")
                except ValueError:
                    print("Invalid input")
                except EdgeException:
                    print("The edge is already in the graph")
            # remove vertex
            elif command == "12":
                try:
                    vertex = int(input("Enter the vertex to be removed: "))
                    self.__graph.remove_vertex(vertex)
                    print("The vertex was removed successfully")
                except ValueError:
                    print("Invalid input")
                except VertexException:
                    print("The vertex is not in the graph")
            # remove edge
            elif command == "13":
                try:
                    vertex1 = int(input("Enter the first vertex of the edge to be removed: "))
                    vertex2 = int(input("Enter the second vertex of the edge to be removed: "))
                    self.__graph.remove_edge(vertex1, vertex2)
                    print("The edge was removed successfully")
                except ValueError:
                    print("Invalid input")
                except EdgeException:
                    print("The edge is not in the graph")
            # set cost
            elif command == "14":
                try:
                    vertex1 = int(input("Enter the first vertex: "))
                    vertex2 = int(input("Enter the second vertex: "))
                    cost = int(input("Enter the cost to be set: "))
                    self.__graph.set_cost(vertex1, vertex2, cost)
                    print("The cost was set successfully")
                except ValueError:
                    print("Invalid input")
                except EdgeException:
                    print("The edge is not in the graph")
            # save to file
            elif command == "15":
                file_name = input("Enter file name where you want to save the graph: ")
                self.__graph.save_graph_to_file(file_name)
                print("The graph was saved successfully")
            # copy graph
            elif command == "16":
                try:
                    copied_graph = Graph()
                    copied_graph.copy_graph(self.__graph)
                    copied_graph.save_graph_to_file("copied_graph.txt")
                    print("The graph was copied successfully")
                except Exception:
                    print("Some error occurred")
            # get the lowest cost walk
            elif command == "17":
                try:
                    start_vertex = int(input("Enter the start vertex: "))
                    end_vertex = int(input("Enter the end vertex: "))

                    if start_vertex not in self.__graph.vertices_iterator() or end_vertex not in self.__graph.vertices_iterator():
                        raise VertexException

                    dist, path = lowest_cost_walk(self.__graph, start_vertex, end_vertex)

                    print(f"The lowest cost walk is: {dist}")
                    for vertex in path:
                        print(vertex, end=" ")

                except ValueError:
                    print("Invalid input")
                except VertexException:
                    print("The vertex is not in the graph")
                except PathDoesNotExistException:
                    print("There is no path between the two vertices")
                except NegativeCycleException:
                    print("The graph contains a negative cycle")
            # geta minimal spanning tree using the Kruskal's algorithm
            elif command == "18":

                spanning_tree = self.__graph.kruskal_algorithm()
                print("The minimal spanning tree is: ")
                for edge in spanning_tree.edges_iterator():
                    print(edge, end=" ")

                print()

                # priting the cost of the spanning tree
                cost = 0
                for edge in spanning_tree.edges_iterator():
                    cost += spanning_tree.get_cost(edge[0], edge[1])

                print(f"The cost of the minimum spanning tree is {cost}")


            # exit
            elif command == "x":
                return
            else:
                print("Invalid command")

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
        16 - Copy the graph and save it to copied_graph.txt
        17 - Get the lowest cost walk between two vertices
        18 - Get a minimal spanning tree using the Kruskal's algorithm
        x - Exit
        """)
