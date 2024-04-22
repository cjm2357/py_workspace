class Node:
    def __init__(self, value) :
        self.value = value
        self.left = None
        self.right = None

class NodeMgmt: 
    def __init__(self, head) :
        self.head = head

    def insert(self, value) :
        # newNode = Node(value)
        # if self.head == None :
        #     self.head = newNode
        # else :
        #     if (self.head.value > value) :
        #         if (self.head.left) :
        #             self.insert(value)
        #         else :
        #             self.head.left = newNode
        #     else :
        #         if (self.head.right) :
        #             self.insert(value)
        #         else :
        #             self.head.right = newNode
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if (self.current_node.left != None) :
                    self.current_node = self.current_node.left
                else :
                    self.current_node.left = Node(value)
                    break
            else :
                if self.current_node.right != None :
                    self.current_node = self.current_node.right
                else :
                    self.current_node.right = Node(value)
                    break

    def search(self, value) :
        current_node = self.head
        while current_node:
            if current_node.value == value :
                return current_node.value
            elif (current_node.value < value) :
                current_node = current_node.right
            else :
                current_node = current_node.left
        return None
    
    def delete(self, value) :
        # 먼저 data가 없는지 확인
            searched = False
            self.current_node = self.head
            self.parent_node = None

            while self.current_node:
                if self.current_node.value == value :
                    searched = True
                    break
                elif self.current_node.value < value :
                    self.parent_node = self.current_node
                    self.current_node = self.current_node.right
                else : 
                    self.parent_node = self.current_node
                    self.current_node = self.current_node.left

            if searched == False :
                return False
            
            # Case 1 Leaf Node
            if self.current_node.left == None and self.current_node.right == None :
                if (self.parent_node.value > self.current_node.value) :
                    self.parent_node.left = None
                else :
                    self.parent_node.right = None
                
                del self.current_node

            # Case 2 Child Node가 한쪽에 만 가지고 있을 경우
            elif self.current_node.left != None and self.current_node.right == None :
                if (self.parent_node.value > self.current_node.value) :
                    self.parent_node.left = self.current_node.left
                else :
                    self.parent_node.right = self.current_node.left

                del self.current_node

            elif self.current_node.left == None and self.current_node.right != None :
                if (self.parent_node.value > self.current_node.value) :
                    self.parent_node.left = self.current_node.right
                else :
                    self.parent_node.right = self.current_node.right

                del self.current_node

            # Case 3 : 삭제할 노드가 left right 둘다 가질때
            # 3-1-1 삭제할 노드가 parent node기준 왼쪽에 있고 
            # child node가 없을 때
            else :
                if self.parent_node.value > self.current_node.value :
                    change_node = self.current_node.right
                    change_node_parent = self.current_node.right
                    while change_node.left :
                        change_node_parent = change_node
                        change_node = change_node.left
            
                    self.parent_node.left = change_node
                    change_node.left = self.current_node.left
                
                    change_node_parent.left = None
                    if change_node.right :
                        change_node_parent.left = change_node.right
                    
                    change_node.right = self.current_node.right
                # 3-2-1 삭제할 노드가 parent node기준 오른쪽에 있고 
                # child node가 없을 때
                else :
                    change_node = self.current_node.right
                    change_node_parent = self.current_node.right
                    while change_node.left :
                        change_node_parent = change_node
                        change_node = change_node.left

                    self.parent_node.right = change_node
                    change_node.left = self.current_node.left

                    change_node_parent.left = None
                    if change_node.right :
                        change_node_parent.left = change_node.right
                    
                    change_node.right = self.current_node.right
                del self.current_node
            



                    


head = Node(10)
tree = NodeMgmt(head)
tree.insert(3)
tree.insert(5)
tree.insert(7)
tree.insert(11)
tree.insert(13)
print(head.left.value)
print(head.right.value)
tree.delete(3)
print(tree.search(3))
print("-------------------")

# Test
import random
# 1~1000 중 100개의 숫자insert
num_set = set()
while len(num_set) != 100 :
    num_set.add(random.randint(0, 999))

# 임의로 500인 root node 생성
root = Node(500)
tree = NodeMgmt(root)
for num in num_set :
    tree.insert(num)

for num in num_set :
    print(tree.search(num))


del_nums = set()
while len(del_nums) != 10 :
    del_nums.add(random.randint(0,999))

for num in del_nums :
    print(tree.delete(num))
