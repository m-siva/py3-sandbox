#!/usr/bin/python3
v1 = [(0,1), (2,3),(3,4)]
v2 = [(2,1), (3,9)]
s = {}
for i in v2:
    s[i[0]] = i[1]
    sum =0
    for i in v1:
        if i[0] in s:
            sum +=i[1]*s[i[0]]

print(sum)