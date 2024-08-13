"""
Implementation of DFS in Python

Done By: Sujal Thakkar
"""


graph = {
    "A" : ["B","C","D"],
    "B" : ["E"],
    "C": ["D","E"],
    "D":[],
    "E":[]
}

# root node is : A
def dfs(visited,graph,root):
    """
    This is our Depth-First Search Function where we will be traversing
    to one by one each node, starting from root and print every node.
    :param visited: it is nothing but the set where we will be storing our visited nodes
    :param graph: the input data, as whole, which states which node is connected to which.
    :param root: Starting node, if not mentioned we can pick randomly
    :return: Return the printed outcome of all the visited nodes
    """
    if root not in visited:
        print(root)
        visited.add(root) #adding it to visited array
        for neighbour in graph[root]:
            #fetching the value of A i.e = ["B","C","D"] in each iteration
            dfs(visited,graph,neighbour) #picking anyone of 3


if __name__ == "__main__":
    print("ROOT NODE : A")
    visited = set()  # which will contains all the nodes which are already been visited

    dfs(visited,graph,"A") #keeping the root node as A
    print("ROOT NODE: B")
    visited = set()  # which will contains all the nodes which are already been visited
    dfs(visited,graph,"B") #keeping the root node as C

