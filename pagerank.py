import numpy as np
import random

def create_random_graph(num_nodes: int, num_links: int):
    graph = {i: [] for i in range(num_nodes)}
    
    # Generate random links
    while len([link for links in graph.values() for link in links]) < num_links:
        # Choose a random source node and a random target node
        source = random.randint(0, num_nodes - 1)
        target = random.randint(0, num_nodes - 1)
        
        # Avoid self-loops and duplicate links
        if source != target and target not in graph[source]:
            graph[source].append(target)

    return graph

def pagerank(graph, num_iterations: int = 100, d: float = 0.85):
    num_pages = len(graph)
    pr = np.ones(num_pages) / num_pages
    M = np.zeros((num_pages, num_pages))
    
    for i, links in graph.items():
        if links:
            for j in links:
                M[j, i] = 1 / len(links)
        else:
            for j in range(num_pages):
                M[j, i] = 1 / num_pages

    for _ in range(num_iterations):
        pr = (1 - d) / num_pages + d * np.dot(M, pr)

    return pr

# Example usage
if __name__ == "__main__":
    num_nodes = 20
    num_links = 250
    graph = create_random_graph(num_nodes, num_links)
    
    ranks = pagerank(graph)
    print("PageRank Values:", ranks)
