class Heap :
    def __init__(self, data) :
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def insert(self, data) :
        self.heap_array.append(data)
        cur_index = len(self.heap_array) -1
        while cur_index > 1 : 
            parent_index = cur_index // 2
            if self.heap_array[parent_index] < data :
                temp = self.heap_array[parent_index]
                self.heap_array[parent_index] = data
                self.heap_array[cur_index] = temp
                cur_index = parent_index
                # swap 코드
                # self.heap_array[cur_index], self.heap_array[parent_index] = self.heap_array[parent_index], self.heap_array[cur_index]
            else :
                break

    def pop(self) :
        result = self.heap_array[1]
        last_index = len(self.heap_array) -1 
        self.heap_array[1], self.heap_array[last_index] = self.heap_array[last_index], self.heap_array[1]
        del self.heap_array[last_index]

        cur_index = 1
        while cur_index < last_index :
            left_index = cur_index * 2
            right_index = cur_index * 2 + 1
            if left_index > last_index-1 : 
                return result
            

            if (right_index > last_index-1 or self.heap_array[left_index] > self.heap_array[right_index]) :
                if self.heap_array[left_index] > self.heap_array[cur_index] :
                     self.heap_array[left_index],  self.heap_array[cur_index] =  self.heap_array[cur_index],  self.heap_array[left_index]
                     cur_index = left_index
                else : return result
            else :
                if self.heap_array[right_index] > self.heap_array[cur_index] :
                     self.heap_array[right_index],  self.heap_array[cur_index] =  self.heap_array[cur_index],  self.heap_array[right_index]
                     cur_index = right_index
                else : return result

       

        
heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
heap.pop()

print(heap.heap_array)

