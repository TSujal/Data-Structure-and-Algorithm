## creating binary tree using Python list
class BinaryTree:
    def __init__(self,size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size



## Insert a value node in to binary tree
    def insert(self,value):
        if self.lastUsedIndex +1 == self.maxSize:
            return "The binary Tree is Full"

        #if the list if not full then we add the value to the custom list lastUSedIndex+1 index position the new value
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex +=1
        return "The value is been successfully inserted!!!"
    #the time complexity = O(1)
    #space complexity = O(1),as we r just adding new element in the list

### Search for a node in a binary tree
    #we will be traversing using level-order-traversal
    def searchNode(self,nodeValue):
        for i in range(len(self.customList)):
            if self.customList[i] == nodeValue:
                return "Success we found the node with the matching value"
        return "The node not found!!"
    #the time complexity of this given function is O(n)
    #space complexity is O(1).


## PRe-order traversal
## ROOT -> LEft -> Right
    def preOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        print(self.customList[index])
        self.preOrderTraversal(index*2) #left child
        self.preOrderTraversal(index*2 + 1) #right child
#So in this case it will traverse first to root node
#then all left child
#then all right child
    ##the time complexity is O(n)
    ## the space complexity is O(n)

    ## In-Order Traversal
## Left subtree -> root -> Right subTree
    def inOrderTraversal(self,index):
        if index > self.lastUsedIndex:
            return
        self.inOrderTraversal(index*2) #left child
        print(self.customList[index]) #root node
        self.inOrderTraversal(index*2 + 1) #right child
##the time complexity is O(n)
## the space complexity is O(n)

    ## Post order Traversal
# LEft -> right -> root
    def postOrderTraversal(self,index):
        if index  > self.lastUsedIndex:
            return
        self.postOrderTraversal(index*2)
        self.postOrderTraversal(index*2 +1)
        print(self.customList[index])
## the time complexity and space remains O(n)


    ## Level order traversal
    def levelOrderTraversal(self,index):
        for i in range(index,self.lastUsedIndex+1):
            print(self.customList[i])


    #delete node
    def deleteNode(self,nodeValue):
        if self.lastUsedIndex ==0:
            return "The binary Tree is empty"
        for i in range(1,self.lastUsedIndex+1):
            if self.customList[i] == nodeValue:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -=1
                return  "The node has been successfully deleted!!"
    #time and space complexity is O(n)
    #space complexity is O(1)


    #Delete an Entire BT
    def deleteBT(self):
        if self.lastUsedIndex ==0:
            return "The binary Tree is empty"
        self.customList = None
        return "the binary tree is been deleted "
    ## O(1) and O(1) for space and time complexity



#creating a new binary tree
newBT = BinaryTree(8) #keeping the size == 8

#uptil now the run time complexity of the binary tree creation upill now code is O(1)
#however the space complexity is O(n), ie the size occupied.

print("Inserting a new value in the binary tree")
print(newBT.insert("Drinks"))#root node
print(newBT.insert("Hot"))#left node
print(newBT.insert("Cold")) #right node
print(newBT.insert("Tea"))#child of HOT-left child
print(newBT.insert("Coffee"))#child of HOT-right child

print("Let's search A value ...")
print(newBT.searchNode("Hot"))
print(newBT.searchNode("Choclate"))

print("-------------------------------------")
print("Pre-order traversal...")
newBT.preOrderTraversal(1)
print("-------------------------------------")
print("In-Order Traversal")
newBT.inOrderTraversal(1)
print("-------------------------------------")
print("Post Order Traversal....")
newBT.postOrderTraversal(1)

print("========================-----------")
print("Level order traversal")
newBT.levelOrderTraversal(1)

print("---------------------------------------")
print("Delete a node")
print(newBT.deleteNode("Hot"))
newBT.levelOrderTraversal(1)

print("===========================================")
print("Deleting entire BT")
print(newBT.deleteBT())
newBT.levelOrderTraversal(1)