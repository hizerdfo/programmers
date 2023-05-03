# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

num1 = input()
num2 = input()

sum = int(num1) + int(num2)
print("두 수의 합은 %d입니다." % sum)

# 몫 구하기

def solution(num1, num2):
    answer = num1 // num2
    return answer

def solution(num1, num2):
    answer = num1 % num2
    return answer


def solution(num1, num2):
    answer = int (1000 * (num1 / num2))
    return answer

#두 분수의 덧셈 , 기약분수 사용

def solution(numer1, denom1, numer2, denom2):
    # 두 분모가 같아질 때까지 분모를 공통분모로 변환
    common_denom = denom1 * denom2
    new_numer1 = numer1 * denom2
    new_numer2 = numer2 * denom1

    # 분자와 분모를 각각 더한 후, 최대공약수를 구하여 약분
    result_numer = new_numer1 + new_numer2
    result_denom = common_denom

    # 최대공약수 구하기
    for i in range(2, min(result_numer, result_denom) + 1):
        while result_numer % i == 0 and result_denom % i == 0:
            result_numer //= i
            result_denom //= i

    # 결과를 기약분수 형태로 반환
    return [result_numer, result_denom]


def solution(numbers):
    for i in range(len(numbers)):
        numbers[i] *= 2;
    answer =numbers
    return answer


def solution(numbers):
    total = 0
    for i in range(len(numbers)):
        total += numbers[i]
    answer =  total / len(numbers)
    return answer


def solution(n, k):
    service = n // 10
    answer = 12000 * n + 2000 * (k - service)
    return answer