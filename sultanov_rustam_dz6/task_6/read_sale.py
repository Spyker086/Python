import sys


def read_sale(argv):
    with open('sales.csv', 'r', encoding='utf-8') as s:
        if len(argv) == 1:
            l = s.readline().strip()
            while l:
                print(l)
                l = s.readline().strip()

        elif len(argv) == 2:
            for i in range(int(argv[1]) - 1):
                s.readline()
            l = s.readline().strip()
            while l:
                print(l)
                l = s.readline().strip()

        elif len(argv) == 3:
            for i in range(int(argv[1]) - 1):
                s.readline()
            for i in range(int(argv[1]) - 1, int(argv[2])):
                print(s.readline().strip())


if __name__ == '__main__':
    read_sale(sys.argv)
    exit(0)