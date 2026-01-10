def gen(num):
    for i in range(num):
        yield i+1

print(list(gen(10)))