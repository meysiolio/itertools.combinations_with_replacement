from itertools import combinations_with_replacement

string, r = input().split()

for i in list(combinations_with_replacement(sorted(string),int(r))):
    print("".join([x for x in i]))