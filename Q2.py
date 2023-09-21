def pattern(n):
    num = 1

    for i in range(1, n+1):
        for j in range(1, n+1):
            print(num, end="")
            num = (num % n) + 1
        print()

n = int(input("Enter the number of rows for the pattern: "))

pattern(n)