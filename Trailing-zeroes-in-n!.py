# Find and return number of trailing 0s in n factorial without calculating n factorial.

  
def count_trailing_zeros(n):
    count = 0
    i = 5

    while n // i >=1:
        count += n // i
        i *= 5
    return count

n = int(input())
zeros_count = count_trailing_zeros(n)
print(zeros_count)
