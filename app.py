def gen_fibonacci(limit):
    first = 1
    second = 1
    yield 1
    yield 1
    next = first + second

    while next <= limit:
        yield next
        first = second
        second = next
        next = first + second

for item in gen_fibonacci(40):
    print(item, end=", ")
print()