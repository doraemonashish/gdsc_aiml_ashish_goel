
def short_string(s):
    str=s.strip()
    l=list(str)
    for i in l:
        if (l[0] == '1' and l[-1] == '0') or (l[0] == '0' and l[-1] == '1'):
            del l[0]
            del l[-1]
    return len(l)
n=int(input("number of test cases: "))
for i in range(n):
    str=input("enter string of 1s and 0s")
    p=short_string(str)
    print(p)