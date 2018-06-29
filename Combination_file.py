with open('abc.txt') as fl1, open('test.txt') as fl2:
    for line1, line2 in zip(fl1, fl2):
        # line1 from abc.txt, line2 from test.txt
        print(line1+line2)

print("\r")
def read_integers(filename):
    with open(filename) as f:
        numbers = [int(x) for x in f]
        return numbers


print(read_integers("integer.txt"))
x = read_integers("integer.txt")
x.sort()
print(x)