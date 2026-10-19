def blocks(n):
    return 0 if n <= 0 else blocks(n - 1) + n

print(blocks(8))
print(blocks(0))
print(blocks(-1))
print(blocks(1))
print(blocks(838))

def sum_of_digits(n):
    return n if n <= 10 else sum_of_digits(n // 10) + (n % 10)

print(sum_of_digits(1234))
print(sum_of_digits(1588))
print(sum_of_digits(-48729))

def print_count_down(n):
    if n == 0:
        print("BOOM")
    else:
        print (n) 
        print_count_down(n-1)

print_count_down(10)
