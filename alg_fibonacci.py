import timeit

def main():
    fib_number = 25

    fibonacci_iterative = fibonacci_iter(fib_number)
    fibonacci_iter_ttr = timeit.timeit(lambda: fibonacci_iter(fib_number), number=1)

    fibonacci_recursive = fibonacci_rec(fib_number)
    fibonacci_rec_ttr = timeit.timeit(lambda: fibonacci_rec(fib_number), number=1)

    print(f"Fibonacci iterative {fibonacci_iterative} Time elapsed: {fibonacci_iter_ttr:.8f} seconds")
    print(f"Fibonacci recursive {fibonacci_recursive} Time elapsed: {fibonacci_rec_ttr:.8f} seconds")
    print(f"Fibonacci iterative is ~{round(fibonacci_rec_ttr/fibonacci_iter_ttr)}x faster")

def fibonacci_rec(n):
    if n == 2 or n == 1:
        return 1
    return fibonacci_rec(n-1) + fibonacci_rec(n-2)

def fibonacci_iter(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1

    fib_sequence = [0, 1]
    for i in range(2, n + 1):
        fib_sequence.append(fib_sequence[i - 1] + fib_sequence[i - 2])

    return fib_sequence[n]



if __name__ == "__main__":
    main()