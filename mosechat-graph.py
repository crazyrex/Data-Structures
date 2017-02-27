
from graph import Node
from graph import Graph

graph = Graph()

graph.addNode(Node("a"))
graph.addNode(Node("b"))
graph.addNode(Node("c"))

print(graph.nodesToString())
