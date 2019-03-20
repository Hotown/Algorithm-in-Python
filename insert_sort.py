def insert_sort(data):
    for i in range(1, len(data)):
        key = data[i]
        ## Insert
        idx = i - 1
        while idx >= 0 and data[idx] > key:
            data[idx + 1] = data[idx]
            idx = idx - 1
        data[idx + 1] = key

data = [2, 1, 4, 3, 5]
insert_sort(data)
print(data)