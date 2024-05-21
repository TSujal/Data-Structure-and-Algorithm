class Node:
    def __init__(self,data=None,next=None):
        self.data=data #this data is nothing but the information data
        self.next=next #this next is nthing but the next node where our address will be stored
class LinkedList:
    def __init__(self):
        self.head= None #initially the head will be none

    def insert_at_beginning(self,data):
        """
        :param data: contains the data/infomation which needs to be stored at the beginning spot
        :return: a printed statements.....about the data in a mannerd way
        """
        node = Node(data,self.head) #making a node where the data will be made and making the exisiting node head as next node
        self.head = node
    def print(self):
        if self.head is None:#is the head of the node is empty then...
            print("Linked list is empty !!!!!")
            return

        itr = self.head
        llstr = " "
        while itr:
            llstr += str(itr.data) + "-->"
            itr = itr.next
        print(llstr)

    def insert_at_end(self,data):
        """
        Here we are adding the element ie Data to the end of the linked list
        :param data:  is the information/data which needs to be stored at the end of the linkedlist
        :return: and return the new linked list by adding the data/information at the end of the linkedlist
        """
        if self.head is None:
            self.head = Node(data, None)
            return
        #if the linkedlist is not empty
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data,None)


    def insert_values(self,data_list):
        """
        Here this function will make a new linked list based on the given data
        :param data_list: takes in this data
        :return: a new linked list <<<--->>>
        """
        self.head = None
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        """
        Here this function counts the length of the list
        :return: the count of the list --
        """
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self,index):
        if index < 0 or index > self.get_length():
            raise Exception("Index out of range")
        if index==0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count +=1

    def insert_at(self,index,data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid Index")
        if index ==0: #if the index is given to be at 0th position
            self.insert_at_beginning(data)
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data,itr.next)
                itr.next = node
                break

            itr = itr.next
            count += 1

    def insert_after_value(self, data_after, data_to_insert):
        """
        Search for the first occurance of data_after value in the linked list
        then now insert data_to_insert after the data_after
        :param data_after: is the data we need to find already in the linked list
        :param data_to_insert:  is the data we need to append after the data_after value
        :return: return the linked list after inserting data_to_insert
        """
        if data_after is None:
            raise Exception("This particular data does not exists in the linked list")
        #count = 0
        itr = self.head
        while itr:
            if itr.data == data_after:
                #index = count + 1
                new_node = Node(data_to_insert,itr.next)
                itr.next = new_node
                return
            itr = itr.next

        raise ValueError("This particular data does not exists in the linked list")
    def remove_by_value(self,data):
        """
        Here we do need to search through the linked list and remove
        that particular value from that linked list
        :param data: is the data which already exists and we need to remove from linked list
        :return: a linked list by removing that particular value from linked list
        """


if __name__ == '__main__':
    l1 = LinkedList() #creating a LinkedList
    l1.insert_at_beginning(5)
    l1.insert_at_beginning(20)
    l1.insert_at_beginning(25)
    l1.insert_at_end(33)
    l1.insert_at_end(9870)
    l1.print()
    print("The length of the linked list: ",l1.get_length())#this will count the length of the linked list
    #lets create a new linked list

    l1.insert_values(["sujal","Roshni","Vansh","Hitesh"])
    l1.print()
    print("The length of the linked list: ", l1.get_length())
    l1.remove_at(2) #i want to remove "VANSH" from the LIST
    l1.print()
    l1.insert_at(3,"MOM")
    l1.print()
    l1.insert_at(1,"Father")
    l1.print()
    l1.insert_after_value("sujal","Mummy")
    l1.print()