num = int(input("숫자를 입력하세요 : "))
sum = 1



for i in range(1, num +1):
    sum =sum*i

if not num == -1:
    print(" %d! = %d" %(num,sum))

