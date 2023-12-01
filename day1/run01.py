import urllib
import re

def main():
    redigit = re.compile("[0-9]")
    mysum = 0
    with open("input.txt") as fin:
        for line in filter(lambda x: x, map(lambda x: x.strip(), fin)):
            print("line", line)
            first = int(redigit.search(line).group())
            last = int(redigit.search(line[::-1]).group())
            mysum += (first * 10) + last
    print("mysum", mysum)

if __name__ == "__main__":
    main()
