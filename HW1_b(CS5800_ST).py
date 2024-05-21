class LinkedL:
    def __init__(self,x):
        self.value = x
        self.next = None
    def len_of_Node(head):
        """
        Counts the length of the elements in the linkedlist
        :param head: given linked list
        :return: return the length of the elements in the linkedlist in int
        """
        count = 0
        current = head
        while current is not None:
            count += 1
            current = current.next
        return count

    def Intersection(headA,headB):
        """
        Finds the intersection of two linked lists
        :param headA, headB: two linked lists:
        :return: intersection node of the two linked lists
        """
        countA = LinkedL.len_of_Node(headA)
        countB = LinkedL.len_of_Node(headB)
        if countA > countB:
            d = countA - countB
            for i in range(d):
                headA = headA.next
        else:
            d = countB -countA
            for i in range(d):
                headB =headB.next
        while headA is not None and headB is not None:
            if headA == headB:
                return headA
            headA = headA.next
            headB = headB.next
        return None
    def showcase(head):
        current = head
        while current:
            print(current.value,end='=>')
            current = current.next
        print("")
if __name__ == '__main__':
    intersection = LinkedL(9)
    intersection.next = LinkedL(11)
    intersection.next.next = LinkedL(13)

    # Creating the non-intersecting parts
    headA = LinkedL(1)
    headA.next = LinkedL(3)
    headA.next.next = LinkedL(5)
    headA.next.next.next = LinkedL(7)
    headA.next.next.next.next = intersection

    headB = LinkedL(2)
    headB.next = LinkedL(4)
    headB.next.next = intersection

    # Print the lists
    print("List A:")
    LinkedL.showcase(headA)
    print("List B:")
    LinkedL.showcase(headB)

    # Find the intersection node
    intersectionNode = LinkedL.Intersection(headA, headB)

    # Print the result
    if intersectionNode:
        print(f"Intersection node value: {intersectionNode.value}")
    else:
        print("No intersection found")