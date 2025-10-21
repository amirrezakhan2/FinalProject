import random
class Array:
    def __init__(self, size):
        self.array = [None] * size
        self.size = size
        self.useful = 0

    def insert(self, data):
        if self.useful == self.size:
            return -1
        self.array[self.useful] = data
        self.useful += 1

    def __getitem__(self, index):
        if index > self.size - 1 or index < 0:
            return -1
        return self.array[index]

    def __repr__(self):
        return str(self.array)
    
    def slice_array(self,start,end):
        result =Array(end - start)
        for j in range(start,end):
            result.insert(self.array[j])
        return result
    def __len__(self):
        return self.size


class Hash:
    def __init__(self):
        self.HashTable = [None] * 10
        self.loadfactor = 0.7
        self.useful = 0
        self.size = 10
        self.DELETED = "DELETED"

    def hashfunction(self, key):
        return int(key) % self.size

    def insert(self, key, Node):
        key = int(key)
        index = self.hashfunction(key)
        if self.search(key) is False:
            original_index = index
            while self.HashTable[index] is not None and self.HashTable[index] != self.DELETED:
                index = (index + 1) % self.size
                if index == original_index:
                    raise Exception("HashTable is full")
            self.HashTable[index] = Node
            self.useful += 1
            if self.useful / self.size >= self.loadfactor:
                self.incerase_hash()
        else:
            return False

    def search(self, key):
        key = int(key)
        index = self.hashfunction(key)
        original_index = index
        while self.HashTable[index] is not None:
            if self.HashTable[index] != self.DELETED and self.HashTable[index].key == key:
                return self.HashTable[index]
            index = (index + 1) % self.size
            if index == original_index:
                break
        return False

    def delete(self, key):
        key = int(key)
        index = self.hashfunction(key)
        original_index = index
        while self.HashTable[index] is not None:
            if self.HashTable[index] != self.DELETED and self.HashTable[index].key == key:
                self.HashTable[index] = self.DELETED
                self.useful -= 1
                return True
            index = (index + 1) % self.size
            if index == original_index:
                break
        return False

    def incerase_hash(self):
        old_hash_table = self.HashTable
        self.size *= 2
        self.HashTable = [None] * self.size
        self.useful = 0
        for node in old_hash_table:
            if node is not None and node != self.DELETED:
                key = node.key
                self.insert(key, node)
    def change_key(self, old_key, new_key):
        node = self.search(old_key)
        if not node:
            return False  
        self.delete(old_key)
        node.key = int(new_key)
        self.insert(new_key, node)
        return True

    def __getitem__(self, index):
        if index > self.size - 1:
            return -1
        return self.HashTable[index]

    def __repr__(self):
        return str(self.HashTable)

    def __len__(self):
        return self.size

class DllNode:
    def __init__(self,data):
        self.data = data 
        self.next = None 
        self.prev = None 


class Linklist:
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
    def insert(self,data): 
        new_node = DllNode(data)
        if self.head == None :
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node 
        self.count +=1
    def linsert(self,data):
        new_node = DllNode(data)
        if self.tail == None :
            self.head = new_node 
            self.tail = new_node
        else:
          self.tail.next = new_node
          new_node.prev = self.tail 
          self.tail = new_node 
        self.count +=1
    def find(self,value):
        temp = self.head 
        while temp:
            if temp.data == value:
                return True
            else:
                temp = temp.next
    def delete(self,value):
        temp = self.head 
        while temp:
            if temp.data == value:
                if temp.prev == None:
                    self.head = temp.next 
                    if self.head:
                        self.head.prev = None
                if temp.next == None:
                    self.tail = temp.prev
                    self.tail.next = None 
                else:
                 temp.prev.next = temp.next
                temp.next.prev = temp.prev 
                self.count -=1
                del temp 
                return
            else:
                temp = temp.next 
    def __len__(self):
        return self.count

    def __repr__(self):
        temp = self.head
        if not temp:
            return "🚫 Empty Doubly Linked List 🚫"

        result = "HEAD 🎯 "
        while temp:
            result += f"⬅️ [{temp.data}] ➡️ "
            temp = temp.next
        result += "🏁 TAIL"
        return result



class BST:
    def __init__(self):
        self.root = None 
    def insert(self,Node):
        if self.root == None :
            self.root = Node
            return
        return self.recureseive_insert(self.root,Node)
    def recureseive_insert(self,root,Node):
        if Node.key < root.key :
            if root.left == None :
                root.left = Node 
                root.left.parent = root
            else:
                self.recureseive_insert(root.left,Node)
        if Node.key > root.key :
            if root.right == None :
                 root.right = Node
                 root.right.Parent = root 
            else:  
                self.recureseive_insert(root.right,Node)

    def search(self,key):
        key = int(key)
        return self.recureseive_search(self.root,key)

    def recureseive_search(self,root,key):
        key = int(key)
        if root == None :
            return False
        if root.key == key:
            return root
        if key< root.key:
            return self.recureseive_search(root.left,key)
        else:
            return self.recureseive_search(root.right,key)
        
    
    def find_min(self, node):
        while node.left:
            node = node.left
        return node
    

    def Delelte_Node(self,node):
        if node == None:
            return None

        if node.left == None and node.right == None:
            Parent = node.Parent
            if Parent:
                if Parent.left == node:
                    Parent.left = None 
                elif Parent.right == node:
                 Parent.right = None
            else:
                self.root == None 

            return node

        if node.left == None or node.right == None:
            Parent = node.Parent
            child = node.left if node.left else node.right
            if Parent:
                if Parent.right == node:
                    Parent.right = child
                    child.Parent = Parent
                    node.Parent = None
                else:
                    Parent.left = child
                    child.Parent = Parent
            else:
                self.root = child 

            return node

        else:
            substitute = self.find_min(node.right)
            node.serial = substitute.serial
            node.name = substitute.name
            node.date = substitute.Date
            node.plate = substitute.plate
            node.color = substitute.color
            node.National = substitute.National
            node.key = substitute.serial
            self.Delelte_Node(substitute)

    def Delete(self,key):

        node = self.recureseive_search(self.root,key)
        if node:
              return self.Delelte_Node(node)
    
        
        
    def in_order(self, root):
        result = ''
        if root is not None:
            result += self.in_order(root.left)
            if hasattr(root, 'color') and root.color:
                result += f"{root.serial} | {root.name} | {root.plate} |  {root.National} | {root.color} | {root.Date} \n"
            else:
                result += f"{root.serial} | {root.Cityname} | {root.plate} |  {root.National} |  activite = {root.Status}\n"
            result += self.in_order(root.right)
        return result

    def __repr__(self):
        return str(self.in_order(self.root))

class BaseNode:
    def __init__(self,key):
        self.key = key 
        self.left = None
        self.right = None 
        self.Parent = None
    


class DynamicArray:
    def __init__(self):
        self.size = 10
        self.array = [None] * self.size 
        self.useful = 0 
    def insert(self,value):
        if self.useful == self.size :
            self.increasearray()
        self.array[self.useful] = value
        self.useful += 1
    def increasearray(self):
        old_array = self.array
        self.size = self.size * 2
        self.array = [None] * self.size 
        for i in range(len(old_array)):
            self.array[i] = old_array[i]
    def __len__(self):
        return self.useful
    
    def __getitem__(self,index):
        return self.array[index]
    
    def __repr__(self):
        return str(self.array[:self.useful])
    def __setitem__(self, index, value):
        if 0 <= index < self.useful:
            self.array[index] = value
        else:
            raise IndexError("Index out of range")
    def restartArray(self):
        self.size = 10
        self.array = [None] * self.size 
        self.useful = 0 


        
          
            




