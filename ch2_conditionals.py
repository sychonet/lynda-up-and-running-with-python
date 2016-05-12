#A simple script demonstrating use of conditional statements in Python

def main():
    x, y = 10, 100

    if(x < y):
        st = "x is less than y"
    elif (x == y):
        st = "x is same as y"
    else:
        st = "x is greater than y"
    print st

main()
