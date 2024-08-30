import sys

file_name = sys.argv[1]

f = open(file_name, "r")

print(f.readline())

f.close()
