from __future__ import annotations
from collections import defaultdict
from typing import DefaultDict, List, Any

class DirectedGraph:
    """
    Implements a directed graph using an adjacency list.
    
    In a directed graph, edges have a direction (from source to destination),
    meaning that if there is an edge from A to B, it does not imply an edge from B to A.
    """

    def __init__(self) -> None:
        """
        Initializes an empty directed graph.
        """
        self.adj_list: DefaultDict[Any, List[Any]] = defaultdict(list)

    def add_vertex(self, vertex: Any) -> bool:
        """
        Adds a vertex to the graph. If the vertex already exists, no action is taken.
        
        Args:
            vertex: The vertex to add.
            
        Returns:
            True if the vertex was added; False if it already exists.
        """
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []
            return True
        return False

    def add_edge(self, source: Any, destination: Any) -> bool:
        """
        Adds a directed edge from source to destination.
        If the vertices do not exist, they are added to the graph.
        
        Args:
            source: The source vertex.
            destination: The destination vertex.
            
        Returns:
            True upon successful addition of the edge.
        """
        self.add_vertex(source)
        self.add_vertex(destination)
        
        # To avoid duplicate edges, check before appending.
        if destination not in self.adj_list[source]:
            self.adj_list[source].append(destination)
        return True

    def remove_edge(self, source: Any, destination: Any) -> bool:
        """
        Removes the directed edge from source to destination.
        
        Args:
            source: The source vertex.
            destination: The destination vertex.
            
        Returns:
            True if the edge was found and removed; False otherwise.
        """
        if source in self.adj_list and destination in self.adj_list[source]:
            self.adj_list[source].remove(destination)
            return True
        return False

    def remove_vertex(self, vertex: Any) -> bool:
        """
        Removes a vertex and all its outgoing edges from the graph.
        Additionally, removes the vertex from any other vertices' adjacency lists.
        
        Args:
            vertex: The vertex to remove.
            
        Returns:
            True if the vertex was removed; False if the vertex does not exist.
        """
        if vertex not in self.adj_list:
            return False
        
        # Remove the vertex from all adjacency lists.
        for src in list(self.adj_list.keys()):
            if vertex in self.adj_list[src]:
                self.adj_list[src].remove(vertex)
        
        # Remove the vertex's own list.
        del self.adj_list[vertex]
        return True

    def __repr__(self) -> str:
        """
        Returns a string representation of the graph's adjacency list.
        """
        result = []
        for vertex, neighbors in self.adj_list.items():
            result.append(f"{vertex} -> {neighbors}")
        return "\n".join(result)


# ----------------- Working Example for DirectedGraph ----------------- #

if __name__ == "__main__":
    d_graph = DirectedGraph()
    
    # Add vertices and edges.
    d_graph.add_edge("A", "B")
    d_graph.add_edge("A", "C")
    d_graph.add_edge("B", "C")
    d_graph.add_edge("C", "D")
    
    print("Directed Graph:")
    print(d_graph)
    
    # Remove an edge.
    d_graph.remove_edge("A", "C")
    print("\nAfter removing edge A -> C:")
    print(d_graph)
    
    # Remove a vertex.
    d_graph.remove_vertex("B")
    print("\nAfter removing vertex B:")
    print(d_graph)