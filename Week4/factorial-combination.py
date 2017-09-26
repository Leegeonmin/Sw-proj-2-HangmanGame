#20171660 이건민

# 1씩 줄어들면서 곱하는 재귀함수를 만든다
def factorial(p):
    sum = 1
    while p > 0:
        sum *= p
        p -= 1
    return sum

#factorial 공식을 이용한 함수를 만든다
def factorial_combination(n, k):
    if not type(n or k) == int:
        print("Enter integer")
        n = int(input("Enter n:"))
        k = int(input("Enter k:"))
        factorial_combination(n,k)
        print(factorial_combination(n,k))
    else:
        numerator = factorial(n)
        denominator1 = factorial(k)
        denominator2 = factorial(n-k)

        return numerator / (denominator1 * denominator2)

if __name__ == '__main__':
    d = factorial_combination("a",2)
    print(d)
