def blocks(n):
    return 0 if n <= 0 else blocks(n - 1) + n

print(blocks(8))
print(blocks(0))
print(blocks(-1))
print(blocks(1))
print(blocks(838852))

def sum_of_digits(n):
    return 10 if n < 10 else n // 10 + n % 10

print(sum_of_digits(1234))
print(sum_of_digits(-48729))
