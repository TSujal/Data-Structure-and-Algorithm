class BinomialHeapNode:
    def __init__(self, key):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.sibling = None

    def __str__(self):
        return f"Node(key={self.key}, degree={self.degree})"
class BinomialHeap:
    def __init__(self):
        self.head = None

    def make_heap(self):
        """Creates and returns an empty Binomial Heap."""
        return BinomialHeap()

    def insert(self, key):
        """Inserts a new key into the Binomial Heap."""
        new_node = BinomialHeapNode(key)
        new_heap = self.make_heap()
        new_heap.head = new_node
        self.head = self.union(new_heap)

    def minimum(self):
        """Finds and returns the minimum key in the Binomial Heap."""
        if self.head is None:
            return None

        min_node = self.head
        current = self.head
        min_key = self.head.key
        while current is not None:
            if current.key < min_key:
                min_key = current.key
                min_node = current
            current = current.sibling

        return min_node

    def extract_min(self):
        """Removes and returns the minimum key from the Binomial Heap."""
        if self.head is None:
            return None

        # Find the minimum root and its previous node
        min_prev = None
        min_node = self.head
        min_key = self.head.key
        prev = None
        current = self.head
        while current is not None:
            if current.key < min_key:
                min_key = current.key
                min_prev = prev
                min_node = current
            prev = current
            current = current.sibling

        # Remove the minimum root from the root list
        if min_prev is None:
            self.head = min_node.sibling
        else:
            min_prev.sibling = min_node.sibling

        # Reverse the order of min_node's children and make them a new heap
        child = min_node.child
        prev_child = None
        while child is not None:
            next_child = child.sibling
            child.sibling = prev_child
            child.parent = None
            prev_child = child
            child = next_child
        new_heap = self.make_heap()
        new_heap.head = prev_child

        # Union the new heap with the current heap
        self.head = self.union(new_heap)

        return min_node.key

    def union(self, other):
        """Unites two Binomial Heaps into one and returns the new heap."""
        self.head = self._merge(self.head, other.head)
        if self.head is None:
            return self.head

        prev_x = None
        x = self.head
        next_x = x.sibling

        while next_x is not None:
            if (x.degree != next_x.degree or
                    (next_x.sibling is not None and next_x.sibling.degree == x.degree)):
                prev_x = x
                x = next_x
            else:
                if x.key <= next_x.key:
                    x.sibling = next_x.sibling
                    self._link(next_x, x)
                else:
                    if prev_x is None:
                        self.head = next_x
                    else:
                        prev_x.sibling = next_x
                    self._link(x, next_x)
                    x = next_x
            next_x = x.sibling

        return self.head

    def decrease_key(self, node, new_key):
        """Decreases the key of a given node in the Binomial Heap."""
        if new_key > node.key:
            raise ValueError("New key is greater than current key.")
        node.key = new_key
        y = node
        z = node.parent
        while z is not None and y.key < z.key:
            y.key, z.key = z.key, y.key
            y = z
            z = z.parent

    def delete(self, node):
        """Deletes a given node from the Binomial Heap."""
        self.decrease_key(node, float('-inf'))
        self.extract_min()

    def find_node(self, root, key):
        """Finds and returns the node with the specified key in the heap rooted at 'root'."""
        if root is None:
            return None
        if root.key == key:
            return root

        # Check the child and sibling nodes
        result = self.find_node(root.child, key)
        if result:
            return result
        return self.find_node(root.sibling, key)
    def _merge(self, h1, h2):
        """Merges two binomial heap root lists into a single sorted root list."""
        if h1 is None:
            return h2
        if h2 is None:
            return h1

        if h1.degree <= h2.degree:
            head = h1
            h1 = h1.sibling
        else:
            head = h2
            h2 = h2.sibling

        current = head
        while h1 is not None and h2 is not None:
            if h1.degree <= h2.degree:
                current.sibling = h1
                h1 = h1.sibling
            else:
                current.sibling = h2
                h2 = h2.sibling
            current = current.sibling

        if h1 is not None:
            current.sibling = h1
        else:
            current.sibling = h2

        return head

    def _link(self, y, z):
        """Links two binomial trees of the same order by making one the child of the other."""
        y.parent = z
        y.sibling = z.child
        z.child = y
        z.degree += 1


    def printing_heap(self):
        """
        Basically prints the binomial heap for us
        """
        def printing_tree(node,indent=""):
            while node is not None:
                print(indent + str(node))
                if node.child is not None:
                    printing_tree(node.child, indent + " ")
                node = node.sibling
        printing_tree(self.head)

if __name__ == '__main__':
    bh = BinomialHeap()
    bh1 = BinomialHeap()
    # Insert nodes
    bh.insert(10)
    bh.insert(1)
    bh.insert(6)
    bh.insert(12)
    bh.insert(33)
    bh.insert(4)
    bh.insert(9)
    print("Binomial Heap after inserts:")
    bh.printing_heap()

    # Print the minimum
    min_node = bh.minimum()
    print(f"Minimum node key: {min_node.key}")

    # Extract min
    min_key = bh.extract_min()
    print(f"Extracted min key: {min_key}")
    bh1.insert(7)
    bh1.insert(8)
    bh1.insert(12)
    bh1.insert(13)

    print("UNION")
    bh1.union(bh)

    bh1.printing_heap()

    print("Binomial Heap after extracting min:")
    bh.printing_heap()

    # Insert additional nodes
    bh.insert(20)
    bh.insert(5)
    bh.insert(8)
    print("Binomial Heap after inserting more nodes:")
    bh.printing_heap()

    # Decrease key of a specific existing node
    key_to_find = 8  # Key of the node whose key you want to decrease
    new_key = 3       # New key value for the node

    node_to_decrease = bh.find_node(bh.head, key_to_find)
    if node_to_decrease is not None:
        bh.decrease_key(node_to_decrease, new_key)
        print(f"Binomial Heap after decreasing key of node with key {key_to_find} to {new_key}:")
        bh.printing_heap()
    else:
        print(f"Node with key {key_to_find} not found.")

    # Delete node
    node_to_delete = bh.head
    if node_to_delete is not None:
        bh.delete(node_to_delete)

    print("Binomial Heap after deleting node:")
    bh.printing_heap()

    # Deleting a specific node
    key_to_delete = 9
    node_to_delete = bh.find_node(bh.head, key_to_delete)
    if node_to_delete is not None:
        bh.delete(node_to_delete)
        print(f"Deleted node with key: {key_to_delete}")
    else:
        print(f"Node with key {key_to_delete} not found.")
    print(f"Binomial heap after deleting the node with value {key_to_delete}:")
    bh.printing_heap()
