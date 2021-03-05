import sys
import math
import string

def solve(case):
    vel, dis = case.split(":")

    try:
        time = float(dis) / float(vel)
    except ZeroDivisionError as err:
        time = 6
    finally:
        if time <= 1:
            print("SWERVE")
        elif time <= 5:
            print("BREAK")
        else:
            print("SAFE")

def main():
    cases = int(sys.stdin.readline().rstrip())
    for case_num in range(cases):
        case = sys.stdin.readline().rstrip()
        solve(case)

if __name__ == "__main__":
    main()
