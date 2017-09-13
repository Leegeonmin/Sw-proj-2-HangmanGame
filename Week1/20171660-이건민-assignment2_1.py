''' 20171660
    이건민 
    Factorial'''

num = int(input("숫자를 입력하세요 : "))   # 숫자 입력받음



while True:
    sum = 1
    for i in range(1, num +1):                 #조건문을 실행 할 수록 곱해지게
        sum =sum*i

    if not num == -1:                          #-1을 예외로 두고 프린트
        print(" %d! = %d" %(num,sum))
        num = int(input("숫자를 입력하세요 : "))

    if num == -1:
        print("Do not enter -1")
        break