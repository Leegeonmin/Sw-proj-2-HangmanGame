# 20171660이건민

def recursive_combination(n, k):    # nCk에서 n,k를 입력받는다
        if not(type(n or k)) == int:    #type이 정수가 아니면 끝냄
            print("Enter Integer")
            n = int(input("Enter integer n:"))
            k = int(input("Enter integer k:"))
            Re = recursive_combination(n, k)
            print(Re)
        elif ((n or k) < 0) or (n < k):           # 예외 처리
            print("Enter n,k(n,k > 0 and n < k)")
            n = int(input("Enter integer n:"))
            k = int(input("Enter integer k:"))
            Re = recursive_combination(n, k)
            print(Re)

        else:
            if k == 1:  # 함수가 k를 1로 입력받을 시 nC1 = n 을 이용한다
                return n
            elif n == k:  # n = k 일시 nCk = 1
             return 1
            elif k == 0:    # k = 0 일시 nCk = 1
             return 1
            else:
                return recursive_combination(n - 1, k - 1) + recursive_combination(n - 1, k)
                print(recursive_combination(n - 1, k - 1) + recursive_combination(n - 1, k))



__name__=="__main__"
N = recursive_combination("a",2)
print(N)