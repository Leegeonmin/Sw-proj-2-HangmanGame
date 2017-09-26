# 20171660이건민
import time
# nCk에서 n,k를 입력받는다
def recursive_combination(n, k):
         # type이 정수가 아니면 다시 입력받음
        if not(type(n or k)) == int:
            print("Enter Integer")
            n = int(input("Enter integer n:"))
            k = int(input("Enter integer k:"))
            Re = recursive_combination(n, k)
            print(Re)
        # 예외처리
        elif ((n or k) < 0) or (n < k):
            print("Enter n,k(n,k > 0 and n < k)")
            n = int(input("Enter integer n:"))
            k = int(input("Enter integer k:"))
            Re = recursive_combination(n, k)
            print(Re)

        else:
        # 처리 시간을 줄이기 위해 nCk에서 k가 클 경우 변환해준다 ex) 5C4 = 5C1
            if n - k >= k:
                # 함수가 k를 1로 입력받을 시 nC1 = n 을 이용한다
                if k == 1:
                    return n
             # n = k 일시 nCk = 1
                elif n == k:
                    return 1
             # k = 0 일시 nCk = 1
                elif k == 0:
                    return 1
                else:
                    return recursive_combination(n - 1, k - 1) + recursive_combination(n - 1, k)
                    print(recursive_combination(n - 1, k - 1) + recursive_combination(n - 1, k))
            else:
                k = n-k
                # 함수가 k를 1로 입력받을 시 nC1 = n 을 이용한다
                if k == 1:
                    return n
                # n = k 일시 nCk = 1
                elif n == k:
                    return 1
                # k = 0 일시 nCk = 1
                elif k == 0:
                    return 1
                else:
                    return recursive_combination(n - 1, k - 1) + recursive_combination(n - 1, k)
                    print(recursive_combination(n - 1, k - 1) + recursive_combination(n - 1, k))

__name__=="__main__"
a = time.time()
N = recursive_combination(25, 15)
print(N)
b = time.time()
print(b - a)


### 처리시간을 줄이기 위해 만든 if, else 문을 이용해 25C15를 실행해본결과 약 2배(1.7초 , 0.8초)차이가