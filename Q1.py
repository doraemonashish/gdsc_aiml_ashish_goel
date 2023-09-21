def check_substring(str1, str2):
    if str1 in str2:
        return "Yes"
    else:
        return "No"

r = int(input("enter number of test cases: "))

for i in range(r):
    str1, str2 = input("enter 2 strings seperated by a string: ").split()

    result = check_substring(str1, str2)
    print(result)
