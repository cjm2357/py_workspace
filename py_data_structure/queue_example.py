import queue

# #FIFO Queue (일반적인)
# data_queue = queue.Queue()
# data_queue.put("encoding")
# data_queue.put(123)

# print(data_queue.get())
# print(data_queue.get())
# print(data_queue.qsize())

# #LIFO Queue (Stack과 비슷)
# data_queue2 = queue.LifoQueue()
# data_queue2.put("input first")
# data_queue2.put("input second")

# print(data_queue2.qsize())
# print(data_queue2.get())
# print(data_queue2.get())

# #Priority Queue (우선 순위 큐)
# data_queue3 = queue.PriorityQueue()
# # 첫번째 인자 우선순위 , 두번째 인자 큐에 넣을 값
# # tuple () 로 삽입한다
# data_queue3.put((10, "A"))
# data_queue3.put((5, "B"))
# data_queue3.put((20, "C"))

# print(data_queue3.qsize())
# # tuple 형태로 출력
# print(data_queue3.get())
# print(data_queue3.get())
# print(data_queue3.get())

#List변수로 Queue를 만들어 보기
queue_list = []

def put(data) :
    queue_list.append(data)

def get() :
    if (len(queue_list) < 1) :
        print("no data")
        return 
    
    result = queue_list[0]
    # queue_list.remove(result)
    del queue_list[0]
    return result

put(1)
put(2)
put(3)

print(get())
print(get())
print(get())

