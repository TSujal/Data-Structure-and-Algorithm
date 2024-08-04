import random

class Node:
    def __init__(self, value, level):
        """
        Initialize the node with the given value and level.
        :param value: The value that the node will store.
        :param level: The level of the node.
        """
        self.value = value
        self.forward = [None] * (level + 1)

class SkipList:
    def __init__(self, max_level, p=0.5):
        """
        Initialize the skip list with the given maximum level and probability.
        :param max_level: The maximum level the skip list can have.
        :param p: Probability used to determine the level of new nodes.
        """
        self.max_level = max_level
        self.head = self.create_node(self.max_level, None)
        self.level = 0
        self.p = p

    def create_node(self, level, value):
        """
        Create a new node with the given level and value.
        :param level: The level of the new node.
        :param value: The value of the new node.
        """
        return Node(value, level)

    def random_level(self):
        """
        Generate a random level for node promotion.
        :return: The randomly generated level.
        """
        level = 0
        while random.random() < self.p and level < self.max_level:
            level += 1
        return level

    def insert(self, value):
        """
        Insert a value into the skip list.
        :param value: The value to be inserted.
        """
        update = [None] * (self.max_level + 1)
        current = self.head

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        current = current.forward[0]

        if not current or current.value != value:
            new_level = self.random_level()

            if new_level > self.level:
                for i in range(self.level + 1, new_level + 1):
                    update[i] = self.head
                self.level = new_level

            new_node = self.create_node(new_level, value)
            for i in range(new_level + 1):
                new_node.forward[i] = update[i].forward[i]
                update[i].forward[i] = new_node

            print(f"Inserted The given value: {value}")

    def delete(self, value):
        """
        Delete a value from the skip list.
        :param value: The value to be deleted.
        """
        update = [None] * (self.max_level + 1)
        current = self.head

        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
            update[i] = current
        current = current.forward[0]

        if current and current.value == value:
            for i in range(self.level + 1):
                if update[i].forward[i] != current:
                    break
                update[i].forward[i] = current.forward[i]

            while self.level > 0 and self.head.forward[self.level] is None:
                self.level -= 1

            print(f"Deleted the given value: {value}")

    def search(self, value):
        """
        Search for a value in the skip list.
        :param value: The value to be searched for.
        :return: True if the value is found, False otherwise.
        """
        current = self.head
        for i in range(self.level, -1, -1):
            while current.forward[i] and current.forward[i].value < value:
                current = current.forward[i]
        current = current.forward[0]
        if current and current.value == value:
            print(f"Found value: {value}")
            return True
        else:
            print(f" The given value does not exists: {value}")
            return False

    def display_skip_list(self):
        """
        Display the contents of the skip list level by level.
        """
        print("\n**** Skip List *****")
        for lvl in range(self.level + 1):
            print(f"Level {lvl}: ", end="")
            node = self.head.forward[lvl]
            while node:
                print(node.value, end=" ")
                node = node.forward[lvl]
            print("")

if __name__ == "__main__":
    slist = SkipList(50, 0.5)
    slist.insert(20)
    slist.insert(40)
    slist.display_skip_list()

    slist.search(40)
    slist.insert(30)
    slist.insert(33)
    slist.insert(10)
    slist.insert(60)
    slist.insert(44)
    slist.insert(21)
    slist.delete(20)
    slist.display_skip_list()
    slist.insert(77)
    slist.insert(77)
    slist.display_skip_list()
    slist.delete(77)
    slist.display_skip_list()

    # Additional insert and search operations
    slist.insert(2)
    slist.search(2)
    slist.search(10)
    slist.search(21)
    slist.search(77)

    slist.search(30)
    slist.display_skip_list()
    slist.search(60)
    slist.search(100)  # Value not in the skip list
    slist.search(33)

    slist.display_skip_list()  # Display the skip list
