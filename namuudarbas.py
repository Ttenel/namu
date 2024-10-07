import random, time

my_list = [random.randint(1, 999) for a in range(100)]

print(my_list)

def b(n):
    for i in range(len(n)):
        for j in range(len(n)-i-1):
            if n[j] > n[j+1]:
                n[j], n[j+1] = n[j+1], n[j]
    return n

start_time = time.time()
b(my_list)
print(f"Bubble sort: {time.time() - start_time:.10f} s")

start_time = time.time()
sorted(my_list)
print(f"Built-in sort: {time.time() - start_time:.10f} s")
