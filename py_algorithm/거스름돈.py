# 문제
# 사용자가 N원을 낼 때 500원 , 100원, 50원 10원으로 낼 수 있는 최소 개수를 구하라




coin_500 = 500
coin_100 = 100
coin_50 = 50
coin_10 = 10

user_money =int(input("사용할 금액을 입력해주세요 : "))


#1
# coin_500_num = int(user_money / coin_500)
# user_money -= coin_500_num * coin_500

# coin_100_num = int(user_money / coin_100) 
# user_money -= coin_100_num * coin_100

# coin_50_num = int(user_money / coin_50)
# user_money -= coin_50_num * coin_50

# coin_10_num = int(user_money / coin_10) 
# user_money -= coin_10_num * coin_10

# print("coin 개수 : " + str(coin_500_num + coin_100_num + coin_50_num + coin_10_num))


#2 
coin_repo = [coin_500, coin_100, coin_100, coin_10]
total_coin_num = 0
for i in range (0, 4) :
    # a // b : 몫
    # a % b : 나머지
    coin_num = int(user_money/coin_repo[i])
    user_money -= coin_repo[i] * coin_num
    total_coin_num += coin_num
    

print("coin 개수 : " + str(total_coin_num))