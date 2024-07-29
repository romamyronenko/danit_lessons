import random


def choose(list_, k):
    m = max(list_[:k])

    for i in list_[k:]:
        if i > m:
            return i
    else:
        return list_[-1]


test_data = [[random.randint(1, 1000) for _ in range(100)] for _ in range(10000)]
res = []
for k in range(1, 100):
    res.append([])
    for td in test_data:
        res_ = choose(td, k)
        res[-1].append(res_ / max(td))

result = []
for i in res:
    result.append(sum(i) / len(i))

for index, value in enumerate(result, start=1):
    print(index, value)
