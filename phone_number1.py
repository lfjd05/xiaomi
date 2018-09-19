import sys


if __name__ == "__main__":
    n = int(sys.stdin.readline())

    for i in xrange(n):
        line = list(sys.stdin.readline().strip())
        ans = []

        while "Z" in line:
            for ch in "ZERO":
                line.remove(ch)
            ans.append("2")

        while "W" in line:
            for ch in "TWO":
                line.remove(ch)
            ans.append("4")

        while "U" in line:
            for ch in "FOUR":
                line.remove(ch)
            ans.append("6")

        while "F" in line:
            for ch in "FIVE":
                line.remove(ch)
            ans.append("7")

        while "X" in line:
            for ch in "SIX":
                line.remove(ch)
            ans.append("8")

        while "S" in line:
            for ch in "SEVEN":
                line.remove(ch)
            ans.append("9")

        while "G" in line:
            for ch in "EIGHT":
                line.remove(ch)
            ans.append("0")

        while "T" in line:
            for ch in "THREE":
                line.remove(ch)
            ans.append("5")

        while "O" in line:
            for ch in "ONE":
                line.remove(ch)
            ans.append("3")

        while "N" in line:
            for ch in "NINE":
                line.remove(ch)
            ans.append("1")

        ans.sort()

        print "".join(ans)
