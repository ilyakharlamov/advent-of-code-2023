import urllib
import re

def main():
    NUM = {
       "one": 1,
       "two": 2,
       "three": 3,
       "four": 4,
       "five": 5,
       "six": 6,
       "seven": 7,
       "eight": 8,
       "nine": 9,
    }
    redigit = re.compile("(?=(%s))" % ("|".join(["[0-9]"]+list(NUM.keys()))))
    print(redigit)
    mysum = 0
    with open("input.txt") as fin:
        for line in filter(lambda x: x, map(lambda x: x.strip(), fin)):
            matches = redigit.findall(line)
            print(line)
            print(matches)
            first = matches[0]
            first = NUM.get(first, first)
            last = matches[-1]
            last = NUM.get(last, last) 
            print(line, first, last)
            mysum += (int(first) * 10) + int(last)
    print("mysum", mysum)

if __name__ == "__main__":
    main()
