from collections import Counter
filename = "Random.txt"
file = open(filename, 'r')
print('\n[---------------------------Text data-------------------------------------------]\n')
for line in file:
        print(line)
file.close()


def word_count(filename):
        with open(filename) as f:
                return Counter(f.read().split())


print('\n-------------------------------FreQuency counting---------------------------------\n')
print("\nNumber of words in the file :", word_count("Random.txt"))
print("-------------------------------------Counting over--------------------------------")

with open("Random.txt") as f:
    with open("pythonpy.txt", "a") as f1:
        for lines in f:
            f1.write(lines)
print("\n---------------------data copied-----------------------------------------")
with open("pythonpy.txt") as f:
    for text in f:
        print(text)
print("------------------------------End of the Program--------------------------------------")
