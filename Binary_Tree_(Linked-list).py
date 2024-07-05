#building a Tree basic structure
class TreeNode:
    def __init__(self, data, children= []):
        self.data = data
        self.children = children

    def __str__(self,level=0):
        set = " " * level + str(self.data) + "\n"
        for child in self.children:
            set += child.__str__(level + 1)
        return  set

    def addchild(self, TreeNode):
        self.children.append(TreeNode)
"""
tree = TreeNode("Drinks",[])
cold = TreeNode("Cold",[])
hot = TreeNode("Hot",[])
tree.addchild(cold)
tree.addchild(hot)
tea = TreeNode("Tea",[])
coffee = TreeNode("Coffee",[])
cola = TreeNode("Cola",[])
fanta = TreeNode("Fanta",[])
pepsi = TreeNode("Pepsi",[])
ice = TreeNode("Ice",[])
not_ice = TreeNode("Not Ice",[])
pepsi.addchild(ice)
pepsi.addchild(not_ice)
cola.addchild(ice)
cola.addchild(not_ice)
fanta.addchild(ice)
fanta.addchild(not_ice)
hot.addchild(tea)
hot.addchild(coffee)
cold.addchild(pepsi)
cold.addchild(cola)
cold.addchild(fanta)
print(tree)
"""

# Creating a binary tree using Linked list
## using Pre-Order Traversal method

class Tree_node:
    def __init__(self, data):
        self.data = data
        self.left_children = None
        self.right_children = None

def pre_order_traversal(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    pre_order_traversal(rootNode.left_children) #this means we are calling this function recursively until the very left child is been visited
    pre_order_traversal(rootNode.right_children) #then recusriely calling right child
    #THE FIRST RECURSIVE FUNCTION IS GOING TO GIVE RUN TIME OF O(N/2)
    #THE SECOND RECURSIVE FUNCITON IS GOING TO GIVE THE RUN TIME OF O(N/2)
# TOTAL time complexity of this function is Constant O(n)

def in_order_traversal(rootNode):
    if not rootNode:
        return
    in_order_traversal(rootNode.left_children) #=> O(n/2)
    print(rootNode.data)
    in_order_traversal(rootNode.right_children) # ==> O(n/2)
    #TOTAL WILL BE O(N) COMPLEXITY

def post_order_traversal(rootNode):
    if not rootNode:
        return
    post_order_traversal(rootNode.left_children)
    post_order_traversal(rootNode.right_children)
    print(rootNode.data)


import Queue_Linked_List as queue
## fifo
def level_order_traversal(rootNode):
    if not rootNode:
        return
    else:
        customQueue = queue.Queue() #CREATING A CUSTOM QUEUE
        customQueue.enqueue(rootNode)
        while not(customQueue.isEmpty()):
            node = customQueue.dequeue() #TAKES OUT THE FIRST IN FIRST OUT ELEMENT
            print(node.value.data)
            if node.value.left_children is not None:
                customQueue.enqueue(node.value.left_children)
            if node.value.right_children is not None:
                customQueue.enqueue(node.value.right_children)

## THE TIME COMPLEXITY OF THE FUNCTION IS O(N) BECAUSE OF WHILE LOOP


##SEARCHING AN ELEMENT IN A BINARY TREE
# we will be using Level order traversal because of queue which gives accurate results.
def Search(rootNode,value):
    if not rootNode:
        return "No Root Node"
    else:
        custom_queue = queue.Queue()
        custom_queue.enqueue(rootNode)
        while not(custom_queue.isEmpty()):
            node = custom_queue.dequeue()
            if node.value.data == value:
                return "The node exists in the Tree"
            if node.value.left_children is not None:
                custom_queue.enqueue(node.value.left_children)
            if node.value.right_children is not None:
                custom_queue.enqueue(node.value.right_children)
        return "The Node does not exist in the Tree"
#the run time of this could be O(n)


## Making a insert method which will insert a node in the Binary Tree
# it will traverse and find a first vacant place where it will insert that particular node
def insert(rootNode,newNode):
    """
    :param rootNode: the assignment of root node
    :param value: the value which we want to insert into the vacant place of the tree
    :return: the TREE with the inserted value
    """
    if not rootNode:
        rootNode = newNode
    else:
        custom_queue = queue.Queue() #creating a custom queue for level order traversal
        custom_queue.enqueue(rootNode)
        while not(custom_queue.isEmpty()):
            node = custom_queue.dequeue()
            if node.value.left_children is not None:
                custom_queue.enqueue(node.value.left_children)
            else:
                node.value.left_children = newNode
                return "Successfully inserted the node"

            if node.value.right_children is not None:
                custom_queue.enqueue(node.value.right_children)
            else:
                node.value.right_children = newNode
                return "Successfully inserted the node"
## the time complexity for this function is O(n)

def get_deepest_node(rootNode):
    """
    To perform the deleting of any node in the binary tree, we first need to get the last node
    :param rootNode: defining the root of the binary tree
    :return: gives us the last leaf node of the binary tree
    """
    if not rootNode:
        return "No root for the binary tree"
    else:
        custom_queue = queue.Queue()
        custom_queue.enqueue(rootNode)
        while not(custom_queue.isEmpty()):
            node = custom_queue.dequeue()
            if node.value.left_children is not None:
                custom_queue.enqueue(node.value.left_children)
            if node.value.right_children is not None:
                custom_queue.enqueue(node.value.right_children)
        deepest_node = node.value
        return deepest_node
## time and space complexity is O(n), we are just doing the level order traversal here.....


def delete(rootNode, dNode):
    """
    we got the deepest node in the above function, now we will be deleting that by swapping it with
    deepest node.
    :param rootNode: root node for our binary tree
    :param dNode: the node which is the deepest and which we will be deleting
    :return: returns the binary tree without that dNode
    """
    if not rootNode:
        return "No root node for the binary tree"
    else:
        custom_queue = queue.Queue()
        custom_queue.enqueue(rootNode)
        while not(custom_queue.isEmpty()):
            node = custom_queue.dequeue()
            #check what if the last node is only node which we want to delete
            if node.value is dNode:
                node.value = None
                return
            #check for right child
            if node.value.right_children:
                if node.value.right_children is dNode:
                    node.value.right_children = None
                    return
                else:
                    custom_queue.enqueue(node.value.right_children)
            #check now the left child
            if node.value.left_children:
                if node.value.left_children is dNode:
                    node.value.left_children = None
                    return
                else:
                    custom_queue.enqueue(node.value.left_children)

#if you want to delete the whole binary tree from the memory
def deleteBT(rootNode):
    rootNode.data = None
    rootNode.left_child = None
    rootNode.right_child = None
    return "The binary tree is been successfully delete"





print("----------------------------------------------------------------------")
new_BT = Tree_node("Drinks")#Root node
#The time and space complexity of this is O(1) ie Constant
left_child = Tree_node("Hot")
right_child = Tree_node("Cold")
new_BT.left_children = left_child
new_BT.right_children = right_child

print("-----------------------------------------------------------------------")
print("NEW BT:",new_BT)
pre_order_traversal(new_BT)
post_order_traversal(new_BT)
level_order_traversal(new_BT)
in_order_traversal(new_BT)

print("-----------------------------------------------------------------------")

print("Check",Search(new_BT,"Drinks"))
print("Check",Search(new_BT,"drinks"))
print("-----------------------------------------------------------------------")
print("Using insert function to insert any node")
newNode = Tree_node("ST")
print(insert(new_BT,newNode))
level_order_traversal(new_BT)
print("-----------------------------------------------------------------------")
print("Get the deepest node")
deepest_node = get_deepest_node(new_BT)
print("Your deepest node for the binary tree is:",deepest_node.data)
print("-----------------------------------------------------------------------")
print("Deleting the specific node")
new_node = get_deepest_node(new_BT) #get the deepestnode
delete(new_BT,new_node) #we are deleting the node which is already last ie ST
level_order_traversal(new_BT)



