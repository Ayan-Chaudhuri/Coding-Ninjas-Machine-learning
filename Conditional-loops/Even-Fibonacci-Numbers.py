# Given a number N find the sum of all the even valued terms in the fibonacci sequence less than or equal to N
# Try generating only even fibonacci numbers instead of iterating over all Fibonacci numbers.

def even_fib_sum(N):
   if N <= 1:
       return 0
       
   fib_prev = 0
   fib_curr = 2
   fib_next = 8 
   even_sum = 2
    
   while fib_next <= N:
       even_sum += fib_next
       fib_prev = fib_curr
       fib_curr = fib_next
       fib_next = 4 * fib_curr + fib_prev
   
   return even_sum

N = int(input())
        
result = even_fib_sum(N)
print(result)
