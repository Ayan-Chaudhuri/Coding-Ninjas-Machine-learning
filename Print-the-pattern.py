#Print the following pattern for n number of rows.
#Note: each line consist of equal number of characters + spaces. Suppose you are printing xth line for N=n. You need to print 1..x followed by (n-x) spaces, again (n-x) spaces followed by x..1
#For eg. N = 5//

def print_pattern(N):
    for i in range (1, N+1):
        line = ""
        for j in range(1, i+1):
            line += str(j)
        line += " " * (2 * (N - i))
        for j in range(i, 0, -1):
            line += str(j)
        print(line)

N = int(input())
print_pattern(N)
