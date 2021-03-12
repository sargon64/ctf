import sys
import math
import string


def solve(case):
    small, big, total = case.split(' ')
    small = int(small)
    big = int(big)
    total = int(total)
    small += 1
    big += 1
    for i in range(small):
        # print(i)
        for j in range(big):
            if i + 5*j == total:
                print('{} is True!'.format(case))
                return True
    print('{} is False!'.format(case))
    return False


def main():
    cases = int(sys.stdin.readline().rstrip())
    for case_num in range(cases):
        case = sys.stdin.readline().rstrip()
        solve(case)


if __name__ == "__main__":
    main()
