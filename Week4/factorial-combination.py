#20171660 이건민


def factorial(p):        # 1씩 줄어들면서 곱하는 재귀함수를 만든
    sum = 1
    while p > 0:
        sum *= p
        p -= 1
    return sum


def factorial_combination(n, k):    #factorial 공식을 이용한 함수를 만든디
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

        return numerator/(denominator1*denominator2)

d = factorial_combination("a",2)
print(d)
