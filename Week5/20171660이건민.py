## 20171660 이건민
## 4분반
## 피보나치 수열을 반복적으로 구현

import time

## fibo라는 리스트를 만들고
## fibo(0), fibo(1) 값을 0 , 1로 지정



def iterfibo(n):
    fibolist = []
    fibolist.append(0)
    fibolist.append(1)
    ## 피보나치 수열의 합을 저장할 sum = 0 지정
    sum = 0
    ## 피보나치 수열을 fibo리스트에 저장
    for i in range(2, n + 1):
        fibolist.append(fibolist[i-1] + fibolist[i-2])
    sum = fibolist[n]
    return sum


def fibo(n):
	if n <= 1:
		return n
	return fibo(n - 1) + fibo(n - 2)


while True:
    try:
        nbr = int(input("Enter a number : "))
        if nbr == -1:
            break
        t = time.time()
        iterfibo(nbr)
        s = time.time() - t

        print("IterFibo(%d) = %d, time %.6f" %(nbr, iterfibo(nbr), s))

        t = time.time()
        fibo(nbr)
        s = time.time() - t

        print("Fibo(%d) = %d, time %.6f" %(nbr, fibo(nbr), s))
    except ValueError:
        print("Enter number")
