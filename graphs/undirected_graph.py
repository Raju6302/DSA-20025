from __future__ import annotations
from collections import defaultdict
from typing import DefaultDict, List, Any


class UnDirectedGraph:
    """
    Implements a simple undirected graph using an adjacency list.
    """

    def __init__(self) -> None:
        """
        Initializes the graph with an empty adjacency list.
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

    def add_edge(self, vertex1: Any, vertex2: Any) -> bool:
        """
        Adds an undirected edge between vertex1 and vertex2.
        If the vertices do not exist, they are added to the graph.

        Args:
            vertex1: The first vertex.
            vertex2: The second vertex.

        Returns:
            True upon successful addition of the edge.
        """
        # Ensure both vertices exist.
        self.add_vertex(vertex1)
        self.add_vertex(vertex2)

        # Avoid duplicate edges.
        if vertex2 not in self.adj_list[vertex1]:
            self.adj_list[vertex1].append(vertex2)
        if vertex1 not in self.adj_list[vertex2]:
            self.adj_list[vertex2].append(vertex1)
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
        if vertex1 in self.adj_list and vertex2 in self.adj_list[vertex1]:
            self.adj_list[vertex1].remove(vertex2)
            removed = True

        if vertex2 in self.adj_list and vertex1 in self.adj_list[vertex2]:
            self.adj_list[vertex2].remove(vertex1)
            removed = True

        return removed

    def remove_vertex(self, vertex: Any) -> bool:
        """
        Removes a vertex and all associated edges from the graph.

        Args:
            vertex: The vertex to remove.

        Returns:
            True if the vertex was removed; False if the vertex does not exist.
        """
        if vertex not in self.adj_list:
            return False

        # Remove the vertex from other vertices' adjacency lists.
        for neighbor in self.adj_list[vertex]:
            self.adj_list[neighbor].remove(vertex)

        # Remove the vertex itself.
        del self.adj_list[vertex]
        return True

    def __repr__(self) -> str:
        """
        Returns a string representation of the graph's adjacency list.
        """
        result = []
        for vertex, neighbors in self.adj_list.items():
            result.append(f"{vertex}: {neighbors}")
        return "\n".join(result)


# ----------------- Working Example for UnDirectedGraph----------------- #

if __name__ == "__main__":
    # Create a graph instance.
    u_graph = UnDirectedGraph()

    # Add vertices.
    u_graph.add_vertex("A")
    u_graph.add_vertex("B")
    u_graph.add_vertex("C")
    u_graph.add_vertex("D")

    # Add edges.
    u_graph.add_edge("A", "B")
    u_graph.add_edge("A", "C")
    u_graph.add_edge("B", "C")
    u_graph.add_edge("C", "D")

    print("Graph after adding vertices and edges:")
    print(u_graph)

    # Remove an edge.
    u_graph.remove_edge("A", "C")
    print("\nGraph after removing the edge between A and C:")
    print(u_graph)

    # Remove a vertex.
    u_graph.remove_vertex("B")
    print("\nGraph after removing vertex B:")
    print(u_graph)