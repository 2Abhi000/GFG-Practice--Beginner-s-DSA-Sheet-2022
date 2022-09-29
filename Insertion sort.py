# Insertion sort
def insertionSort(array):
    for step in range(1, len(array)):
        key = array[step]
        j = step - 1
        while j >= 0 and key < array[j]:
            array[j + 1] = array[j]
            j = j - 1
        array[j + 1] = key

n=int(input("Size: "))
a=[]
for i in range(n):
    a.append(int(input("Value: ")))
insertionSort(a)
print(a)