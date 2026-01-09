# def even_generator(limit):
#     for i in range(2, limit + 1, 2):
#         return i
    
# print(even_generator(10))        # 2

# ---------------------------------------------------------------

# def even_generator(limit):
#     li = []
#     for i in range(2, limit + 1, 2):
#         li.append(i)
#     return li
    
# print(even_generator(10))        # [2, 4, 6, 8, 10]

# ---------------------------------------------------------------


def even_generator(limit):
    for i in range(2, limit + 1, 2):
        yield i

# print(even_generator(10))          # <generator object even_generator at 0x000002D17E0002E0>

for i in even_generator(10):
    print(i)