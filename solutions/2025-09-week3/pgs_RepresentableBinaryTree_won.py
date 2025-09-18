import math


def check(bin_num, parent):
    if not bin_num:
        return True

    mid = len(bin_num) // 2

    node_exists = (bin_num[mid] == '1')

    if node_exists and not parent:
        return False

    return check(bin_num[:mid], node_exists) and check(bin_num[mid+1:], node_exists)


def sol(number):
    if number == 1:
        return 1

    bin_numbers = bin(number)[2:]

    num = 2 ** (int(math.log2(len(bin_numbers))) + 1) - 1

    bin_numbers = "0" * (num - len(bin_numbers)) + bin_numbers

    if bin_numbers[len(bin_numbers) // 2] == '1' and check(bin_numbers, True):
        return 1
    else:
        return 0


def solution(numbers):
    answer = []

    for n in numbers:
        answer.append(sol(n))
    return answer
