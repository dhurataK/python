import random, datetime

def bubblesort(array):
    length = len(array)
    swaped = True
    while(swaped):
        swaped = False
        for i in range(0, length-1):
            if array[i] > array[i+1]:
                temp = array[i]
                array[i] = array[i+1]
                array[i+1] = temp
                swaped = True
    return array

arr = []
for i in range(0 , 100):
    rand_num = random.randint(0,10000)
    arr.append(rand_num)
print arr
time = datetime.datetime.now()
print time
print bubblesort(arr)
time2 = datetime.datetime.now()
print time2
