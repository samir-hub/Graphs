from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        if vertex_id in self.vertices:
            #print("WARNING: That vertex already exists")
            pass
        else:
            self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_parents(self, vertex_id):
        """
        Get parents (edges) of a vertex.
        """
        return self.vertices[vertex_id]    



def earliest_ancestor(ancestors, starting_vertex):
    graph = Graph()
    for i in ancestors: 
        graph.add_vertex(i[0])
        graph.add_vertex(i[1])
        graph.add_edge(i[1], i[0])
    # Create an empty stack
    s = Stack()
    # Add A PATH TO the starting vertex_id to the queue
    s.push([starting_vertex])
    # Create an empty set to store visited nodes
    visited = set()
    results = []
    # While the queue is not empty...
    while s.size() > 0:
        # Dequeue, the first PATH
        p = s.pop()
        # GRAB THE LAST VERTEX FROM THE PATH
        last_vertex = p[-1]
        # CHECK IF IT'S THE TARGET
        if len(graph.get_parents(last_vertex)) == 0:
            results.append(p)
            # IF SO, RETURN THE PATH    
        # Check if it's been visited
        if last_vertex not in visited:
        # If it has not been visited...
            # Mark it as visited
            visited.add(last_vertex)
            # Then add A PATH TO all neighbors to the back of the queue
                # (Make a copy of the path before adding)
            for neighbor in graph.get_parents(last_vertex):
                copy = p.copy()
                copy.append(neighbor)
                s.push(copy) 
    if results[-1][-1] == starting_vertex: 
        return -1  
    if len(results) == 1:
        return results[-1][-1]                   
    if len(results[-1]) > len(results[-2]):
        return results[-1][-1]
    if results[-1][-1] < results[-2][-1]:
        return results[-1][-1]
    else: 
        return results[-2][-1]    


    
test = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]    
print(earliest_ancestor(test, 1))




# s = Stack()
#     # Push the starting vertex_id to the stack
#     s.push(starting_vertex)
#     # Create an empty set to store visited nodes
#     visited = []
#     # While the stack is not empty...
#     while s.size() > 0:
#         # Pop the first vertex
#         v = s.pop()
#         # Check if it's been visited
#         # If it has not been visited...
#         if v not in visited:
#             # Mark it as visited
#             visited.append(v)
#             # Then push all parents to the top of the stack
#             for parent in graph.get_parents(v):
#                 s.push(parent)
#     return visited  