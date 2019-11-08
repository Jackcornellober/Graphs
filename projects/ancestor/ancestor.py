from util import Graph

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()
    for pair in ancestors:
        if pair[0] not in graph.vertices:
            graph.add_vertex(pair[0])
        if pair[1] not in graph.vertices:
            graph.add_vertex(pair[1])
        graph.add_edge(pair[1],pair[0])
    if graph.find_ancestor(starting_node) == starting_node:
        print('my name is bruce wayne and i have no parents')
        return -1
    else:
        return graph.find_ancestor(starting_node)