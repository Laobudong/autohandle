def sum_two_numbers(a, b):
    return a + b            # return result to the function caller

c = sum_two_numbers(3, 12)  # assign result of function execution to variable 'c'
print(c)

def fib(n):
    """This is documentation string for function. It'll be available by fib.__doc__()
    Return a list containing the Fibonacci series up to n.
    F(0)=0，F(1)=1, F(n)=F(n-1)+F(n-2)（n>=2，n∈N*
    1、1、2、3、5、8、13、21、34"""
    result = [0]
    a = 1
    b = 0
    while a <= n:
        result.append(a)
        tmp_var = b
        update variable b
        a += a #update variable a
    return result

print(fib(5))
