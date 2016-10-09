
import random, datetime

def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j>=0 and array[j] > key:
            array[j+1] = array[j]
            j = j-1
        array[j+1] = key
    return array


arr = []
for i in range(0 , 100):
    rand_num = random.randint(0,10000)
    arr.append(rand_num)
print arr
time = datetime.datetime.now()
print time
print insertionSort(arr)
time2 = datetime.datetime.now()
print time2
