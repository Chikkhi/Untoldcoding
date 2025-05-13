
# Fibonacci Generator without input()

def generate_fibonacci(n):
    fib_series = []
    a, b = 0, 1
    for _ in range(n):
        fib_series.append(a)
        a, b = b, a + b
    return fib_series

# Fixed number of terms
terms = 10  # Change this to any number you want
series = generate_fibonacci(terms)
print("Fibonacci Series:")
print(series)
