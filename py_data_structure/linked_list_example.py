class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class Node2:
    # self는 넣는 인자가 아니고, next는 넣으면 넣은값으로 안넣으면 None으로 들어간다. 
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


node1 = Node(1)
node2 = Node(2)
node1.next = node2
head = node1

def add(data):
    node = head
    while(node.next):
        node = node.next
    newNode = Node(data)
    node.next= newNode

for index in range(1,10) :
    add(index)

node = head 
while(node.next) :
    print(node.data)
    node = node.next
print(node.data)
print("---------------")

# 중간 삽입 코드
node = head 
search = True
while(search) :
    if (node.data == 3) :
        search = False 
    else :
        node = node.next
    
newNode = Node(3.5)
newNode.next= node.next
node.next= newNode


node = head 
while(node.next) :
    print(node.data)
    node = node.next
print(node.data)


class Node3 :
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class NodeMgmt:
    def __init__(self, data) :
        self.head = Node3(data)

    def add(self, data) :
        node = self.head
        while(node.next) :
            node = node.next
        newNode = Node3(data)
        node.next = newNode

    def desc(self) :
        node = self.head
        while(node) :
            print(node.data)
            node = node.next

    def delete(self, data) :
        if (self.head == ''):
            print ("해당 값을 가진 노드가 없습니다.")
            return
        
        
        if (self.head.data == data) :
            temp = self.head
            head = self.head.next
            del temp
        else :
           node = self.head
           target = None
           while node.next != None :
               if node.next.data == data :
                   target = node.next
                   break
               else :
                   node = node.next
           
        if target :
            node.next= target.next
            del target
        else :
            print("target 없음")
    
     

mgmt = NodeMgmt(0)
mgmt.add(3)
mgmt.add(1)
mgmt.add(2)
print("--------------")
mgmt.delete(2)
mgmt.desc()


class DoubleNode :
    def __init__ (self, data, prev=None, next=None) :
        self.data = data
        self.prev = prev
        self.next = next

class DoubleNodeMgmt :
    def __init__ (self, data):
        node = DoubleNode(data)
        self.head = node
        self.tail = node

    def insert(self, data) :
        if (self.head == None) :
            node = DoubleNode(data)
            self.head = node
            self.tail = node
        else :
            node = self.head
            while(node.next) :
                node = node.next
            newNode = DoubleNode(data, node)
            node.next = newNode
            self.tail = newNode

    def desc(self) :
        node = self.head
        while (node) :
            print(node.data)
            node = node.next

    def insert_forward(self, data, target_data) :
        target_node = self.search_from_head(target_data)
        if (target_node == self.head) : 
            newNode = DoubleNode(data)
            newNode.next = target_node
            target_node.prev = newNode


        if (target_node) :
            newNode = DoubleNode(data)
            if (target_node != self.head) :
                target_node.prev.next = newNode
                newNode.prev = target_node.prev
            else :
                self.head = newNode


            newNode.next= target_node
            target_node.prev = newNode
        
    
    def search_from_head(self, data) :
        node = self.head 
        result = None
        while(node) :
            if (node.data == data) :
                result = node
                break
            else :
                node = node.next

        return result
    
    def search_from_tail(self, data) :
        node = self.tail
        result = None
        while(node) :
            if (node.data == data) :
                result = data
                break
            else :
                node = node.prev

        return result

print("-----------------------") 
print("더블링크드 리스트")
doubleNodeMgmt = DoubleNodeMgmt(0)
for i in range(1, 10) :
    doubleNodeMgmt.insert(i)
doubleNodeMgmt.desc()
print("----------insert_foward-------------") 

doubleNodeMgmt.insert_forward(99, 0)
doubleNodeMgmt.desc()
    