import sys


def add_s(argv):
    with open('sales.csv', 'a', encoding='utf-8') as s:
        for i in range(len(argv) - 1):
            s.write(f'{argv[i+1]}\n')


if __name__ == '__main__':
    add_s(sys.argv)
    exit(0)