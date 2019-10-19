"""
Task 1:
Write a program which will find all such numbers
which are divisible by 7 but are not a multiple of 5,
between 2000 and 3200 (both included).
The numbers obtained should be printed in a
comma-separated sequence on a single line.
"""
def task01(start, end):
    print(','.join(str(i) for i in range(start, end + 1) if i % 7 == 0 and i % 5 != 0))

condition = lambda i: i % 7 == 0 and i % 5 != 0

def task02(start, end, condition):
    print(','.join(str(i) for i in range(start, end + 1) if condition(i)))

task02(2000, 3200, condition)