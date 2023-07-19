
from Graph import UndirectedGraph, generate_random_graph, EdgeException, VertexException


# class User_Interface:
#     def __init__(self):
#         self.__graph = UndirectedGraph()
#
#     @staticmethod
#     def print_start_menu():
#         print("""
#           1 - Read graph from a file
#           2 - Generate a random graph and save it to random_graph.txt
#           x - Exit
#           """)
#
#     def start(self):
#         while True:
#             self.print_start_menu()
#             command = input("Enter command: ")
#
#             if command == "1":
#                 file_name = input("Enter file name: ")
#                 try:
#                     self.__graph.read_graph_from_file(file_name)
#                     print("Graph read successfully from file")
#                 except FileNotFoundError:
#                     print("File not found")
#
#                 # and start the main menu
#                 self.main_menu()
#
#             elif command == "2":
#                 try:
#                     nr_of_vertices = int(input("Enter the number of vertices: "))
#                     nr_of_edges = int(input("Enter the number of edges: "))
#                     if nr_of_edges > nr_of_vertices * (nr_of_vertices):
#                         print("The number of edges is too big")
#                         continue
#                     self.__graph = generate_random_graph(nr_of_vertices, nr_of_edges)
#                     self.__graph.save_graph_to_file("random_graph.txt")
#                 except ValueError:
#                     print("Invalid input")
#
#             elif command == "x":
#                 return
#             else:
#                 print("Invalid command")
#
#     def main_menu(self):
#         while True:
#             self.print_main_menu()
#             command = input("Enter command: ")
#             # print number of vertices
#             if command == "1":
#                 print("The number of vertices is: " + str(self.__graph.get_nr_of_vertices()))
#             # print vertices
#             elif command == "2":
#                 print("The set of vertices is:")
#                 # iterate through the vertices and print them with space between them
#                 for vertex in self.__graph.vertices_iterator():
#                     print(vertex, end=" ")
#             # is edge
#             elif command == "3":
#                 try:
#                     vertex1 = int(input("Enter the first vertex: "))
#                     vertex2 = int(input("Enter the second vertex: "))
#                     if self.__graph.is_edge(vertex1, vertex2):
#                         print("There is an edge between these two vertices")
#                     else:
#                         print("There is no edge between these two vertices")
#                 except ValueError:
#                     print("Invalid input")
#             # get cost
#             elif command == "4":
#                 try:
#                     vertex1 = int(input("Enter the first vertex: "))
#                     vertex2 = int(input("Enter the second vertex: "))
#                     print("The cost of the edge is: " + str(self.__graph.get_cost(vertex1, vertex2)))
#                 except ValueError:
#                     print("Invalid input")
#                 except EdgeException:
#                     print("There is no edge between these two vertices")
#             # get in degree
#             elif command == "5":
#                 try:
#                     vertex = int(input("Enter the vertex: "))
#                     print("The in degree of the vertex is: " + str(self.__graph.get_in_degree(vertex)))
#
#                 except ValueError:
#                     print("Invalid input ")
#                 except VertexException:
#                     print("The vertex is not in the graph")
#             # get out degree
#             elif command == "6":
#                 try:
#                     vertex = int(input("Enter the vertex: "))
#                     print("The out degree of the vertex is: " + str(self.__graph.get_out_degree(vertex)))
#                 except ValueError:
#                     print("Invalid input")
#                 except VertexException:
#                     print("The vertex is not in the graph")
#             # get outbound edges
#             elif command == "7":
#                 try:
#                     vertex = int(input("Enter the vertex: "))
    #                 print("The set of outbound edges of the vertex is: ")
    #                 for vertex in self.__graph.outbound_iterator(vertex):
    #                     print(vertex, end=" ")
    #             except ValueError:
    #                 print("Invalid input")
    #         # get inbound edges
    #         elif command == "8":
    #             try:
    #                 vertex = int(input("Enter the vertex: "))
    #                 print("The set of inbound edges of the vertex is: ")
    #                 for vertex in self.__graph.inbound_iterator(vertex):
    #                     print(vertex, end=" ")
    #             except ValueError:
    #                 print("Invalid input")
    #         # get nr of edges
    #         elif command == "9":
    #             try:
    #                 print(f"The number of edges are {self.__graph.get_nr_of_edges()} and the set of edges is: ")
    #                 for edge in self.__graph.edges_iterator():
    #                     print(edge, end=" ")
    #             except ValueError:
    #                 print("Invalid input")
    #         # add vertex
    #         elif command == "10":
    #             try:
    #                 vertex = int(input("Enter the vertex to be added: "))
    #                 self.__graph.add_vertex(vertex)
    #                 print("The vertex was added successfully")
    #             except ValueError:
    #                 print("Invalid input")
    #             except VertexException:
    #                 print("The vertex is already in the graph")
    #         # add edge
    #         elif command == "11":
    #             try:
    #                 vertex1 = int(input("Enter the first vertex of the edge to be added: "))
    #                 vertex2 = int(input("Enter the second vertex of the edge to be added: "))
    #                 cost = int(input("Enter the cost: "))
    #                 self.__graph.add_edge(vertex1, vertex2, cost)
    #                 print("The edge was added successfully")
    #             except ValueError:
    #                 print("Invalid input")
    #             except EdgeException:
    #                 print("The edge is already in the graph")
    #         # remove vertex
    #         elif command == "12":
    #             try:
    #                 vertex = int(input("Enter the vertex to be removed: "))
    #                 self.__graph.remove_vertex(vertex)
    #                 print("The vertex was removed successfully")
    #             except ValueError:
    #                 print("Invalid input")
    #             except VertexException:
    #                 print("The vertex is not in the graph")
    #         # remove edge
    #         elif command == "13":
    #             try:
    #                 vertex1 = int(input("Enter the first vertex of the edge to be removed: "))
    #                 vertex2 = int(input("Enter the second vertex of the edge to be removed: "))
    #                 self.__graph.remove_edge(vertex1, vertex2)
    #                 print("The edge was removed successfully")
    #             except ValueError:
    #                 print("Invalid input")
    #             except EdgeException:
    #                 print("The edge is not in the graph")
    #         # set cost
    #         elif command == "14":
    #             try:
    #                 vertex1 = int(input("Enter the first vertex: "))
    #                 vertex2 = int(input("Enter the second vertex: "))
    #                 cost = int(input("Enter the cost to be set: "))
    #                 self.__graph.set_cost(vertex1, vertex2, cost)
    #                 print("The cost was set successfully")
    #             except ValueError:
    #                 print("Invalid input")
    #             except EdgeException:
    #                 print("The edge is not in the graph")
    #         # save to file
    #         elif command == "15":
    #             file_name = input("Enter file name where you want to save the graph: ")
    #             self.__graph.save_graph_to_file(file_name)
    #             print("The graph was saved successfully")
    #         # copy graph
    #         elif command == "16":
    #             try:
    #                 copied_graph = Graph()
    #                 copied_graph.copy_graph(self.__graph)
    #                 copied_graph.save_graph_to_file("copied_graph.txt")
    #                 print("The graph was copied successfully")
    #             except Exception:
    #                 print("Some error occurred")
    #         # exit
    #         elif command == "x":
    #             return
    #         else:
    #             print("Invalid command")
    #
    # @staticmethod
    # def print_main_menu():
    #     print("""
    #     ---> Main menu <---
    #     1 - Get the number of vertices
    #     2 - Parse the set of vertices
    #     3 - Check if an edge exists
    #     4 - Get the cost of an edge
    #     5 - Get the in degree of a vertex
    #     6 - Get the out degree of a vertex
    #     7 - Parse the set of outbound edges of a vertex
    #     8 - Parse the set of inbound edges of a vertex
    #     9 - Parse the set of edges
    #     10 - Add a new vertex
    #     11 - Add a new edge
    #     12 - Remove a vertex
    #     13 - Remove an edge
    #     14 - Modify the cost of an edge
    #     15 - Save the graph to a file
    #     16 - Copy the graph and save it to copied_graph.txt
    #     x - Exit
    #     """)


# having the UndirectedGraph class and the model of user interface for directed graph, create a UserInterface class for undirected graph

class UserInterface:
    def __init__(self):
        self.__graph = UndirectedGraph()

    @staticmethod
    def print_start_menu():
        print("""
              1 - Read graph from a file
              2 - Generate a random graph and save it to random_graph.txt
              x - Exit
              """)

    def start(self):
        while True:
            UserInterface.print_start_menu()
            command = input("Enter command: ")
            if command == "1":
                file_name = input("Enter file name: ")
                self.__graph.read_graph_from_file(file_name)
                self.main_menu()
            elif command == "2":
                try:
                    vertices = int(input("Enter the number of vertices: "))
                    edges = int(input("Enter the number of edges: "))
                    self.__graph = generate_random_graph(vertices, edges)
                    self.__graph.save_graph_to_file("random_graph.txt")
                    print("The graph was generated successfully")
                    self.main_menu()
                except ValueError:
                    print("Invalid input")
            elif command == "x":
                return
            else:
                print("Invalid command")

    def print_main_menu(self):
        print("""
        ---> Main menu <---
        1 - Get the number of vertices
        2 - Parse the set of vertices
        3 - Check if an edge exists
        4 - Get the degree of a vertex
        5 - Parse the set of neighbours of a vertex
        6 - Parse the set of edges 
        7 - Add a new vertex
        8 - Add a new edge
        9 - Remove a vertex
        10 - Remove an edge
        11 - Save the graph to a file
        12 - Connected Components
        x - Exit
        """)

    def main_menu(self):
        while True:
            self.print_main_menu()
            command = input("Enter command: ")
            # get number of vertices
            if command == "1":
                print("The number of vertices is: " + str(self.__graph.get_number_of_vertices()))

            # parse the set of vertices
            elif command == "2":
                print("The set of vertices is:")
                for vertex in self.__graph.vertices_iterator():
                    print(vertex, end=" ")

            # check if an edge exists
            elif command == "3":
                try:
                    vertex1 = int(input("Enter the first vertex: "))
                    vertex2 = int(input("Enter the second vertex: "))
                    if self.__graph.is_edge(vertex1, vertex2):
                        print("The edge exists")
                    else:
                        print("The edge does not exist")
                except ValueError:
                    print("Invalid input")

            # get the degree of a vertex
            elif command == "4":
                try:
                    vertex = int(input("Enter the vertex: "))
                    print("The degree of the vertex is: " + str(self.__graph.get_degree(vertex)))
                except ValueError:
                    print("Invalid input")

            # parse the set of neighbours of a vertex
            elif command == "5":
                try:
                    vertex = int(input("Enter the vertex: "))
                    print("The set of neighbours is:")
                    for neighbour in self.__graph.neighbours_iterator(vertex):
                        print(neighbour, end=" ")
                except ValueError:
                    print("Invalid input")

            # parse the set of edges
            elif command == "6":
                print("The set of edges is:")
                for edge in self.__graph.edges_iterator():
                    print(edge, end=" ")

            # add a new vertex
            elif command == "7":
                try:
                    vertex = int(input("Enter the vertex: "))
                    self.__graph.add_vertex(vertex)
                    print("The vertex was added successfully")
                except ValueError:
                    print("Invalid input")
                except VertexException:
                    print("The vertex already exists")

            # add a new edge
            elif command == "8":
                try:
                    vertex1 = int(input("Enter the first vertex: "))
                    vertex2 = int(input("Enter the second vertex: "))
                    self.__graph.add_edge(vertex1, vertex2)
                    print("The edge was added successfully")
                except ValueError:
                    print("Invalid input")
                except EdgeException:
                    print("The edge already exists")

            # remove a vertex
            elif command == "9":
                try:
                    vertex = int(input("Enter the vertex: "))
                    self.__graph.remove_vertex(vertex)
                    print("The vertex was removed successfully")
                except ValueError:
                    print("Invalid input")
                except VertexException:
                    print("The vertex does not exist")

            # remove an edge
            elif command == "10":
                try:
                    vertex1 = int(input("Enter the first vertex: "))
                    vertex2 = int(input("Enter the second vertex: "))
                    self.__graph.remove_edge(vertex1, vertex2)
                    print("The edge was removed successfully")
                except ValueError:
                    print("Invalid input")
                except EdgeException:
                    print("The edge does not exist")

            # save the graph to a file
            elif command == "11":
                file_name = input("Enter file name: ")
                self.__graph.save_graph_to_file(file_name)
                print("The graph was saved successfully")

            # connected components
            elif command == "12":
                print("The connected components are:")
                nr = 1
                for component in self.__graph.connected_components():
                    print("--->Component " + str(nr) + ":")
                    print("Vertices:", end=" ")
                    for vertex in component.vertices_iterator():
                        print(vertex, end=" ")
                    print("\nEdges:", end=" ")
                    for edge in component.edges_iterator():
                        print(edge, end=" ")
                    print("\n")
                    nr += 1

            # exit
            elif command == "x":
                return

            else:
                print("Invalid command")






