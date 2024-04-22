hash_table = list([0 for i in range(10)])
print(hash_table)

# division 법을 이용한 hash 함수
# 나머지 return 
def hash_func(key) :
    return key%5 

data1 = "Andy"
data2 = "Dave"
data3 = "Trump"

# ord() 문자의 ASCII 코드리턴
print(ord(data1[0]))

def storage_data(data, value) :
    # 데이터를 가지고 key 값을 만듬
    key = ord(data[0])
    # key값을 이용해 hash_adress를 만듬
    hash_adress = hash_func(key)
    hash_table[hash_adress] = value

def get_data(data) :
    key = ord(data[0])
    hash_adress = hash_func(key)
    return hash_table[hash_adress]

storage_data("Andy", "01055553333")
storage_data("Dave", "01012341234")
storage_data("Trump", "01099999999")

print(get_data("Dave"))

print("------------------")

hash_table2 = list([0 for i in range(8)])

#chaining 기법
def put(key, value) :
    index_key = hash(key)
    hash_addres = index_key%8
    if hash_table2[hash_addres] != 0 :
        for index in range(len(hash_table2[hash_addres])) :
            if hash_table2[hash_addres][index][0] == index_key :
                hash_table2[hash_addres][index][1] == value
                return
            
        hash_table2[hash_addres].append([index_key, value])
    else :
        hash_table2[hash_addres] = [[index_key, value]]

#Linear Probing 기법
def put2(key, value) :
    index_key = hash(key)
    hash_addres = index_key%8
    if hash_table2[hash_addres] != 0 :
        for index in range(hash_addres, len(hash_table2)) :
            if hash_table2[index] == 0 :
                hash_table2[index] = [index_key, value]
                return
            elif hash_table2[index][0] == index_key :
                hash_table2[index][1] = value
                return
           
    else :
        hash_table2[hash_addres] = [index_key, value]
        
        


def get(key) :
    index_key = hash(key)
    hash_addres = index_key%8
    for i in range(len(hash_table2[hash_addres])) :
        if hash_table2[hash_addres][i][0] == index_key :
            return hash_table2[hash_addres][i][1]
    
    return None

def get2(key) :
    index_key = hash(key)
    hash_addres = index_key%8
    if (hash_table2[hash_addres] != 0) :
        for i in range(hash_addres, len(hash_table2)) :
            #초기화가 된적이 없기 때문에 그 이후의 index에 들어간 적이 없다. 
            if hash_table2[i] == 0 :
                return None
            elif hash_table2[i][0] == index_key :
                return hash_table2[i][1]
    
    
    return None

# print(hash("Dave")%8)
# print(hash("Daivid")%8)
# print(hash("Dd")%8)
# put("Dave", "010")
# put("Daivid", "011")
# put("Dd", "0123")
# print(get("Dave"))
# print(get("Daivid"))
# print(get("Dd"))
# print(hash_table2)

print("----------------")
print(hash("Dave")%8)
print(hash("Daivid")%8)
print(hash("Dd")%8)
put2("Dave", "010")
put2("Daivid", "011")
put2("Dd", "0123")
print(get2("Dave"))
print(get2("Daivid"))
print(get2("Dd"))
print(hash_table2)

print("--------------")
import hashlib

#byte로 바꿔주는 코드
data = 'test'.encode() 
hash_object = hashlib.sha1()
#-> b'string' 도 바이트로 바꿔줌
hash_object.update(b'test') 
#-> 몇진수로 추출할건지 (16진수)
hex_dig = hash_object.hexdigest()
print(hex_dig) 
# int로 변환 , 2번째 파라미터에 1번째 파리미터의 인수 삽입
int(hex_dig, 16)
 
