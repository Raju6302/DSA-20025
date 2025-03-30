from __future__ import annotations
from collections import defaultdict
from typing import DefaultDict, List, Tuple, Any

class WeightedGraph:
    """
    Implements a weighted graph using an adjacency list.
    
    Each edge has an associated weight. In the adjacency list,
    each vertex maps to a list of tuples where each tuple contains:
      (neighboring vertex, weight)
    The graph can be either directed or undirected; here we assume an undirected graph,
    but the implementation can be easily adapted to directed graphs.
    """

    def __init__(self) -> None:
        """
        Initializes an empty weighted graph.
        """
        self.adj_list: DefaultDict[Any, List[Tuple[Any, float]]] = defaultdict(list)

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

    def add_edge(self, vertex1: Any, vertex2: Any, weight: float) -> bool:
        """
        Adds an undirected weighted edge between vertex1 and vertex2.
        If the vertices do not exist, they are added to the graph.
        
        Args:
            vertex1: The first vertex.
            vertex2: The second vertex.
            weight: The weight of the edge.
            
        Returns:
            True upon successful addition of the edge.
        """
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)
        
        # For undirected graph, add edge in both directions.
        if not any(neighbor == vertex2 for neighbor, _ in self.adj_list[vertex1]):
            self.adj_list[vertex1].append((vertex2, weight))
        if not any(neighbor == vertex1 for neighbor, _ in self.adj_list[vertex2]):
            self.adj_list[vertex2].append((vertex1, weight))
        return True

    def remove_edge(self, vertex1: Any, vertex2: Any) -> bool:
        """
        Removes the undirected edge between vertex1 and vertex2.
        
        Args:
            vertex1: The first vertex.
            vertex2: The second vertex.
            
        Returns:
            True if the edge was found and removed; False otherwise.
        """
        removed = False
        
        if vertex1 in self.adj_list:
            new_list = [pair for pair in self.adj_list[vertex1] if pair[0] != vertex2]
            if len(new_list) != len(self.adj_list[vertex1]):
                self.adj_list[vertex1] = new_list
                removed = True
        
        if vertex2 in self.adj_list:
            new_list = [pair for pair in self.adj_list[vertex2] if pair[0] != vertex1]
            if len(new_list) != len(self.adj_list[vertex2]):
                self.adj_list[vertex2] = new_list
                removed = True
        
        return removed

    def remove_vertex(self, vertex: Any) -> bool:
        """
        Removes a vertex and all its associated edges from the graph.
        
        Args:
            vertex: The vertex to remove.
            
        Returns:
            True if the vertex was removed; False if the vertex does not exist.
        """
        if vertex not in self.adj_list:
            return False

        # Remove the vertex from other vertices' lists.
        for other_vertex in list(self.adj_list.keys()):
            self.adj_list[other_vertex] = [
                (neighbor, weight)
                for neighbor, weight in self.adj_list[other_vertex]
                if neighbor != vertex
            ]
        
        # Remove the vertex itself.
        del self.adj_list[vertex]
        return True

    def __repr__(self) -> str:
        """
        Returns a string representation of the weighted graph.
        """
        result = []
        for vertex, edges in self.adj_list.items():
            edges_str = ", ".join(f"({neighbor}, weight: {weight})" for neighbor, weight in edges)
            result.append(f"{vertex} -> [{edges_str}]")
        return "\n".join(result)


# ----------------- Working Example for WeightedGraph ----------------- #

if __name__ == "__main__":
    w_graph = WeightedGraph()
    
    # Add weighted edges.
    w_graph.add_edge("A", "B", 4.5)
    w_graph.add_edge("A", "C", 2.0)
    w_graph.add_edge("B", "C", 1.5)
    w_graph.add_edge("B", "D", 3.0)
    w_graph.add_edge("C", "D", 2.5)
    
    print("Weighted Graph:")
    print(w_graph)
    
    # Remove an edge.
    w_graph.remove_edge("A", "C")
    print("\nAfter removing edge A-C:")
    print(w_graph)
    
    # Remove a vertex.
    w_graph.remove_vertex("B")
    print("\nAfter removing vertex B:")
    print(w_graph)