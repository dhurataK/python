import random, datetime

def selectionSort(array):
    for idx in range(0, len(array)-1):
        minIndex = idx
        for j in range(idx+1,len(array)):
            if array[j] < array[minIndex]:
                minIndex = j
        tmp = array[idx]
        array[idx] = array[minIndex]
        array[minIndex] = tmp
    return array


arr = []
for i in range(0 , 100):
    rand_num = random.randint(0,10000)
    arr.append(rand_num)
print arr
time = datetime.datetime.now()
print time
print selectionSort(arr)
time2 = datetime.datetime.now()
print time2
