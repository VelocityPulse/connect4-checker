import sys

from process import process


def main():

    if len(sys.argv) < 2:
        print("ERROR: GIVE FILE TO ANALYZE")
        return

    file = open(sys.argv[1], mode='r')
    brut_data = file.read()
    file.close()

    print("Analyzing this game :" + sys.argv[1])
    print(brut_data)
    process(brut_data)


main()
