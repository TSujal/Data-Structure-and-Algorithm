"""
Implementation of DFS using Stack in Python

Done By: Sujal Thakkar
"""

graph = {
    "A" : ["B", "C", "D"],
    "B" : ["E"],
    "C" : ["D", "E"],
    "D" : [],
    "E" : []
}

def dfs_stack(graph, root):
    """
    This is our Depth-First Search Function where we will be traversing
    each node using a stack starting from the root and printing every node.
    :param graph: the input data, as a whole, which states which node is connected to which.
    :param root: Starting node, if not mentioned we can pick randomly.
    :return: Returns the printed outcome of all the visited nodes.
    """
    visited = set()  # to track visited nodes
    stack = [root]  # initialize the stack with the root node

    while stack:
        node = stack.pop()  # remove and return the last element from the stack

        if node not in visited:
            print(node)
            visited.add(node)  # mark the node as visited

            # Add all unvisited neighbors to the stack
            for neighbour in reversed(graph[node]):
                if neighbour not in visited:
                    stack.append(neighbour)

if __name__ == "__main__":
    print("ROOT NODE : A")
    dfs_stack(graph, "A")  # starting the DFS from node "A"
