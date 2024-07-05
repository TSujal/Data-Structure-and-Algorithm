## Creating Binary Search Tree

class BSTNode:
    def __init__(self,data):
        self.data = data
        self.left_child = None
        self.right_child = None

    #insert a node in BST
def insert(rootnode,nodevalue):
    if rootnode.data == None:
        rootnode.data = nodevalue
    elif nodevalue <= rootnode.data:
        #we will continuing with the left child
        if rootnode.left_child is None:
            rootnode.left_child = BSTNode(nodevalue)
        else:
            insert(rootnode.left_child,nodevalue) #==> O(n/2)
    else:
        #we will be continuing with the right child here
        if rootnode.right_child is None:
            rootnode.right_child = BSTNode(nodevalue)
        else:
            insert(rootnode.right_child, nodevalue) #=> O(n/2)

    return "Node is successfully inserted into the BST..."
## the time complexity O(logn) time complexity...
## the space complexity O(logn)

    ## TRAVERSAL IN BST
def preOrderTraversal(rootNode):
    if rootNode is None:
        return "There is no Root Node in the BST"
    print(rootNode.data)
    preOrderTraversal(rootNode.left_child)
    preOrderTraversal(rootNode.right_child)
    #time and space complexity == O(n)

## In-Order Traversal
def InOrderTraversal(rootNode):
    if rootNode is None:
        return "There is no Root node in your BST..!!"
    InOrderTraversal(rootNode.left_child)#first the left child
    print(rootNode.data)
    InOrderTraversal(rootNode.right_child)
    #the time and space complexity is O(n) again here

## Post Order Traversal
def PostOrderTraversal(rootNode):
    if rootNode is None:
        return "There is no Root"
    PostOrderTraversal(rootNode.left_child)
    PostOrderTraversal(rootNode.right_child)
    print(rootNode.data)
    #the time and space complexity is O(n)


## Level order traversal
import Queue_Linked_List as queue
#FIFO
def levelOrderTraversal(rootNode):
    if rootNode is None:
        return "There is no root"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not customQueue.isEmpty():
            node = customQueue.dequeue()
            print(node.value.data)
            if node.value.left_child is not None:
                customQueue.enqueue(node.value.left_child)
            if node.value.right_child is not None:
                customQueue.enqueue(node.value.right_child)
#the time and space complexity is O(n)

def searchNode(rootNode, value):
    if rootNode.data == value:
        return "Found the value"
    elif value < rootNode.data:
        if rootNode.left_child == value:
            return "Found the value"
        else:
            searchNode(rootNode.left_child, value)#--> O(n/2)
    else:
        if rootNode.right_child == value:
            return "Found the value"
        else:
            searchNode(rootNode.right_child, value) #--> O(n/2)
    return "Value found.."
## Time and space complexity of the given function is: O(log n)


## Deleting a node in the binary search tree
## with all the 3 case, leaf,1child,2child.....
## Remember Successor : is the minimum value node in the right subtree
def minValueNode(bstNode):
    """
    To delete any value CASE 3, we are writing the function
    to get the minvalue in the BST
    :param bstNode: BST
    :return: return the minimum node value in the BST
    """
    current = bstNode
    while current.left_child is not None:
        #we are traversing to left sub tree because min_value will be last left value of the left subtree
        current = current.left_child
    return current


#Delete function
def deleteNode(rootNode, value):
    if rootNode is None:
        return rootNode
    if value < rootNode.data:
        rootNode.left_child = deleteNode(rootNode.left_child, value)## --> O(n/2)
    elif value > rootNode.data:
        rootNode.right_child = deleteNode(rootNode.right_child,value) ## --> O(n/2)
    else:
        if rootNode.left_child is None:
            temp = rootNode.right_child
            rootNode = None
            return temp
        if rootNode.right_child is None:
            temp = rootNode.left_child
            rootNode = None
            return temp

        temp = minValueNode(rootNode.right_child)#successor ##---> O(log n)
        rootNode.data = temp.data
        rootNode.right_child = deleteNode(rootNode.right_child, temp.data) ##--> O(n/2)
    return rootNode

## time complexity O(log n)
## Space complexity O(log n)




#creating the bst time complexity is O(1) and space complexity 0(1)
newBST = BSTNode(None)
print(insert(newBST,70))#currently it is at none so it will be creating rootnode as 70
print(insert(newBST,50))
print(insert(newBST,90))
print(insert(newBST,30))
print(insert(newBST,60))
print(insert(newBST,80))
print(insert(newBST,100))
insert(newBST,20)
insert(newBST,40)

print("Root node:",newBST.data)##thats going to be printing the root node value
print("Left child: ",newBST.left_child.data) #that's going to be printing the left child's
print("Right child:",newBST.right_child.data)
print("---------------------------")
print("Pre-Order-TRaversal BST...")
preOrderTraversal(newBST) # which will traverse first root->left->right
print("---------------------------")
print("In-Order Traversal BST....")
InOrderTraversal(newBST)
print("---------------------------")
print("In-Order-Traversal BST....")
InOrderTraversal(newBST)


print("-------------------------------")
print("Levell order Traversal")
levelOrderTraversal(newBST)

print("----------------------------")
print("Searching a value in the BST...")
print(searchNode(newBST,40))

print("---------------------------------------")
print("Delete method")
deleteNode(newBST,70)
levelOrderTraversal(newBST)