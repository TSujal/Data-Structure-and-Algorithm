"""
PYTHON : Dictionary
JAVA: HASH MAP and LINKED-HASH-MAP
C++ : std::map
"""
# we will be implementing hash table using dictionary in python

class HashTable:
    def __init__(self):
        self.MAX =10
        self.arr = [[] for i in range(self.MAX)] #list comprehension
        # we are storing key value pair in the list
#first step is to write a hash function
    def get_hash(self,key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __setitem__(self,key,value):
        """add an item to the hash map, and get an value from the hash map
        """
        h = self.get_hash(key) #for a given key it will give us a index value
        #for march 6 => h = 9
        #self.arr[h] = value

        found = False
        for idx, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                self.arr[h][idx] = (key,value)
                found =True
                break
        if not found:
            self.arr[h].append((key,value)) #if the key does not exists in the list


    def __getitem__(self,key):
        h = self.get_hash(key)
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __delitem__(self,key):
        h = self.get_hash(key)
        #self.arr[h] = None
        for index, kv in enumerate(self.arr[h]):
            if kv[0] == key:
                del self.arr[h][index]



#so basically we are picking up each key and taking its asci value and storing in the memory by taking the index number by %100

if __name__ == '__main__':
    ht = HashTable()
    #print("Index: ",ht.get_hash('march 17'))
    #ht.add('march 6',130)
    #print(ht.arr)
    #print(ht.get_hash('march 6'))
    #print("value:",ht.get('march 6'))
    ht["march 6"]= 130   #using __setitem__
    print(ht["march 6"])   #using __getitem__

    ht["march 1"] = 20
    ht["march 17"] = 120 #when using %10
    #it points index 9 and even march 6 points same
    # so it overrights the last implemented value in the table
    ht["dec 19"] = 21
    #print(ht.arr)
    #print(ht["dec 19"])

    #del ht["march 1"]
    #print(ht.arr)

    #effect of collision
    #we have store march 6 = 130
    # march 17 = 120
    print("Value of march 6:",ht["march 6"]) # it prints 120 because of collision
    print(ht.arr)
    del ht["march 17"]
    print(ht.arr)
    print(ht["dec 19"])