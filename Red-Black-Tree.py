class Node:
    def __init__(self,data,color="red"):
        self.data = data
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(data=None,color = "black")
        self.root = self.NIL

    def rotate_left(self,x):
        y = x.right
        x.right = y.left
        if y.left != self.NIL:
            y.left.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y
        y.left = x
        x.parent = y

    def rotate_right(self,x):
        y = x.left
        x.left = y.right
        if y.right != self.NIL:
            y.right.parent = x
        y.parent = x.parent
        if x.parent == self.NIL:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y
        y.right = x
        x.parent = y

    def insert_fixup(self, z):
        while z.parent.color == 'red':
            if z.parent == z.parent.parent.left:
                y = z.parent.parent.right
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.right:
                        z = z.parent
                        self.rotate_left(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.rotate_right(z.parent.parent)
            else:
                y = z.parent.parent.left
                if y.color == 'red':
                    z.parent.color = 'black'
                    y.color = 'black'
                    z.parent.parent.color = 'red'
                    z = z.parent.parent
                else:
                    if z == z.parent.left:
                        z = z.parent
                        self.rotate_right(z)
                    z.parent.color = 'black'
                    z.parent.parent.color = 'red'
                    self.rotate_left(z.parent.parent)
        self.root.color = 'black'

    def insert(self, data):
        z = Node(data)
        y = self.NIL
        x = self.root
        while x != self.NIL:
            y = x
            if z.data < x.data:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y == self.NIL:
            self.root = z
        elif z.data < y.data:
            y.left = z
        else:
            y.right = z
        z.left = self.NIL
        z.right = self.NIL
        z.color = 'red'
        self.insert_fixup(z)

    def search(self,node,data):
        if node == self.NIL or data == node.data:
            return node
        if data < node.data:
            #data is less then root so search left side
            return self.search(node.left,data)
        else:
            #search in the right side
            return self.search(node.right, data)

    def min(self,node):
        #to find the minimum of the value
        #which will be in the left most corner
        while node.left != self.NIL:
            node = node.left
        return node

    def max(self,node):
        #to find the max of the value
        #which will be in the right most side
        while node.right !=self.NIL:
            node = node.right
        return node

    def successor(self,x):
        #we need to find the successor of given value x node
        # successor: RIGHT SUB TREE SMALLEST NODE
        if  x.right != self.NIL:
            return self.min(x.right)
        y = x.parent
        while y != self.NIL and x == y.right:
            x = y
            y = y.parent
        return y

    def predecessor(self,x):
        if x.left != self.NIL:
            return self.max(x.left)
        y = x.parent
        while y != self.NIL and x == y.left:
            x = y
            y = y.parent
        return y

    def inorder_traversal(self,node,result):
        if node != self.NIL:
            self.inorder_traversal(node.left,result)
            result.append(node.data)
            self.inorder_traversal(node.right,result)


    #let's calculate the height
    def calculate_height(self,node):
        if node == self.NIL:
            #if empty tree or no root node
            return 0
        else:
            left_height = self.calculate_height(node.left)
            right_height = self.calculate_height(node.right)
            return max(left_height,right_height) + 1

    #show case height
    def print_height(self):
        height = self.calculate_height(self.root)
        print("Height of the given tree :",height)

    def delete_fixup(self, x):
        while x != self.root and x.color == 'black':
            if x == x.parent.left:
                w = x.parent.right
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.rotate_left(x.parent)
                    w = x.parent.right
                if w.left.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.right.color == 'black':
                        w.left.color = 'black'
                        w.color = 'red'
                        self.rotate_right(w)
                        w = x.parent.right
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.right.color = 'black'
                    self.rotate_left(x.parent)
                    x = self.root
            else:
                w = x.parent.left
                if w.color == 'red':
                    w.color = 'black'
                    x.parent.color = 'red'
                    self.rotate_right(x.parent)
                    w = x.parent.left
                if w.right.color == 'black' and w.right.color == 'black':
                    w.color = 'red'
                    x = x.parent
                else:
                    if w.left.color == 'black':
                        w.right.color = 'black'
                        w.color = 'red'
                        self.rotate_left(w)
                        w = x.parent.left
                    w.color = x.parent.color
                    x.parent.color = 'black'
                    w.left.color = 'black'
                    self.rotate_right(x.parent)
                    x = self.root
        x.color = 'black'

    def transplant(self, u, v):
        if u.parent == self.NIL:
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def delete(self, data):
        z = self.search(self.root, data)
        if z == self.NIL:
            print("Node not found")
            return

        y = z
        y_original_color = y.color
        if z.left == self.NIL:
            x = z.right
            self.transplant(z, z.right)
        elif z.right == self.NIL:
            x = z.left
            self.transplant(z, z.left)
        else:
            y = self.min(z.right)
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color

        if y_original_color == 'black':
            self.delete_fixup(x)

        self.print_height()


# to make read the inputs from the selected file
def read_input_file(file_path):
    with open(file_path, 'r') as file:
        numbers = list(map(int, file.readlines()))
    return numbers

def build_tree_from_file(file_path, tree):
    numbers = read_input_file(file_path)
    for number in numbers:
        tree.insert(number)

def print_tree(node, indent, last):
    if node != tree.NIL:
        print(indent, end=' ')
        if last:
            print("R----", end=' ')
            indent += "   "
        else:
            print("L----", end=' ')
            indent += "|  "
        print(f"({node.data}, {node.color})")
        print_tree(node.left, indent, False)
        print_tree(node.right, indent, True)
# Passing the interactive commands from the user to the tree
def commands(tree):
    while True:
        command = input("Enter command: ")
        if command.startswith("insert"):
            _, value = command.split()
            tree.insert(int(value))
            tree.print_height()
        elif command == "sort":
            sorted_list = []
            tree.inorder_traversal(tree.root, sorted_list)
            print("Sorted list:", sorted_list)
            tree.print_height()
        elif command.startswith("search"):
            _, value = command.split()
            found = tree.search(tree.root, int(value))
            print("Found" if found != tree.NIL else "Not found")
            tree.print_height()
        elif command == "min":
            min_node = tree.min(tree.root)
            print("Min value:", min_node.data if min_node else "Tree is empty")
            tree.print_height()
        elif command == "max":
            max_node = tree.max(tree.root)
            print("Max value:", max_node.data if max_node else "Tree is empty")
            tree.print_height()
        elif command.startswith("successor"):
            _, value = command.split()
            node = tree.search(tree.root, int(value))
            successor = tree.successor(node)
            print("Successor:", successor.data if successor != tree.NIL else "No successor")
            tree.print_height()
        elif command.startswith("predecessor"):
            _, value = command.split()
            node = tree.search(tree.root, int(value))
            predecessor = tree.predecessor(node)
            print("Predecessor:", predecessor.data if predecessor != tree.NIL else "No predecessor")
            tree.print_height()
        elif command.startswith("delete"):
            _,value = command.split()
            tree.delete(int(value))
            #tree.print_height()

        elif command == "print":
            print_tree(tree.root, "", True)
        elif command == "exit":
            break
        else:
            print("Unknown command")


if __name__ == "__main__":
    tree = RedBlackTree() #obj of class
    file_path = input("Enter the path of the file:")
    build_tree_from_file(file_path,tree)

    print("Tree built from file. You can now enter the commands to interact with the tree.")
    commands(tree)